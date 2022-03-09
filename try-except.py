# The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

# Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# You can use the ELSE keyword to define a block of code to be executed if no errors were raised:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# The FINALLY block, if specified, will be executed regardless if the try block raises an error or not.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# Raise an error and stop the program if x is less than 0:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")