from sklearn.metrics import f1_score, precision_score, recall_score

def compute_detection_metrics(preds, targets, iou_threshold=0.5):
    # Implement mean Average Precision (mAP50) calculation
    pass

def compute_segmentation_metrics(pred_mask, true_mask):
    f1 = f1_score(true_mask.flatten(), pred_mask.flatten())
    return {'F1-score': f1}