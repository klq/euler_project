import math

def euler24():
    """
    A permutation is an ordered arrangement of objects. 
    For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
    If all of the permutations are listed numerically or alphabetically, 
    we call it lexicographic order. 

    The lexicographic permutations of 0, 1 and 2 are: 

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """

    # import math
    # math.factorial(10) = 3628800, 3.6 million combinations
    # math.factorial(9) = 362880, so the first digit is '2'

    import time
    start = time.time()

    p = 10 
    limit = 1000000-1
    result = []

    LIST = [0,1,2,3,4,5,6,7,8,9]


    # higest digit, 10! permutations in total
    while p > 0:
        l = len(result)
        m, r = divmod(limit, math.factorial(p-1))
        result.append(LIST[m])
        LIST.remove(LIST[m]) # remove first element with VALUE LIST[m]
        limit -= m * math.factorial(p-1)
        p -= 1

    end = time.time()
    print "Time:"  , (end-start)*1000 , "ms"
    
    return result

print euler24() #2783915460
