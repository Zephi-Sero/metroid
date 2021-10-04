import sys
from art import text2art as ascii
from metroid_utils import *
from data.objects import *
from data.battle import *

type(ascii("METROID"),300)

type('1. New Game\n\n2. Load Game\n\n',300)

type("Press the corresponding key for an option, then hit enter to confirm.\n\n",300)

menuoption = input().upper()

if menuoption == '1':
    print("\nStarting New Game...")
    type(f"\nSamus appears.\n\n",20)
    Samus = player()
    while Samus.Alive == True:
        encounter(Samus,'Arachnus',40,8,True)
        input()
elif menuoption == '2':
    print("\nLocate the path of your save file.")
else:
    print("\nQuitting...")
    sys.exit()