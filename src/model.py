# ==============================================================================
#  REG: Refined Generalized Focal Loss for Road Asset Detection & Segmentation
#  ----------------------------------------------------------------------------
#  Author   : Teerapong Panboonyuen (Kao)
#  Paper    : "REG: Refined Generalized Focal Loss for Road Asset Detection 
#              on Thai Highways Using Vision-Based Detection and Segmentation Models"
#  Version  : 1.0
#  Github   : https://github.com/yourusername/REG-road-assets
#  License  : Apache 2.0 or MIT (choose one and apply it to your repo)
# ==============================================================================
#  Description:
#
#     This code is part of the REG framework, implementing a multi-task model
#     with the proposed REG loss for handling class imbalance, spatial refinement,
#     and multi-label segmentation/detection tasks in the context of Thai highways.
# ==============================================================================

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models

class REGLoss(nn.Module):
    """
    Refined Generalized Focal Loss (REG) for multi-task (detection + segmentation).
    Includes probabilistic and spatial context refinements.
    """
    def __init__(self, alpha=0.25, gamma=2.0, lambda_seg=1.0, lambda_det=1.0):
        super(REGLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.lambda_seg = lambda_seg
        self.lambda_det = lambda_det
        self.bce = nn.BCEWithLogitsLoss()

    def focal_loss(self, inputs, targets):
        bce_loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction='none')
        pt = torch.exp(-bce_loss)
        focal = self.alpha * (1 - pt) ** self.gamma * bce_loss
        return focal.mean()

    def spatial_refinement(self, logits):
        # Example: Laplacian smoothness regularization
        laplacian_kernel = torch.tensor([[0, 1, 0], [1, -4, 1], [0, 1, 0]],
                                        dtype=torch.float32, device=logits.device).unsqueeze(0).unsqueeze(0)
        pad = nn.ReflectionPad2d(1)
        refined = F.conv2d(pad(logits), laplacian_kernel)
        return torch.mean(refined ** 2)

    def forward(self, det_logits, seg_logits, det_targets, seg_targets):
        det_loss = self.focal_loss(det_logits, det_targets)
        seg_loss = self.bce(seg_logits, seg_targets)

        # Spatial regularization on segmentation logits
        spatial_reg = self.spatial_refinement(seg_logits)

        total_loss = self.lambda_det * det_loss + self.lambda_seg * seg_loss + 0.1 * spatial_reg
        return total_loss


class DetectionSegmentationModel(nn.Module):
    """
    A multi-task model for object detection + segmentation.
    Backbone: ResNet50
    """
    def __init__(self, num_classes=1, seg_classes=1):
        super(DetectionSegmentationModel, self).__init__()
        resnet = models.resnet50(pretrained=True)
        self.backbone = nn.Sequential(*list(resnet.children())[:-2])  # Remove avgpool and fc
        self.conv = nn.Conv2d(2048, 512, kernel_size=3, padding=1)

        # Detection Head (bounding box heatmap)
        self.det_head = nn.Sequential(
            nn.Conv2d(512, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, num_classes, kernel_size=1)
        )

        # Segmentation Head (pixel-wise mask)
        self.seg_head = nn.Sequential(
            nn.Conv2d(512, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, seg_classes, kernel_size=1)
        )

    def forward(self, x):
        features = self.backbone(x)
        features = self.conv(features)

        det_out = self.det_head(features)
        seg_out = self.seg_head(features)

        # Upsample outputs to match input size
        det_out = F.interpolate(det_out, size=x.shape[2:], mode='bilinear', align_corners=False)
        seg_out = F.interpolate(seg_out, size=x.shape[2:], mode='bilinear', align_corners=False)

        return det_out, seg_out