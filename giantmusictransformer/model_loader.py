#===================================================================================================
# Giant Music Transformer model_loader Python module
#===================================================================================================
# Project Los Angeles
# Tegridy Code 2024
#===================================================================================================
# License: Apache 2.0
#===================================================================================================

import os
os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'

#===================================================================================================

from huggingface_hub import hf_hub_download

from models import *

import torch

from x_transformer_1_23_2 import TransformerWrapper, AutoregressiveWrapper, Decoder

from torchsummary import summary

#===================================================================================================

def load_model(model_size='medium', device='cuda', verbose=False):

    if verbose:
        os.environ['HF_HUB_DISABLE_PROGRESS_BARS'] = '0'
        
        print('=' * 70)
        print('Selected model:', model_size.title(), '/', MODELS_PARAMETERS[model_size]['params'], 'M params')
        print('=' * 70)
        print('Model info:')
        print('-' * 70)
        print(MODELS_INFO[model_size])

        print('=' * 70)
        print('Downloading model...')

    else:
        os.environ['HF_HUB_DISABLE_PROGRESS_BARS'] = '1'

    model_data = hf_hub_download(repo_id=MODELS_HF_REPO_LINK,
                                filename=MODELS_FILE_NAMES[model_size]
                                )

    if verbose:
        print('Done!')
        print('=' * 70)
        
        print('Instantiating model...')
    
    gmt_model = TransformerWrapper( num_tokens = MODELS_PAD_IDX+1,
                                    max_seq_len = MODELS_SEQ_LEN,
                                    attn_layers = Decoder(dim = MODELS_PARAMETERS[model_size]['dim'],
                                                          depth = MODELS_PARAMETERS[model_size]['depth'],
                                                          heads = MODELS_PARAMETERS[model_size]['heads'],
                                                          rotary_pos_emb = MODELS_PARAMETERS[model_size]['rope'],
                                                          attn_flash = True
                                                         )
                                    )
    
    gmt_model = AutoregressiveWrapper(gmt_model, ignore_index = MODELS_PAD_IDX, pad_value=MODELS_PAD_IDX)

    if verbose:
        print('Done!')
        print('=' * 70)
        
        print('Loading model...')
    
    gmt_model.load_state_dict(torch.load(model_data, weights_only=True))

    if verbose:
        print('Done!')
        print('=' * 70)
    
        print('Activating model...')
        
    gmt_model.to(device)
    gmt_model.eval()  

    if verbose:
        print('Done!')
        print('=' * 70)
        
        summary(gmt_model)

    return gmt_model

#===================================================================================================
# This is the end of model_loader Python module
#===================================================================================================