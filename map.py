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
        
    def insert_word(self,word, x, y, orientation = "horizontal"):
        if orientation == "horizontal":
            for i in range(len(word)):
                print(word[i])
                self.grid[x][y + i] = word[i]
                
    def fill_first_collumn(self):
        for i in range( int(self.height/2)):
            print(f"i = {i}")
            random_word = generer_mot_francais_aleatoire()
            print(random_word)
            self.insert_word(random_word, 1+2*i, 0, "horizontal")
        
        
        
    