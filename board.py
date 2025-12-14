import random

class Board:

    def __init__(self):
        self.matrix = [[0 for i in range(4)] for j in range(4)]
        self.n_elements = 0 #pour compter combien de chiffres on a tout au long de la partie

    def __str__(self):
        string = ""
        for i in range(4):#utile d'avoir un \n finalement
            string += str(self.matrix[i][0]) + " " + str(self.matrix[i][1]) +" "+ str(self.matrix[i][2]) +" "+ str(self.matrix[i][3])+"\n"
        return string
    

    def random_start(self):

        if self.n_elements >= 16:
            print("game over")#plus de place :'(
            exit()

        start_value = random.randint(0,15)
        x = start_value%4
        y = start_value//4
        #si tu trouves un moyen d'optimiser ici
        while(self.matrix[x][y]!=0):
            start_value = random.randint(0,15)
            x = start_value%4
            y = start_value//4
        
        
        self.matrix[x][y] = 2
        self.n_elements += 1
    

board1 = Board()
print(board1)

#demonstration
for i in range(17):
    board1.random_start()
    print(board1)