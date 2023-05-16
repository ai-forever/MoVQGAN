import numpy as np
import random
import pandas as pd
from tqdm import tqdm
from PIL import Image
import io
import os

import torch
import sys, time
from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as pl

from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from tqdm import tqdm
from random import randint

try:
    from torchvision.transforms import InterpolationMode

    BICUBIC = InterpolationMode.BICUBIC
except ImportError:
    BICUBIC = Image.BICUBIC


def _convert_image_to_rgb(image):
    return image.convert("RGB")


def _transform(n_px):
    return Compose(
        [
            Resize(n_px, interpolation=BICUBIC),
            CenterCrop(n_px),
            _convert_image_to_rgb,
            ToTensor(),
            Normalize(
                (0.48145466, 0.4578275, 0.40821073),
                (0.26862954, 0.26130258, 0.27577711),
            ),
        ]
    )


def center_crop(image):
    width, height = image.size
    new_size = min(width, height)
    left = (width - new_size) / 2
    top = (height - new_size) / 2
    right = (width + new_size) / 2
    bottom = (height + new_size) / 2
    return image.crop((left, top, right, bottom))


class ImageDataset(Dataset):
    def __init__(
        self,
        df_path,
        image_size=256,
        infinity=False,
    ):
        self.df = pd.read_csv(df_path, sep='\t')
        self.image_size = image_size
        self.infinity = infinity

    def __len__(self):
        if self.infinity:
            return 99999999
        else:
            return len(self.df)

    def __getitem__(self, item):
        if self.infinity:
            ind = randint(0, len(self.df) - 1)
        else:
            ind = item
        image = Image.open(self.df["image_name"].iloc[ind])
        image = center_crop(image)
        image = image.resize(
            (self.image_size, self.image_size), resample=Image.BICUBIC, reducing_gap=1
        )
        image = np.array(image.convert("RGB"))
        image = image.astype(np.float32) / 127.5 - 1
        
        return np.transpose(image, [2, 0, 1])


def create_loader(batch_size, num_workers, shuffle=False, **dataset_params):
    dataset = ImageDataset(**dataset_params)
    return DataLoader(
        dataset,
        batch_size=batch_size,
        num_workers=num_workers,
        shuffle=shuffle,
        pin_memory=True,
    )


class LightningDataModule(pl.LightningDataModule):
    """PyTorch Lightning data class"""

    def __init__(self, train_config):
        super().__init__()
        self.train_config = train_config

    def train_dataloader(self):
        return create_loader(**self.train_config)