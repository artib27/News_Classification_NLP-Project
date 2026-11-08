import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    """
    A simple feed-forward neural network.
    Architecture:
      - FC: input -> 128 (ReLU + Dropout 0.5)
      - FC: 128 -> 64 (ReLU + Dropout 0.5)
      - FC: 64 -> 32 (ReLU)
      - FC: 32 -> num_classes (output logits)
    """
    def __init__(self, input_dim, num_classes):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.dropout1 = nn.Dropout(0.5)
        self.fc2 = nn.Linear(128, 64)
        self.dropout2 = nn.Dropout(0.5)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout1(x)
        x = F.relu(self.fc2(x))
        x = self.dropout2(x)
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x
	