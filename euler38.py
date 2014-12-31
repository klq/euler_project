def is_pandigital(n):
    return sorted(str(n)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def euler38():
    """https://projecteuler.net/problem=38
       Pandigital multiples
    """
    
    pans = []

    for seed in xrange(1, 10000):
        concat = ''
        concat += str(seed)

        multiples = 1

        while len(concat) < 9:
            multiples += 1
            concat += str(multiples*seed)
        
        if len(concat) == 9 and is_pandigital(concat):
            print concat
            pans.append(concat)

    print max(pans)

    # Answer is:
    # 932718654


def main():
    euler38()

if __name__ == '__main__':
    main()