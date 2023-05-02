from dataclasses import dataclass

@dataclass
class Registry:

    items = {}
    biomes = {}
    structures = {}
    buildings = {}
    furniture = {}
    npcs = {}
    plants = {}
    weathers = {}
    
    def item(self, codename:str, item):
        self.items[codename] = item
    
    def biome(self, codename:str, biome):
        self.biomes[codename] = biome

    def structure(self, codename:str, structure):
        self.structures[codename] = structure
    
    def building(self, codename:str, building):
        self.buildings[codename] = building
    
    def furnit(self, codename:str, furnit):
        self.furniture[codename] = furnit
    
    def npc(self, codename:str, npc):
        self.npcs[codename] = npc
    
    def plant(self, codename:str, plant):
        self.plants[codename] = plant
    
    def weather(self, codename:str, weather):
        self.plants[codename] = weather

