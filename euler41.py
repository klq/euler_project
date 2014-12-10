import itertools
import math

def is_prime(n):
    """returns True if n is a prime number"""
    if n < 2:
        return False
    if n in [2,3]:
        return True
    if n % 2 == 0:
        return False

    for factor in range(3, int(math.sqrt(n))+1, 2):
        if n % factor == 0:
            return False
    return True


def get_primes(maxi):
    """return a list of Booleans is_prime in which is_prime[i] is True if i is a prime number for every  i <= maxi"""

    is_prime = [True] * (maxi + 1)
    
    is_prime[0] = False
    is_prime[1] = False
    # is_prime[2] = True and all other even numbers are not prime
    for i in range(2,maxi+1):
        if is_prime[i]: # if current is prime, set multiples to current not prime
            for j in range(2*i, maxi+1, i):
                is_prime[j] = False

    return is_prime

def get_all_permutations(l):
    # returns n-length iterable object, n = len(l)
    # in lexical order (which means if input is [5,4,3,2,1], output will be in strictly decreasing order)
    return itertools.permutations(l)

def list2num(l):
    s = ''.join(map(str, l))
    return int(s)

def get_sorted_pandigital(m):
    """returns a (reversed) sorted list of all pandigital numbers given m digits"""
    perms = get_all_permutations(range(m,0,-1))

    for perm in perms: 
        # per is a m-length tuple
        perm = list2num(perm)
        yield perm
   

def euler41():
    """https://projecteuler.net/problem=41
       Pandigital Prime
       What is the largest n-digit pandigital prime that exists?
    """
    # Method 1: -----Turns out 1.1 itself is too costly
    # 1. Get all the primes
    # 2. Get all the pandigital numbers (sorted)
    # 3. Test if prime from largest to smallest, stop when first one found 
    # is_prime = get_primes(987654321) taking too long

    # Method 2: ----
    # 1. Get all the pandigital numbers (sorted)
    # 2. Test if prime from largest to smallest, stop when first one found 
    # !!! There will not be 8-digit or 9-digit pandigital prime numbers 
    # !!! Because they are all divisible by 3!
    # !!! Only check 7-digit and 4-digit pandigital numbers

    for m in [7,4]:
        for pd in get_sorted_pandigital(m):
            if is_prime(pd):
                print pd

                return

    # Answer is:
    # 7652413


def main():
    euler41()

if __name__ == '__main__':
    main()