import math

def euler39():
    """https://projecteuler.net/problem=39
       Integer Right Triangles
       Assume the sides of the right triangles are a, b and c, and a < b < c
    """
    num_of_solutions = {}
    
    for a in range (1,1000):
        for b in range(a+1,1000-a):
            for c in range(b+1, 1000-a-b):
            #print 'a={0}, b={1}, c={2}'.format(a, b, c)
                if a+b+c>1000:
                    break
                elif a**2 + b**2 == c**2:
                    p = a + b + c                              
                    if p not in num_of_solutions:
                        num_of_solutions[p] = 1
                    else:
                        num_of_solutions[p] += 1

    print max(num_of_solutions.keys(), key=(lambda p: num_of_solutions[p]))  # answer is: 840
    print num_of_solutions[840]  # answer is 8 right triangles


def euler39_2():
    """https://projecteuler.net/problem=39
       Integer Right Triangles
       Assume the sides of the right triangles are a, b and c, c is diagonal side, a and b the shorter sides, a < b
    """
    num_of_solutions = {}

    for a in range (1,1000/3):
        for b in range(a+1,(1000-a)/2):
            c = math.sqrt(a**2 + b**2)
            if int(c) == c:  # c is an integer
                p = a + b + int(c)     
                if p < 1000:
                    if p not in num_of_solutions:
                        num_of_solutions[p] = 1
                    else:
                        num_of_solutions[p] += 1

    print max(num_of_solutions.keys(), key=(lambda p: num_of_solutions[p]))  # answer is: 840
    print num_of_solutions[840]  # answer is 8 right triangles



def main():
    euler39_2()

if __name__ == '__main__':
    main()