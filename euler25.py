def euler25():
    """fibo
    The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

    What is the first term in the Fibonacci sequence to contain 1000 digits?
    """
    import time
    start = time.time()

    fibo = []
    fibo.append(0)
    fibo.append(1)

    i = 2
    while True:
        new_fibo = fibo[i-2] + fibo[i-1]
        fibo.append(new_fibo)

        if len(str(new_fibo)) == 1000:
            print i
            break
            
        i += 1

    end = time.time()
    print "Time:"  , (end-start)*1000 , "ms"

    return new_fibo

# shorter code:
# f = [1,1]
# while True:
#   f.append(sum(f[(len(f)-2):]))
#   if len(str(f[-1])) >= 1000:
#     break
# print len(f)


euler25()
