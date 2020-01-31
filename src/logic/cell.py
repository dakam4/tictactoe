class Cell:
    valuePossibilities = ['X', 'O']

    def __init__(self):
        self.value = ''

    def setValue(self, value):
        if(value != 'O'):
            if(value != 'X'):
                raise Exception("Value should be capital 'X' or 'O'")
        self.value = value
        
    def getValue(self):
        return self.value