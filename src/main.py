"""setear numero aleatorio"""
"""- funcion que dada una variable numero esta diga si esta por arriba, por abajo o si es el numero
        *si es el numero romper el ciclo"""
import random
import time
from utils import player_validation
"""variable mayuscula para que sea una variable global (buenas practicas)"""
RANDOM_NUM: int = random.randint(1,101)
MIN_NUM = 1
MAX_NUM = 101
COUNTER = 0
RECORDS = []

print(f"Numero a adivinar {RANDOM_NUM}")


"""ciclo refactorizar """
while True:
        COUNTER += 1
        result, MIN_NUM, MAX_NUM, choosen = player_validation("me", RANDOM_NUM, MIN_NUM, MAX_NUM)
        RECORDS.append({"player": "me", "turn": COUNTER, "choosen": choosen})
        if result == "winner":
                print("Felicidades, ganaste!")
                break
        time.sleep(1)

        result, MIN_NUM, MAX_NUM, choosen = player_validation("computadora", RANDOM_NUM, MIN_NUM, MAX_NUM)
        RECORDS.append({"player": "computer", "turn": COUNTER, "choosen": choosen})
        if result == "winner":
                print("Computadora ha ganado!")
                break
        
print(f"Juego finalizado en {COUNTER} rondas")
print(*RECORDS, sep="\n")