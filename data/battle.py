from data.objects import *
import math, random

def encounter(Samus,name,health,damage,flee):
    Enemy = entity(name,health,damage,flee)
    while Enemy.Alive == True and Samus.Alive == True:
        
        Samus.attack(Enemy)
        Enemy.attack(Samus)
    tmp = Samus.HP
    Samus.HP += random.randint(0,20)
    if Samus.HP > Samus.MHP:
        Samus.HP = Samus.MHP
    gained = Samus.HP - tmp
    type(f"\nYou have restored {gained} energy.\n",40)