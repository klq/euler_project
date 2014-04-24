def euler22():
    """
    Using names.txt (right click and 'Save Link/Target As...''), 
    a 46K text file containing over five-thousand first names, 
    begin by sorting it into alphabetical order. 
    Then working out the alphabetical value for each name, 
    multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, 
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
    So, COLIN would obtain a score of 938 x 53 = 49714.

    What is the total of all the name scores in the file?
    """

    f = open('./euler22_names.txt','rU')
    
    # read whole file into string
    # replace " by empty string
    # split by comma
    # append to a list
    allnames = f.read().replace('"','').split(',')
    allnames = sorted(allnames)

    # calculate the total score:
    total_score = 0
    for i in range(len(allnames)):
        total_score += score(allnames[i]) * (i+1) 

    return total_score


def score(s):
    score = 0
    for c in s.lower():
        score += ord(c) - ord('a') + 1 
    return score

print euler22() #871198282

