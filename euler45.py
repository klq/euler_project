def generate_triangulars(n):
    for i in xrange(1,n+1):
        yield i * (i+1) / 2

def generate_pentagonals(n):
    for i in xrange(1, n+1):
        yield i * (3 * i - 1) / 2


def generate_hexagonals(n):
    for i in xrange(1, n+1):
        yield i * (2 * i - 1) 


def euler45():
    """https://projecteuler.net/problem=45
    Triangular, pentagonal, and hexagonal
    """

    n = 100000
    hexagonals = set(generate_hexagonals(n))
    pentagonals = set(generate_pentagonals(n))
    triangulars = set(generate_triangulars(n))

    print {x for x in hexagonals if x in pentagonals and x in triangulars}

    # Answer is: 
    # set([1, 40755, 1533776805])


    # tris = set({i * (i+1) /2 for i in xrange(1, n)})
    # pens = set({i * (3*i - 1) / 2 for i in xrange(1, n)})
    # hexs = set({i * (2*i - 1) for i in xrange(1, n)})
    # print {x for x in hexs if x in pens and x in tris}

def main():
    euler45()

if __name__ == '__main__':
    main()