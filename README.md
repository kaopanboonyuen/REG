# REG: Refined Generalized Focal Loss for Road Asset Detection on Thai Highways

Welcome to the official repository for our research on **Refined Generalized Focal Loss (REG)** for road asset detection and segmentation on Thai highways. This novel framework leverages advanced mathematical formulations to enhance the detection and segmentation of critical road elements using state-of-the-art vision-based models.

## 📚 Overview

This paper introduces an advanced REG formulation designed to tackle class imbalance and localization challenges in road asset detection. The REG model integrates into vision-based detection and segmentation frameworks to improve accuracy and robustness, especially in complex environments with varying lighting conditions and cluttered backgrounds.

**Key Contributions:**
- **Refined Generalized Focal Loss (REG):** A sophisticated loss function that dynamically adjusts for class imbalance and incorporates spatial-contextual adjustments.
- **Multi-Task Learning:** Enhances both detection and segmentation accuracy by optimizing REG across multiple tasks.
- **Performance Metrics:** Achieved a mAP50 of 80.34 and an F1-score of 77.87, demonstrating significant improvements over conventional methods.

For a detailed explanation of the mathematical model and background, please check out our previous work at [Refined Generalized Focal Loss Explained](https://kaopanboonyuen.github.io/blog/2024-09-07-refined-generalized-focal-loss-for-road-asset-detection-on-thai-highways-using-vision-models/).

## 🔬 Key Features

- **Class Imbalance Handling:** Advanced adjustments for rare and challenging classes.
- **Spatial-Contextual Adjustments:** Incorporates spatial distribution for better asset localization.
- **Probabilistic Refinement:** Captures prediction uncertainty to enhance model robustness.

## 📈 Results

Our rigorous experiments demonstrate the effectiveness of REG in improving road asset detection and segmentation accuracy. The model's performance outperforms conventional methods, making it a robust solution for real-world applications.

**Results Summary:**
- **mAP50:** 80.34
- **F1-Score:** 77.87

## 📥 Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/kaopanboonyuen/REG.git
cd REG
pip install -r requirements.txt
```

## 🚀 Usage

Detailed usage instructions and example code can be found in the `docs` directory. For questions or contributions, please refer to the [contributing guidelines](CONTRIBUTING.md).

## 📄 Citation

If you use this work in your research, please cite our paper:

```bibtex
@inproceedings{panboonyuen2025reg,
  title={Reg: Refined Generalized Focal Loss for Road Asset Detection on Thai Highways Using Vision Models},
  author={Panboonyuen, Teerapong},
  booktitle={2025 17th International Conference on Knowledge and Smart Technology (KST)},
  pages={324--329},
  year={2025},
  organization={IEEE}
}
```

## 📫 Contact

For further inquiries, reach out to:

- **Teerapong Panboonyuen**  
  Postdoctoral Researcher, Chulalongkorn University  
  Senior Research Scientist, MARSAIL (Motor AI Recognition Solution Artificial Intelligence Laboratory)  
  Email: [teerapong.panboonyuen@gmail.com](mailto:teerapong.panboonyuen@gmail.com)

---

Thank you for visiting our repository! We hope you find our work useful in advancing road asset detection and segmentation.