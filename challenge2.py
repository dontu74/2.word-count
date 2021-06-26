# Import the python sys library to read a file

from enum import unique
import sys
import re

print("\nWelcome !, this demo is using text content from the novel 'Oliver Twisted' Chapter III.\n")

# Create a function call to count how many characters in the file
def count_char (letter):
    x = [] # create an new array list to separate each alpahbet letter in the for loop
    y =""
    new_word = re.sub(r'[^\w\s]', y, letter) # Using regex and sub () method to deliminated the punctuation marks and assign to a new string (y)
    new_word = new_word.split() # Using the split () to deliminate all the white spaces
    # print(new_word)
    for n in new_word: # using the for loop to add each alphabet letter to the x array list
        x += n
    return print("\nTotal number of characters in this file: " + str(len(x))) # using the len() to determine the length of the contents
    # return print(x)

# Create a function call to count how many words in the file
def count_words (letter):
    y = ""
    cont = 0
    new_word = re.sub(r'[^\w\s]', y, letter) # Using regex and sub () method to deliminated the punctuation marks - \s new line, tab, ^ = not, \w = word character
    new_word = new_word.split() # Using the split () to deliminate all the white spaces
    # print(new_word)
    # new_array = []
    for n in new_word:
        # print(letter)
        # new_array += n
        cont += 1
        # print(cont)
    return print("\nTotal number of words count in this file: " + str(cont))


# Create a function call to count how many sentence in the file
def count_sent (letter):
    cnt = 0
    for n in letter:
        if n.endswith("."): # the endswith() method will search for a period at the end of the sentence
            cnt += 1
            # print(n)
    return print("\nTotal number of sentences in this file: " + str(cnt))

# Create a function call to count how many paragraph in the file
def count_para (letter):
    # print(letter)
    paragraphCount = 0
    x = re.findall('\n\n',letter)  # The findall() method will find all the white spaces -- \n\n = empty lines
    for n in x:
        paragraphCount += 1
    # print(paragraphCount)
  
    return print("\nTotal number of paragraphs in this file: " + str(paragraphCount))

# Create a function call to count how many unique word in the file
def count_bigr (letter):
  # Dictionary for counting the words
    y = ""
    new_word = re.sub(r'[^\w\s]', y, letter) # Using regex and sub () method to deliminated the punctuation marks - \s new line, tab, ^ = not, \w = word character
    new_word = new_word.split()
    word_count = {}
    # print(new_word)
    for line in new_word:
        if line not in word_count:
            word_count[line] = 1
        else:
            word_count[line] += 1
    # for k, v in word_count:
    # sortedbyKey = {k: v for k, v in sorted(word_count.items())}
    sortedbyVal = {k: v for k, v in sorted(word_count.items(), key= lambda v: v[1])}
    sortedbyVal2 = {k: v for k, v in sorted(word_count.items(), key= lambda v: v[1], reverse=True)}
    
    arr = set(sortedbyVal)
    # print(sortedbyKey)
    # print(sortedbyVal)
    print("\nThe following are the most unique words in the content:\n\n " + str(arr))
    # print(sortedbyVal2)
    # print(sorted(word_count.keys()))
    # print(sorted(word_count.values()))

    # return print("Total number of unique pairs of words in this file: " + str(unique_words_count))

# This function will replace all the "a" or "A" to "@" and all the "e" and "E" to "3"
def funker_words(phrase):
    new_phrase = ''
    for letter in phrase:
        if letter == 'A' or letter == 'a':
            new_phrase += '@'
        elif letter == 'E' or letter == 'e':
            new_phrase += '3'
        elif letter == 'I' or letter == 'i':
            new_phrase += '!'
        elif letter == 'G' or letter == 'g':
            new_phrase += '9'
        else:
            new_phrase += letter
    return print(new_phrase + "\n")

with open('demo.txt', 'r') as f:
    word_string = f.read()   # the read () method read the contents from the file and assigned a variable "word_string" as a place holder for those contents
    # y = re.sub(r'[^\w\s]', y, word_string)  # using the regex (regular expression) library imported and sub () method in python to - search for pattern (punctuation and special characters)
    # word_string = y.split() # use the split() to remove all white spaces
    # print(word_string)

    count_char(word_string) 
    count_words(word_string) 
    count_sent(word_string) 
    count_para(word_string) 
    count_bigr(word_string) 
    # funker_words(word_string)
    
  
# assign y as an empty word_string - for place holder
# using the with open() in the sys library to read an external file name " demo.txt" as a f variable