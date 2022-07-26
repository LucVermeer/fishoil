import torch
import torch.nn as nn

class LSTM(nn.LSTM):
    def __init__(self, args):
        self.LSTM = super().init(**args)