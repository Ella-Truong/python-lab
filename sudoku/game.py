from board import *
from cell import *
import random

class Game:
    def __init__(self,name,level):
        self.name=name
        self.level=level
        
        given=self.level_to_given(level)
        self.board=Board(given)
    


    #each level will have different number of given cells
    #level 1 = easy, level 2 = medium, level 3 = hard. 
    def level_to_given(self,level):
        if level==1:
            return 30
        elif level==2:
            return 20
        elif level==3:
            return 10
        else: 
            return 30     #default given 
        

    '''
    After provide the difficulty level, let's create a board with corresponding number of given potisions. 
    -> choose arbitrary positions in the board for given -> set their values -> display the board with givens.
    This step is done by Board class. 
    '''
    
    #-------------------------------- GAME BEGINNING -------------------------------
    
    '''
    Player starts fill a value in a cell -> validate:
    1. location of cell
    2. value    
    3. sudoku rules
    -> 1 & 2 is like to check input, 3 is to check game rules. 
    '''
    
    #function to check cell's location -> return True of False
    def is_valid_location(self,row,col):
        return 0<=row<9 and 0<=col<9
    

    #start to fill value 
    def fill_cell(self,value,loc):
        row,col=loc
        
        #validate the target cell's location
        if not self.is_valid_location(row,col):
            print('Invalid location.')
            return
        
        #validate value
        if not 1<=value<=9:
            print('Invalid value! Must be 1-9.')
            return
        
        #if the loc is valid -> get that target cell = get Cell Object, then assign it to 'cell' variable
        cell=self.board.get_cell(loc)         
        
        #check if it's a given cell
        if cell.is_given:
            print('Cannot change a given cell')
            return 
        
        #check if the fill is valid - match Sudoku rules
        if not self.board.is_fill_valid(value,loc):
            print('Filling is not valid according to Sudoku rules')
            return 
        
        #save current value of the loc to history before fill the value -> needed for undo() method
        self.board.history.append((cell.val,loc))

        #make the move
        cell.val=value
        print(f"Placed {value} at ({row}, {col})")



    #undo whatever the last move was, automatically target to the most recent move
    def undo_move(self):
        if not self.board.history:
            return
        
        old_val, loc=self.board.history.pop()
        self.board.get_cell(loc).val=old_val

    
    #clear a cell's value
    def delete_value(self,loc):
        row,col=loc
        cell=self.board.get_cell(loc)    #get_cell(loc) return a Cell object

        if not cell.is_given and cell.val is not None:
            self.board.history.append((cell.val,loc))
            cell.val=None

    
    #check if the Sudoku puzzle has been completely and correctly solved
    def is_solved(self):
        pass

    def end_game(self):
        pass





    

    

    

    

    
