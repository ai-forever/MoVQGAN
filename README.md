# MoVQGAN

[![Framework: PyTorch](https://img.shields.io/badge/Framework-PyTorch-orange.svg)](https://pytorch.org/) [![Huggingface space](https://img.shields.io/badge/🤗-Huggingface-yello.svg)](https://huggingface.co/ai-forever/MoVQGAN)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EVKDFsa17VgdyiaPdbKShBIm4N_18Xlj?usp=sharing)

[Habr post]()

MoVQGAN is a new SOTA model in the image reconstruction problem. This model is based on code from the [VQGAN](https://github.com/CompVis/taming-transformers) repository and modifications from the original [MoVQGAN](https://arxiv.org/pdf/2209.09002.pdf) paper.

## Models
+ [67M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_67M.ckpt)
+ [102M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_102M.ckpt)
+ [270M MoVQGAN](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_270M.ckpt)

The following table shows a comparison of the models on the Imagenet dataset in terms of FID, SSIM, and PSNR metrics. A more detailed description of the experiments and a comparison with other models can be found in the [Habr post]().

|Model|Latent size|Num Z|Train steps|FID|SSIM|PSNR|L1|
|:----|:----|:----|:----|:----|:----|:----|:----|
|[ViT-VQGAN\*](https://arxiv.org/pdf/2110.04627.pdf)|32x32|8192|500000|1,28|\-|\-|\-|
|[RQ-VAE\*](https://arxiv.org/pdf/2203.01941.pdf)|8x8x16|16384|10 epochs|1,83|\-|\-|\-|
|[Mo-VQGAN\*](https://arxiv.org/pdf/2209.09002.pdf)|16x16x4|1024|40 epochs|1,12|0,6731|22,42|\-|
| [VQ CompVis](https://github.com/CompVis/latent-diffusion)| 32x32| 16384 | 971043| 1,34| 0,6499| 23,8469| 0,0533|
| [KL CompVis](https://github.com/CompVis/latent-diffusion)| 32x32| \- | 246803| 0,9682| 0,6918| 25,1121| 0,0474|
| [SBER-VQGAN (from pretrain)](https://habr.com/ru/companies/sberbank/articles/581738/)| 32x32| 8192| 1 epoch| 1,4378| 0,6816| 24,3135| 0,0503|
| [SBER-MoVQGAN 67M](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_67M.ckpt) | 32x32 | 16384 | 2M | 0,9647| 0,7249| 26,4485| 0,0415
| [SBER-MoVQGAN 102M](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_102M.ckpt)|32x32|16384|2360k|0,7764|0,7373 | 26,8887| 0,0398|
|[SBER-MoVQGAN 270M](https://huggingface.co/ai-forever/MoVQGAN/resolve/main/movqgan_270M.ckpt)|32x32|16384|1330k| **0,6858**| **0,7411**| **27,0370**| **0,0393**|

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
Check jupyter notebook with example in `./notebooks` folder or [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EVKDFsa17VgdyiaPdbKShBIm4N_18Xlj?usp=sharing)

## Examples
![](./examples/examples.png)

## Authors
+ Anastasia Maltseva: [Github](https://github.com/NastyaMittseva)
+ Arseniy Shakhmatov: [Github](https://github.com/cene555), [Blog](https://t.me/gradientdip)
+ Andrey Kuznetsov: [Github](https://github.com/kuznetsoffandrey), [Blog](https://t.me/complete_ai)
+ Denis Dimitrov: [Github](https://github.com/denndimitrov), [Blog](https://t.me/dendi_math_ai)