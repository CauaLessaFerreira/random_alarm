import random
from playsound3 import playsound
import os.path
import time

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(CURRENT_DIRECTORY, "Assets/alarme.mp3")

sorte = int(input("Digite um numero de 0 a 100 para escolher a chance: "))
atocado = False
alarme = int(random.randrange(0, 100))

while atocado == False:
    if sorte >= alarme:
        playsound(filename)
        print("Alarme Tocou!")
        atocado = True

        break
    time.sleep(1)


