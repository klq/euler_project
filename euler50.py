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

def euler50():
    """https://projecteuler.net/problem=50
       Consecutive prime sum
    """
    
    
    N = 1000000
    is_prime = get_primes(N)
    primes = [index for index, flag in enumerate(is_prime) if flag ]

    longest_length = 1
    limit = len(primes)
    for i in xrange(0, limit) :
        length = 1
        prime_sum = primes[i]      
        for j in xrange(i+1,limit):
            length += 1
            prime_sum += primes[j]
            if prime_sum > N:
                break
            if is_prime[prime_sum]:
                if length > longest_length:
                    longest_length = length
                    print i, primes[i], j, primes[j], length, prime_sum
          

    # Answer is:
    #  3 7 545 3931 543 997651
    # 7 + 11 + 13 + ..... + 3931 = 997651


def main():
    euler50()

if __name__ == '__main__':
    main()