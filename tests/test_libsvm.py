"""
Test the LIBSVM loader.

@author: David Diaz Vico
@license: MIT
"""

from sklearn.model_selection import BaseCrossValidator

from skdatasets.libsvm import fetch_libsvm


def check(data, shape, splits=1):
    """Check dataset properties."""
    assert data.data.shape == shape
    assert data.target.shape[0] == shape[0]
    if splits > 1:
        assert len(list(data.outer_cv.split())) == splits
    if hasattr(data, 'inner_cv'):
        if data.inner_cv is not None:
            assert isinstance(data.inner_cv, BaseCrossValidator)


def test_fetch_libsvm_australian():
    """Tests LIBSVM australian dataset."""
    data = fetch_libsvm(collection='binary', name='australian')
    check(data, (690, 14))


def test_fetch_libsvm_liver_disorders():
    """Tests LIBSVM liver-disorders dataset."""
    data = fetch_libsvm(collection='binary', name='liver-disorders')
    check(data, (145, 5), 1)


def test_fetch_libsvm_duke():
    """Tests LIBSVM duke dataset."""
    data = fetch_libsvm(collection='binary', name='duke')
    check(data, (44, 7129))


def test_fetch_libsvm_cod_rna():
    """Tests LIBSVM cod-rna dataset."""
    data = fetch_libsvm(collection='binary', name='cod-rna')
    check(data, (59535, 8))


def test_fetch_libsvm_satimage():
    """Tests LIBSVM satimage dataset."""
    data = fetch_libsvm(collection='multiclass', name='satimage.scale')
    check(data, (4435, 36), 1)
