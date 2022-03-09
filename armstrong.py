num = int(input('Enter your number to test whether it\'s an Armstrong number: '))

def isArmstrong(num):
  sum = 0
  stringNum = str(num)
  n = len(stringNum)
#  for i in range(0,n):
  for digit in stringNum:
#    sum = sum + (int(stringNum[i])**3)
    sum = sum + int(digit)**3
    if sum == num:
      return True
  return False

print('Is', num, 'Armstrong?', isArmstrong(num))