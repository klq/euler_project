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

def euler37():
    """https://projecteuler.net/problem=37
       Truncatable primes
    """
    # generate a list of prime numbers < N
    N = 1000000
    is_prime = get_primes(N)
    primes = [index for index, flag in enumerate(is_prime) if flag]

    truncs = []

    for p in primes:
        if p < 10:
            continue

        p_str = str(p)
        pp = p_str
        l = len(p_str)

        if p_str[-1] in ['1', '9']:
            continue 
        if p_str[0] in ['1', '4', '6', '8', '9']:
            continue

        # truncate from left to right
        
        while l > 1:
            pp = pp[1:]
            l -= 1

            if int(pp) not in primes: # not still prime
                break
        else: 
            pp = p_str
            l = len(str(p))

            while l > 1:
                pp = pp[:-1]
                l -= 1

                if int(pp) not in primes:
                    break

            else: 
                print p
                truncs.append(p)
         

    print sum(truncs)

    # Answer is:
    # 748317


def main():
    euler37()

if __name__ == '__main__':
    main()