def is_palindrome(n):
    """returns True if n is a palindrome, False if not a palindrome"""
    s = str(n)
    while len(s) > 1:
        if s[0] != s[-1]:
            return False
        else:
            s = s[1:-1]           
    return True

def is_palindrome2(n):
    s = str(n)
    return ( s == s[::-1] )

def euler4():
    # Problem:
    """A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    
    # Solve:
    max_palindrome = 0
    for a in range(999,900,-1):
        for b in range(999,900,-1):
            product = a * b

            if is_palindrome2(product) and product > max_palindrome:
                max_palindrome = product
                print a,b,product
    return max_palindrome

euler4() #906609
