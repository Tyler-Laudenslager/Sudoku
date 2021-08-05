import copy
import sys

class Sudoku_Board:

    def __init__(self):
        self._grid = self.__grid_generator(9,9,init_value=0)
        self._grid_solved = None
        self._first_quad = [(a,b) for a in range(3) for b in range(3)]
        self._second_quad = [(a,b) for a in range(3) for b in range(3,6)]
        self._third_quad = [(a,b) for a in range(3) for b in range(6,9)]
        self._fourth_quad = [(a,b) for a in range(3,6) for b in range(3)]
        self._fifth_quad = [(a,b) for a in range(3,6) for b in range(3,6)]
        self._sixth_quad = [(a,b) for a in range(3,6) for b in range(6,9)]
        self._seventh_quad = [(a,b) for a in range(6,9) for b in range(3)]
        self._eighth_quad = [(a,b) for a in range(6,9) for b in range(3,6)]
        self._ninth_quad = [(a,b) for a in range(6,9) for b in range(6,9)]

    def __repr__(self):
        return "Sudoku_Board()"
        

    def possible(self,row,column,number):
        if number in self._grid[row]:
            return False
        
        for row_number in range(9):
            if number == self._grid[row_number][column]:
                return False
            
        quadrant = self.get_quad(row,column)[self.find_quad(row,column)]
        new_numbers = list()
        
        for (row,column) in quadrant:
            new_numbers.append(self._grid[row][column])
            
        if number in new_numbers:
            return False
        
        return True

    def is_solved(self):
        if self._grid_solved == None:
            self.solve()
        for row_index, row_number in enumerate(self._grid):
            for column_index, number in enumerate(row_number):
                solved_number = self._grid_solved[row_index][column_index]
                if number == solved_number:
                    continue
                else:
                    return False
        return True

    def get_quad(self,row,column):
        return [self._first_quad,
                self._second_quad,
                self._third_quad,
                self._fourth_quad,
                self._fifth_quad,
                self._sixth_quad,
                self._seventh_quad,
                self._eighth_quad,
                self._ninth_quad]

    def find_quad(self,row,column):

        if (row,column) in self._first_quad:
            return 0
        elif (row,column) in self._second_quad:
            return 1
        elif (row,column) in self._third_quad:
            return 2
        elif (row,column) in self._fourth_quad:
            return 3
        elif (row,column) in self._fifth_quad:
            return 4
        elif (row,column) in self._sixth_quad:
            return 5
        elif (row,column) in self._seventh_quad:
            return 6
        elif (row,column) in self._eighth_quad:
            return 7
        elif (row,column) in self._ninth_quad:
            return 8
        else:
            return ValueError

    def solve(self):
        for row in range(0,9):
            for column in range(0,9):
                if self._grid[row][column] == 0:
                    for add_number in range(1,10):
                        if self.possible(row,column,add_number):
                            self.insert_number(row,column,add_number)
                            self.solve()
                            self._grid[row][column] = 0
                    return
        self._grid_solved = copy.deepcopy(self._grid)
        return

    def __grid_generator(self,n,m,init_value):
        n_grid = list()
        for row in range(n):
            n_row = list()
            for column in range(m):
                n_row.append(init_value)
            n_grid.append(n_row)

        return n_grid

    def print(self, solved=False):
        
        if solved:
            print("<<---Sudoku--Solved---->>")
            if self._grid_solved == None:
                self.solve()
                grid = self._grid_solved
        else:
            grid = self._grid
        print()
        print("<<-------Sudoku-------->>")
        print("|-----------------------|")
        row_number = 0
        column_number = 0
        for row in range(len(grid)):
            row_number += 1
            print("|",end=' ')
            for column in grid[row]:
                column_number += 1
                if column_number == 3:
                    column_number = 0
                    print(column,end=' ')
                    print("|",end=' ')
                else:
                    print(column,end=' ')
            print()
            if row_number == 3:
                row_number = 0
                print("|-----------------------|")
        
    def insert_number(self,x,y,number):
        if self.possible(x,y,number):
            self._grid[x][y] = number
            return
        else:
            print("Error: Cannot place number in grid")
            return
    

    def remove_number(self,x,y):
        self._grid[x][y] = 0
        return

    def clear(self):
        self._grid = self.__grid_generator(9,9)
        return

# End of class definition #
# -------------------------------------------
# Make easy sudoku puzzle board
        
def build_easy_sudoku_board():
    sudoku_board = Sudoku_Board()
    sudoku_board.insert_number(0,1,8)
    sudoku_board.insert_number(0,6,2)
    sudoku_board.insert_number(1,7,9)
    sudoku_board.insert_number(1,5,4)
    sudoku_board.insert_number(1,4,8)
    sudoku_board.insert_number(2,2,6)
    sudoku_board.insert_number(2,3,3)
    sudoku_board.insert_number(2,4,2)
    sudoku_board.insert_number(2,7,1)
    sudoku_board.insert_number(3,1,9)
    sudoku_board.insert_number(3,2,7)
    sudoku_board.insert_number(3,7,8)
    sudoku_board.insert_number(4,0,8)
    sudoku_board.insert_number(4,3,9)
    sudoku_board.insert_number(4,5,3)
    sudoku_board.insert_number(4,8,2)
    sudoku_board.insert_number(5,1,1)
    sudoku_board.insert_number(5,6,9)
    sudoku_board.insert_number(5,7,5)
    sudoku_board.insert_number(6,1,7)
    sudoku_board.insert_number(6,4,4)
    sudoku_board.insert_number(6,5,5)
    sudoku_board.insert_number(6,6,8)
    sudoku_board.insert_number(7,1,3)
    sudoku_board.insert_number(7,3,7)
    sudoku_board.insert_number(7,4,1)
    sudoku_board.insert_number(8,2,8)
    sudoku_board.insert_number(8,7,4)
    return sudoku_board

def splash_screen():
    print("""
Sudoku "No Ads"

Objective: Replace all zeros "0" with numbers
between 1-9 such that each row, column and 3x3
has no duplicate numbers between 1-9.
   
Example 2,3,4 means we wish to enter the number
"4" into the second row third column position in
the matrix.
""")

def action_menu(puzzle):
    while True:
        try:
            x,y,number = [int(x) for x in input("Enter x,y,number: ").split(",")]
            if x == 0 or y == 0 or number == 0:
                raise ValueError
            puzzle.insert_number(x-1,y-1,number)
            return
        except ValueError:
            print("Invalid Value\nx -> 1-9\ny -> 1-9\nnumber -> 1-9")
            puzzle.print()
        except IndexError:
            print("Invalid Value\nx -> 1-9\ny -> 1-9\nnumber -> 1-9")
            puzzle.print()
        
    
    

def puzzle():
    splash_screen()
    sudoku_puzzle = build_easy_sudoku_board()
    sudoku_puzzle.print()
    while not sudoku_puzzle.is_solved():
        action_menu(sudoku_puzzle)
        sudoku_puzzle.print()
    print("Sudoku solved nice!")
        
    


def main():
    print("   Sudoku Solver v2.0")
    print("<<-------------------->>")
    sudoku_puzzle = build_easy_sudoku_board()
    print("repr: ",sudoku_puzzle)
    sudoku_puzzle.print()
    sudoku_puzzle.print(solved=True)
    

if __name__ == "__main__":
    main()
    
