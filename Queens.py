#  File: Queens.py

#  Description: Fill each column of a chess board with queens in
#               a way that no queen can eliminate another

#  Student Name: Matthew Umana

#  Student UT EID: msu245

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 03/09/20

#  Date Last Modified: 

class Queens (object):
    # initialize the board
    def __init__ (self, n = 8, total=0):
        self.board = []
        self.n = n
        self.total = total
        for i in range (self.n):
            row = []
            for j in range (self.n):
                row.append ('*')
            self.board.append(row)

    # print the board
    def print_board (self):
        for i in range (self.n):
            for j in range (self.n):
                print (self.board[i][j], end = ' ')
            print ()

    # check if no queen captures another
    def is_valid (self, row, col):
        for i in range (self.n):
            if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
                return False
        for i in range (self.n):
            for j in range (self.n):
                row_diff = abs (row - i)
                col_diff = abs (col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do a recursive backtracking solution
    def recursive_solve (self, col):
        count = 0
        if(col == self.n):
            # see if there are enough queens
            for i in self.board:
                for j in i:
                    if j == 'Q':
                        count += 1
            if count == self.n:
                self.total += 1
                self.print_board()
                print()
                
        else:
            for i in range(self.n):
                if(self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    if(self.recursive_solve (col + 1)):
                        return True
                    self.board[i][col] = '*'
            return False

    # if the problem has a solution print the board
    def solve (self):
        for i in range(self.n):
            if (self.recursive_solve(i)):
                self.print_board()
    
def main():
    num_queens = int(input("Enter the size of board (no more than 8, no less than 1): "))
    while num_queens > 8 or num_queens < 1:
        num_queens = int(input("Enter the size of board: "))
    print()
    # create a regular chess board
    game = Queens(num_queens)

    # place the queens on the board
    game.solve()
    print("There are " + str(game.total) + " solutions for a " + str(num_queens) + " x " + str(num_queens) + " board.")

main()


                    




        
