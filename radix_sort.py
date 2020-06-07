import math
import os
import random
import re
import sys

class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

    # function for testing. displays the contents of your queue
    def display(self):
        for item in self.queue:
            print(item + ", ", end="")
        print()


def radix_sort(nums, dict):
    lst = []
    lst_lens = []
    q_lst = []

    #find length of largest str
    for i in nums:
        lst_lens.append(len(i))
    total_len = max(lst_lens)

    #make list of queues
    for q in range(total_len):
        q_lst.append(Queue())
    for q in q_lst:
        for i in range(36):
            q.enqueue([])
    #format string list
    for i in nums:
        while len(i) < total_len:
            #nums.pop(0)
            i = "+" + i
        lst.append(i)
    print(lst)
    #populate queues
    place = total_len - 1
    for q in q_lst:
        for s in lst:
            if s != None:
                char = s[place]
                if char.isalpha() or char.isdigit():
                    place_val = dict[char]
                else:
                    temp_place = place
                    temp_char = char
                    while True:
                        temp_place += 1
                        temp_char = s[temp_place]
                        if temp_char.isalpha() or temp_char.isdigit():
                            break
                    place_val = dict[temp_char]
                q.queue[place_val].append(s)
            else:
                continue
        place-=1
        #print(place)
        lst = []
        for i in q.queue:
            for j in i:
                if j != None:
                    lst.append(j)
    return lst

def main():
    # We went ahead and created the dictionary for you
    dict = {
    '0': 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9':
    9,
    'a': 10,'b': 11,'c': 12,'d': 13,'e': 14,'f': 15,'g': 16,'h': 17,'i':
    18,
    'j': 19,'k': 20,'l': 21,'m': 22,'n': 23,'o': 24,'p': 25,'q': 26,'r':
    27,
    's': 28,'t': 29,'u': 30,'v': 31,'w': 32,'x': 33,'y': 34,'z': 35
    }
    sorted_lst = radix_sort(['311', '796', '495', '137', '158', '984', '145', 'abc'], dict)
    formatted = []
    for i in sorted_lst:
        formatted.append(i.replace("+", ''))
    print(formatted)

if __name__ == "__main__":
    main()