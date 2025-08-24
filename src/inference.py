import torch
from model import DetectionSegmentationModel
from utils import load_image, visualize_results, parse_args

def infer():
    args = parse_args()
    model = DetectionSegmentationModel(...)
    model.load_state_dict(torch.load(args.checkpoint, map_location=args.device))
    model.eval()

    img = load_image(args.image_path)
    with torch.no_grad():
        det_out, seg_out = model(img.unsqueeze(0))
    visualize_results(img, det_out, seg_out, args.output_path)

if __name__ == "__main__":
    infer()