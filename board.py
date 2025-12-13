class Board:

    def __init__(self):
        self.matrix = [[0 for i in range(4)] for j in range(4)]

        

    def __str__(self):
        string = ""
        for i in range(3):
            string += str(self.matrix[i][0]) + " " + str(self.matrix[i][1]) +" "+ str(self.matrix[i][2]) +" "+ str(self.matrix[i][3])+"\n"
        string+= str(self.matrix[3][0]) + " " + str(self.matrix[3][1]) +" "+ str(self.matrix[3][2]) +" "+ str(self.matrix[3][3])
        
        return string
    

board1 = Board()
print(board1)