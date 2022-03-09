num = int(input('Enter your number to test whether it\'s a Neon number: '))

def isNeon(num):
  sum = 0
  squaredNum = num**2
  stringSquaredNum = str(squaredNum)
  n = len(stringSquaredNum)
  for i in range(0,n):
    sum = sum + (int(stringSquaredNum[i]))
    if sum == num:
      return True
  return False

print('Is', num, 'Neon?', isNeon(num))