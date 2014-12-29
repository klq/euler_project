import math

def euler53():
    """https://projecteuler.net/problem=53
       Combinatoric selections
    """
    
    count = 0
    for n in xrange(23,101):
        for r in xrange(2, n):
            if math.factorial(n) / math.factorial(r) / math.factorial(n-r) > 1000000 :
                count += 1

    print count

    # Answer is:
    # 4075


def main():
    euler53()

if __name__ == '__main__':
    main()