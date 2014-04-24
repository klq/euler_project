def euler18():
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
    the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
    However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
    it cannot be solved by brute force, and requires a clever method! ;o)
    """



def get_pile():

    pile_file = open('./euler18_file.txt','rU')

    pile = []
    for l in pile_file:
        pile.append([int (ele) for ele in l.split()])
    
    pile_file.close()
    
    return pile

def merge_rows(a,b):
    """a has one less element than b"""
    
    b[0] = a[0] + b[0]
    b[-1] = a[-1] + b[-1]

    for i in range(1,len(b)-1):

        if (a[i-1] + b[i]) >= (a[i] + b[i]):
            b[i] = a[i-1] + b[i]
        else:
            b[i] = a[i] + b[i]

    #return b


def max_total_route():

    """
    1. from row 1, pick a number
    2. row 1, from left to right, merge row 1 and 2 , place in row 2
    3. row 2, merge row 2 and 3, place in row 3..
    ...
    ...
    n. last row....find largest number in last row

    """
    
    pile = get_pile()

    row = 0
    while (row < len(pile)-1 ):
        merge_rows(pile[row], pile[row+1])
        row += 1

    max_total = max(pile[-1])
    return max_total

    
print max_total_route()






