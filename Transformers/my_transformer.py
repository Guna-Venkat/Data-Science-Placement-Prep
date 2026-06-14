'''
================================================================================
                    UNDERSTANDING THE TRANSFORMER ARCHITECTURE
================================================================================
This script implements a complete Transformer model (Encoder-Decoder) from scratch 
using PyTorch. It is designed specifically for students and beginners.

Every line of code is commented to explain:
1. WHAT PyTorch functions (like unsqueeze, transpose, view) actually do.
2. WHY we are reshaping, permuting, or scaling tensors.
3. HOW the mathematical equations of the Transformer paper map directly to code.

--------------------------------------------------------------------------------
Key PyTorch Concepts Explained in this Code:
--------------------------------------------------------------------------------
1. Tensors & Shapes: Tensors are multi-dimensional arrays (like matrices). Their 
   shape tells us their dimensions: e.g., (Batch Size, Sequence Length, Embedding Size).

2. unsqueeze(dim): Inserts a dimension of size 1 at the specified index.
   - Example: A tensor of shape (3, 4) unsqueezed at dim=1 becomes shape (3, 1, 4).
   - Example: A tensor of shape (3, 4) unsqueezed at dim=0 becomes shape (1, 3, 4).
   - Why use it? To allow broadcasting (automatic stretching of dimensions) when 
     adding tensors of different shapes.

3. view(*shape): Reshapes a tensor without changing its data or copying memory.
   - Example: A tensor of shape (2, 6) can be viewed as (2, 2, 3) or (4, 3) or (12).
   - Note: The total number of elements must remain exactly the same (2 * 6 = 12).
   - Use `-1` as one of the dimensions to let PyTorch calculate that dimension automatically.

4. transpose(dim0, dim1): Swaps two dimensions.
   - Example: A tensor of shape (Batch, Seq_Len, Heads, Head_Dim) transposed at (1, 2)
     becomes shape (Batch, Heads, Seq_Len, Head_Dim).
   - Unlike view(), transpose does not require the new shape's dimensions to be contiguous.

5. contiguous(): 
   - Transpose/Permute operations don't physically move data in memory; they just change 
     how the indices map to memory. Some operations (like view) require the memory layout 
     to be consecutive (contiguous). Calling .contiguous() forces PyTorch to copy and 
     re-arrange the data in memory consecutively.

6. Matrix Multiplication (@ operator):
   - Computes standard matrix multiplication. In PyTorch, if tensors have more than 
     2 dimensions, `@` performs batch matrix multiplication on the last two dimensions 
     while broadcasting/matching the leading dimensions.
================================================================================
'''

import torch
import torch.nn as nn
from torch.nn import Embedding
import numpy as np

class InputEmbeddings(nn.Module):
    """
    Converts input token IDs (integers representing words) into continuous vectors.
    
    Vocabulary:
        Suppose we have a vocabulary of size 10,000 words. A sentence is represented 
        as a list of integers: "I love deep learning" -> [412, 89, 2105, 54]
        
    Embedding:
        Each word ID (e.g., 412) is mapped to a vector of size `d_model` (e.g., 512).
    """
    def __init__(self, d_model, vocab_size):
        super().__init__()
        self.d_model = d_model       # Dimension of the embedding vectors (e.g., 512)
        self.vocab_size = vocab_size # Size of the dictionary (total unique tokens)
        
        # nn.Embedding is a lookup table of shape (vocab_size, d_model)
        # It maps each token index to a d_model-dimensional vector.
        self.embedding = Embedding(vocab_size, d_model)

    def forward(self, x):
        # Input 'x' shape: (batch_size, seq_len)
        # Output embedding shape: (batch_size, seq_len, d_model)
        #
        # Why multiply by sqrt(d_model)?
        # According to the paper, this scales up the embeddings. Without scaling, 
        # when we add the Positional Encodings (which have values between -1 and 1),
        # the token embedding values would be relatively small and get "drowned out".
        # Scaling by sqrt(d_model) keeps their variance stable and dominant.
        return self.embedding(x) * (self.d_model ** 0.5)


class PositionalEmbeddings(nn.Module):
    """
    Transformers process all words in a sequence simultaneously, meaning they have 
    no inherent sense of word order (unlike RNNs). To fix this, we inject positional 
    information by adding a unique vector to each token's embedding based on its position.
    
    Mathematical formula:
        PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))   <- Even indices of the embedding vector
        PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))   <- Odd indices of the embedding vector
    """
    def __init__(self, d_model, seq_len, dropout):
        super().__init__()
        self.d_model = d_model   # Vector dimension size (e.g., 512)
        self.seq_len = seq_len   # Max sequence length (e.g., 100)
        self.dropout = nn.Dropout(dropout) # Regularization layer to prevent overfitting

        # Step 1: Create a matrix of zeros with shape (seq_len, d_model)
        pe = torch.zeros(seq_len, d_model)
        
        # Step 2: Create a column vector containing positions [0, 1, 2, ..., seq_len-1]
        # torch.arange(0, seq_len) creates a 1D tensor: [0, 1, 2, ...] of shape (seq_len)
        # .unsqueeze(1) inserts a new dimension at index 1, turning it into shape (seq_len, 1)
        #   Visual: 
        #   [0, 1, 2]  --(unsqueeze(1))-->  [[0], 
        #                                    [1], 
        #                                    [2]]
        position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
        
        # Step 3: Compute the division term in the denominator: 10000^(2i/d_model)
        # We calculate it using exp and log for numerical stability:
        # 10000^(-2i / d_model) = exp(-2i * log(10000) / d_model)
        # torch.arange(0, d_model, 2) creates a sequence of even indices: [0, 2, 4, ..., d_model-2]
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-np.log(10000.0) / d_model))
        
        # Step 4: Apply the sine formula to even dimensions (0, 2, 4, ...)
        # Slicing notation '0::2' means: "start at index 0, step by 2"
        # position * div_term multiplies shape (seq_len, 1) with shape (d_model/2) 
        # using broadcasting, resulting in shape (seq_len, d_model/2)
        pe[:, 0::2] = torch.sin(position * div_term)
        
        # Step 5: Apply the cosine formula to odd dimensions (1, 3, 5, ...)
        # Slicing notation '1::2' means: "start at index 1, step by 2"
        pe[:, 1::2] = torch.cos(position * div_term)
        
        # Step 6: Add a batch dimension at index 0
        # pe shape: (seq_len, d_model) -> .unsqueeze(0) -> shape (1, seq_len, d_model)
        # Why? Because our training batches will have shape (batch_size, seq_len, d_model).
        # When we add `pe` to `x`, PyTorch will automatically replicate (broadcast) 
        # this single positional encoding matrix across all batch items.
        pe = pe.unsqueeze(0)

        # Step 7: Register this tensor as a buffer.
        # A "buffer" in PyTorch is a state tensor that is part of the model but is 
        # NOT a learnable parameter (it won't be updated by gradient descent / optimizer).
        # It is saved along with the model's weights and moved to the GPU when you call model.to('cuda').
        self.register_buffer('pe', pe)
        
    def forward(self, x):
        # x shape: (batch_size, seq_len, d_model)
        #
        # self.pe[:, :x.shape[1], :] extracts the positional encoding up to the current sequence length.
        # .requires_grad_(False) explicitly prevents gradients from being calculated for this tensor 
        # because the sine/cosine values are fixed and do not need to be updated.
        x = x + (self.pe[:, :x.shape[1], :]).requires_grad_(False)
        
        # Apply dropout to the combined token and positional embeddings
        return self.dropout(x)


class LayerNormalization(nn.Module):
    """
    Layer Normalization stabilizes training by ensuring that the features (dimensions)
    of each word embedding have a mean of 0 and a standard deviation of 1.
    
    Formula:
        y = alpha * (x - mean) / (std + eps) + bias
        
    - alpha (gamma) is a learnable scaling factor (initialized to 1).
    - bias (beta) is a learnable shift factor (initialized to 0).
    - eps (epsilon) is a tiny value (like 1e-6) added to prevent division by zero.
    """
    def __init__(self, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        # nn.Parameter wraps a tensor so PyTorch recognizes it as a learnable weight
        self.alpha = nn.Parameter(torch.ones(1)) # Multiplicative scale
        self.bias = nn.Parameter(torch.zeros(1))  # Additive shift
    
    def forward(self, x):
        # x shape: (batch_size, seq_len, d_model)
        # 
        # dim=-1 means we compute the mean and std along the last dimension (d_model).
        # This normalizes each word's embedding vector individually.
        #
        # keepdim=True preserves the dimension so that shape remains (batch_size, seq_len, 1).
        # This is crucial so that PyTorch can broadcast (subtract/divide) this mean/std 
        # value against the original tensor `x` of shape (batch_size, seq_len, d_model).
        mean = x.mean(dim=-1, keepdim=True)
        std = x.std(dim=-1, keepdim=True)
        
        # Standard normalization formula with learnable scale (alpha) and shift (bias)
        return self.alpha * (x - mean) / (std + self.eps) + self.bias


class FeedForward(nn.Module):
    """
    A simple two-layer fully connected (dense) feed-forward neural network 
    applied to each position (word) in the sequence individually and identically.
    
    Formula:
        FFN(x) = max(0, x * W1 + B1) * W2 + B2
    """
    def __init__(self, d_model, d_ff, dropout):
        super().__init__()
        # Linear layer 1: Projects representation from d_model (e.g. 512) to a larger space d_ff (e.g. 2048)
        self.linear1 = nn.Linear(d_model, d_ff) 
        self.dropout = nn.Dropout(dropout)
        # Linear layer 2: Projects representation back to d_model (e.g. 512)
        self.linear2 = nn.Linear(d_ff, d_model) 
    
    def forward(self, x):
        # 1. self.linear1(x) -> (batch_size, seq_len, d_ff)
        # 2. torch.relu(...) -> Applies Rectified Linear Unit activation function
        # 3. self.dropout(...) -> Zeroes out random activations to reduce overfitting
        # 4. self.linear2(...) -> Projects back to (batch_size, seq_len, d_model)
        return self.linear2(self.dropout(torch.relu(self.linear1(x))))


class MultiHeadAttentionBlock(nn.Module):
    """
    Allows the model to jointly attend to information from different representation 
    subspaces at different positions. Instead of computing attention once over the 
    whole d_model, we split the embedding size into 'h' different "heads" and 
    compute attention on each head separately.
    """
    def __init__(self, d_model, h, dropout):
        super().__init__()
        self.d_model = d_model  # Embedding size (e.g., 512)
        self.h = h              # Number of attention heads (e.g., 8)
        assert d_model % h == 0, "d_model must be divisible by h"

        # Dimension of each head (e.g., 512 / 8 = 64)
        self.d_k = d_model // h

        # Linear projections for Query, Key, and Value tensors.
        # We project the input embeddings into Q, K, and V spaces.
        self.w_q = nn.Linear(d_model, d_model, bias=False)
        self.w_k = nn.Linear(d_model, d_model, bias=False)
        self.w_v = nn.Linear(d_model, d_model, bias=False)

        # Final projection layer to merge the concatenated head outputs back to d_model
        self.w_o = nn.Linear(d_model, d_model, bias=False)
        self.dropout = nn.Dropout(dropout)

    @staticmethod
    def attention(query, key, value, mask, dropout: nn.Dropout):
        """
        Computes Scaled Dot-Product Attention:
            Attention(Q, K, V) = softmax( (Q @ K^T) / sqrt(d_k) ) @ V
        """
        # query shape: (batch_size, h, seq_len, d_k)
        # key shape:   (batch_size, h, seq_len, d_k)
        # value shape: (batch_size, h, seq_len, d_k)
        d_k = query.shape[-1] # Gets the size of the last dimension (d_k)
        
        # Step 1: Calculate Query-Key dot products (similarity scores)
        # key.transpose(-2, -1) swaps the last two dimensions of the key tensor:
        #   (batch_size, h, seq_len, d_k) -> (batch_size, h, d_k, seq_len)
        #
        # Matrix multiplication using '@':
        #   (batch_size, h, seq_len, d_k) @ (batch_size, h, d_k, seq_len) 
        #   -> Output shape: (batch_size, h, seq_len, seq_len)
        # 
        # Scaling: Divide by sqrt(d_k) to prevent dot products from becoming too large 
        # (which makes softmax gradients extremely small).
        scores = (query @ key.transpose(-2, -1)) / (d_k ** 0.5)

        # Step 2: Masking (Optional)
        # For padding tokens or future tokens (in the decoder), we mask them.
        # mask is 0 at positions we want to ignore.
        # masked_fill replaces all 0s in mask with negative infinity (-inf).
        # Softmax(-inf) is exactly 0, meaning the model pays zero attention to those tokens.
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))

        # Step 3: Softmax to get probability distribution (attention weights)
        # dim=-1 means apply softmax across the last dimension (column-wise).
        scores = torch.softmax(scores, dim=-1)
        
        # Step 4: Dropout on attention weights
        if dropout is not None:
            scores = dropout(scores)
        
        # Step 5: Multiply weights by Values
        # (batch_size, h, seq_len, seq_len) @ (batch_size, h, seq_len, d_k) 
        # -> Output shape: (batch_size, h, seq_len, d_k)
        #
        # Also return the scores so we can plot/visualize attention maps.
        return (scores @ value, scores)

    def forward(self, q, k, v, mask):
        # Inputs q, k, v shape: (batch_size, seq_len, d_model)
        
        # 1. Project inputs into Query, Key, and Value spaces
        query = self.w_q(q) # shape: (batch_size, seq_len, d_model)
        key = self.w_k(k)   # shape: (batch_size, seq_len, d_model)
        value = self.w_v(v) # shape: (batch_size, seq_len, d_model)
        
        # 2. Split into multiple heads.
        #
        # How view() works here:
        # We change (batch_size, seq_len, d_model) -> (batch_size, seq_len, h, d_k)
        #
        # How transpose(1, 2) works here:
        # Swaps dimension 1 and 2 to obtain shape: (batch_size, h, seq_len, d_k)
        # Why? Because we want each head (dimension 1) to evaluate the entire sequence (seq_len) 
        # independently. PyTorch matrix multiplication is parallelized across leading dimensions.
        query = query.view(query.shape[0], query.shape[1], self.h, self.d_k).transpose(1, 2)
        key = key.view(key.shape[0], key.shape[1], self.h, self.d_k).transpose(1, 2)
        value = value.view(value.shape[0], value.shape[1], self.h, self.d_k).transpose(1, 2)

        # 3. Compute Attention
        # x shape: (batch_size, h, seq_len, d_k)
        # self.attention_scores shape: (batch_size, h, seq_len, seq_len)
        x, self.attention_scores = MultiHeadAttentionBlock.attention(query, key, value, mask, self.dropout)

        # 4. Concatenate heads back together.
        #
        # First, transpose(1, 2) swaps back: (batch_size, h, seq_len, d_k) -> (batch_size, seq_len, h, d_k)
        #
        # .contiguous() is required here because transpose changes the memory stride layout.
        # view() requires memory to be contiguous. If you call view() on a transposed tensor 
        # without .contiguous(), PyTorch throws a runtime error.
        #
        # .view(x.shape[0], -1, self.d_model) flattens the last two dimensions (h and d_k) back to d_model.
        # -1 automatically computes the seq_len dimension.
        # Output shape: (batch_size, seq_len, d_model)
        x = x.transpose(1, 2).contiguous().view(x.shape[0], -1, self.d_model)
        
        # 5. Project the combined output back through a linear layer
        # Output shape: (batch_size, seq_len, d_model)
        x = self.w_o(x)
        return x


class ResidualConnection(nn.Module):
    """
    Implements a residual connection (skip-connection) followed by layer normalization.
    
    Formula:
        Output = x + Dropout( Sublayer( LayerNorm(x) ) )
        
    This is often referred to as "Pre-LN" (Layer Normalization applied BEFORE the sublayer),
    which makes deep networks much easier to train and stabilize compared to Post-LN.
    """
    def __init__(self, dropout: float):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        self.norm = LayerNormalization()
    
    def forward(self, x, sublayer):
        # x: original input tensor
        # sublayer: a lambda function representing the attention or feedforward block
        #
        # 1. self.norm(x) -> Normalize input
        # 2. sublayer(...) -> Pass normalized input to attention/FFN
        # 3. self.dropout(...) -> Apply dropout to sublayer output
        # 4. x + ... -> Add the original input (skip connection)
        return x + self.dropout(sublayer(self.norm(x)))


class EncoderBlock(nn.Module):
    """
    An Encoder block consists of two sublayers:
    1. Multi-head self-attention
    2. Position-wise Feed Forward network
    
    Both sublayers are wrapped in Residual Connections.
    """
    def __init__(self, self_attention_block, feed_forward_block, dropout):
        super().__init__()
        self.self_attention_block = self_attention_block
        self.feed_forward_block = feed_forward_block
        # We need two residual connections: one for attention, one for FFN
        self.residual_connection = [ResidualConnection(dropout) for _ in range(2)]
    
    def forward(self, x, mask):
        # Sublayer 1: Self-Attention
        # In encoder self-attention, Query, Key, and Value are all the SAME input tensor 'x'.
        # lambda function lets us pass x to attention and wrap it inside the residual block.
        x = self.residual_connection[0](x, lambda x: self.self_attention_block(x, x, x, mask))
        
        # Sublayer 2: Feed Forward Network
        x = self.residual_connection[1](x, self.feed_forward_block)
        return x


class Encoder(nn.Module):
    """
    A stack of N EncoderBlocks.
    """
    def __init__(self, layers: nn.ModuleList):
        super().__init__()
        # nn.ModuleList is like a normal python list, but registered as a module 
        # so PyTorch knows how to keep track of its gradients and parameters.
        self.layers = layers
        self.norm = LayerNormalization()
    
    def forward(self, x, mask):
        # Feed the output of one encoder block into the next sequentially
        for layer in self.layers:
            x = layer(x, mask)
        # Final layer normalization
        return self.norm(x)


class DecoderBlock(nn.Module):
    """
    A Decoder block consists of three sublayers:
    1. Masked Multi-head self-attention (over target sequence)
    2. Multi-head cross-attention (Query from decoder, Key and Value from encoder output)
    3. Position-wise Feed Forward network
    """
    def __init__(self, self_attention_block, cross_attention_block, feed_forward_block, dropout):
        super().__init__()
        self.self_attention_block = self_attention_block
        self.cross_attention_block = cross_attention_block
        self.feed_forward_block = feed_forward_block
        # We need three residual connections (one for each sublayer)
        # Note: Wrapped in nn.ModuleList so parameters are properly registered.
        self.residual_connection = nn.ModuleList([ResidualConnection(dropout) for _ in range(3)])
    
    def forward(self, x, encoder_output, src_mask, tgt_mask):
        # Sublayer 1: Self-Attention (Decoder attends to past generated target tokens)
        # Uses 'tgt_mask' to prevent attending to future tokens (causal masking).
        x = self.residual_connection[0](x, lambda x: self.self_attention_block(x, x, x, tgt_mask))
        
        # Sublayer 2: Cross-Attention
        # Query (Q) comes from the Decoder itself ('x').
        # Key (K) and Value (V) come from the Encoder's output ('encoder_output' / memory).
        # This is how the decoder looks at the original source sentence to translate/generate.
        x = self.residual_connection[1](x, lambda x: self.cross_attention_block(x, encoder_output, encoder_output, src_mask))
        
        # Sublayer 3: Feed Forward network
        x = self.residual_connection[2](x, self.feed_forward_block)
        return x


class Decoder(nn.Module):
    """
    A stack of N DecoderBlocks.
    """
    def __init__(self, layers: nn.ModuleList):
        super().__init__()
        self.layers = layers
        self.norm = LayerNormalization()
    
    def forward(self, x, encoder_output, src_mask, tgt_mask):
        for layer in self.layers:
            x = layer(x, encoder_output, src_mask, tgt_mask)
        # Final layer normalization
        return self.norm(x)


class ProjectionLayer(nn.Module):
    """
    Takes the final output of the Decoder and maps it to vocabulary logits (scores).
    """
    def __init__(self, d_model, vocab_size):
        super().__init__()
        # A simple linear layer that maps from d_model (e.g. 512) to the size of target vocabulary.
        self.proj = nn.Linear(d_model, vocab_size)
    
    def forward(self, x):
        # x shape: (batch_size, seq_len, d_model)
        # Output shape: (batch_size, seq_len, vocab_size)
        #
        # torch.log_softmax computes logarithm of softmax probabilities over dim=-1 (vocab_size).
        # Log-softmax is used because it is numerically more stable during loss computation 
        # (e.g., when paired with Negative Log-Likelihood loss, nn.NLLLoss).
        return torch.log_softmax(self.proj(x), dim=-1)


class Transformer(nn.Module):
    """
    The full Transformer architecture integrating the Encoder, Decoder, 
    embeddings, positional encodings, and projection layer.
    """
    def __init__(self, encoder, decoder, src_embed, tgt_embed, src_pos, tgt_pos, proj_layer):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = src_embed
        self.tgt_embed = tgt_embed
        self.src_pos = src_pos
        self.tgt_pos = tgt_pos
        self.proj_layer = proj_layer
    
    def encode(self, src, src_mask):
        # 1. Convert token IDs to vectors
        src = self.src_embed(src)
        # 2. Add positional indicators
        src = self.src_pos(src)
        # 3. Process through the stacked encoder layers
        return self.encoder(src, src_mask)
    
    def decode(self, tgt, encoder_output, src_mask, tgt_mask):
        # 1. Convert target token IDs to vectors
        tgt = self.tgt_embed(tgt)
        # 2. Add positional indicators
        tgt = self.tgt_pos(tgt)
        # 3. Process through stacked decoder layers (attending to encoder output)
        return self.decoder(tgt, encoder_output, src_mask, tgt_mask)

    def project(self, x):
        # Convert final decoder vectors into word prediction scores
        return self.proj_layer(x)
    
    def forward(self, src, tgt, src_mask, tgt_mask):
        # Step 1: Run Encoder on source sentence
        encoder_output = self.encode(src, src_mask)
        # Step 2: Run Decoder on target sentence
        decoder_output = self.decode(tgt, encoder_output, src_mask, tgt_mask)
        # Step 3: Project to get probability distributions over vocabulary
        return self.project(decoder_output)


def build_transformer(
    src_vocab_size: int, 
    tgt_vocab_size: int, 
    src_seq_len: int, 
    tgt_seq_len: int, 
    d_model: int = 512, 
    h: int = 8, 
    num_layers: int = 6, 
    dropout: float = 0.1, 
    d_ff: int = 2048
):
    """
    A helper (factory) function that instantiates and constructs a complete Transformer model.
    """
    # 1. Create embeddings for source and target sequences
    src_embed = InputEmbeddings(d_model, src_vocab_size)
    tgt_embed = InputEmbeddings(d_model, tgt_vocab_size)
    
    # 2. Create positional encoding tables
    src_pos = PositionalEmbeddings(d_model, src_seq_len, dropout)
    tgt_pos = PositionalEmbeddings(d_model, tgt_seq_len, dropout)
    
    # 3. Create the stacked list of Encoder layers
    encoder_blocks = []
    for _ in range(num_layers):
        self_attention_block = MultiHeadAttentionBlock(d_model, h, dropout)
        feed_forward_block = FeedForward(d_model, d_ff, dropout)
        encoder_block = EncoderBlock(self_attention_block, feed_forward_block, dropout)
        encoder_blocks.append(encoder_block)

    # 4. Create the stacked list of Decoder layers
    decoder_blocks = []
    for _ in range(num_layers):
        self_attention_block = MultiHeadAttentionBlock(d_model, h, dropout)
        cross_attention_block = MultiHeadAttentionBlock(d_model, h, dropout)
        feed_forward_block = FeedForward(d_model, d_ff, dropout)
        decoder_block = DecoderBlock(self_attention_block, cross_attention_block, feed_forward_block, dropout)
        decoder_blocks.append(decoder_block)

    # 5. Wrap block lists into PyTorch modules
    encoder = Encoder(nn.ModuleList(encoder_blocks))
    decoder = Decoder(nn.ModuleList(decoder_blocks))
    
    # 6. Create the final classification layer
    proj_layer = ProjectionLayer(d_model, tgt_vocab_size)
    
    # 7. Construct the complete Transformer architecture
    transformer = Transformer(encoder, decoder, src_embed, tgt_embed, src_pos, tgt_pos, proj_layer)
    
    # 8. Parameter Initialization:
    # Initialize weights using Xavier Uniform method (also called Glorot initialization).
    # This keeps scale of output variances in linear layers constant across layers, 
    # preventing exploding/vanishing gradients at start of training.
    # Note: Only initialize weights that are multi-dimensional (dim > 1).
    for p in transformer.parameters():
        if p.dim() > 1:
            nn.init.xavier_uniform_(p)
            
    return transformer