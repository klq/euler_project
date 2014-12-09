from operator import mul

def get_integers(number):
    """generator function that returns the next integer till (possibly) infinity"""
    while True:
        yield number
        number += 1

def len_num(number):
    """return the digits length of an integer"""
    return len(str(abs(number)))

def euler40():
    """https://projecteuler.net/problem=40
       Champernowne's constant
    """
    
    fractional_str = ''
    digit_count = 0

    for number in get_integers(1):
        digit_count += len_num(number) 
        fractional_str+=str(number)

        if digit_count > 1000000:
            break

    l = fractional_str
    ll = list([int(l[0]), int(l[9]) , int(l[99]) , int(l[999]) , int(l[9999]), int(l[99999]), int(l[999999])])
    result = reduce(mul,ll)
    print ll
    print result

    # Answer is:
    # [1,1,5,3,7,2,1]
    # 210
    




def main():
    euler40()

if __name__ == '__main__':
    main()