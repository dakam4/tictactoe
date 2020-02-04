class Cell:
    playerSigns = ['X', 'O']

    def __init__(self):
        self.value = '-'
        self.state = False

    def setValue(self, value):
        if(not value in self.playerSigns):
            raise Exception("Value should be capital 'X' or 'O'.")
        if(self.state == True):
            raise Exception("Cell occupied by PLAYER " + self.value)
        
        self.value = value
        self.state = True
        
    def getValue(self):
        return self.value
    
    def getState(self):
        return self.state