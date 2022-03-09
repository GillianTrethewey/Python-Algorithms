word = str(input('Enter the word for the vowel count (no array method): '))
word.lower()

def findVowels1(word):
    count = 0
    for char in word:
      if (char == "a" or char  == "e" or char  == "i" or char  == "o" or char  == "u"):
        count = count + 1
    return count;

print('The number of vowels in', word, 'is:',findVowels1(word))

word = str(input('Enter the word for the vowel count (vowel array method)'))
word.lower()
listWord = list(word)
vowels = ["a", "e", "i", "o", "u"]
def findVowels2(listWord):
    count = 0
    for char in listWord:
      if char in vowels:
        count += 1
    return count;

print('The number of vowels in', word, 'is:',findVowels2(word))

word = str(input('Enter the word for the vowel replacement: '))
word.lower()
listWord = list(word)
vowels = ["a", "e", "i", "o", "u"]

def vowelReplace(listWord):
  s = []
  changedS = ''
  for char in listWord:
    if char in vowels:
      char = "x"
    s.append(char)
  s = changedS.join(s)
  return s;

print('The word:', word, ' is tranformed into:', vowelReplace(listWord))
