class FirstDayOfMonth:
  def __init__(self, year, month, day_of_week):
    self.year = year
    self.month = month
    self.day_of_week = day_of_week

  def in_leap_year(self):
    output = False
    if self.year % 4 == 0:
      output = True
    if self.year % 100 == 0:
      output = False
    if self.year % 400 == 0:
      output = True
    return output

  def month_length(self):
    if self.month in [1, 3, 5, 7, 8, 10, 12]:
      return 31
    if self.month == 2:
      if self.in_leap_year():
        return 29
      else:
        return 28
    else:
      return 30

  def next(self):
    month_length = self.month_length()
    new_day_of_week = (self.day_of_week + month_length) % 7
    new_month = self.month + 1
    new_year = self.year
    if new_month == 13:
      new_month = 1
      new_year += 1
    return FirstDayOfMonth(new_year, new_month, new_day_of_week)

  def to_string(self):
    return str(self.year) + '-' + str(self.month) + '-1, ' + str(self.day_of_week)

def main():
  count = 0
  current_day = FirstDayOfMonth(1900, 1, 1)
  while current_day.year < 2001:
    if current_day.year >= 1901 and \
      current_day.day_of_week == 0:
      count += 1
    current_day = current_day.next()
  print count

main()