from c4 import ConnectFour
import os
import sys
import pygame

SQUARESIZE = 100
width = 7*SQUARESIZE
height = 7*SQUARESIZE
size = (width,height)
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
RADIUS = int(SQUARESIZE/2 - 5)
pygame.font.init()

class Hard(ConnectFour):
    def __init__(self, psym, csym):
        ConnectFour.__init__(self,psym,csym)
        self.DLIM = 6
        pygame.init()
        self.screen = pygame.display.set_mode(size)

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
    
    def minimax(self, depth, isMaximizing, alpha, beta):
        c = self.checkWin()
        if c:
            if c == self.psym:
                return -1000
            else:
                return +1000
        if self.tie() or depth == self.DLIM:
            return self.getScore()
        
        choices = [j for j in range(7) if self.avail[j]>=0]
        if isMaximizing:
            bestscore = float('-inf')
            bestcol = -1
            for col in choices:
                self.updtBoard(col, self.csym)
                score = self.minimax(depth+1, False, alpha, beta)
                self.avail[col] += 1
                self.board[self.avail[col]][col] = '*'
                if score > bestscore:
                    bestscore = score
                    bestcol = col
                alpha = max(alpha, bestscore)
                if beta<=alpha:
                    break
            if depth == 0:
                return (bestcol, bestscore)
            else:
                return bestscore
        else:
            worstscore = float('inf')
            for col in choices:
                self.updtBoard(col, self.psym)
                score = self.minimax(depth+1, True, alpha, beta)
                self.avail[col] += 1
                self.board[self.avail[col]][col] = '*'
                if score < worstscore:
                    worstscore = score
                beta = min(beta, worstscore)
                if beta<=alpha:
                    break
            return worstscore
    
    def drawBoard(self):
        for c in range(7):
            for r in range(6):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE,(r+1)*SQUARESIZE, SQUARESIZE,SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)

        for c in range(7):
            for r in range(6):
                if self.board[r][c] == 'R':
                    pygame.draw.circle(self.screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2),int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif self.board[r][c] == 'Y':
                    pygame.draw.circle(self.screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()
    
    def play(self): 
        if self.csym == 'R':
            m, _ = self.minimax(0,True,float('-inf'),float('+inf'))
            self.updtBoard(m, self.csym)
        c = ' '
        t = False
        gameover = False
        while not gameover:
            self.drawBoard()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pygame.draw.rect(self.screen,BLACK,(0,0,width,SQUARESIZE))
                if event.type == pygame.MOUSEMOTION:
                    posx = event.pos[0]
                    if self.psym == 'R':
                        pygame.draw.circle(self.screen,RED,(posx, int(SQUARESIZE/2)),RADIUS)
                    else:
                        pygame.draw.circle(self.screen,YELLOW,(posx, int(SQUARESIZE/2)),RADIUS)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = posx//SQUARESIZE
                    if self.avail[col] >= 0:
                        self.updtBoard(col, self.psym)
                        self.drawBoard()
                        c = self.checkWin()
                        if c:
                            gameover = True
                        t = self.tie()
                        if t:
                            gameover = True
                        m, _ = self.minimax(0,True,float('-inf'),float('+inf'))
                        self.updtBoard(m, self.csym)
                        c = self.checkWin()
                        if c:
                            gameover = True
                        t = self.tie()
                        if t:
                            gameover = True
                
        _ = os.system('cls')
        print('Final Board:')
        self.showBoard()
        if t:
            print('Tie') 
        if c == self.psym:
            print('You have won!')
        elif c == self.csym:
            print('You lost')
        self.drawBoard()
        myfont = pygame.font.SysFont("monospace", 75)
        if c == self.psym:
            label = myfont.render("You have won!!", True, (255,255,255))
            labelRect = label.get_rect()
            labelRect.center = (width/2,SQUARESIZE/2)
            self.screen.blit(label,labelRect)
        elif c == self.csym:
            label = myfont.render("You lost!!", True, (255,255,255))
            labelRect = label.get_rect()
            labelRect.center = (width/2,SQUARESIZE/2)
            self.screen.blit(label,labelRect)
        else:
            label = myfont.render("Game tied!!", True, (255,255,255))
            labelRect = label.get_rect()
            labelRect.center = (width/2,SQUARESIZE/2)
            self.screen.blit(label,labelRect)
        pygame.display.update()
        pygame.time.wait(15000)
        pygame.quit()

if __name__ == '__main__':
    print('Pick R to go first')
    psym = input('Enter R or Y for your symbol ')
    csym = {'R':'Y', 'Y':'R'}[psym]
    game = Hard(psym, csym)
    game.play()
    input()