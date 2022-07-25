def levenshtein(a: str, b: str) -> int:
    """
    Computes the Levenshtein distance: the number of
    insertions, deletions or substitutions required
    to transform a -> b.

    Uses the Wagner-Fischer dynamic programming algorithm [1,2].

    1. R. Wagner and M. Fisher, "The string to string correction problem," 
    Journal of the ACM, 21:168-178, 1974.
    2. https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
    
    Parameters:
        a: First string
        b: Second string
    Returns:
        Levenshtein distance (integer)
    """
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)

    _a, _b  = " " + a, " " + b
    a_len, b_len = len(_a), len(_b)
    dist_matrix =  [[0] * a_len for _ in range(b_len)]

    for i in range(a_len):
        for j in range(b_len):
            if min([i, j]) == 0:
                dist_matrix[j][i] = max(i, j)
            else:
                dist_matrix[j][i] = min(dist_matrix[j-1][i],
                                        dist_matrix[j][i-1],
                                        dist_matrix[j-1][i-1])
            if _a[i] != _b[j]:
                dist_matrix[j][i] += 1

    return dist_matrix[-1][-1]


def levenshtein_recursive(a: str, b: str) -> int:
    """
    Computes the Levenshtein distance using the naive
    recursive implementation.

    See: https://en.wikipedia.org/wiki/Levenshtein_distance

    Parameters:
        a: First string
        b: Second string

    Returns:
        Levenshtein distance (integer)
    """
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    elif a[0] == b[0]:
        return levenshtein_recursive(a[1:], b[1:])
    else:
        return 1 + min(levenshtein_recursive(a[1:], b),
                       levenshtein_recursive(a, b[1:]),
                       levenshtein_recursive(a[1:], b[1:]))


def normalized_levenshtein(a: str, b: str) -> float:
    """
    Implements the normalized Levenshtein metric by Yujian & Bo [1].

    1. L. Yujian and L. Bo, "A normalized Levenshtein distance metric," 
    IEEE Transactions on Pattern Analysis and Machine Intelligence (2007).
    https://ieeexplore.ieee.org/document/4160958

    Parameters:
        a: First string
        b: Second string

    Returns:
        Normalized Levenshtein distance (float)
    """
    a_len, b_len = len(a), len(b)
    d = levenshtein(a, b)
    return (2 * d) / ((a_len+b_len) + d)


def damerau_levenshtein(a: str, b: str) -> int:
    """

    """
    pass


def longest_common_subsequence(a: str, b: str) -> int:
    """
    Longest common subsequence (LCS), i.e. the number ofinsertions 
    and deletions (no substitutions) to transform a -> b.
    """
    pass


def jaro_distance(a: str, b: str) -> float:
    """
    Computes the Jaro distance, the number of transpositions
    required to transform a -> b.
    """
    pass


def jaro_winkler_distance(a: str, b: str) -> float:
    """

    """
    pass


def hamming_distance(a: str, b: str) -> int:
    """
    Finds the Hamming distance, the number of substitutions
    (only) to transform a -> b.

    Parameters:
        a: First string
        b: Second string

    Returns:
        Hamming distance (integer)
    """
    if len(a) != len(b):
        raise ValueError("Inputs must be of equal length!")
    return sum([1 for i, j in zip(a, b) if i != j ])
