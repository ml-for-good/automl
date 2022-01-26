import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from model import *
from colorama import Fore
from metric import *
import pandas as pd


class SeedDataset(Dataset):

    def __init__(self, annotations_file):
        super().__init__()
        self.data: pd.DataFrame = pd.read_csv(annotations_file)
        self.data: pd.DataFrame = self.data[self.data['label'].notna()]
        self.Y = self.data['label']
        self.X = self.data.drop(columns=['id', 'label', 'utm_channel']).fillna(value=-1)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return torch.as_tensor(self.X.iloc[idx].values).type(torch.FloatTensor), torch.as_tensor(self.Y.iloc[idx]).type(
            torch.LongTensor)


def train(dataloader, model, loss_fn, optimizer, device, positive_weight):
    model.train()

    Y = []
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        logit = model(X)
        positive_index = y == 1

        loss = loss_fn(logit, y)
        loss = (positive_weight * loss_fn(logit[positive_index], y[positive_index]) + loss_fn(logit[~positive_index], y[
            ~positive_index])) / len(X)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss = loss.item()
            print(f"{Fore.GREEN + '[train]===>'} loss: {loss} {'' + Fore.RESET}")


def valid(dataloader, model, loss_fn, device):
    model.eval()

    num_dataset = len(dataloader.dataset)
    loss = 0

    with torch.no_grad():
        pred, Y = [], []
        for batch, (X, y) in enumerate(dataloader):
            X, y = X.to(device), y.to(device)

            logit = model(X)
            loss += loss_fn(logit, y).item()

            pred.append(logit.argmax(1))
            Y.append(y)

        loss /= num_dataset

        pred = torch.cat(pred)
        Y = torch.cat(Y)
        print(f"{Fore.CYAN + '[valid]===>'} " \
              f"loss: {loss}  acc: {100 * Accuracy(pred, Y)}%  precision: {Precision(pred, Y)}  recall: {Recall(pred, Y)}   fscore: {Fscore(pred, Y)}" \
              f"{'' + Fore.RESET}")
    return loss


if __name__ == '__main__':

    torch.manual_seed(777)
    device = torch.device('cpu')

    batch_size, in_features, out_features = 30, 27, 2
    lr, positive_weight = 1e-3, 2.33
    epochs = 40

    model = Fake1DAttention(in_features, out_features)
    loss_fn = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=0.001)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min')

    train_dataset = SeedDataset("./data/train.csv")
    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    valid_dataset = SeedDataset("./data/valid.csv")
    valid_dataloader = DataLoader(valid_dataset, batch_size=1, shuffle=False)


    for t in range(epochs):
        print(f"{Fore.GREEN + '===>'} Epoch {t + 1} {'' + Fore.RESET}\n" \
              "---------------------------------------")
        train(train_dataloader, model, loss_fn, optimizer, device, positive_weight)
        val_loss = valid(valid_dataloader, model, loss_fn, device)
        scheduler.step(val_loss)
        torch.save(model.state_dict(), f"./checkpoints/{t}_epoc.pt")
