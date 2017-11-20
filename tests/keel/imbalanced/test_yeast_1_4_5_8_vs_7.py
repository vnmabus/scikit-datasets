"""
Tests.

@author: David Diaz Vico
@license: MIT
"""

from ...base import check_load_dataset

from skdatasets.keel.imbalanced import load_yeast_1_4_5_8_vs_7


def test_load_yeast_1_4_5_8_vs_7():
    """Tests yeast-1-4-5-8_vs_7 dataset."""
    n_patterns = (693, )
    n_variables = 8
    array_names = (('data', 'target'), )
    n_folds = (5, )
    check_load_dataset(load_yeast_1_4_5_8_vs_7, n_patterns, n_variables,
                       array_names, n_targets=None, n_folds=n_folds)