def get_order(s):
    """returns the aphabetical order of a letter.
    treats upper and lower cases letters alike.

    eg.
    get_order('S') = 19
    get_order('K') = 11
    get_order('Y') = 26
    """

    return 0 if s=='"' else ord(s) - 64

def get_word_value(s):
    summ = 0
    for c in s:
        summ += get_order(c)   
    return summ
 

def euler42():
    # find all triangle numbers under 520 (26*20, no words will have numbers bigger than this)
    all_tris = []
    for n in range(1,40): # pretty arbitrary., 0.5 * 40 * 41 ~= 800
        all_tris.append(0.5*n*(n+1))


    # open and read file
    f = open('p042_words.txt','rU+')
    all_text = f.read()
    all_text_list = all_text.split(',')

    f.close()

    triangle_count = 0
    for word in all_text_list:
        word_value =  get_word_value(word)

        if word_value in all_tris:
            triangle_count += 1
            

    print triangle_count


def main():
    euler42()


if __name__ == '__main__':
    main()

