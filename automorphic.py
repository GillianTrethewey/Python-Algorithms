
def automorphic():
    
    num = int(input('Enter your number to test: '))
    numDigits = len(str(num))
    numSquared = pow(num,2)
    print("The square of your number is: " , numSquared)

    lastNDigits = numSquared%pow(10,numDigits)

    if lastNDigits == num:
      print(num, "is an automorphic number.")
    else:
      print(num, "is not an automorphic number.")


def automorphic2():
    num = int(input('Enter your number to test: '))
    numDigits = len(str(num))
    print("The square of your number is: " , pow(num,2))

    string_num_squared = str(num**2)
    listNumSquared = []
    listNumSquared[:] = string_num_squared

    lastNDigits = listNumSquared[(len(listNumSquared) - len(str(num))):]

    stringNDigits = ''
    stringNDigits = stringNDigits.join(lastNDigits)
    numberNDigits = 0
    numberNDigits = int(stringNDigits)

    if num != numberNDigits:
        print(num , " is not an automorphic number.") 
    else:
        print(num , " is an automorphic number.")


automorphic()
automorphic2()

# reversed 