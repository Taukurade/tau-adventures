from typing import Union, Set
from Player import Player
from Registry import Registry
import random

class Building:
    def __init__(self,):
        pass

class Structure:
    def __init__(self,):
        pass

class Biome:
    def __init__(self,):
        pass


class Cell:
    def __init__(self,pos:Set[int,int],seed:int) -> None:
        self.seed = seed
        self.pos = pos
        self.biome = self.gen_biome()
        self.structures = self.gen_structures()
        self.npcs = self.gen_npcs()
    
    def gen_biome(self):
        random.seed(self.seed)
        return random.choice(Registry().biomes.items())
    
    def gen_structures(self):
        pass

    def gen_npcs(self):
        pass

class World:
    def __init__(self,size:Set[int],player:Player,seed:int = 0) -> None:
        self.seed = seed
        self.size = size
        self.player = player
        self.cells = {}

    def load_cell(self):
        if self.cells.get(self.player.data.pos[0],False):
            if self.cells[self.player.data.pos[0]].get(self.player.data.pos[1],False):
                return self.cells[self.player.data.pos[0]][self.player.data.pos[1]]
        return self.gen_cell()

    def gen_cell(self):
        cell = Cell((self.player.data.pos[0],self.player.data.pos[1]),self.seed)
        
        if self.cells.get(self.player.data.pos[0],False):
            self.cells[self.player.data.pos[0]][self.player.data.pos[1]] = cell
        else:
            self.cells[self.player.data.pos[0]] = {}
            self.cells[self.player.data.pos[0]][self.player.data.pos[1]] = cell
        
        return cell
    