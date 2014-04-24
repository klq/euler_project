import math

def euler21():
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    N = 10000

    divisor_sums = [0]*2

    for i in range(2,N):
        divisor_sums.append(divisor_sum(i))

    amicable_total = 0
    for i in range(2,N):
        j = divisor_sums[i]

        # if amicable:
        if j<N and i == divisor_sums[j] and i!=j:
            amicable_total = amicable_total + i + j
            print i, j

    amicable_total /= 2 

    return amicable_total


def divisor_sum(n):
    """
    returns the sum of proper divisors of n (numbers less than n which divide evenly into n)
    """
    divisors = [1]

    upper = int(math.sqrt(n))
    for i in range(2, upper+1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(n/i)
    
    return sum(divisors)

print euler21() #31626