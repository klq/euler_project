def euler33():
    """
    https://projecteuler.net/problem=50
    Digit canceling fractions:

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to 
    simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """

    for de in xrange(11,100):
        for nu in xrange(10,de):
            d1,d2 = divmod(de,10)
            n1,n2 = divmod(nu,10)

            tru_div = de*1.0/nu 

            if d2 == 0 or n2 == 0:
                continue

            if d1 == n1 and d2 * 1.0 / n2 == tru_div:
                print de, nu, "---->", d2, n2

            elif d1 == n2 and d2 * 1.0 / n1 == tru_div:
                print de, nu, "---->", d2, n1

            elif d2 == n1 and d1 * 1.0 / n2 == tru_div:
                print de, nu, "---->", d1, n2

            elif d2 == n2 and d1 * 1.0 / n1 == tru_div:
                print de, nu, "---->", d1, n1
                

def main():
    euler33()

    # Answer is:
    # 100 

if __name__ == '__main__':
    main()




