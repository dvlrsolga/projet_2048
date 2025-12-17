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
    

    """
    génère les 2 dans les espaces vides à chaque mouvement
    """
    def random_start(self):

        if self.n_elements >= 16:
            print("game over")#plus de place :'(
            exit()

        start_value = random.randint(0,15)
        x = start_value%4
        y = start_value//4
        #si tu trouves un moyen d'optimiser ici
        # do while parfait mais pas en python :'(
        while(self.matrix[x][y]!=0):
            start_value = random.randint(0,15)
            x = start_value%4
            y = start_value//4
        
        
        self.matrix[x][y] = 2 # ajouter petite proba que ce soit un 4
        self.n_elements += 1
    

my_board = Board()
print(my_board)

#demonstration
for i in range(17):
    my_board.random_start()
    print(my_board)