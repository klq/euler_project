def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i  in range(2, n+1):
        if is_prime[i]:
            j = 2*i
            while j < n+1:
                is_prime[j] = False
                j += i

    return is_prime


def get_distinct_factors(n, primes):
    distinct_factors = []
    
    for p in primes:
        if n == 1:
            return distinct_factors

        new = True
        while n % p == 0 :
            if new:
                distinct_factors.append(p)
                new = False
            n = n / p


def euler47():
    """https://projecteuler.net/problem=47
       Distinct primes factors
    """
    
    # generate a list of prime numbers < N
    N = 200000
    is_prime = get_primes(N)
    primes = [index for index, flag in enumerate(is_prime) if flag]

    
    # find 4 consecutive integers with exactly 4 distinct prime factors
    for i in range(1,N):
        if len(get_distinct_factors(i, primes)) == 4:
            if len(get_distinct_factors(i+1, primes)) == 4:
                if len(get_distinct_factors(i+2, primes)) == 4:
                    if len(get_distinct_factors(i+3, primes)) == 4:
                        print i
                        
                        return

    # Answer is:
    # 134043


def main():
    euler47()

if __name__ == '__main__':
    main()