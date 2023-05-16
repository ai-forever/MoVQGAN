import pytorch_lightning as pl
from omegaconf import OmegaConf
import torch
import os
from movqgan.data.dataset import LightningDataModule
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor
from pytorch_lightning.loggers import WandbLogger
from movqgan.util import instantiate_from_config
import movqgan

os.environ["WANDB_API_KEY"] = ""
os.environ["WANDB_MODE"] = "online"

config = OmegaConf.load('./configs/movqgan_270M.yaml')

model = instantiate_from_config(config['model'])
data = LightningDataModule(config['data']['train'])

if os.path.exists(config['ModelCheckpoint']['dirpath']) == False:
    os.makedirs(config['ModelCheckpoint']['dirpath'])
callbacks = [
        ModelCheckpoint(**config['ModelCheckpoint']),
        LearningRateMonitor(logging_interval='step')
]

wandb_logger = WandbLogger(project=config['wandb_project_name'])
trainer = pl.Trainer(logger=wandb_logger, callbacks=callbacks, **config['trainer'])

if config['ckpt_path'] == '':
    ckpt_path = None
else:
    ckpt_path = config['ckpt_path']
trainer.fit(model, data, ckpt_path=ckpt_path)