"""setear numero aleatorio"""
"""- funcion que dada una variable numero esta diga si esta por arriba, por abajo o si es el numero
        *si es el numero romper el ciclo"""
import random
import time
from utils import comparation_result
"""variable mayuscula para que sea una variable global (buenas practicas)"""
RANDOM_NUM: int = random.randint(1,101)
MIN_NUM = 1
MAX_NUM = 101

print(f"Numero a adivinar {RANDOM_NUM}")


"""ciclo refactorizar """
while True: 
        player_turn = int(input("Te toca jugar, por favor ingresa un numero\n"))
        comparar = comparation_result(player_turn, RANDOM_NUM)
        if comparar == "winner":
                print("Felicidades acertaste al numero correcto")
                break
        print("El numero que elegiste es menor" 
              if comparar == "menor"
              else "El numero que elegiste es mayor")
        
        time.sleep(1)

        print("\nComputador jugando " + "-"*10)
        computer_turn = random.randint(MIN_NUM, MAX_NUM)
        comparar_pc = comparation_result(computer_turn, RANDOM_NUM)
        print(f"\nComputadora eligio el numero {computer_turn}")
        if comparar_pc == "winner":
                print("la computadora gano")
                break
        else :
                if comparar_pc == "menor":
                        print("El numero que el computador elegio es menor")
                        MIN_NUM = computer_turn + 1
                else:
                        print("El numero que el computador elegio es mayor")
                        MAX_NUM = computer_turn
                print("\n")
        print(MIN_NUM, MAX_NUM, '-'*5)

