#  File: Nim.py

#  Description: Winning a game of nim - find the right number to take from a heap in your first turn to ensure you win

#  Student's Name: Matthew Umana

#  Course Name: CS 313E 

#  Unique Number: 50300

#  Date Created: 1/28/20

#  Date Last Modified:

# calculates the nim_sum for all the heaps
def nim_sum (heaps):
    total_nim_sum = 0 
    for i in heaps:
        total_nim_sum ^= i
    return total_nim_sum

# calculates how much to take from which heap and returns the heap and the amount
def find_heap (heaps, nim_sum):
    new_heaps = []
    for i in heaps:
        new_heaps.append(i ^ nim_sum)
    heap = new_heaps.index(min(new_heaps))
    take = heaps[heap] - new_heaps[heap]
    return take, heap+1

# function is meant to catch edge cases for when all heaps are only 1
def edge_case(heap):
    for i in heap:
        if i == 1 and len(heap)%2 == 0:
            return True
        elif i == 1 and len(heap)%2 == 1:
            return False
        else:
            return False

def main():
    # read input from input file nim.txt
    # the input file's first line is the number of test cases followed by the test cases
    # each subsequent row are numbers that symbolize the size of the heap
    f = open("nim.txt", "r")
    for i in range(int(f.readline())):
        string_heaps = f.readline().split()
        integer_heaps = []
        for j in string_heaps:
            integer_heaps.append(int(j))
        nim_summed = nim_sum(integer_heaps)
        remove, pile = find_heap(integer_heaps, nim_summed)
        # print the result of nim_summed
        if nim_summed == 0 or nim_summed == 1:
            if edge_case(integer_heaps):
                print("Remove", remove + 1, "counters from Heap", pile)
            else:
                print("Lose Game")
        else:
            print("Remove", remove, "counters from Heap", pile)

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()









  
