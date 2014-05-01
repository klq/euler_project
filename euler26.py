def euler26():
    """
    Reciprocal cycles:
    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    """

    max_length = 0
    for i in range(2,1000):
        cycle = unit_fraction(i)
        if cycle > max_length:
            d = i
            max_length = cycle

    print d, max_length


def unit_fraction(n):
    # Key to solve: just need to store a list of remainders
    current_digit = 1
    temp_r = []
    
    while True:
        m,r = divmod(current_digit * 10, n)

        if r == 0:
            return 0 # no recurring cycle

        if r not in temp_r: # not recurring yet
            temp_r.append(r)
            current_digit = r

        else:
            recurring_cycle = len(temp_r) - temp_r.index(r) 
            return recurring_cycle

#print unit_fraction(81)
euler26() # 983