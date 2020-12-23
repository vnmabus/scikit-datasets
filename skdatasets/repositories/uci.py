"""
UCI datasets (https://archive.ics.uci.edu/ml/datasets.html).

@author: David Diaz Vico
@license: MIT
"""

import os
from builtins import None
from urllib.request import urlretrieve

import numpy as np
from sklearn.datasets import get_data_home
from sklearn.utils import Bunch

BASE_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases'


def _load_csv(fname, **kwargs):
    """Load a csv file with targets in the last column and features in the rest.
    """
    data = np.genfromtxt(fname, dtype=str, delimiter=',', encoding=None,
                         **kwargs)
    X = data[:, :-1]
    y = data[:, -1]
    return X, y


def _fetch(name, dirname=None):
    """Fetch dataset."""
    filename = name + '.data'
    url = BASE_URL + '/' + name + '/' + filename
    filename = filename if dirname is None else os.path.join(dirname, filename)
    filename, _ = urlretrieve(url, filename=filename)
    X, y = _load_csv(filename)
    try:
        filename = name + '.test'
        url = BASE_URL + '/' + name + '/' + filename
        filename = filename if dirname is None else os.path.join(
            dirname, filename)
        filename, _ = urlretrieve(url, filename=filename)
        X_test, y_test = _load_csv(filename)
    except:
        X_test = y_test = None
    try:
        filename = name + '.names'
        url = BASE_URL + '/' + name + '/' + filename
        filename = filename if dirname is None else os.path.join(dirname,
                                                                 filename)
        filename, _ = urlretrieve(url, filename=filename)
    except:
        filename = name + '.info'
        url = BASE_URL + '/' + name + '/' + filename
        filename = filename if dirname is None else os.path.join(dirname,
                                                                 filename)
        filename, _ = urlretrieve(url, filename=filename)
    with open(filename) as rst_file:
        fdescr = rst_file.read()
    return X, y, X_test, y_test, fdescr


def fetch(name, data_home=None):
    """Fetch UCI dataset.

    Fetch a UCI dataset by name. More info at
    https://archive.ics.uci.edu/ml/datasets.html.

    Parameters
    ----------
    name : string
        Dataset name.
    data_home : string or None, default None
        Specify another download and cache folder for the data sets. By default
        all scikit-learn data is stored in ‘~/scikit_learn_data’ subfolders.

    Returns
    -------
    data : Bunch
        Dictionary-like object with all the data and metadata.

    """
    dirname = os.path.join(get_data_home(data_home=data_home), 'uci', name)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    X_train, y_train, X_test, y_test, DESCR = _fetch(name, dirname=dirname)

    if X_test is None or y_test is None:
        X = np.concatenate((X_train, X_test))
        y = np.concatenate((y_train, y_test))

        train_indexes = np.arange(len(X_train))
        test_indexes = np.arange(len(X_train), len(X))
    else:
        X = X_train
        y = y_train
        
        train_indexes = None
        test_indexes = None

    data = Bunch(
        data=X,
        target=y,
        train_indexes=train_indexes,
        validation_indexes=None,
        test_indexes=test_indexes,
        inner_cv=None,
        outer_cv=None,
        DESCR=DESCR,
    )
    return data
