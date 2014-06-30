__author__ = 'zmiller'


def base_frequency(strand):
    """return frequency of dna base occurrence

    DNA is made up of four bases: guanine (G), adenine (A), thymine (T), or cytosine (C)
    this function analyzes a DNA strand and returns a report of the number of times each base occurs

    >>> base_frequency("AAAACCCGGT")
    'guanine (G):2, adenine (A):4, thymine (T):1, cytosine (C):3'

    >>> base_frequency("ACGT")
    'guanine (G):1, adenine (A):1, thymine (T):1, cytosine (C):1'

    >>> base_frequency("acgt")
    'guanine (G):1, adenine (A):1, thymine (T):1, cytosine (C):1'
    """
    pass


def reverse_strand(strand):
    """returns the reverse compliment of a strand

    >>> reverse_strand("AAAACCCGGT")
    'ACCGGGTTTT'

    >>> reverse_strand("aaaacccggt")
    'ACCGGGTTTT'

    """
    pass
