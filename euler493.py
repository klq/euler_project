def euler493():
    """https://projecteuler.net/problem=493
    Under The Rainbow

    70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.
    What is the expected number of distinct colors in 20 randomly picked balls?
    Give your answer with nine digits after the decimal point (a.bcdefghij).

    """

    # x_red = 1 if picked ones has red, x_red = 0 if picked ones has no red
    # x_yellow = 1 if picked ones has yellow, x_yellow = 0 if picked ones has no yellow
    # E(number of colors picked) = E(x_red + x_orange + x_yellow + .... + x_purple)
    # E(x_red + x_orange + x_yellow + .... + x_purple) = E(x_red) + E(x_orange) + E(x_yellow) + E(x_green) + E(x_blue) + E(x_brown) + E(x_purple)
    #

    # E(x_red) = E(there is red in the pick) = 1 - E(there is no red in the pick) 

    # result = (1 - (60./70.) * (59./69.) * (58./68.) * (57./67./) * ..... * (41./51.)) * 7.0

    upper = 1
    for i in range(41,61):
        upper *= i

    downer = 1
    for j in range(51,71):
        downer *= j

    result = 7.0 * (1.0 - upper * 1.0 / downer )
    print result

    # Answer is:
    # 6.81874180202






def main():
    euler493()

if __name__ == '__main__':
    main()