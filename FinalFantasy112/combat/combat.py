"""
Entity, Player, and Enemy Classes

    Entity:
        - Base class for all entities
        - Has combat stats
        - Has combat methods

    Player:
        - Inherits from Entity
        - Has an inventory
        - Has a corresponding View class

    Enemy:
        - Inherits from Entity
        - Has an appearance image
"""

import random
from tkinter import PhotoImage

class Entity:
    def __init__(self,
            attack: int,
            hitpoints: int,
            defense: int) -> None:
        
        self.attack = attack #Amount of HP to be subtracted from the enemy
        self.hitpoints = hitpoints
        self.isBlocking = False
        self.defense = defense
        self.maxHitpoints = hitpoints

        self.accuracy = 0.95 #Probability of attacks landing
        self.criticalHit = 0.2 #Probability of a critical hit
        self.criticalHitMultiplier = 2 #Multiplier for critical hits

    def attackEntity(self, entity) -> None:
        if not isinstance(entity, Entity): 
            raise(Exception("entity must be an instance of Entity"))
        if self.isDead(): return 
        #Calculate the damage done
        damage = self.attack + random.randint(0, self.attack // 4)
        miss = random.random()
        crit = random.random()

        if miss > self.accuracy: 
            damage = 0
        elif crit < self.criticalHit:
            damage = self.attack * self.criticalHitMultiplier
        else:
            pass
        
        #If the target is blocking, reduce the damage, have target unblock
        if entity.isBlocking:
            damage -= entity.defense ** 2
            entity.toggleBlock()
        else:
            damage -= entity.defense
        
        #Subtract the damage from the target's HP
        entity.hitpoints -= damage if damage > 0 else 0

        return damage if damage > 0 else 0


    def isDead(self) -> bool:
        """Returns True if the entity is dead"""
        return self.hitpoints <= 0
    
    def toggleBlock(self):
        """Block or unblock the attack"""
        self.isBlocking = not self.isBlocking

class Player(Entity):
    def __init__(self, 
            view: object,
            inventory: list,
            attack: int,
            hitpoints: int,
            defense: int) -> None:

        if type(inventory) != list: 
            raise(Exception("view and inventory must be instances of View and list"))

        self.inv = inventory
        self.isTurn = False
        super(Player, self).__init__(attack, hitpoints, defense)

        self.gague = 0  
        self.gagueMax = 58
        self.dG = 2

        self.exp = 0
        self.nextLevel = 100
    
    def gagueUp(self):
        """Increase the combat gague"""
        if self.isTurn: return 

        if self.gague < self.gagueMax:
            self.gague += self.dG
        else:
            self.gague = self.gagueMax
            self.isTurn = True
    
    def resetGague(self):
        """Reset the combat gague"""
        self.gague = 0
        self.isTurn = False
    
    def flee(self) -> bool:
        """Returns True if the player flees"""
        return random.random() < 0.2
    
    def levelUp(self):
        """Level up the player"""
        if self.exp >= self.nextLevel:
            self.attack *= 1.1
            self.hitpoints = self.maxHitpoints
            self.defense *= 1.1
            self.dG += 1
            self.nextLevel *= 1.1
            self.exp = 0
    

class Enemy(Entity):
    namesAndDialogues = {
        "DANIEL": "Daniel: *Daniel Noises*",
    }
    specialNamesAndDialogues = {
        "Economic Minister": "Economic Minister: NOOOO DONT ATTACK ME, THE GDP WILL PLUMET",
        "King King": "I am the king of this land, and I happen to be named King",
        "Emperor King": "I am now EMPEROR of this land, and I am still named King >:)",
    }
    def __init__(self,
            attack: int,
            hitpoints: int,
            defense: int,
            specialName: str="") -> None:
        super(Enemy, self).__init__(attack, hitpoints, defense)
        self.exp = 25

        self.name = random.choice(list(Enemy.namesAndDialogues.keys()))
        self.dialogue = Enemy.namesAndDialogues[self.name]




