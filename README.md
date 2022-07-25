# python-editdistance
A pure, minimalist Python library of various edit distance metrics.

Implemented methods:
    - Levenshtein (iterative and recursive implementations)
    - Normalized Levenshtein (using Yujian-Bo [1]).
    - Damerau-Levenshtein
    - Hamming distance

Levenshtein and Damerau-Levenshtein distances use the Wagner-Fischer
dynamic programming algorithm [2].

Some basic unit tests can be executed using `pytest`


1. L. Yujian and L. Bo, "A normalized Levenshtein distance metric," 
    IEEE Transactions on Pattern Analysis and Machine Intelligence (2007).
    https://ieeexplore.ieee.org/document/4160958
2.  R. Wagner and M. Fisher, "The string to string correction problem," 
    Journal of the ACM, 21:168-178, 1974.
