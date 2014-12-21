def euler48():
    """https://projecteuler.net/problem=48
       Self powers
    """
    
    
    N = 1000
    l = range(1, N+1)
    ll = [i**i for i in l]
    powers = str(sum(ll))
    print powers[-10:]

    # Answer is:
    # 9110846700


def main():
    euler48()

if __name__ == '__main__':
    main()