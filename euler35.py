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

def all_rotations(n):
    # returns all rotations of digits in a list
    str_n = str(n)
    rotations = [str_n]

    for i in range(1, len(str_n)):
        rot = str_n[i:] + str_n[0:i]
        rotations.append(rot)

    return rotations

def euler35():
    """https://projecteuler.net/problem=35
       Circular primes
    """
    
    N = 1000000
    count = 0
    is_prime = get_primes(N)
    primes = [index for index, flag in enumerate(is_prime) if flag ]

    for prime in primes:
        perms = all_rotations(prime)
        for p in perms:
            if not is_prime[int(p)]:
                break
        else:
            print prime
            count += 1

    print count

    # Answer is:
    # 55


def main():
    euler35()

if __name__ == '__main__':
    main()