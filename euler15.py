def euler15():
    # Problem:
    """
    Starting in the top left corner of a 2x2 grid, 
    and only being able to move to the right and down, 
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20x20 grid?
    """

    # Solve:
    N = 21
    routes = [[None] * N] * N
    for i in range(N):
        routes[i][N-1] = 1
        routes[N-1][i] = 1

    for i in range(N-2,-1,-1):
        for j in range(N-2,-1,-1):
            routes[i][j] = routes[i+1][j] + routes[i][j+1]
            print i,j,routes[i][j]

    return routes


euler15() #137846528820


"""
Analytical solution:
You will go down exactly 20 steps, and go right exactly 20 steps. 40 steps in total.
So the total number of different routes is 40 choose 20.
C(20,40) = P(20,40) / P(20,20) = 40! / (20! (40-20)!) 
"""
import math
print math.factorial(40) / (math.factorial(20)**2)

    