import os
from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix

def quality_score(tp, tn, fp, fn):
    total = tp + tn + fp + fn
    if total == 0:
        return 0.0
    truth_sum = tp + tn
    quality = truth_sum/(truth_sum + 10 * fp + fn)
    return quality

def compute_quality_for_corpus(corpus_dir):
    truth_dict = read_classification_from_file(os.path.join(corpus_dir, "!truth.txt"))
    pred_dict = read_classification_from_file(os.path.join(corpus_dir, "!prediction.txt"))

    matrix = BinaryConfusionMatrix(pos_tag="SPAM", neg_tag="OK")
    matrix.compute_from_dicts(truth_dict, pred_dict)

    return quality_score(matrix.tp, matrix.tn, matrix.fp, matrix.fn)