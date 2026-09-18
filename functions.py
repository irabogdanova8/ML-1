def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """

    product = 1
    non_zero = False

    size = min(len(x),len(x[0]))

    for i in range(size):
        if x[i][i] != 0:
            non_zero = True
            product = product * x[i][i]

    if non_zero:
        return int(product)
    else:
        return 0

    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """

    return sorted(list(x)) == sorted(list(y))

    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    largest = None
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            if largest is None or x[i] > largest:
                largest = x[i]
    return largest

    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    h = len(img)
    w = len(img[0])
    result = [[0.0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            s = 0.0
            for c in range(len(coefs)):
                s += img[i][j][c] * coefs[c]
            result[i][j] = s
    return result

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    elements = []
    counters = []
    for value in x:
        if elements and elements[-1] == value:
            counters[-1] += 1
        else:
            elements.append(int(value))
            counters.append(1)
    return elements, counters

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    result = []
    for x_i in x:
        row = []
        for y_j in y:
            s = 0.0
            for k in range(len(x_i)):
                d = x_i[k] - y_j[k]
                s += d * d
            row.append(s ** 0.5)
        result.append(row)
    return result

    pass
