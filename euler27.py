import math

def euler27():
    """
    Quadratic primes:
    Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

    It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

    The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -9 and 1601, is -126479.

    Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4
    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
    
    """

    max_consec_primes = 0
    product_coeff = 0
    params = [None] * 2

    for a in range(-999, 1001):
        for b in range(-999, 1001):

            if consecutive_primes(a,b) > max_consec_primes:
                max_consec_primes = consecutive_primes(a,b)
                params = [a,b]
                product_coeff = a * b
                
    print params, product_coeff, max_consec_primes


def consecutive_primes(a,b):
    consecutive_primes = 0

    i = 0
    while True:
        result = i * i + a * i + b
        
        if result > 0 and if_prime(result):
            consecutive_primes += 1
            i += 1
        else:
            return consecutive_primes


def if_prime(n):
    limit = int(math.sqrt(n)+1)
    for i in range(2,limit):
        if n % i == 0:
            return False
    return True


#print consecutive_primes(-79,1601)
euler27()  # -59231


