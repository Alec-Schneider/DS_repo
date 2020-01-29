from math import sqrt
import numpy as np

def euclidean_distance1(a, b):
    """
    a :param array like object
    b :param array like object

    :return the euclidean distance of two arrays of points
    """
    return sqrt(sum([(val1 - val2)**2 for val1, val2 in zip(a, b)]))


def euclidean_distance2(a, b):
    """
    a :param array like object
    b :param array like object

    :return the euclidean distance of two arrays of points
    """
    a = np.array(a)
    b = np.array(b)
    return np.sqrt(np.sum((a - b)**2))


if __name__ == '__main__':
    a = list(range(10))
    b = np.random.random(10)

    import timeit

    start = timeit.time.time()
    one = euclidean_distance1(a, b)
    past1 = timeit.timeit('euclidean_distance1(a, b)', 'from __main__ import euclidean_distance1, a, b')
    print(past1)

    start = timeit.time.time()
    two = euclidean_distance2(a, b)
    # past = round(timeit.time.time() - start, 5)
    past2 = timeit.timeit('euclidean_distance2(a, b)', 'from __main__ import euclidean_distance2, a, b' )
    print(past2)

    with open('euc_testing_results.txt', 'w') as f:
        f.write('Results of Euclidean Distance using source library vs numpy arrays:\n')
        f.write('Lists and built-in: %s\n'% past1)
        f.write('Result with lists and source library: %s\n'% one)
        f.write('Numpy arrays: %s\n'% past2)
        f.write('Result with numpy arrays: %s\n'% two)

