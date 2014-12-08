import math

def euler39():
    """https://projecteuler.net/problem=39
       Integer Right Triangles
    """
    num_of_solutions = {}

    
    for a in range (1,1000):
        for b in range(a+1,1000-a):
            for c in range(b+1, 1000-a-b):
            #print 'a={0}, b={1}, c={2}'.format(a, b, c)

                if a+b+c<=1000 and a**2+b**2 == c**2:
                    p = a + b + c                              
                    if p not in num_of_solutions:
                        num_of_solutions[p] = 1
                    else:
                        num_of_solutions[p] += 1

    print max(num_of_solutions.keys(), key=(lambda p: num_of_solutions[p]))  # answer is: 840


def main():
    euler39()

if __name__ == '__main__':
    main()