# REG: Refined Generalized Focal Loss for Road Asset Detection on Thai Highways

<!-- ![REG Logo](https://img.icons8.com/ios/50/000000/road.png)  -->

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
@article{panboonyuen2024REG,
  title={REG: Refined Generalized Focal Loss for Road Asset Detection on Thai Highways Using Vision-Based Detection and Segmentation Models},
  author={Teerapong Panboonyuen},
  journal={Journal of Computer Vision},
  year={2024},
  url={https://github.com/kaopanboonyuen/REG}
}
```

## 📫 Contact

For further inquiries, reach out to:

- **Teerapong Panboonyuen**  
  Postdoctoral Researcher, Chulalongkorn University  
  Senior Research Scientist, MARS (Motor AI Recognition Solution)  
  Email: [teerapong.panboonyuen@gmail.com](mailto:teerapong.panboonyuen@gmail.com)

---

Thank you for visiting our repository! We hope you find our work useful in advancing road asset detection and segmentation.