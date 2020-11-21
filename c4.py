import random

class ConnectFour:
    def __init__(self, psym, csym):
        self.avail = [5 for i in range(7)] #the row that a piece falls into for each column
        self.board = [['*' for i in range(7)] for j in range(6)]
        self.psym = psym
        self.csym = csym
    
    def showBoard(self):
        print()
        for i in range(6):
            for j in range(7):
                print(self.board[i][j], end = '  ')
            print()
    
    def updtBoard(self, col, sym):
        row = self.avail[col]
        self.board[row][col] = sym
        self.avail[col] -= 1
    
    def tie(self): 
        for i in self.avail:
            if i >= 0:
                return False
        return True

    def checkWin(self): #returns winning symbol, else returns false
        for i in range(6): #horizontal four in a row
            for j in range(4):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] != '*':
                    return self.board[i][j]
        
        for j in range(7): #vertical
            for i in range(3):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] != '*':
                    return self.board[i][j]
        
        for i in range(5,2,-1): #rightward diagonal
            for j in range(0,4):
                if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3] != '*':
                    return self.board[i][j]
        
        for i in range(5,2,-1): #leftward diagonal
            for j in range(6,2,-1):
                if self.board[i][j] == self.board[i-1][j-1] == self.board[i-2][j-2] == self.board[i-3][j-3] != '*':
                    return self.board[i][j]
        
        return False
    

            
        
