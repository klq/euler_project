def euler17():
    """
    If the numbers 1 to 5 are written out in words: 
    one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
    how many letters would be used?

    """

    "1-10"
    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    total_l = 0
    for word in ones:
        total_l += len(word)
    print total_l  #39  # 36 without 'ten'


    """21-99"""
    ties = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    total_l = 0
    for word in ties:
        total_l += len(word)
    print total_l  #46

    """11-19"""
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    total_l = 0
    for word in teens:
        total_l += len(word)
    print total_l  #67


    # Solve:
    # 1-10:
    letters1_10 = 39
    letters11_19 = 67 
    letters20_99 = 36*8 + 46*10


    # 1-99:
    letters1_99 = letters1_10 + letters11_19 + letters20_99
    print letters1_99

    # one hundred and 1-99:
    "one hundred and" + "1-99"
    letters101_999 = 36 * 99 + 99*9*10 + letters1_99*9

    # 100, 200, 300......900, 1000
    letters_hundreds = 36 + 7 * 9 + 3 + 8

    # grand total
    grand_total = letters1_99 + letters101_999 + letters_hundreds

    return grand_total



print euler17()