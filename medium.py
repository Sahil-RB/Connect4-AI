from c4 import ConnectFour
import os
class Medium(ConnectFour):
    def __init__(self, psym, csym):
        ConnectFour.__init__(self, psym,csym)
        

    def selectMove(self):
        cols = [j for j in range(7) if self.avail[j]>=0]
        bestCol = -1
        bestScore = float('-inf')
        for col in cols:
            self.updtBoard(col, self.csym)
            score = self.getScore()
            self.avail[col] += 1
            self.board[self.avail[col]][col] = '*'
            if score > bestScore:
                bestScore = score
                bestCol = col
        return bestCol
    
    def play(self):
        if self.csym == 'R':
            self.updtBoard(self.selectMove(), self.csym)
        c = ' '
        t = False
        while True:
            _ = os.system('cls')
            self.showBoard()
            while True:
                m = int(input('Enter the column index of your move '))
                if self.avail[m] < 0:
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
        
        _ = os.system('cls')
        print('Final Board:')
        self.showBoard()
        if t:
            print('Tie')
            return 
        if c == self.psym:
            print('You have won!')
        else:
            print('You lost')

    def evalhelper(self, s, ans): #checks a particular set of four, and counts lines of threes and twos for player and comp
        if s.count(self.psym) == 3 and s.count('*') == 1:
            ans[self.psym][-1] += 1
        elif s.count(self.psym) == 2 and s.count('*') == 2:
            ans[self.psym][-2] += 1
        if s.count(self.csym) == 3 and s.count('*') == 1:
            ans[self.csym][-1] += 1
        elif s.count(self.csym) == 2 and s.count('*') == 2:
            ans[self.csym][-2] += 1
    
    def eval(self): #returns the number of pieces for each player in the center col, twos and threes
        ans = {self.psym:[0,0,0], self.csym:[0,0,0]} #[centercol, twos, threes]
        for i in range(6):
            if self.board[i][3] == self.psym:
                ans[self.psym][0] += 1
            elif self.board[i][3] == self.csym:
                ans[self.csym][0] += 1
        for i in range(6): #horizontal four in a row
            for j in range(4):
                s = self.board[i][j] + self.board[i][j+1] + self.board[i][j+2] + self.board[i][j+3]
                self.evalhelper(s,ans)
        
        for j in range(7): #vertical
            for i in range(3):
                s =  self.board[i][j] + self.board[i+1][j] + self.board[i+2][j] + self.board[i+3][j]
                self.evalhelper(s,ans)
        
        for i in range(5,2,-1): #rightward diagonal
            for j in range(0,4):
                s = self.board[i][j] + self.board[i-1][j+1] + self.board[i-2][j+2] + self.board[i-3][j+3]
                self.evalhelper(s,ans)
        
        for i in range(5,2,-1): #leftward diagonal
            for j in range(6,2,-1):
                s = self.board[i][j] + self.board[i-1][j-1] + self.board[i-2][j-2] + self.board[i-3][j-3] 
                self.evalhelper(s,ans)
        
        return ans

    
    def getScore(self):
        c = self.checkWin()
        if c == self.csym:
            return 1000
        elif c == self.psym:
            return -1000
        ans = self.eval()
        score = 0
        score += 4*ans[self.csym][0]
        score += 2*ans[self.csym][1]
        score += 5*ans[self.csym][2]
        score -= 2*ans[self.psym][1]
        score -= 100*ans[self.psym][2]
        return score

if __name__ == '__main__':
    print('Pick R to go first')
    psym = input('Enter R or Y for your symbol ')
    csym = {'R':'Y', 'Y':'R'}[psym]
    game = Medium(psym, csym)
    game.play()
    input()