import random

class ConnectFour:
    def __init__(self, psym, csym):
        self.avail = [5 for i in range(7)] #row number piece falls into for a column
        self.board = [['*' for i in range(7)] for j in range(6)]
        self.psym = psym
        self.csym = csym
    
    def showBoard(self):
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
                if self.board[i][j] == self.board[i-1][j-1] == self.board[i-2][j-2] == self.board[i-3] != '*':
                    return self.board[i][j]
        
        return False
    
class Easy(ConnectFour):
    def __init__(self, psym, csym):
        ConnectFour.__init__(self,psym,csym)
    
    def selectMove(self):
        choices = [i for i in range(len(self.avail)) if self.avail[i] >= 0]
        mov = random.choice(choices)
        return mov

    def play(self):
        if self.csym == 'R':
            self.updtBoard(self.selectMove, self.csym)
        c = ' '
        t = False
        while True:
            self.showBoard()
            while True:
                m = int(input('Enter the column index of your move '))
                if self.avail[m] <= 0:
                    print('Enter a valid index')
                else:
                    self.updtBoard(m, self.psym)
                    break
            c = self.checkWin()
            if c:
                break 
            t = self.tie()
            if t:
                break
            self.updtBoard(self.selectMove(), self.csym)
            c = self.checkWin()
            if c:
                break 
            t = self.tie()
            if t:
                break
        
        print('Final Board:')
        self.showBoard()
        if t:
            print('Tie')
            return 
        if c == self.psym:
            print('You have won!')
        else:
            print('You lost')

class Medium(ConnectFour):
    def __init__(self, psym, csym):
        ConnectFour.__init__(self, psym, csym)

    def checkThreeRow(self):
        count = 0
        for i in range(6): #horizontal
            for j in range(3):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] != '*':
                    return self.board[i][j]
        
        for j in range(7): #vertical
            for i in range(2):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] != '*':
                    return self.board[i][j]
        
        for i in range(5,2,-1): #rightward diagonal
            for j in range(0,4):
                if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3] != '*':
                    return self.board[i][j]
        
        for i in range(5,2,-1): #leftward diagonal
            for j in range(6,2,-1):
                if self.board[i][j] == self.board[i-1][j-1] == self.board[i-2][j-2] == self.board[i-3] != '*':
                    return self.board[i][j]

    
if __name__ == '__main__':
    psym = input('Enter R or Y for your symbol ')
    csym = {'R':'Y', 'Y':'R'}[psym]
    game = Easy(psym, csym)
    game.play()
    input()
            
        
