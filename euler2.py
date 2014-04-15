def euler2():
    fibo = []
    fibo.append(1)
    fibo.append(2)
    fibo.append(3)

    i = 2
    evensum = 2
    while fibo[i] < 4000000:
        newfibo = fibo[i-1] + fibo[i]
        fibo.append(newfibo)
        i += 1

        if newfibo%2 == 0:
            evensum += newfibo
    print evensum

euler2()



