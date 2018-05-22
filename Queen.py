class Queen():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    def setCoords(self, x, y):
         self.x = x
         self.y = y
    def printQueen(self):
        return("(" + str(self.x) + ", " + str(self.y) + ")")