from c4 import ConnectFour

class Hard(ConnectFour):
    def __init__(self, psym, csym):
        ConnectFour.__init__(self,psym,csym)
    
    def minimax(self, depth, isMaximizing):
        c = self.checkWin()
        if c:
            if c == self.psym:
                return -1000
            else:
                return +1000
        if self.tie() or depth == self.DLIM:
            return self.eval()
        
        choices = [j for j in range(7) if self.avail[j]>=0]
        if isMaximizing:
            bestscore = float('-inf')
            bestcol = -1
            for col in choices:
                self.updtBoard(col, self.csym)
                score = self.minimax(depth+1, False)
                self.avail[col] += 1
                self.board[self.avail[col]][col] = '*'
                self.board[]
                if score > bestscore:
                    bestscore = score
                    bestcol = col
            if depth == 0:
                return (bestcol, bestscore)
            else:
                return bestscore
        else:
            worstscore = float('inf')
            for col in choices:
                self.updtBoard(col, self.psym)
                score = self.minimax(depth+1, True)
                self.avail[col] += 1
                self.board[self.avail[col]][col] = '*'
                if score < worstscore:
                    worstscore = score
            return worstscore