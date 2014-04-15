def least_common_multiple(numbers):
    lcm = 1
    for i in range(len(numbers)):
        factor = numbers[i]
  
        if factor != 1:
            lcm = lcm * factor
            
            for j in range(len(numbers)):
                if numbers[j] % factor == 0 :
                    numbers[j] = numbers[j] / factor

    return lcm

def euler5():
  # Problem:
  """2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
  """

  # Solve:
  return least_common_multiple(range(1,21)) #232792560

euler5()