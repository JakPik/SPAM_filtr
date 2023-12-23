import os
from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix

def quality_score(tp, tn, fp, fn):
    numerator = tp + tn
    denominator = tp + tn + 10*fp +fn
    score = numerator / denominator
    return score

def compute_quality_for_corpus(corpus_dir):
    truth_dir = os.path.join(corpus_dir, '!truth.txt')
    pred_dir = os.path.join(corpus_dir, '!prediction.txt')
    truth_dict = read_classification_from_file(truth_dir)
    pred_dict = read_classification_from_file(pred_dir)
    matrix = BinaryConfusionMatrix(pos_tag='SPAM', neg_tag='OK')
    matrix.compute_from_dicts(truth_dict, pred_dict)
    return quality_score(matrix.tp, matrix.tn, matrix.fp, matrix.fn)