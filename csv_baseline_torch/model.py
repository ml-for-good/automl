import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
import torch.nn as nn
from collections import Counter




class FCModel(nn.Module):
    def __init__(self, in_features, out_features) -> None:
        """Naive FCModel as reference.

        Args:
            in_features (int): input size for feature dimension
            out_features (int): output size for feature dimension
        """
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features

        self.fc1 = nn.Linear(self.in_features, 2 * self.in_features)
        self.bn1 = nn.BatchNorm1d(2 * self.in_features)
        self.activation1 = nn.ReLU()
        self.fc2 = nn.Linear(2 * self.in_features, self.in_features)
        self.bn2 = nn.BatchNorm1d(self.in_features)
        self.activation2 = nn.ReLU()
        self.fc3 = nn.Linear(self.in_features, self.out_features)

        self.softmax = nn.Softmax(1)
        self.model = nn.Sequential(self.fc1, self.activation1, self.bn1, self.fc2, self.bn2, self.activation2, self.fc3,
                                   self.softmax)

    def forward(self, x):
        return self.model(x)


class Fake1DAttention(nn.Module):

    def __init__(self, in_features, out_features):
        """Fake 1D attention model as reference.

        Args:
            in_features (int): input size for feature dimension
            out_features (int): output size for feature dimension
        """
        super().__init__()

        self.attn1 = nn.parameter.Parameter(torch.randn(in_features), requires_grad=True)
        self.fc1 = nn.Linear(in_features, 2 * in_features)
        self.activation1 = nn.ReLU()
        self.bn1 = nn.BatchNorm1d(2 * in_features)

        self.fc2 = nn.Linear(2 * in_features, in_features)
        self.activation2 = nn.ReLU()  # 激活函数
        self.bn2 = nn.BatchNorm1d(in_features)
        self.bn_in = nn.BatchNorm1d(in_features)
        self.fc3 = nn.Linear(in_features, out_features)
        self.softmax = nn.Softmax(1)

        self.model = nn.Sequential(
            self.fc1, self.activation1,  # self.bn1,
            self.fc2, self.activation2,  # self.bn2,
            self.fc3, self.softmax
        )

    def forward(self, x):
        # return self.model(self.attn1 * x)
        x = self.bn_in(x)
        x = F.relu(self.fc1(x))
        x = self.bn1(x)
        # print(x)

        x = F.relu(self.fc2(x))
        x = self.bn2(x)
        # print(x)

        x = self.fc3(x)
        x = torch.sigmoid(x)
        return x


if __name__ == '__main__':
    batch, in_features, out_features = 10, 10, 5
    model = FCModel(in_features, out_features)
    x = torch.randn(batch, in_features)
    print(model(x).shape)
