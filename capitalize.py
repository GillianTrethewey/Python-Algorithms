s = str(input('Enter the string to be capitalized: '))

def solve(s):
  for word in s.split(): #splits the string into a list where default separator is space
    s = s.replace(word,word.capitalize()) #replaces all incidences of word with word that is capitalized
  print(s)

solve(s)  

# prints out for s.split : ['alison hack']
# prints out for s: alison hack, Alison hack, Alison Hack