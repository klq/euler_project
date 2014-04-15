def euler3():
    n = 600851475143
    for i in range(2, 1000000):
    	if n%i == 0:
    		print str(i) + " is a factor"
    		while n%i == 0:
    			n = n/i

    print i

euler3()