#  File: Reducible.py

#  Description: Find the largest word in a file that is
#               reducible - a word that when you take a letter from is still a valid word

#  Student Name: Matthew Umana

#  Student UT EID: msu245

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 03/23/20

#  Date Last Modified:

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that 
# string
def step_size (s, const = 13):
  word_size = len(s)
  step = 0
  for i in range(word_size):
    step = (step * 26 + (ord(s[i]) - 96)) % const
  return const - step

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):
  hash_table_size = len(hash_table)
  step = step_size(s)
  index = hash_word(s, hash_table_size)
  new_idx = index + step

  if hash_table[index] != " ":
    while hash_table[new_idx] != " ":
      new_idx = (new_idx + step) % hash_table_size
    hash_table[new_idx] = s
  else:
    hash_table[index] = s

# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):
  hash_table_size = len(hash_table)
  index = hash_word(s, hash_table_size)
  step = step_size(s)
  next_idx = (step + index) % hash_table_size

  if hash_table[index] == " ":
    return False
  elif hash_table[index] == s:
    return True
  while True:
    if hash_table[next_idx] == " ":
      return False
    elif hash_table[next_idx] == s:
      return True
    next_idx = (step + next_idx) % hash_table_size

# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise

def is_reducible (s, hash_table, hash_memo):
  if len(s) == 1:
    return vowel(s)
  else:
    if (find_word(s, hash_memo)):
      return True
    if ((vowel(s) == False) or (find_word(s, hash_table) == False)):
      return False
    for char in range(len(s)):
      sub = s[0:char] + s[char+1:]
      if is_reducible(sub, hash_table, hash_memo):
        insert_word(sub, hash_memo)
        return True
    return False
    
def vowel(s):
  vowels = ["a", "i", "o"]
  for i in vowels:
    for char in s:
      if char == i:
        return True
  return False

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
  max_len = 0
  biggest_words = []
  
  for word in string_list:
    if len(word) == max_len:
      biggest_words.append(word)
    if len(word) > max_len:
      max_len = len(word)
      biggest_words = []
      biggest_words.append(word)
  return biggest_words

def main():
  # create an empty word_list
    word_list = []
  # open the file words.txt
    f = open("words.txt","r")
  # read words from words.txt and append to word_list
    for line in f:
        line = line.strip()
        word_list.append(line)
  # close file words.txt
    f.close()
  # find length of word_list
    word_list_size = len(word_list)
  # determine prime number N that is greater than twice
  # the length of the word_list
    N = word_list_size * 2
    while (is_prime(N) == False):
        N += 1
  # create an empty hash_list
    hash_list=[]
  # populate the hash_list with N blank strings
    for spot in range(N):
        hash_list.append(" ")
  # hash each word in word_list into hash_list
  # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)
    
  # create an empty hash_memo of size M
    hash_memo = []
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list

  # populate the hash_memo with M blank strings
    M = 0.3 * word_list_size
    while (is_prime(M) == False):
        M += 1

    for spot in range(int(M)):
        hash_memo.append(" ")

  # create an empty list reducible_words
    reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if (vowel(word) and is_reducible(word, hash_list, hash_memo)):
            reducible_words.append(word)
  # find words of the maximum length in reducible_words
    biggest_words = get_longest_words(reducible_words)
  
  # print the words of maximum length in alphabetical order
  # one word per line
    for word in biggest_words:
        print(word)

if __name__ == "__main__":
  main()
