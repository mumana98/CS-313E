#  File: Work.py 

#  Description: See the difference in the time of calculating linear versus binary search algorithms

#  Student Name:  Matthew Umana

#  Student UT EID:  msu245

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 02/21/20

#  Date Last Modified:

import time

# Returns the amount of lines you need to write before 
# you drink your first cup of coffee. k is the productivity 
# factor - when ever you take a drink of coffee, the number 
# of lines you are able to write will decrease by v//k**exp.
# Each intermident drink of coffee must equate to the total 
# number of lines minimum you must write.
def lines_sufficient(v: int, k: int) -> int:
    exp = 0
    lines = 0
    while(True):
        if (v//k**exp) == 0:
            break
        else:
            lines += v//k**exp
            exp += 1
    return lines
    
# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    min_lines = 0
    for v in range(1,n+1):
        min_lines = lines_sufficient(v, k)
        if min_lines >= n:
            return v 

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:  
    low = 1
    high = n
    mid = (low + high) // 2

    while(low < high):
        if (lines_sufficient(mid, k) >= n) and (lines_sufficient(mid-1, k) < n): 
            return mid
        elif lines_sufficient(mid, k) < n:
            low = mid + 1
            mid = (low + high) // 2
        else:
            high = mid - 1
            mid = (low + high) // 2
            
    # Element is not present in the array 
    return -1

def main():
    # open work.txt file for reading
    in_file = open("work.txt", "r")

    # num cases is the first number character in the file which totals the number of cases to run
    num_cases = int((in_file.readline()).strip())


    for i in range(num_cases):
        inp = (in_file.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        # start Binary Search time and print result and time taken
        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        
        # start Linear Search time and print result and time taken
        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
    main()
