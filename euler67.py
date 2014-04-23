def euler67():
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
    the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
    a 15K text file containing a triangle with one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. 
    It is not possible to try every route to solve this problem, 
    as there are 2^99 altogether! 

    If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
    There is an efficient algorithm to solve it. ;o)
    """



def get_pile():

    pile_file = open('./euler67_file.txt','rU')

    pile = []
    for l in pile_file:
        pile.append([int (ele) for ele in l.split()])
    
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

    #return b  # no need to return...list b will be changed because pointers are passed in


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






