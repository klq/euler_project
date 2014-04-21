def euler16():
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
    """

    # Solve:
    power = 2**1000
    power_str = str(power)

    digit_sum = 0
    for c in power_str:
        digit_sum += int(c)

    return digit_sum


print euler16() #1366

# or one-liner sum(int(digit) for digit in str(2**1000))