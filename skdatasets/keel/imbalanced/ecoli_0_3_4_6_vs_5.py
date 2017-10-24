"""
Keel ecoli-0-3-4-6_vs_6 dataset.

@author: David Diaz Vico
@license: MIT
"""

from ..base import load_imbalanced


def load_ecoli_0_3_4_6_vs_5(return_X_y=False):
    """Load ecoli-0-3-4-6_vs_5 dataset.

    Loads the ecoli-0-3-4-6_vs_5 dataset.

    Parameters
    ----------
    return_X_y: bool, default=False
                If True, returns (data, target) instead of a Bunch object..

    Returns
    -------
    data: Bunch
          Dictionary-like object with all the data and metadata.
    ((X, y), ): list of arrays
                If return_X_y is True

    """
    return load_imbalanced('ecoli-0-3-4-6_vs_5',
                           'http://sci2s.ugr.es/keel/keel-dataset/datasets/imbalanced/imb_IRhigherThan9p2',
                           names=['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
                                  'class'],
                           target_names=['class'], return_X_y=return_X_y)
