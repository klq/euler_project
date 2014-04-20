def euler9():
    # Problem:
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    
    # Solve:
    for a in range(999):
        for b in range(500):
            c = 1000-a-b
            if c > 0:
                if (a*a + b*b == c*c):
                    return a*b*c

print euler9() #31875000