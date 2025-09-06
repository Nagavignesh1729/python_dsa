""" Given a list of element, check whether it has no duplicate elements """

def unique1(S):
    """ Return True if there are no duplicates in the Sequence S """

    for i in range(S):
        for j in range(i+1, len(S)):
            if S[i] == S[j]:
                return False                # duplicate found
    
    return True                             # if we reach this, no duplicated were found
    """Complexity: O(n^2)"""

""" Using sorting as a tool (Duplicate elements become adjacent in sorted list) """
def unique2(S):
    """ Return True if there are no duplicates in the Sequence S """

    temp = sorted(S)                        # store a sorted copy

    for i in range(1, len(S)):  
        if temp[i-1] == temp[i]:
            return False                    # duplicates found

    return True                             # if we reach this, no duplicated were found
    """ In-built sorting is O(nlogn) worst case ==> our algorithm is O(nlogn) """


""" Incomplete test code """
if __name__ == "__main__":
    """ need to draw the time complexity """
    print("incomplete")
