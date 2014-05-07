def euler32():
    """
    Pandigital products:
    We shall say that an n-digit number is pandigital if it makes use of all the digits 
    1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
    containing multiplicand, multiplier, 
    and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product 
    identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
    """

    pandigital_set = set('123456789')
    products_set = set()

    for m1 in range(1,2000):
        for m2 in range(1,5000):
            p = m1 * m2

            totalstr = str(m1) + str(m2) + str(p)

            if len(totalstr) == len(set(totalstr)) and  set(totalstr) == pandigital_set:  
                print m1, m2, p
                products_set.add(p)

    return sum(products_set)

print euler32()

"""
4 1738 6952
4 1963 7852
12 483 5796
18 297 5346
27 198 5346
28 157 4396
39 186 7254
42 138 5796
48 159 7632
138 42 5796
157 28 4396
159 48 7632
186 39 7254
198 27 5346
297 18 5346
483 12 5796
1738 4 6952
1963 4 7852
45228
"""

