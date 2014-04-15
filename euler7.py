def euler7():
    # Problem:
    """By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """

    # Solve:
    MAX = 200000
    num = 10001

    primes = [True] * MAX  # primes[i] == 1 if i is a prime number, otherwise 0
    primes[0:2] = [False] * 2
    only_primes = []

    for factor in range(2,MAX):
        if len(only_primes) == num:
            print '\nThe %d-th prime number is: %d' % (num, only_primes[num-1])
            return

        if primes[factor] == True: # if is prime, then mark all multiples as false
            for j in range(factor+1,MAX):
                if primes[j] == True and j % factor == 0:
                    primes[j] = False

            only_primes.append(factor)

#euler7() #104743


def eratosthenes(n,i):
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
    primes[0:2] = [False]*2

    j = 0
    for p in range(2,n+1):
        if primes[p] == True:
            j += 1
            if j == i:
                print p

            pr = 2*p
            while pr <= n:   
                primes[pr] = False
                pr += p

    return

eratosthenes(200000,10001)
