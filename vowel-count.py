vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];

words = str(input('Enter the phrase: '))

def findVowels(word):
    count = 0
    for char in word:
      if char in vowels:
        count += 1
    return count;

def getWords(words):
  length = 0
  listWord = words.split()
  vowelCount = 0
  for word in listWord:
    lengthWord = len(word)
    vowelCount=findVowels(word)
    print('The word \"', word, '\" has',lengthWord, ' characters and', vowelCount,'vowels.')
  return 

getWords(words)

#list(word) gives individual characters
#word.split() gives separate words