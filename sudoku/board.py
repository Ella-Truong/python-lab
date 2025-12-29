from cell import *
import random

class Board:
    def __init__(self,given=30):
        self.grid=[[Cell() for _ in range(9)] for _ in range(9)]
        self.given=given
        self.history=[]   #for undo()
    
    def set_given(self):
        all_positions=[]
        for row in range(9):
            for col in range(9):
                all_positions.append((row,col))   #all_potitions is a list of tuples for 81 locations in grid 9x9 -> [(0,0),(0,1),(0,2),....]

        given_positions=random.sample(all_positions,30)   #list of 30 tuples picked randomly from the all_potisions list

        for row, col in given_positions:
            value=random.randint(1,9)
            self.grid[row][col].val=value
            self.grid[row][col].is_given=True


    def display_board(self):
        print("Here is the puzzle. Good luck!\n")
        for row in range(9):
            for col in range(9):
                cell=self.grid[row][col]
                #show None for empty, number otherwise
                print(cell.val if cell.val!=0 else None, end=' ')
            print()     # add this to move to the next line after each row


    
    def get_cell(self,loc):
        row, col = loc
        return self.grid[row][col]   #return a Cell object 


    
    #ensure the value doesn't already exist in the same row, same column, or in the same 3x3 box
    #this method in Board is to check Sudoku's rules
    def is_fill_valid(self,value,loc):
        row,col=loc

        #check column
        for r in range(9):
            if self.grid[r][col].val==value:
                return False
        
        #check row
        for c in range(9):
            if self.grid[row][c].val==value:
                return False
            
        #check 3x3 block
        start_row=(row//3)*3
        start_col=(col//3)*3
        for r in range(start_row, start_row+3):
            for c in range(start_col, start_col+3):
                if self.grid[r][c].val==value:
                    return False
        
        return True
    

    '''
        1. Check if the move is valid (delegated to Game class or validated elsewhere)
        2. Confirm the cell is not a given
        3. Save the current state/value to history for undo()
        4. Update the cell's value
        5. if the cell is empty, and this is the initial game setup, mark it as given and increment _given.
    '''
    def add_filled(self,val,loc): 
        pass
      
    ''' to reset the whole board - two options:
        1. keep places and values of given values -> reset()
        2. new game board with new places and new values of pre-filled values -> generate() 
    '''
    def reset(self):    
        pass


    '''
        1. No duplicate placements
        2. Values placed follow Sudoku rules
        3. The puzzle is solvable
    '''
    def generate(self):
        pass



    '''
        1. Return Cell object at the loction
        2. Useful for inspection, manual updates,...
        For example: place number 5 at location (3,4)
        -> At Game class: 
           1. make_move(val,loc)
           2. Call board.get_cell(loc) to get the target Cell 
            -> is the cell not given?
            -> is val a valid move, based on row, col, and block
           3. If valid, call board.add_filled(val,loc)
    '''



    

    
    


