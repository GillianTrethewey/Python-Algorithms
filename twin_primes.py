# twin primes - two adjacent primes that have a difference of 2
# e.g. 3 and 5, 5 and 7, 7 and 9, 9 and 11


def twin_primes():    
    num1 = int(input('Enter the first number to test: '))
    num2 = int(input('Enter the second number to test: '))
    twin_prime_result = False
    if check_prime(num1) == True:
        if check_prime(num2) == True:
            diff = abs(num1-num2)
            if (diff == 2):
                twin_prime_result = True   
    print("Are your numbers twin Primes? " , twin_prime_result)


def check_prime(num):
    is_prime = True
    for i in range(2,num):
        if num%i == 0:
            is_prime = False
    return is_prime

twin_primes()