"""
LIBSVM diabetes dataset.

@author: David Diaz Vico
@license: MIT
"""

from ..base import load_train_scale


def load_diabetes(return_X_y=False):
    """Load diabetes dataset.

    Loads the diabetes dataset.

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
    return load_train_scale('diabetes',
                            'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/diabetes',
                            'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/diabetes_scale',
                            return_X_y=return_X_y)