# second assignment - series
# sum of factorials e.g. sum of first 3 terms is 3! + 2! + 1!
# looping

def sum_factorial():
    sum_terms = 0    
    num1 = int(input('Enter the number of terms to sum their factorials: '))
    for i in range(1,num1+1):
        sum_terms = sum_terms + factorial(i)  
    print("The sum of ", num1, "terms is ", sum_terms)

def factorial(num): 
    factorial = 1 
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

sum_factorial()

