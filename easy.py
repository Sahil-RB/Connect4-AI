from c4 import ConnectFour
import random
import os

class Easy(ConnectFour):
    def __init__(self, psym, csym):
        ConnectFour.__init__(self,psym,csym)
    
    def selectMove(self):
        choices = [i for i in range(len(self.avail)) if self.avail[i] >= 0]
        mov = random.choice(choices)
        return mov

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



    
if __name__ == '__main__':
    print('Pick R to go first')
    psym = input('Enter R or Y for your symbol ')
    csym = {'R':'Y', 'Y':'R'}[psym]
    game = Easy(psym, csym)
    game.play()
    input()