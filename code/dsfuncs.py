"""
Functions learned or created during my Data Science course at General Assembly.
"""
import numpy as np

def euclidean_distance(a, b):
    """
    a :param array like object
    b :param array like object

    :return the euclidean distance of two arrays of points
    """
    a = np.array(a)
    b = np.array(b)
    return np.sqrt(np.sum((a - b)**2))