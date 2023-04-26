from typing import Union

class Cell:
    def __init__(self,pos:set[int,int]) -> None:
        self.pos = pos
        self.biome = self.gen_biome()
        self.structures = self.gen_structures()
        self.entity = self.gen_entity()
    
    def gen_biome(self):
        pass
    
    def gen_structures(self):
        pass

    def gen_entity(self):
        pass

class World:
    def __init__(self,size:set[int,int]) -> None:
        self.size = size
        self.cells = {}
    def load_cell(self):
        pass