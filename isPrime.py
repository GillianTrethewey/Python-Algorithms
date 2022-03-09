def isPrime(num):
	i = 1
	results = False
	if num < 2:
		return results
	i = 2
	while i < num:
		if num%i == 0:
			return results
		i += 1
	results = True
	return results

num = int(input('Enter your number to test whether it\'s a Prime number: '))
print("Is ", num ," prime: ", isPrime(num))

num = int(input("Enter your number to test whether it's prime: "))

def isPrime(num):
  for i in range(2,num):
    if num%i == 0:
      return False
    else:
      return True
  
print('Is', num, 'prime?', isPrime(num))