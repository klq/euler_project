def euler13():
  f = open('./euler13_file.txt','ru')
  thesum = 0
  for line in f:
    thesum += int(line)
  
  return str(thesum)[:10]

print euler13()
