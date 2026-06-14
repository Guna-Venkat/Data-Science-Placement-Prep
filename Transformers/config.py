'''
================================================================================
                    CONFIGURATION MODULE (config.py)
================================================================================
This file defines the configuration dictionary containing all hyper-parameters, 
file paths, and settings needed to build, train, and preload our Transformer.

By centralizing settings, we make sure that our dataset loaders, models, 
and training loops share exactly the same configurations without hard-coding.
================================================================================
'''

from pathlib import Path

def get_config():
    """
    Returns a dictionary of parameters for the Transformer model.
    """
    return {
        # --- Training Settings ---
        'batch_size': 8,          # Number of sentence pairs processed together in one step
        'num_epochs': 20,         # Total passes over the training dataset
        'lr': 1e-4,               # Learning rate for the Adam optimizer
        'seq_len': 350,           # Maximum token length for padding/cropping sentences
        'd_model': 512,           # Dimension of word embeddings and hidden states in model
        'vocab_size': 30000,      # Vocabulary size limit for tokenizers
        
        # --- Translation Languages ---
        'lang_src': 'en',         # Source language (e.g. 'en' for English)
        'lang_tgt': 'it',         # Target language (e.g. 'it' for Italian)
        
        # --- Model Weights Storage ---
        'model_folder': 'weights', # Folder name where model checkpoints are saved
        'model_filename': 'tmodel_', # Prefix for saved checkpoint files
        
        # --- Preloading Weight Checkpoints ---
        # Options:
        # - None: Start training from scratch.
        # - True or 'latest': Automatically search the 'weights' folder for the highest epoch model.
        # - Integer/String epoch (e.g., 5 or '5'): Load the weights for epoch 5 ('weights/tmodel_5.pt').
        'preload': None,          
        
        # --- Tokenizer Settings ---
        'tokenizer_file': "tokenizer_{0}.json", # Format string for tokenizer save files
        
        # --- Tensorboard Tracking ---
        'experiment_name': 'runs/tmodel' # Folder path where TensorBoard logs will be saved
    }

def get_weights_file_path(config, epoch):
    """
    Generates the filepath for saving or loading a model checkpoint at a given epoch.
    Example: get_weights_file_path(config, 5) -> "weights/tmodel_5.pt"
    """
    model_folder = f"{config['model_folder']}"
    model_filename = f"{config['model_filename']}{epoch}.pt"
    return str(Path(model_folder) / model_filename)
