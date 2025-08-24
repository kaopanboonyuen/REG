# 🚧 REG: Refined Generalized Focal Loss for Road Asset Detection on Thai Highways

> Official implementation of our paper:  
> **“REG: Refined Generalized Focal Loss for Road Asset Detection on Thai Highways Using Vision-Based Detection and Segmentation Models”**  
> 📌 Presented at **IEEE KST 2025** | 🔬 Designed by **Teerapong Panboonyuen (Kao)**

---

## 🌟 Highlights

- ✅ **REG Loss**: Combines focal loss, spatial refinement, and probabilistic uncertainty.
- 🎯 **Multi-task Model**: Supports object detection & segmentation in one architecture.
- 📊 **Performance**: Achieves `mAP50 = 80.34`, `F1-score = 77.87` on real-world Thai highway data.
- 🧱 **Modular PyTorch Codebase**: Easy to adapt for new datasets or vision tasks.
- 📦 **Dockerized Deployment**: Reproducible, scalable, CV-ready.

---

## 🗂 Project Structure

```bash
REG/
├── src/
│   ├── model.py         # REG Loss + Multi-task Detection-Segmentation Model
│   ├── train.py         # Training Pipeline
│   ├── inference.py     # Inference Script for Images
│   ├── metrics.py       # Evaluation Metrics (mAP, F1, etc.)
│   └── utils.py         # Utility Functions & Argument Parsers
├── Dockerfile           # Docker Environment for Reproducibility
├── requirements.txt     # Python Dependencies
└── README.md            # Project Documentation (this file)
````

---

## 🚀 Getting Started

### 🔧 1. Installation

```bash
git clone https://github.com/kaopanboonyuen/REG.git
cd REG
pip install -r requirements.txt
```

Or via Docker (recommended):

```bash
docker build -t reg-road-assets .
```

---

### 📊 2. Training

Train REG on your dataset (edit `--data-path` and config as needed):

```bash
python src/train.py \
  --data-path ./data/ \
  --batch 8 \
  --epochs 50 \
  --lr 1e-4
```

---

### 🖼 3. Inference on Image

Run inference on a single image using a trained model checkpoint:

```bash
python src/inference.py \
  --checkpoint ./checkpoints/best_model.pth \
  --image-path ./images/test.jpg \
  --output-path ./output/result.png
```

---

### 📏 4. Evaluation

Evaluate detection and segmentation metrics:

```bash
python src/metrics.py \
  --pred-dir ./predictions/ \
  --gt-dir ./ground_truth/
```

---

## 📈 Results Summary

| Metric   | Value     |
| -------- | --------- |
| mAP\@50  | **80.34** |
| F1-Score | **77.87** |

REG outperforms traditional focal loss and other baselines in both segmentation and detection under challenging road conditions including glare, occlusion, and rare asset classes.

---

## 📚 Learn More

📖 Blog post:
[🔗 Refined Generalized Focal Loss Explained](https://kaopanboonyuen.github.io/blog/2024-09-07-refined-generalized-focal-loss-for-road-asset-detection-on-thai-highways-using-vision-models/)

📄 Paper (arXiv):
[🔗 REG Paper on arXiv](https://arxiv.org/abs/2409.09877)

📄 Paper (IEEE):
[🔗 REG Paper on IEEE](https://ieeexplore.ieee.org/document/11003314/)

---

## 📄 Citation

If you use this repo in your research or projects, please cite:

```bibtex
@inproceedings{panboonyuen2025reg,
  title={REG: Refined Generalized Focal Loss for Road Asset Detection on Thai Highways Using Vision Models},
  author={Panboonyuen, Teerapong},
  booktitle={2025 17th International Conference on Knowledge and Smart Technology (KST)},
  pages={324--329},
  year={2025},
  organization={IEEE}
}
```

---

## 👨‍💻 Contact

**Teerapong Panboonyuen (Kao)**
Postdoctoral Researcher, Chulalongkorn University
Senior Research Scientist, MARSAIL
📧 [teerapong.panboonyuen@gmail.com](mailto:teerapong.panboonyuen@gmail.com)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🧠 License

MIT License — free to use, share, and modify.

---

> “If it moves on the road, REG sees it.”

```

---