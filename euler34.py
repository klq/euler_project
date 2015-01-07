import math

def euler34():
    """https://projecteuler.net/problem=34
       Digit factorials
    """

    result = []
    N = 2540160 #factorial(9) * 7
    for n in xrange(10, N):
        str_n = str(n)
        facts = [ math.factorial(int(l)) for l in str(n)]
        if sum(facts) == n:
            print n
            result.append(n)

    print sum(result)

    # Answer is:
    # 145
    # 40585
    # 40730


def main():
    euler34()

if __name__ == '__main__':
    main()