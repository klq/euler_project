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



def main():
    euler31()

if __name__ == '__main__':
    main()