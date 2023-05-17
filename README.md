# MoVQGAN

[![Framework: PyTorch](https://img.shields.io/badge/Framework-PyTorch-orange.svg)](https://pytorch.org/) [![Huggingface space](https://img.shields.io/badge/🤗-Huggingface-yello.svg)](https://huggingface.co/ai-forever/MoVQGAN)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()

[Habr post]()

MoVQGAN is a new SOTA model in the image reconstruction problem. This model is based on code from the [VQGAN](https://github.com/CompVis/taming-transformers) repository and modifications from the original [MoVQGAN](https://arxiv.org/pdf/2209.09002.pdf) paper.

## Models
+ [67M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_67M.ckpt)
+ [102M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_102M.ckpt)
+ [270M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_67M.ckpt)

The following table shows a comparison of the models on the Imagenet dataset in terms of FID, SSIM, and PSNR metrics. A more detailed description of the experiments and a comparison with other models can be found in the [Habr post]().

|Model|Train steps|FID|SSIM|PSNR|
|:----|:----|:----|:----|:----|
|f=8, [ViT-VQGAN](https://arxiv.org/pdf/2110.04627.pdf)|500000|1,28|-|-|
|f=32, [RQ-VAE](https://arxiv.org/pdf/2203.01941.pdf)|10 epochs|1,83|-|-|
|f=16, [Mo-VQGAN](https://arxiv.org/pdf/2209.09002.pdf)|40 epochs|1,12|0,6731|22,42|
|f=8, VQ [CompVis](https://github.com/CompVis/latent-diffusion)|971043|1,14|-|23,07 +/- 3,99|
|f=8, KL [CompVis](https://github.com/CompVis/latent-diffusion)|246803|0,90|-|24,19 +/- 4,19|
| f=8, SBER-MoVQGAN 67M | 2M | 0,9647 | 0,7249 | 26,4485 |
| f=8, SBER-MoVQGAN 102M| 2360k | 0,7764 | 0,7373 | 26,8887 |
| f=8, SBER-MoVQGAN 270M | 1330k | **0,6858** | **0,7411** | **27,037** |

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

## Authors
+ Anastasia Maltseva: [Github](https://github.com/NastyaMittseva)
+ Arseniy Shakhmatov: [Github](https://github.com/cene555), [Blog](https://t.me/gradientdip)
+ Andrey Kuznetsov: [Github](https://github.com/kuznetsoffandrey), [Blog](https://t.me/complete_ai)
+ Denis Dimitrov: [Github](https://github.com/denndimitrov), [Blog](https://t.me/dendi_math_ai)