import math

def euler23():
    """
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
    which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors 
    is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
    the smallest number that can be written as the sum of two abundant numbers is 24. 
    By mathematical analysis, it can be shown that all integers greater than 28123 
    can be written as the sum of two abundant numbers. 
    However, this upper limit cannot be reduced any further by analysis even though 
    it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

    """


    N = 28123
    abundant_list = []
    abundant_list.append(False)

    abundant_sum_list = [False]*N

    result = 0 
    for i in range(1, N):
        if abundant_sum_list[i] ==  False:
            result += i            

        abundant_list.append(if_abundant(i))

        if abundant_list[i] == True:
            for j in range (1,i+1): # can be the sum of 2 of the same abundant_number
                if abundant_list[j] == True and i+j < N:
                    abundant_sum_list[i+j] = True

    return result

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


def if_abundant(n):
    return divisor_sum(n) > n

print euler23()  # 4179871