import torch


def Precision(pred: torch.Tensor, y: torch.Tensor):

    index_ = pred == 1
    TP = (y[index_] == 1).sum()

    return (TP / index_.sum()).item()


def Recall(pred: torch.Tensor, y: torch.Tensor):

    index_ = y == 1
    TP = (pred[index_] == 1).sum()

    return (TP / index_.sum()).item()


def Accuracy(pred: torch.Tensor, y: torch.Tensor):

    return ((pred == y).sum() / len(y)).item()


def Fscore(pred: torch.Tensor, y: torch.Tensor):

    P = Precision(pred, y)
    R = Recall(pred, y)
    F = 5 * P * R / (2 * P + 3 * R)

    return F


if __name__ == "__main__":
    pred = torch.tensor([0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1])
    y = torch.cat([torch.zeros(8), torch.ones(8)])
    print(Precision(pred, y))
    print(Recall(pred, y))
    print(Accuracy(pred, y))
    print(Fscore(pred, y))
    print(Precision(y, y))
    print(Recall(y, y))
    print(Accuracy(y, y))
    print(Fscore(y, y))
