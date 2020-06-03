#  File: Spiral.py

#  Description: number spiral represented in a 2D list. When the number chosen is in the list, 
#               it prints the number itself and the numbers around it

#  Student's Name: Matthew Umana

#  Student's UT EID: msu245

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 02/15/20

#  Date Last Modified:


#  Input: dim is a positive odd integer
#  Output: function returns a 2-D list of integers arranged
#          in a spiral
def create_spiral (dim):
    spiral_list=[]
    
    # creates an empty 2D list of dim x dim size
    for i in range (dim):
        row=[]
        for j in range(dim):
            row.append(0)
        spiral_list.append(row)

    # final number is max_num or dim squared
    max_num = dim * dim
    start = 1
    x = dim//2
    y = dim//2

    # starting position is the center of the 2D list
    spiral_list[x][y]=start
    start += 1
    length = 1

    # populates a 2D list that is dim x dim size. Goes from 0 to dim squared sprialing the list
    for i in range(dim):
        for j in range(length):
            if start <= max_num:
                y += 1
                spiral_list[x][y] = start
                start += 1
        for k in range(length):
            if start <= max_num:
                x += 1
                spiral_list[x][y] = start
                start += 1
        for l in range(length+1):
            if start <= max_num:
                y -= 1
                spiral_list[x][y] = start
                start += 1
        for m in range(length+1):
            if start <= max_num:
                x -= 1
                spiral_list[x][y] = start
                start += 1
        length += 2
        
    return spiral_list
    

#  Input: grid a 2-D list containing a spiral of numbers
#         val is a number withing the range of numbers in
#         the grid
#  Output: sub-grid surrounding the parameter val in the grid
#          sub-grid could be 1-D or 2-D list
def sub_grid (grid, val):
    sub_list = list()
    ind = 0
    list_ind = None
    counter = 0
    
    for k in grid:
        if val in k:
            ind = k.index(val)
            list_ind = counter
            break
        else:
            counter += 1
            pass
     
    ind_left = ind - 1
    ind_right = ind + 2
    list_indUp = list_ind - 1
    list_indDown = list_ind + 1
    
    # checks if the index is on the first row and/or column
    if ind == 0 or list_ind == 0:
        if ind_left <= 0:
            ind_left = ind
        if list_indUp <= 0:
            list_indUp = list_ind

    # checks if the index is on the last row and/or column
    if list_ind == len(grid)-1:       
        if list_indDown >= len(grid)-1:
            list_indDown = list_ind  
        if ind_right >= len(grid[1]):
            ind_right = ind + 1
    
    # if the number index is the first row, print it, the numbers next to it, and the 3 numbers below it on the next row
    if grid[list_indUp][ind_left:ind_right] == grid[list_ind][ind_left:ind_right]:
        for i in grid[list_ind][ind_left:ind_right]:
            print(i, end=" ")
        print()
        for j in grid[list_indDown][ind_left:ind_right]:
            print(j, end=" ")
        print()
    
    # if the number index is the last row, print it, the numbers next to it, and the 3 numbers above it on the next row
    elif grid[list_indDown][ind_left:ind_right] == grid[list_ind][ind_left:ind_right]:
        for i in grid[list_indUp][ind_left:ind_right]:
            print(i, end=" ")
        print()
        for j in grid[list_ind][ind_left:ind_right]:
            print(j, end=" ")
        print()
        
    # print the numbers directly next to, above, and diagonal to the given number
    else:  
        for i in grid[list_indUp][ind_left:ind_right]:
            print(i, end=" ")
        print()
        for j in grid[list_ind][ind_left:ind_right]:
            print(j, end=" ")
        print()
        for k in grid[list_indDown][ind_left:ind_right]:
            print(k, end=" ")
        print()
    
    sub_list.append(grid[list_ind][ind_left:ind_right])
    
    if list_ind > len(grid):
        list_ind = counter
    else:
        list_ind += 1
        
    return sub_list


def main():
    
    # prompt user to enter dimension of grid
    user_dim=int(input("Enter Dimension: "))
    spiral_num = int(input("Enter number in spiral: "))

    # if the dimension is even, make it odd   
    if user_dim%2==0:
        user_dim = user_dim+1

    # create spiral
    grid = create_spiral(user_dim)

    # prompt user to enter value in grid
    # print subgrid surrounding the value
    if spiral_num > 0 and spiral_num <= user_dim**2:
        sub_grid(grid, spiral_num)
    else:
        print("Number not in Range")

if __name__ == "__main__":
    main()


  
