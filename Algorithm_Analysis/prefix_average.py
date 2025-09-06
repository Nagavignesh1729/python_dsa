""" Implementing the Prefix Average of an array in 3 different Time complexity. """

""" Quadratic Time Complexity """
def prefix_avg1(S):
    """ Returns list such that, for all j, A[j] = average of S[0] S[1]... S[j] """
    
    n = len(S)
    A = [0] * n

    for j in range(n):
        tot = 0
        for i in range(j+1):
            tot += S[i]
        A[j] = tot/(j+1)

    return A


""" Second Implementation - Same Quadratic Complexity """
def prefix_avg2(S):
    """ Returns list such that, for all j, A[j] = average of S[0] S[1]... S[j] """
    
    n = len(S)
    A = [0] * n

    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)

    return A

""" 
    Asymptotically, this implementation is no better. Even though the expression, sum(S[0:j+1]), 
    seems like a single command, it is a function call and an evaluation of that function 
    takes O(j + 1) time in this context. 
"""

""" A Linear Time Algorithm """
def prefix_avg3(S):
    """ Returns list such that, for all j, A[j] = average of S[0] S[1]... S[j] """

    n = len(S)
    A = [0] * n
    
    tot = 0
    for j in range(n):
        tot += S[j]
        A[j] = tot/(j+1)

    return A

if __name__ == "__main__":
    """
        Plot the time complexity to understand the difference between each algorithm
        Mainly the difference between O(n) and O(n^2)
    """
    print("Hi")
