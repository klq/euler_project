def euler44():
    """https://projecteuler.net/problem=44
    Pentagon numbers
    """

    # get all pentagon numbers
    all_pentagon_nums = []
    for n in range(1,5000):
        all_pentagon_nums.append( n * (3*n-1) / 2)

    diff = []
    for i in range(0,2500):
        for j in range(j+1,2500):
            a = all_pentagon_nums[i]
            b = all_pentagon_nums[j]

            if b-a in all_pentagon_nums and b+a in all_pentagon_nums:
                    diff.append(b-a)

    print min(diff)    

    # Answer is: 
    # 5482660


def generate_pentagonals(x):
    for i in xrange(1, x+1):
        yield i * (3 * i - 1) / 2

def euler44_better_solution():
    pentagonals =set(generate_pentagonals(2500))
    print min({x-y for x in pentagonals for y in pentagonals if x + y in pentagonals and x - y in pentagonals})


def main():
    euler44()

if __name__ == '__main__':
    main()