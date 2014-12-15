import itertools

def euler43():
    """https://projecteuler.net/problem=43
    Sub-string divisibility
    """

    good_list = []

    for pan in itertools.permutations(range(0,10)):        
        d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = pan

        # exclude the obvious ones

        if d1 == 0:
            continue
        if d6 not in [0,5]:
            continue       
        if d4 % 2 != 0:
            continue
        if (d3+d4+d5)% 3 != 0:
            continue

        if (100*d5 + 10*d6 + d7) % 7 != 0:
            continue

        if (100*d6 + 10*d7 + d8) % 11 != 0:
            continue

        if (100*d7 + 10*d8 + d9) % 13 != 0:
            continue
        if (100*d8 + 10*d9 + d10) % 17 != 0:
            continue
        
        print pan
        good_list.append(int(''.join(map(str,pan))))


    print sum(good_list)

    # Answer is: 
    # (1, 4, 0, 6, 3, 5, 7, 2, 8, 9)
    # (1, 4, 3, 0, 9, 5, 2, 8, 6, 7)
    # (1, 4, 6, 0, 3, 5, 7, 2, 8, 9)
    # (4, 1, 0, 6, 3, 5, 7, 2, 8, 9)
    # (4, 1, 3, 0, 9, 5, 2, 8, 6, 7)
    # (4, 1, 6, 0, 3, 5, 7, 2, 8, 9)
    # 16695334890



def main():
    euler43()

if __name__ == '__main__':
    main()