# tests de Guinou

import random
import sys
from time import sleep

class Board:

    def __init__(self):
        self.matrix = [[0 for i in range(4)] for j in range(4)]
        self.n_elements = 0 #pour compter combien de chiffres on a tout au long de la partie
        self.score = 0

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
    
    def move_left(self):
        for i in range(4):
            for j in range(1,4):
                x = i
                y = j
                if self.matrix[x][y] != 0:
                    while True:
                        if y<=0:
                            break
                        if self.matrix[x][y-1] == 0: # si la case a gauche est libre : deplacer
                            self.matrix[x][y-1] = self.matrix[x][y]
                            self.matrix[x][y] = 0
                            y-=1
                        elif self.matrix[x][y-1] == self.matrix[x][y]: # si la case a gauche a la meme valeur : merge
                            self.matrix[x][y-1] = self.matrix[x][y]*2
                            self.matrix[x][y] = 0
                            self.n_elements-=1
                            self.score += self.matrix[x][y]*2
                            y-=1
                            break
                        else:
                            y-=1


def game_loop():

    board1 = Board()
    #print(board1)

    #ajouter contrôle utilisateur

    while True:
        board1.random_start()
        print(board1)
        sleep(0.5)
        sys.stdout.write("\033[5A")
        sys.stdout.write("\033[0J")
        board1.move_left()
        print(board1)
        sleep(0.5)
        sys.stdout.write("\033[5A")
        sys.stdout.write("\033[0J")


game_loop()


####################################################################################################################################
my_board = Board()
print(my_board)

#demonstration
"""for i in range(6):
    my_board.random_start()
print(my_board)

my_board.move_left()
print(my_board)"""