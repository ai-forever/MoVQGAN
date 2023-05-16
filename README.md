# MoVQGAN

[![Framework: PyTorch](https://img.shields.io/badge/Framework-PyTorch-orange.svg)](https://pytorch.org/) [![Huggingface space](https://img.shields.io/badge/🤗-Huggingface-yello.svg)](https://huggingface.co/ai-forever/MoVQGAN)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()

[Habr post]()

# Models
+ [67M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_67M.ckpt)
+ [102M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_102M.ckpt)
+ [270M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_67M.ckpt)

## How to use:
### Install
```
pip install "git+https://github.com/ai-forever/MoVQGAN.git"
```
### Train
```
python main.py --config configs/movqgan_270M.yaml
```
### Inference
Check jupyter notebook with example in `./notebooks` folder or [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()