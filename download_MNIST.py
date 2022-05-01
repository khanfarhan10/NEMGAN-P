"""Functions for downloading data.
"""
import os
from six.moves import urllib # pylint: disable=redefined-builtin

SOURCE_URL = "http://yann.lecun.com/exdb/mnist/"

def maybe_download(filename, work_directory):
    """Download the data from Yann's website, unless it's already here."""
    if not os.path.exists(work_directory):
        os.mkdir(work_directory)
    filepath = os.path.join(work_directory, filename)
    if not os.path.exists(filepath):
        filepath, _ = urllib.request.urlretrieve(SOURCE_URL + filename, filepath)
        statinfo = os.stat(filepath)
        print("Successfully downloaded", filename, statinfo.st_size, "bytes.")
    return filepath

def download_mnist_dataset(train_dir):
    TRAIN_IMAGES = "train-images-idx3-ubyte.gz"
    TRAIN_LABELS = "train-labels-idx1-ubyte.gz"
    TEST_IMAGES = "t10k-images-idx3-ubyte.gz"
    TEST_LABELS = "t10k-labels-idx1-ubyte.gz"

    maybe_download(TRAIN_IMAGES, train_dir)
    maybe_download(TRAIN_LABELS, train_dir)
    maybe_download(TEST_IMAGES, train_dir)
    maybe_download(TEST_LABELS, train_dir)
    print("Successfully Downloaded MNIST Dataset!")
