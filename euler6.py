def euler6():
  # Problem:
  """Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.
  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
  """

  # Solve:
  sum_squares = 0
  sums = 0

  for i in range(101):
    sums += i
    sum_squares += i*i

  squared_sum = sums * sums

  print abs(sum_squares - squared_sum)

euler6() #25164150
