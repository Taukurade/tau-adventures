from .Utils import Map


class Player:
    def __init__(self, nick,save = None) -> None:
        self.stats = Map()
        self.data = Map(nick=nick)
        
        self.stats.maxHealth = 100
        self.stats.maxStamina = 100
        self.stats.maxMana = 100
        self.stats.maxHunger = 100
        self.stats.capacity = 50
        
        self.data.health = 100
        self.data.stamina = 100
        self.data.mana = 100
        self.data.hunger = 100

        self.data.pos = (0,0)
    
    def receive_damage(self,amount:float):
        self.data.health -= amount