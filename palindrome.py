vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];


def repeats():
  repeatedWords = []
  word = ''
  palindromeList = []
  sentence1 = str(input('Enter sentence 1: '))
  sentence2 = str(input('Enter sentence 2: '))
  listWords1 = sentence1.split()
  listWords2 = sentence2.split()
  print('sentence1 is: ', sentence1, 
    'sentence2 is: ' , sentence2, 
    'listWords1 is: ', listWords1, 
    'listWords2 is: ', listWords2)
  for element1 in listWords1:
    for element2 in listWords2:
      if element1 == element2:
        repeatedWords.append(element1)
        print('repeated Words: ', repeatedWords)
        if (isPalindrome(element1) == True):
          palindromeList.append(element1)
        print('palindromes contained within repeated words: ', palindromeList)
  return


def isPalindrome(word):
  revWord = ''.join(reversed(word))
  if (word == revWord):
    return True
  return False

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

repeats()

