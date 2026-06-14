'''
================================================================================
                    BILINGUAL DATASET & CAUSAL MASKING
================================================================================
This module defines the Dataset pipeline used to feed translation sentence pairs 
to our Transformer model. 

In PyTorch, a custom Dataset must inherit from `torch.utils.data.Dataset` and 
implement three key methods:
1. __init__: Initializes dataset variables, tokenizers, and special tokens.
2. __len__: Returns the total number of sentence pairs in the dataset.
3. __getitem__: Loads, tokenizes, pads, and formats a single training sample 
   at a given index.

--------------------------------------------------------------------------------
Key Concept: Teacher Forcing & Shifted Right Inputs
--------------------------------------------------------------------------------
During training, the decoder is fed the expected translation shifted to the right.
- Decoder Input:  [SOS] + Target_Tokens + [PAD]...
- Decoder Label:  Target_Tokens + [EOS] + [PAD]...

This means:
1. The Decoder Input starts with [SOS] (Start of Sentence) so the decoder has 
   a token to start predicting from, but does NOT include [EOS] at the end because 
   we don't want it to learn to predict tokens after it sees the end-of-sentence.
2. The Decoder Label (what we expect the model to predict) does NOT have [SOS] 
   at the beginning but ends with [EOS] (End of Sentence).

--------------------------------------------------------------------------------
Visual representation of Sequence Padding (Sequence Length = 8):
--------------------------------------------------------------------------------
Source text: "I love cats" (Tokenized: [12, 45, 99])
Encoder Input:  [SOS]  12   45   99  [EOS] [PAD] [PAD] [PAD]  <- length = 8
Encoder Mask:     1     1    1    1    1     0     0     0    <- 1: keep, 0: ignore

Target text: "Amo i gatti" (Tokenized: [22, 9, 87])
Decoder Input:  [SOS]  22    9   87  [PAD] [PAD] [PAD] [PAD]  <- length = 8 (No EOS)
Decoder Label:    22    9   87  [EOS] [PAD] [PAD] [PAD] [PAD]  <- length = 8 (No SOS)
================================================================================
'''

import torch
from torch.utils.data import Dataset

class BilingualDataset(Dataset):
    """
    Preprocesses raw text translation pairs, converts them to token IDs,
    applies padding/special tokens, and generates attention masks.
    """
    def __init__(self, dataset, tokenizer_src, tokenizer_tgt, src_lang, tgt_lang, seq_len):
        super().__init__()
        
        self.dataset = dataset             # Raw dataset containing translation dictionaries
        self.tokenizer_src = tokenizer_src # Tokenizer for the source language (e.g. English)
        self.tokenizer_tgt = tokenizer_tgt # Tokenizer for the target language (e.g. Italian)
        self.src_lang = src_lang           # Source language key (e.g., 'en')
        self.tgt_lang = tgt_lang           # Target language key (e.g., 'it')
        self.seq_len = seq_len             # Fixed sequence length for all tensors

        # Retrieve special token IDs and store them as integers
        self.sos_token = tokenizer_src.token_to_id('[SOS]')
        self.eos_token = tokenizer_src.token_to_id('[EOS]')
        self.pad_token = tokenizer_src.token_to_id('[PAD]')

    def __len__(self):
        # Returns the total number of sentences in the dataset
        return len(self.dataset)

    def __getitem__(self, idx):
        # Fetch the raw translation pair at the specified index
        item = self.dataset[idx]
        src_text = item['translation'][self.src_lang]
        tgt_text = item['translation'][self.tgt_lang]

        # Convert raw strings into lists of integer token IDs
        # Example: "Hello" -> [152]
        enc_input_tokens = self.tokenizer_src.encode(src_text).ids
        dec_input_tokens = self.tokenizer_tgt.encode(tgt_text).ids

        # Calculate how many padding tokens we need to reach the fixed 'seq_len'
        # - Encoder input needs: [SOS] + tokens + [EOS] -> (2 special tokens)
        # - Decoder input needs: [SOS] + tokens -> (1 special token)
        enc_num_padding_tokens = self.seq_len - (len(enc_input_tokens) + 2)
        dec_num_padding_tokens = self.seq_len - (len(dec_input_tokens) + 1)
        
        # If the sentence is longer than seq_len, we raise an error.
        # In practice, sentences longer than seq_len are filtered out beforehand.
        if enc_num_padding_tokens < 0 or dec_num_padding_tokens < 0:
            raise ValueError("Sentence is too long for the given sequence length")

        # Construct the Encoder Input tensor:
        # [SOS] + Source_Tokens + [EOS] + [PAD]...
        enc_input = torch.cat([
            torch.tensor([self.sos_token], dtype=torch.int64),
            torch.tensor(enc_input_tokens, dtype=torch.int64),
            torch.tensor([self.eos_token], dtype=torch.int64),
            torch.full((enc_num_padding_tokens,), self.pad_token, dtype=torch.int64)
        ])

        # Construct the Decoder Input tensor (Teacher Forcing):
        # [SOS] + Target_Tokens + [PAD]... (No [EOS] token!)
        dec_input = torch.cat([
            torch.tensor([self.sos_token], dtype=torch.int64),
            torch.tensor(dec_input_tokens, dtype=torch.int64),
            torch.full((dec_num_padding_tokens,), self.pad_token, dtype=torch.int64)
        ])

        # Construct the Label tensor (what the Decoder is expected to output):
        # Target_Tokens + [EOS] + [PAD]... (No [SOS] token!)
        label = torch.cat([
            torch.tensor(dec_input_tokens, dtype=torch.int64),
            torch.tensor([self.eos_token], dtype=torch.int64),
            torch.full((dec_num_padding_tokens,), self.pad_token, dtype=torch.int64)
        ])

        # Ensure all processed tensors are exactly of size 'seq_len'
        assert enc_input.shape == (self.seq_len,)
        assert dec_input.shape == (self.seq_len,)
        assert label.shape == (self.seq_len,)

        # Construct masks:
        # 1. encoder_mask: Tells self-attention to ignore [PAD] positions in the source text.
        #    Shape becomes: (1, 1, seq_len) to allow broadcasting across heads and batch items.
        encoder_mask = (enc_input != self.pad_token).unsqueeze(0).unsqueeze(0)

        # 2. decoder_mask: Prevents the decoder from attending to future tokens (causal masking)
        #    AND prevents it from attending to [PAD] tokens.
        #    - (dec_input != self.pad_token).unsqueeze(0).unsqueeze(0) -> padding mask: (1, 1, seq_len)
        #    - casual_mask(self.seq_len) -> causal mask: (1, seq_len, seq_len)
        #    - Bitwise/logical AND combines both masks.
        decoder_mask = (dec_input != self.pad_token).unsqueeze(0).unsqueeze(0) & casual_mask(self.seq_len)

        return {
            'encoder_input': enc_input,        # Tensor of shape (seq_len,)
            'decoder_input': dec_input,        # Tensor of shape (seq_len,)
            'encoder_mask': encoder_mask,      # Boolean tensor of shape (1, 1, seq_len)
            'decoder_mask': decoder_mask,      # Boolean tensor of shape (1, seq_len, seq_len)
            'label': label,                    # Tensor of shape (seq_len,)
            'src_text': src_text,              # Raw text string (for debugging/validation)
            'tgt_text': tgt_text               # Raw text string (for debugging/validation)
        }


def casual_mask(size):
    """
    Creates an upper triangular matrix filled with zeros above the diagonal,
    representing a look-ahead mask for self-attention.
    
    Example: size = 3
    torch.triu(..., diagonal=1) produces:
    [[0, 1, 1],
     [0, 0, 1],
     [0, 0, 0]]
     
    We compare to 0 (mask == 0), which returns a boolean mask:
    [[True, False, False],
     [True, True,  False],
     [True, True,  True]]
     
    This ensures that at sequence position 1, we can only attend to position 1.
    At position 2, we can attend to 1 and 2. At position 3, we can attend to 1, 2, and 3.
    """
    # Create a 2D matrix of shape (size, size) with 1s above the diagonal, and a dummy batch dim.
    mask = torch.triu(torch.ones((1, size, size), dtype=torch.int), diagonal=1)
    # Positions where mask is 0 are allowed (True); positions where mask is 1 are blocked (False).
    return mask == 0