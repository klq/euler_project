#import collections

def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i  in range(2, n+1):
        if is_prime[i]:
            j = 2*i
            while j < n+1:
                is_prime[j] = False
                j += i

    return is_prime

def euler49():
    """https://projecteuler.net/problem=49
       Prime permutations
    """
    
    
    N = 10000
    is_prime = get_primes(N)
    primes = [index for index, flag in enumerate(is_prime) if flag and index > 1000]


    for i in range(1,len(primes)):
        p1 = primes[i]

        for j in range(i+1, len(primes)):
            
            #if collections.Counter(str(primes[i])) == collections.Counter(str(primes[j])):
            if sorted(str(primes[i])) == sorted(str(primes[j])):
                p2 = primes[j]

                p3 = p2 + (p2 - p1)

                if p3 in primes and sorted(str(p3)) == sorted(str(p2)):
                    print p1, p2, p3
                    break

    # Answer is:
    # 1487 4817 8147
    # 2969 6299 9629


def main():
    euler49()

if __name__ == '__main__':
    main()