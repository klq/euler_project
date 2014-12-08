def euler28():
    """
    Number spiral diagonals:
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
    """

    """
    diagnols:
    1
    3,5,7,9
    13,17,21,25
    31,37,43,49
    
    sides:
    1
    3
    5
    7
    ...
    1001
    """

    diagnols = [1]
    last = diagnols[0]
    for size in range(1,1001,2):
        delta = size+1

        for unused_i in range(4):
            last += delta
            diagnols.append(last)

    return sum(diagnols)

print euler28() #669171001