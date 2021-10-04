from metroid_utils import *
import sys
import os

class entity:
    def __init__(self,name,health,damage,flee):
        self.Name = name
        self.HP = health
        self.MHP = health
        self.DMG = damage
        self.Alive = True
        self.CanFlee = flee
        render(f'assets/enemies/{self.Name}',True)
        type(f"\nYou encounter {self.Name}!\n\nHealth: {self.HP}\n\nDamage: {self.DMG}\n",40)
    def attack(self,opponent):
        if self.HP <= 0:
            self.Alive = False
        else:
            type(f"\n{self.Name} is at {self.HP} HP.\n",160)
        if self.Alive == True:
            opponent.HP = opponent.HP - self.DMG
            type(f"\n{self.Name} damages you for {self.DMG} energy!\n",80)
        else:
            type(f"\n{self.Name} has died.\n",40)

class player:
    def __init__(self):
        self.EnergyTanks = 1
        self.HP = 30
        self.MHP = (99 * self.EnergyTanks)
        self.Beams = 1
        self.DMG = (20 * self.Beams)
        self.Missiles = 255
        self.MaxMissiles = 255
        self.SMissiles = 255
        self.MaxSMissiles = 255
        self.PowerBombs = 255
        self.MaxPowerBombs = 255
        self.Alive = True
    def attack(self,opponent):
        if self.HP <= 0:
            self.Alive = False
        else:
            type(f"\nYou are at {self.HP} energy.\n",160)
        if self.Alive == True:
            valid = False
            while not valid:
                type("\n1. Fire Beam\n",160)
                if self.MaxMissiles > 0:
                    type(f"\n2. Launch Missile ({self.Missiles}/{self.MaxMissiles})\n",160)
                if self.MaxSMissiles > 0:
                    type(f"\n3. Launch Super Missile ({self.SMissiles}/{self.MaxSMissiles})\n",160)
                if True: #change to detect bomb when item system is added 
                    type(f"\n4. Throw Bomb\n",160)
                if self.MaxPowerBombs > 0:
                    type(f"\n5. Throw Power Bomb ({self.PowerBombs}/{self.MaxPowerBombs})\n\n",160)
                choice = input().upper()
                valid = True
                if choice == "1":
                    opponent.HP -= self.DMG
                    type(f"\nYou fire a beam at {opponent.Name} for {self.DMG} damage!\n",80)
                elif choice == "2" and self.Missiles > 0:
                    opponent.HP -= 100
                    self.Missiles -= 1
                    type(f"\nYou launch a missile at {opponent.Name} for 100 damage!\n",80)
                elif choice == "3" and self.SMissiles > 0:
                    opponent.HP -= 300
                    self.SMissiles -= 1
                    type(f"\nYou launch a super missile at {opponent.Name} for 300 damage!\n",80)
                elif choice == "4":
                    opponent.HP -= 20
                    type(f"\nYou throw a bomb at {opponent.Name} for 20 damage!\n",80)    
                elif choice == "5" and self.PowerBombs > 0:
                    opponent.HP -= 200
                    self.PowerBombs -= 1
                    type(f"\nYou throw a power bomb at {opponent.Name} for 200 damage!\n",80)
                else:
                    valid = False
        else:
            type(f"\nYou have died.\n",20)
            sys.exit()