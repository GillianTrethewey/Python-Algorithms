#third assignment - series
# sum ((-1)**(n+1)) / n e.g. 1/1 - 1/2 + 1/3 - 1/4 (7/12)
# array (list in python)
# array[2]: array[1] + next term

def series_array_method():
    sum_terms = []   
    num1 = int(input('Enter the number of terms to sum the series: '))
    sum_terms.append(1)
    print(sum_terms)
   for i in range(1,num1): #1,2,3 for num1 =4 (set 0 to 1)
        sum_terms.append(sum_terms[i-1] + ((-1)**(i))/(i+1))
#       sum_terms[i] = sum_terms[i-1] + ((-1)**(i))/(i+1)

       print(sum_terms)
    print("The sum of ", num1, "terms is ", sum_terms[num1-1])



series_array_method()
