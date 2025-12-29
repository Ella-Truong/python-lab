class Cell:
    def __init__(self,val=None,is_given=False):
        self.val=val
        self.is_given=is_given     # mark if this cell was part of the original puzzle and non-editable

    def update_value(self,value,turn=3):
        if not self.is_given:
            self.val=value
        return self.value
    

    def clear_value(self):
        if not self.is_given:
            self.val=None           # empty cell
    
    def is_empty(self):
        return self.val is None
    
    def __str__(self):
        return self._val
    

