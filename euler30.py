def euler30():
    """
    Digit fifth powers:
    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:


    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
    """
    fifth_powers = []

    for i in range(2,200000):
        digit_powers = sum([int(c)**5 for c in str(i)])
        if i == digit_powers:
            fifth_powers.append(i)

    print sum(fifth_powers)

euler30() #443839