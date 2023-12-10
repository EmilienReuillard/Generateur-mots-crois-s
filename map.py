import numpy as np


class MAP:
    
    def __init__(self) -> None:
        pass

    def create_grid(self,height=9,width=9):
        self.grid = np.zeros((height,width))
        
    