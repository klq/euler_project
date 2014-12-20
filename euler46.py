import math

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

def euler46():
    """https://projecteuler.net/problem=46
       Goldbach's other conjecture
       What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    """
    
    # generate a list of prime numbers < N
    N = 10000
    is_prime = get_primes(N)
    primes = [index for index, flag in enumerate(is_prime) if flag]
    odd_composites = [index for index, flag in enumerate(is_prime) if (not flag) and (index % 2 == 1)] # this list has "1" in there but we'll deal with it later
    
    for i in odd_composites:
        if i == 1: # 1 is not a real composite, nor prime
            print 'begin searching..........\n'
            continue 

        
        for j in range(int(math.sqrt((i-1)/2)), 0, -1):
            r = i - 2*j*j

            if is_prime[r]:
               break
        else: # loop fell through without finding a solution
            print i
            return

    # Answer is:
    # 5777


def main():
    euler46()

if __name__ == '__main__':
    main()