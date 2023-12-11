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
                self.grid[x][y + i] = word[i]

        # Vertical
        if orientation == 1:
            for i in range(len(word)):
                self.grid[x + i][y] = word[i]

    def detect_intersections(self, start_x, start_y, sens):

        letters = []
        pos = []

        if sens == 0:
            for j in range(len(self.grid[0])):
                if self.grid[start_x][j] != '':
                    letters.append(self.grid[start_x][j])
                    pos.append(j)

        if sens == 1:

            # print(f"len(self.grid[:][0]) = {len(self.grid[:][0])}")

            for i in range(len(self.grid[:][0])):
                if self.grid[i][start_y] != '':
                    letters.append(self.grid[i][start_y])
                    pos.append(i)

        return letters, pos
    
    def set_definition_cases(self):
        for j in range(self.width):
            if self.grid[0][j] == '':
                self.grid[0][j] = "X"
                
        for i in range(self.width):
            if self.grid[i][0] == '':
                self.grid[i][0] = "X"
        

                
    def fill_grid(self):
        #insert first word Horizontal
        random_word = generer_mot_francais_aleatoire()
        self.insert_word(random_word, 1, 0, 0)

        # insert first verical
        lettre, pos = self.detect_intersections(0,1,1)
        # print(lettre, pos)
        finded_word = find_word(lettre,pos)
        self.insert_word(finded_word, 0, 1, 1)

        for i in range(1,self.height,2):
            
            #horizontal
            try:
                lettre, pos = self.detect_intersections(i,0,0)
                # print(lettre, pos)
                finded_word = find_word(lettre,pos)
                self.insert_word(finded_word, i, 0, 0)
            except:
                random_word = generer_mot_francais_aleatoire()
                # print(random_word)
                self.insert_word(random_word, i, 0, 0)
            
            #vertical
            try:
                lettre, pos = self.detect_intersections(0,i,1)
                # print(lettre, pos)
                finded_word = find_word(lettre,pos)
                self.insert_word(finded_word,0,i, 1)
            except:
                random_word = generer_mot_francais_aleatoire()
                # print(random_word)
                self.insert_word(random_word,0 ,i, 1)
        
        # Ajout des cases de définition sur les bords
        self.set_definition_cases()
        
        print(self.grid)
        print("\n\n")
        
        # Deuxième génération
        for i in range(2,self.height,2):
            
            #horizontal
            try:
                lettre, pos = self.detect_intersections(i,1,0)
                finded_word = find_word(lettre,pos)
                print(f"{lettre}, {pos}, {finded_word}")
                self.insert_word(finded_word, i, 1, 0)
            except:
                random_word = generer_mot_francais_aleatoire()
                # print(random_word)
                self.insert_word(random_word, i, 1, 0)
            
            #vertical
            try:
                lettre, pos = self.detect_intersections(1, i, 1)
                # print(lettre, pos)
                finded_word = find_word(lettre,pos)
                self.insert_word(finded_word, 1, i, 1)
            except:
                random_word = generer_mot_francais_aleatoire()
                # print(random_word)
                self.insert_word(random_word,1 ,i, 1)
        
        
        
    