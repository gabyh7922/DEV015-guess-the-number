"""setear numero aleatorio"""
"""- funcion que dada una variable numero esta diga si esta por arriba, por abajo o si es el numero
        *si es el numero romper el ciclo"""
import random
import time
"""variable mayuscula para que sea una variable global (buenas practicas)"""
RANDOM_NUM: int = random.randint(1,101)
MIN_NUM = 1
MAX_NUM = 101

print(f"Numero a adivinar {RANDOM_NUM}")

def Comparation_result(consult):
        if (consult > RANDOM_NUM):
                return "mayor"
        elif (consult < RANDOM_NUM):
                return "menor"
        else:
                return "winner"
"""ciclo"""
while True: 
        player = int(input("Te toca jugar, por favor ingresa un numero\n"))
        comparar = Comparation_result(player)
        if Comparation_result(player) == "winner":
                print("Felicidades acertaste al numero correcto")
                break
        print("El numero que elegiste es menor" 
              if comparar == "menor" 
              else "El numero que elegiste es mayor")
        
        time.sleep(1)

        print("\nComputador jugando " + "-"*10)
        computadora_numero = random.randint(MIN_NUM, MAX_NUM)
        comparar_pc = Comparation_result(computadora_numero)
        print(f"\nComputadora eligio el numero {computadora_numero}")
        if comparar_pc == "winner":
                print("la computadora gano")
                break
        else :
                if comparar_pc == "menor":
                        print("El numero que el computador elegio es menor")
                        MIN_NUM = computadora_numero + 1
                else:
                        print("El numero que el computador elegio es mayor")
                        MAX_NUM = computadora_numero
                print("\n")
        print(MIN_NUM, MAX_NUM, '-'*5)

