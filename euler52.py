def is_permutated(m, n):
    return sorted(str(m)) == sorted(str(n))


def euler52():
    """https://projecteuler.net/problem=52
       Permuted multiples
    """
    
    
    N = 1000000
    for i in xrange(1,N):
        if is_permutated(i, 2*i):
            if is_permutated(i, 3*i):
                if is_permutated(i, 4*i):
                    if is_permutated(i, 5*i):
                        if is_permutated(i, 6*i):
                            print i
                            return

    # Answer is:
    # 142857


def main():
    euler52()

if __name__ == '__main__':
    main()