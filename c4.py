import random
from colorama import Fore, Back, Style, init
class ConnectFour:
    '''
        Base connect four class that is inherited by each level
     '''
    def __init__(self, psym, csym):
        init()
        self.avail = [5 for i in range(7)] #the row that a piece falls into for each column, initially pieces fall to the bottom
        self.board = [['*' for i in range(7)] for j in range(6)] # board object
        self.psym = psym #player symbol
        self.csym = csym #computer symbol
        self.ccol, self.pcol = None, None
        if self.psym == 'R':
            self.ccol = Fore.YELLOW
            self.pcol = Fore.RED
        else:
            self.ccol = Fore.RED
            self.pcol = Fore.YELLOW

    
    def showBoard(self):  #prints out the board
        print()
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == 'R':
                    print(Fore.RED + self.board[i][j], end = '\t')
                elif self.board[i][j] == 'Y':
                    print(Fore.YELLOW + self.board[i][j], end = '\t')
                else:
                    print(Style.RESET_ALL+self.board[i][j], end = '\t')
            print(Style.RESET_ALL+ '\n')
    
    def updtBoard(self, col, sym): #takes in a column and symbol and drops piece into that column
        row = self.avail[col]
        self.board[row][col] = sym
        self.avail[col] -= 1 #for that column, the piece now has to land one row above
    
    def tie(self):  #checks if there are no more possible moves to be made
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
    

            
        
