# Name: Ella Truong & Caleb Sheets
# Lab 10 - Singleton - Dungeon Maze

class Map:
    _instance=None
    _initialized=False

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    
    
    def __init__(self):
        if not Map._initialized:
            with open('map.txt','r') as file:
                map_data=[]
                for line in file:
                    map_data.append(list(line.strip()))
                self._map=map_data
            self._revealed=[[False for _ in range(5)] for _ in range(5)]
            Map._initialized=True


    def __getitem__(self,row):
        return self._map[row]
    

    def __len__(self):
        return len(self._map)

    def show_map(self,loc):
        #return a string of 5x5 view around the hero at loc [row,col]
        r, c=loc
        rows=len(self._map)
        cols=len(self._map[0])
        output=[]

        for i in range(rows):
            row_str=''
            for j in range(cols):
                if (i,j) == (r,c):
                    row_str+='*'
                elif self._revealed[i][j]:
                    row_str+=self._map[i][j]
                else:
                    row_str+='x'
            output.append(row_str)
        return '\n'.join(output)

   
    def reveal(self,loc):
        row,col=loc
        self._revealed[row][col]=True
    
    def remove_at_loc(self,loc):
        r,c=loc
        self._map[r][c]='n'
    

    


