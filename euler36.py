def is_palindromes(s):
    # input should be a string
    return s == s[-1::-1]

def euler36():
    """https://projecteuler.net/problem=36
       Double-base palindromes
    """
    db_pal = []

    N = 1000000
    for n in xrange(1,N):
        # if palindrome in DEC
        dec_str = str(n)
        if is_palindromes(dec_str):
            # if palindrome in BIN
            bin_str = bin(n)
            bin_str = bin_str[2:]
            if is_palindromes(bin_str):
                print dec_str, bin_str
                db_pal.append(n)

    print sum(db_pal)

    # Answer is:
    # 872187


def main():
    euler36()

if __name__ == '__main__':
    main()