# coding=utf-8 

def euler31():
    """
    Coin Sums:
    n England the currency is made up of pound and pence, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, (100p) and (200p).
    It is possible to make 200 in the following way:

    
    How many different ways can 200p be made using any number of coins?
    """

    # Just need to find how many combinations of [b,c,d,e,f,g, h] in which  100g + 50f + 20e +10d + 5c + 2b <= 200

    # Only look at the highest seven digits, 1p digit can be ignored

    num_combinations = 1 

    l = [0,0,0,0,0,0,0]
    while list_increment(l):
        num_combinations += 1

    print num_combinations


def list_increment(l):
    
    for i in range(0,7):   # l[0]是最低位，l[6]是最高位
        l[i] += 1
        new_value = 200*l[6] + 100*l[5] + 50*l[4] + 20*l[3] +10*l[2] + 5*l[1] + 2*l[0]

        if new_value <= 200: 
            return l
        else:
            # clear all the digits below i
            for j in range(i,-1,-1):
                l[j] = 0
    return None


def euler31_recursive():
    print p_level(200,7)

def p_level(n, level):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    if n < 0:
        return 0
    if level == 0:
        return 1
    return p_level(n-coins[level],level) + p_level(n,level-1)

def euler31_iterative():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    limit = 200

    p_level_cache = [[1 for x in range(len(coins))] for x in range(limit + 1)] # 8 by 201 matrix

    # because p_level_cache[0, y] = 1 for all y, p_level_cache[x,0] = 1 for all x

    for sum in range(1, limit + 1):
        for level in range(1, len(coins)):
                sub_sum = sum - coins[level]
                p_level_cache[sum][level] = p_level_cache[sum][level - 1] + (p_level_cache[sub_sum][level] if (sub_sum >= 0) else 0)


    print p_level_cache[limit][len(coins) - 1]


def main():
    euler31()

if __name__ == '__main__':
    main()