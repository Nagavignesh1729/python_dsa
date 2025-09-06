"""
    Suppose we are given three sequences of numbers, A, B, and C. We will assume
    that no individual sequence contains duplicate values, but that there may be some
    numbers that are in two or three of the sequences. The three-way set disjointness
    problem is to determine if the intersection of the three sequences is empty, namely,
    that there is no element x such that x ∈ A, x ∈ B, and x ∈ C. 
"""

""" A crude implementation """
def disjoint1(A, B, C):
    """ Return True if there is no common element to all three lists """

    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False        # we have found a common value

    return True                         # if we reach this point, sets are disjoint
    """ Notice worst case time being O(n^3) """


""" A small improvement - Notice once inside the body of the loop over B, 
    if selected elements a and b do not match each other, 
    it is a waste of time to iterate through all values of C looking for a matching triple. 
"""
def disjoint2(A, B, C):    
    """ Return True if there is no common element to all three lists """

    for a in A:
        for b in B:
            if a == b:                  # only check C if we found match in A and B
                for c in C:
                    if a == c:          # a == b == c
                        return False    # found common value
    
    return True                         # set is disjonit
    """ Algorithm becomes O(n^2) (Think Why) """


if __name__ == "__main__":
    """ Graphically verify if disjoint2 is actually quadratic or not
        (will code later)
    """
    print("Incomplete")
