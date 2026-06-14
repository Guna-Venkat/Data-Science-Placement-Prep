'''
================================================================================
                    TRAINING LOOP & PIPELINE (train.py)
================================================================================
This script orchestrates the entire lifecycle of our Transformer model:
1. Loads the raw translation dataset (Opus Books, English-Italian).
2. Builds or loads tokenizers for both source and target languages.
3. Prepares training and validation DataLoader objects.
4. Initializes the Transformer model on the best available hardware (GPU/CPU).
5. Defines the Adam optimizer and Cross Entropy Loss (with Label Smoothing).
6. Runs validation cycles during training to track BLEU/qualitative progress.
7. Saves checkpoint weight files so that we can resume training anytime.

--------------------------------------------------------------------------------
Key Concepts for Beginners:
--------------------------------------------------------------------------------
1. PyTorch train vs eval mode:
   - model.train() enables dropout and batchnorm updates.
   - model.eval() disables dropout/batchnorm for deterministic evaluation.

2. torch.no_grad():
   - Disables PyTorch's autograd engine. We use it during validation to save 
     memory and speed up calculation since we do not compute gradients/backprop.

3. Label Smoothing:
   - Softens target labels. Instead of telling the model to be 100% confident 
     in a single word (hard 1.0 probability), we redistribute 10% (0.1) of the 
     probability mass across all other vocabulary words. This prevents the model 
     from over-fitting and becoming over-confident.

4. ignore_index:
   - Tells the loss function (CrossEntropyLoss) to completely ignore padding 
     tokens when calculating training loss.
================================================================================
'''

import torch
import torch.nn as nn
from pathlib import Path
from tqdm import tqdm

# Dataset utilities
from datasets import load_dataset
from torch.utils.data import DataLoader, random_split

try:
    from torch.utils.tensorboard import SummaryWriter
except ImportError:
    # If tensorboard is not installed, define a dummy SummaryWriter to prevent crashing
    class SummaryWriter:
        def __init__(self, *args, **kwargs):
            pass
        def add_scalar(self, *args, **kwargs):
            pass
        def flush(self, *args, **kwargs):
            pass
        def close(self, *args, **kwargs):
            pass

from torch.optim import Adam

# Hugging Face Tokenizers
from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
from tokenizers.pre_tokenizers import Whitespace

# Custom files
from config import get_config, get_weights_file_path
from my_transformer import build_transformer
from dataset import BilingualDataset, casual_mask


def greedy_decode(model, source, source_mask, tokenizer_src, tokenizer_tgt, max_len, device):
    """
    Decodes the model output token-by-token (greedily) at inference time.
    Instead of calculating attention for the whole target sentence at once, 
    the model predicts the next word based on past predicted words.
    """
    sos_idx = tokenizer_tgt.token_to_id('[SOS]')
    eos_idx = tokenizer_tgt.token_to_id('[EOS]')

    # 1. Run the encoder once. This output (context) remains constant.
    # source shape: (1, seq_len)
    encoder_output = model.encode(source, source_mask)
    
    # 2. Initialize the decoder input with just the [SOS] token.
    # shape: (1, 1) -> (batch_size=1, seq_len=1)
    decoder_input = torch.empty(1, 1).fill_(sos_idx).type_as(source).to(device)

    # 3. Predict tokens one-by-one until we hit max_len or [EOS]
    while True:
        if decoder_input.size(1) == max_len:
            break

        # Causal mask so decoder can't look at future generated tokens
        decoder_mask = casual_mask(decoder_input.size(1)).to(device)

        # Decode: passes current target prefix and encoder representation
        out = model.decode(decoder_input, encoder_output, source_mask, decoder_mask)
        
        # Project only the LAST predicted token position (out[:, -1]) to vocabulary
        # out[:, -1] shape: (1, d_model) -> projected to (1, vocab_size)
        prob = model.project(out[:, -1])

        # Find the token ID with the highest probability (greedy choice)
        _, next_word = torch.max(prob, dim=1)
        
        # Append the predicted word to our decoder input for the next step.
        # .view(1, 1) reshapes next_word from shape (1,) to (1, 1) for concatenation.
        decoder_input = torch.cat([decoder_input, next_word.view(1, 1)], dim=1)

        # Stop if the model predicts the End-of-Sentence [EOS] token
        if next_word.item() == eos_idx:
            break
    
    # Squeeze out the batch dimension to return a 1D tensor: (seq_len_decoded,)
    return decoder_input.squeeze(0)


def run_validation(model, validation_ds, tokenizer_src, tokenizer_tgt, max_len, device, print_msg, global_step, writer, num_examples=2):
    """
    Runs evaluation on a few validation samples to print predictions side-by-side 
    with target translations. Helps inspect model progress.
    """
    model.eval() # Set model to evaluation mode (disables dropout)
    count = 0
    console_width = 80

    # Ensure no gradients are tracked during validation (saves RAM and time)
    with torch.no_grad():
        for batch in validation_ds:
            count += 1
            encoder_input = batch['encoder_input'].to(device) # (1, seq_len)
            encoder_mask = batch['encoder_mask'].to(device)   # (1, 1, seq_len)
            
            # Validation batch size must be 1 for token-by-token greedy decoding
            assert encoder_input.size(0) == 1, "Validation batch size must be 1"
            
            # Run greedy decoding
            model_out = greedy_decode(model, encoder_input, encoder_mask, tokenizer_src, tokenizer_tgt, max_len, device)
            
            # Convert token ID tensors back to raw strings
            source_text = batch['src_text'][0]
            expected_text = batch['tgt_text'][0]
            predicted_text = tokenizer_tgt.decode(model_out.detach().cpu().numpy())

            # Log to console
            print_msg('-' * console_width)
            print_msg(f"Source:     {source_text}")
            print_msg(f"Expected:   {expected_text}")
            print_msg(f"Prediction: {predicted_text}")
            print_msg('-' * console_width)

            if count == num_examples:
                break


def get_all_sentences(dataset, language):
    """
    Helper generator to stream sentences for training the tokenizer.
    """
    for item in dataset:
        yield item['translation'][language]


def get_or_build_tokenizer(config, dataset, language):
    """
    Creates a new WordLevel tokenizer trained on the dataset if it doesn't 
    exist on disk. Otherwise, loads the pre-existing tokenizer file.
    """
    tokenizer_path = Path(config['tokenizer_file'].format(language))
    
    # Ensure folder structure exists
    tokenizer_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not tokenizer_path.exists():
        # WordLevel tokenizer maps exact words to integer IDs
        # [UNK] is used for unknown out-of-vocabulary words
        tokenizer = Tokenizer(WordLevel(unk_token="[UNK]"))
        tokenizer.pre_tokenizer = Whitespace() # Split sentences by whitespace
        
        # WordLevelTrainer trains vocabulary limit and specifies special tokens
        trainer = WordLevelTrainer(
            vocab_size=config['vocab_size'], 
            special_tokens=["[UNK]", "[PAD]", "[SOS]", "[EOS]"], 
            min_frequency=2
        )
        
        # Train and save
        tokenizer.train_from_iterator(get_all_sentences(dataset, language), trainer)
        tokenizer.save(str(tokenizer_path))
        print(f"Created and saved tokenizer to {tokenizer_path}")
    else:
        # Load existing tokenizer
        tokenizer = Tokenizer.from_file(str(tokenizer_path))
        print(f"Loaded existing tokenizer from {tokenizer_path}")
        
    return tokenizer


def get_dataset(config):
    """
    Downloads raw translation books, builds/loads tokenizers, splits the dataset 
    into Train/Validation, and returns DataLoader wrappers.
    """
    # Load dataset from Hugging Face Datasets
    ds_raw = load_dataset('opus_books', f'{config["lang_src"]}-{config["lang_tgt"]}', split='train')

    # Build or retrieve tokenizers
    tokenizer_src = get_or_build_tokenizer(config, ds_raw, config['lang_src'])
    tokenizer_tgt = get_or_build_tokenizer(config, ds_raw, config['lang_tgt'])

    # 90% for training, 10% for validation
    train_ds_size = int(0.9 * len(ds_raw))
    val_ds_size = len(ds_raw) - train_ds_size
    train_ds_raw, val_ds_raw = random_split(ds_raw, [train_ds_size, val_ds_size])

    # Convert to custom BilingualDataset objects
    train_ds = BilingualDataset(train_ds_raw, tokenizer_src, tokenizer_tgt, config['lang_src'], config['lang_tgt'], config['seq_len'])
    val_ds = BilingualDataset(val_ds_raw, tokenizer_src, tokenizer_tgt, config['lang_src'], config['lang_tgt'], config['seq_len'])

    # Calculate and display the max length of source/target sentences in dataset
    max_len_src = 0
    max_len_tgt = 0
    for item in ds_raw:
        src_ids = tokenizer_src.encode(item['translation'][config['lang_src']]).ids
        tgt_ids = tokenizer_tgt.encode(item['translation'][config['lang_tgt']]).ids
        max_len_src = max(max_len_src, len(src_ids))
        max_len_tgt = max(max_len_tgt, len(tgt_ids))

    print(f'Max length of source sequence in corpus: {max_len_src}')
    print(f'Max length of target sequence in corpus: {max_len_tgt}')

    # Create PyTorch DataLoaders (batching, shuffling, and multi-threaded loading)
    train_dataloader = DataLoader(train_ds, batch_size=config['batch_size'], shuffle=True)
    val_dataloader = DataLoader(val_ds, batch_size=1, shuffle=False)

    return train_dataloader, val_dataloader, tokenizer_src, tokenizer_tgt


def get_model(config, vocab_src_len, vocab_tgt_len):
    """
    Creates the complete Transformer architecture.
    """
    model = build_transformer(
        vocab_src_len, 
        vocab_tgt_len, 
        config['seq_len'], 
        config['seq_len'], 
        config['d_model']
    )
    return model


def train_model(config):
    # Set up hardware accelerator: CUDA GPU > Apple Silicon MPS > Standard CPU
    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Using device: {device}")

    # Ensure weights storage directory exists
    Path(config['model_folder']).mkdir(parents=True, exist_ok=True)

    # Get data loaders and tokenizers
    train_dataloader, val_dataloader, tokenizer_src, tokenizer_tgt = get_dataset(config)

    # Initialize model and transfer it to the target device (GPU)
    model = get_model(config, tokenizer_src.get_vocab_size(), tokenizer_tgt.get_vocab_size()).to(device)

    # TensorBoard logging
    writer = SummaryWriter(config['experiment_name'])
    
    # Optimizer (Adam) with hyper-parameters matching original Transformer paper
    optimizer = Adam(model.parameters(), lr=config['lr'], eps=1e-9)
    
    initial_epoch = 0
    global_step = 0
    preload = config.get('preload')

    # Preload model weights if specified in configuration
    if preload:
        model_filename = None
        # Handle auto-detection of weights if set to True or 'latest'
        if preload is True or preload == 'latest':
            model_files = list(Path(config['model_folder']).glob(f"{config['model_filename']}*.pt"))
            if model_files:
                # Parse filenames tmodel_<epoch>.pt to find the latest epoch
                epochs = []
                for f in model_files:
                    try:
                        epoch_num = int(f.stem.split('_')[-1])
                        epochs.append((epoch_num, f))
                    except ValueError:
                        continue
                if epochs:
                    _, model_file = max(epochs, key=lambda x: x[0])
                    model_filename = str(model_file)
        else:
            # Load specific weights file
            model_filename = get_weights_file_path(config, preload)

        if model_filename and Path(model_filename).exists():
            print(f'Preloading model weights from {model_filename}')
            state_dict = torch.load(model_filename, map_location=device)
            # CRITICAL FIX: Actually load the model state dict!
            model.load_state_dict(state_dict['model_state_dict'])
            initial_epoch = state_dict['epoch'] + 1
            optimizer.load_state_dict(state_dict['optimizer_state_dict'])
            global_step = state_dict['global_step']
            print(f'Starting from epoch {initial_epoch}')
        else:
            print(f'No weights found at {model_filename or "specified path"}. Training from scratch.')

    # Loss Function: ignores padding tokens in calculating loss
    # and applies label smoothing to prevent overfitting.
    loss_fn = nn.CrossEntropyLoss(
        ignore_index=tokenizer_tgt.token_to_id('[PAD]'), 
        label_smoothing=0.1
    )

    # Training loop
    for epoch in range(initial_epoch, config['num_epochs']):
        model.train() # Enable training mode (dropout active)
        batch_iter = tqdm(train_dataloader, desc=f'Epoch {epoch}', unit='batch')

        for batch in batch_iter: 
            encoder_input = batch['encoder_input'].to(device) # Shape: (B, seq_len)
            decoder_input = batch['decoder_input'].to(device) # Shape: (B, seq_len)
            encoder_mask = batch['encoder_mask'].to(device)   # Shape: (B, 1, 1, seq_len)
            decoder_mask = batch['decoder_mask'].to(device)   # Shape: (B, 1, seq_len, seq_len)

            # 1. Run the forward pass through encoder and decoder
            encoder_output = model.encode(encoder_input, encoder_mask)
            decoder_output = model.decode(decoder_input, encoder_output, encoder_mask, decoder_mask)

            # 2. Project output vectors to target vocabulary size
            # proj_output shape: (B, seq_len, vocab_tgt_size)
            proj_output = model.project(decoder_output)

            label = batch['label'].to(device) # Shape: (B, seq_len)

            # 3. Calculate Loss
            # We reshape the output to a 2D matrix of shape (Batch_size * seq_len, vocab_size) 
            # and labels to a 1D vector of shape (Batch_size * seq_len) to compute Cross Entropy.
            loss = loss_fn(
                proj_output.view(-1, tokenizer_tgt.get_vocab_size()), 
                label.view(-1)
            )
            
            # Update progress bar
            batch_iter.set_postfix({'loss': f'{loss.item():.4f}'})

            # Log loss to TensorBoard
            writer.add_scalar('train loss', loss.item(), global_step)
            writer.flush()
            
            # 4. Backpropagation
            optimizer.zero_grad() # Reset accumulated gradients
            loss.backward()      # Calculate gradients
            optimizer.step()     # Update model weights

            global_step += 1
        
        # Run validation examples after each epoch to monitor quality
        run_validation(
            model, 
            val_dataloader, 
            tokenizer_src, 
            tokenizer_tgt, 
            config['seq_len'], 
            device, 
            lambda msg: batch_iter.write(msg), 
            global_step, 
            writer
        )
        
        # Save model checkpoint every 5 epochs
        if epoch % 5 == 0:
            model_filename = get_weights_file_path(config, epoch)
            torch.save({
                'epoch': epoch,
                'global_step': global_step,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict()
            }, model_filename)
            print(f'Model checkpoint saved to {model_filename}')
            
if __name__ == '__main__':
    config = get_config()
    train_model(config)