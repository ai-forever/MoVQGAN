import os

import torch
from huggingface_hub import hf_hub_url, cached_download

from .models.vqgan import MOVQ


__all__ = ['MOVQ', 'get_movqgan_model']
            

MODELS = {
    '67M': dict(
        description='',
        model_params=dict(
            ddconfig={
                "double_z": False,
                "z_channels": 4,
                "resolution": 256,
                "in_channels": 3,
                "out_ch": 3,
                "ch": 128,
                "ch_mult": [1, 2, 2, 4],
                "num_res_blocks": 2,
                "attn_resolutions": [32],
                "dropout": 0.0,
            },
            n_embed=16384,
            embed_dim=4,
        ),
        repo_id='ai-forever/MoVQGAN',
        filename='movqgan_67M.ckpt',
        authors='SberAI',
        full_description='',
    ),
    '102M': dict(
        description='',
        model_params=dict(
            ddconfig={
                "double_z": False,
                "z_channels": 4,
                "resolution": 256,
                "in_channels": 3,
                "out_ch": 3,
                "ch": 128,
                "ch_mult": [1, 2, 2, 4],
                "num_res_blocks": 4,
                "attn_resolutions": [32],
                "dropout": 0.0,
            },
            n_embed=16384,
            embed_dim=4,
        ),
        repo_id='ai-forever/MoVQGAN',
        filename='movqgan_102M.ckpt',
        authors='SberAI',
        full_description='',
    ),
    '270M': dict(
        description='',
        model_params=dict(
            ddconfig={
                "double_z": False,
                "z_channels": 4,
                "resolution": 256,
                "in_channels": 3,
                "out_ch": 3,
                "ch": 256,
                "ch_mult": [1, 2, 2, 4],
                "num_res_blocks": 2,
                "attn_resolutions": [32],
                "dropout": 0.0,
            },
            n_embed=16384,
            embed_dim=4,
        ),
        repo_id='ai-forever/MoVQGAN',
        filename='movqgan_270M.ckpt',
        authors='SberAI',
        full_description='',
    )
}


def get_movqgan_model(name, pretrained=True, device='cuda', cache_dir='/tmp/movqgan', **model_kwargs):
    assert name in MODELS

    config = MODELS[name].copy()
    config['model_params'].update(model_kwargs)
    model = MOVQ(**config['model_params'])
    if pretrained:
        cache_dir = os.path.join(cache_dir, name)
        config_file_url = hf_hub_url(repo_id=config['repo_id'], filename=config['filename'])
        cached_download(config_file_url, cache_dir=cache_dir, force_filename=config['filename'])
        checkpoint = torch.load(os.path.join(cache_dir, config['filename']))
        model.load_state_dict(checkpoint, strict=False)
    model.eval()
    model = model.to(device)
    return model