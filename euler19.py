import datetime

def if_leap(y):
    leap = False

    if y % 4 == 0:
        leap = True

    if y % 100 == 0:
        leap = False

    if y % 400 == 0:
        leap = True
    
    return leap

def days_since_start(y,m,d): 
    pass

    if if_leap(y):
        return 366
    else:
        return 365

    days_dict = { 1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31}

def euler19():
    """
    You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """


    count = 0
    date = datetime.date(1901,1,1)

    while date < datetime.date(2000,12,31):
        # day of the week as an integer, where Monday is 0 and Sunday is 6.
        if date.day == 1 and date.weekday() == 6:
            count += 1

        date = date + datetime.timedelta(1)

    print count 

    # Answer is:
    # 171


def main():
    euler19()


if __name__ == '__main__':
    main()



