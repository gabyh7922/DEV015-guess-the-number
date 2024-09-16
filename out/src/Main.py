from random import randint
"""Genera un número aleatorio entre 1 y 100"""


def random_number():

    # Arroja un numero aleatorio entre 1 y 100
    num_aleatorio = randint(1, 100)
    return num_aleatorio


"""Implementa un bucle que solicite a la jugadora que adivine el número"""
"""logica: compara la entrada de la jugadora con el numero aleatorio
si adivina termina el juego, si no: infica una pista si es mayor o menor el numero"""


def compara(num_aleatorio, num_player):
    if num_aleatorio > num_player:
        print("El numero es mayor")
    elif num_aleatorio < num_player:
        print("El numero es menor")


def ordenador(num_aleatorio, list_computer):
    """lista debe tener algo donde la comutadora guarde una lista y genere una manera de recordar los numeros que se utilizan"""
    list_computer.append(num_aleatorio)
    return list_computer


"""iniciando juego"""


def start():
    print("Bienvenido, puedes iniciar el juego")
    print("Intenta adivinar un numero del 1 al 100")


def end_game(surpassed, list_computer):
    """
    final del juego
lo que se espera: 
    wsurpassed: quien logro superar el reto el usuario o la computadora
    list_computer: lista de registro 
    """
    print(f"correcto!! {surpassed} acertaste el numero")
    print(f"Registro de números {list_computer}")
