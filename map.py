import numpy as np
from dictionnaire import *


class MAP:
    
    def __init__(self) -> None:
        pass

    def create_grid(self,height=9,width=9):
        self.height = height
        self.width = width
        self.grid = np.zeros((height,width), dtype=str)
        
    def affiche_grid(self):
        print(self.grid)
        
    def insert_word(self,word, x, y, orientation = 0):
        # Horizontal
        if orientation == 0:
            for i in range(len(word)):
                # print(word[i])
                self.grid[x][y + i] = word[i]

        # Vertical
        if orientation == 1:
            for i in range(len(word)):
                # print(word[i])
                self.grid[x + i][y] = word[i]

    def detect_intersections(self, start_x, start_y, sens):

        letters = []
        pos = []

        print(f"sens = {sens}")

        if sens == 0:
            for j in range(len(self.grid[0])):
                if self.grid[start_x][j] != '':
                    letters.append(self.grid[0][j])
                    pos.append([start_x, j])

        if sens == 1:

            print("In sens == 1")
            print(f"len(self.grid[:][0]) = {len(self.grid[:][0])}")

            for i in range(len(self.grid[:][0])):
                if self.grid[i][start_y] != '':
                    letters.append(self.grid[i][start_y])
                    pos.append(i)

        return letters, pos
        

                
    def fill_grid(self):
        # Variable
        sens = 1    #0 = Horizontal // 1 = Vertical

        #insert first word Horizontal
        random_word = generer_mot_francais_aleatoire()
        self.insert_word(random_word, 1, 0, 0)

        # insert first verical
        lettre, pos = self.detect_intersections(0,1,sens)
        print(lettre, pos)
        finded_word = find_word(lettre,pos)
        self.insert_word(finded_word, 0, 1, 1)

        for i in range(1,self.height):
            for j in range(1,self.width):
                pass

        if sens == 1:
            sens = 0
        else:
            sens = 1
        
        
        
    