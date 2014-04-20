def euler10():
    # Problem:
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """

    # Solve:
    # Resue the eratosthenes function from euler7.py

def eratosthenes(n):
    """
    To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

    1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the first prime number.
    3. Starting from p, enumerate its multiples by counting to n in increments of p, and mark them in the list 
       (these will be 2p, 3p, 4p, etc.; the p itself should not be marked).
    4. Find the first number greater than p in the list that is not marked. 
       If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
    """

    primes = [True] * (n+1)
    primes[0:2] = [False]*2 # set 0 and 1 as not prime

    prime_sum = 0
    for p in range(2,n+1):
        if primes[p] == True:
            prime_sum += p

            # mark the multiples of current prime as not-prime
            pr = 2*p
            while pr <= n:   
                primes[pr] = False
                pr += p

    return prime_sum

print eratosthenes(2000000)  #142913828922