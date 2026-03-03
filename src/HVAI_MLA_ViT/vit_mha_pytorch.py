import torch
from torch import nn
from torch.nn import Module, ModuleList

from einops import rearrange, repeat
from einops.layers.torch import Rearrange


import torch
import torch.nn as nn
from torch.nn import Module, ModuleList
from einops import rearrange, repeat                                                                                                                          
from einops.layers.torch import Rearrange
                                                                                                                           
                                                                                                                                                                                          
def pair(t):
    return t if isinstance(t, tuple) else (t, t)
                                                                                                                
                                                                                                                              
class FeedForward(Module):
    def __init__(self, dim, hidden_dim, dropout = 0.):
        super().__init__()
        self.net = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, dim),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        return self.net(x)
                                                                

class Transformer(Module):
    def __init__(self, dim, depth, heads, mlp_dim, dropout = 0.):
        super().__init__()
        self.norm = nn.LayerNorm(dim)
        self.layers = ModuleList([])
                                                                                                                                                                                                  
        for _ in range(depth):                                 
            self.layers.append(ModuleList([
                nn.MultiheadAttention(embed_dim = dim, num_heads = heads, batch_first=True), 
                FeedForward(dim, mlp_dim, dropout = dropout)                         
            ]))                                                                                                                             
                                                                                                                                                  
    def forward(self, x):                                                  
        for attn, ff in self.layers:                                                                                     
            #print("&&&&&&&&&&&&&&&&&&&7____x.shape:", x.shape)

            
            out_data, _ = attn(x, x, x)
            x = out_data + x            
            x = ff(x) + x                                                                                                  
                                                                                             
        return self.norm(x)                                                                                                           
                                                                                                        
class ViT_mha_pytorch(Module):                                                                                                                                                             
    def __init__(self, *,  image_size, patch_size, num_classes, embed_dim, depth, heads, mlp_dim, pool = 'cls', channels = 3, dropout = 0., emb_dropout = 0.):
        super().__init__()
        image_height, image_width = pair(image_size)
        patch_height, patch_width = pair(patch_size)

        assert image_height % patch_height == 0 and image_width % patch_width == 0, 'Image dimensions must be divisible by the patch size.'

        num_patches = (image_height // patch_height) * (image_width // patch_width)
        patch_dim = channels * patch_height * patch_width

        assert pool in {'cls', 'mean'}, 'pool type must be either cls (cls token) or mean (mean pooling)'
        num_cls_tokens = 1 if pool == 'cls' else 0

        self.to_patch_embedding = nn.Sequential(
            Rearrange('b c (h p1) (w p2) -> b (h w) (p1 p2 c)', p1 = patch_height, p2 = patch_width),
            nn.LayerNorm(patch_dim),
            nn.Linear(patch_dim, embed_dim),
            nn.LayerNorm(embed_dim),
        )                                                                  
                                                            
        self.cls_token = nn.Parameter(torch.randn(num_cls_tokens, embed_dim))
        self.pos_embedding = nn.Parameter(torch.randn(num_patches + num_cls_tokens, embed_dim))

        self.dropout = nn.Dropout(emb_dropout)

        self.transformer = Transformer(embed_dim, depth, heads, mlp_dim, dropout)

        self.pool = pool
        self.to_latent = nn.Identity()

        self.mlp_head = nn.Linear(embed_dim, num_classes)

    def forward(self, img):
        batch = img.shape[0]
        x = self.to_patch_embedding(img)

        cls_tokens = repeat(self.cls_token, '... d -> b ... d', b = batch)
        x = torch.cat((cls_tokens, x), dim = 1)

        seq = x.shape[1]

        x = x + self.pos_embedding[:seq]
        x = self.dropout(x)

        x = self.transformer(x)

        x = x.mean(dim = 1) if self.pool == 'mean' else x[:, 0]

        x = self.to_latent(x)
        return self.mlp_head(x)