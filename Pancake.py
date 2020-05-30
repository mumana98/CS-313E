#  File: Pancake.py

#  Description: Without using the built-in function 'sort', sort a list of numbers by flipping them as if they were a stack of pancakes

#  Student's Name: Matthew Umana

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 02/18/2020

#  Date Last Modified:

#  Input: pancakes is a list of positive integers
#  Output: a list of the pancake stack each time you
#          have done a flip with the spatula 
#          this is a list of lists
#          the last item in this list is the sorted stack

def sort_pancakes ( pancakes ):
    every_flip = []
    len_of_lst = len(pancakes)
    for i in range(len_of_lst):
        sub_lst = pancakes[:len_of_lst]
        # finds the largest number from the subset
        max_pancake = max(sub_lst)
        # finds the index of the largest number from the subset
        mx_ind = pancakes.index(max_pancake) + 1
        # creates a temporary list up to the largest number's index
        temp_lst = pancakes[:mx_ind]
        # reverses the temporary list
        temp_lst.reverse()
        # deletes the original subset
        del pancakes[:mx_ind]
        # places the temporary list in the old subset's place
        ind = 0
        for j in temp_lst:
            pancakes.insert(ind,j)
            ind += 1

        print(pancakes)
        # temp_lst2 becomes a copy of pancakes list
        temp_lst2 = pancakes[:len_of_lst]
        # temp_lst2 is reversed
        temp_lst2.reverse()
        # the old pancakes list is deleted up to the new len_of_lst
        del pancakes[:len_of_lst]

        # temp_lst2 is reinserted into pancakes 
        ind2 = 0
        for j in temp_lst2:
            pancakes.insert(ind2,j)
            ind2 += 1
        
        # len_of_lst is decreased by 1
        len_of_lst -= 1
        # the flip for one number is printed
        print(pancakes)
    every_flip = pancakes
    return every_flip    # return a list of flipped pancake stacks

def main():
    # open the file pancakes.txt for reading
    in_file = open ("pancakes.txt", "r")

    line = in_file.readline()
    line = line.strip()
    line = line.split()
    print (line)
    pancakes = []
    # populate pancakes list with numbers from the file
    for item in line:
        pancakes.append (int(item))

    # print content of list before flipping
    print ("Initial Order of Pancakes = ", pancakes)

    # call the function to sort the pancakes
    every_flip = sort_pancakes ( pancakes )

    # print the contents of the pancake stack after
    # every flip
    '''
    for i in range (len(every_flip)):
        print (every_flip[i])
    '''
    # print content of list after all the flipping
    print ("Final Order of Pancakes = ", every_flip)

if __name__ == "__main__":
    main()
