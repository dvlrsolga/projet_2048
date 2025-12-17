import random
from time import sleep
import sys

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

    
    #a l'air correct seul, avec plusieurs (vérifier si c'est correct avec des chiffres différents) ok
    #+implémenter merge ok
    #ne pas permettre l'action si elle ne fait rien
    def move_right(self):
        for i in range(4):#pour toutes les lignes
            for j in range(2,-1,-1):#de droite à gauche
                if self.matrix[i][j] != 0:#deplace les valeurs non nulles de 1 vers la droite
                    start_index = j
                    merge = False
                    value = self.matrix[i][j]# tant que ce n'est pas le bord ou un autre chiffre
                    while True:
                        if start_index == 3:
                            break
                        if self.matrix[i][start_index+1]!=0:#si collision avec chiffre ->
                            merge = True
                            break

                        self.matrix[i][start_index] = 0
                        start_index+=1
                        self.matrix[i][start_index] = value

                    if merge and self.matrix[i][start_index+1]==value:# -> et même valeur
                        self.matrix[i][start_index] = 0
                        self.n_elements -= 1
                        start_index+=1
                        self.matrix[i][start_index] = value*2
                        self.score += value*2
    
    #ne fonctionne pas, trouver le bug
    #fonctionne mieux, vérifier
    def move_down(self):
        for i in range(4):
            for j in range(2,-1,-1):#de bas en haut
                if self.matrix[j][i] != 0:
                    start_index = j
                    merge = False
                    value = self.matrix[j][i]
                    while True:
                        if start_index == 3:
                            break
                        if self.matrix[start_index+1][i]!=0:#si collision avec chiffre ->
                            merge = True
                            break

                        self.matrix[start_index][i] = 0
                        start_index+=1
                        self.matrix[start_index][i] = value
                    
                    if merge and self.matrix[start_index+1][i]==value:# -> et même valeur
                        self.matrix[start_index][i] = 0
                        self.n_elements -= 1
                        start_index+=1
                        self.matrix[start_index][i] = value*2
                        self.score += value*2

def game_loop():

    board1 = Board()
    #print(board1)

    #ajouter contrôle utilisateur

    while True:
        print("Score : " + str(board1.score))
        print()
        board1.random_start()
        print(board1)
        sleep(0.5)
        sys.stdout.write("\033[5A")
        sys.stdout.write("\033[0J")
        board1.move_right()
        print(board1)
        sleep(0.5)
        sys.stdout.write("\033[5A")
        sys.stdout.write("\033[0J")
        board1.random_start()
        print(board1)
        sleep(0.5)
        sys.stdout.write("\033[5A")
        sys.stdout.write("\033[0J")
        board1.move_down()
        print(board1)
        sleep(0.5)
        sys.stdout.write("\033[7A")
        sys.stdout.write("\033[0J")


game_loop()
