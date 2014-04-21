def euler14():
    
    # Problem:
    """
    The following iterative sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    # Solve: (fast method)
    N = 1000001
    longest_steps = [0]*N
    longest_steps[1] = 1

    for i in range(1,N):
        temp = []

        j = i
        
        # keeping looking for the next one while:
        while (j>=N) or longest_steps[j] == 0 :
            temp.append(j)      
            j = collatz_walk(j)
        found_steps = longest_steps[j]

        # pop the elements from the temp list:
        count = 1
        while temp:
            j = temp.pop()
            if j < N:
                longest_steps[j] = found_steps + count
            count += 1

    max_index = max( (v, i) for i, v in enumerate(longest_steps) )[1]
    
    return max_index

def collatz_walk(n):
    if n%2==0:
        n = n/2
    else:
        n = 3*n+1
    return n

def count_steps(n):
    # chain start at 1
    steps = 1
    if n == 1:
        return steps
    
    while (n>1):
        n = collatz_walk(n)
        steps += 1
    return steps

def main(): 
    # slow method:
    longest_steps = [0]*1000001
    for i in range(1000001):
        longest_steps[i] =  count_steps(i)

    max_index = max( (v, i) for i, v in enumerate(longest_steps) )[1]
    print max_index, longest_steps[max_index]


print euler14() #837799 
