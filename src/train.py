import torch
from torch.utils.data import DataLoader
from model import DetectionSegmentationModel, REGLoss
from utils import load_dataset, parse_args

def train():
    args = parse_args()
    model = DetectionSegmentationModel(...)
    criterion = REGLoss(...)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    train_loader = DataLoader(load_dataset(args.data_path, train=True), batch_size=args.batch, shuffle=True)
    val_loader = DataLoader(load_dataset(args.data_path, train=False), batch_size=args.batch)

    for epoch in range(args.epochs):
        model.train()
        for imgs, targets in train_loader:
            preds = model(imgs)
            loss = criterion(*preds, targets)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch} — Loss: {loss.item():.4f}")
        evaluate(model, val_loader, criterion)

def evaluate(model, loader, criterion):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for imgs, targets in loader:
            preds = model(imgs)
            total_loss += criterion(*preds, targets).item()
    print(f"Validation loss: {total_loss / len(loader):.4f}")

if __name__ == "__main__":
    train()