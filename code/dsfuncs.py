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


def coefs_df(cols, coefs):
    df = pd.DataFrame(
        {
        'Coefficients': coefs
        }, index=cols)
    return df

    
def standard_scaler(X):
    X = X.copy()
    X = X - X.mean()
    X = X / X.std()
    return X


def r_2(preds, y):
    model_cost = np.sum((y - preds)**2)
    naive_cost = np.sum((y - y.mean())**2)
    r2 = 1 - (model_cost / naive_cost)
    return r2