import random

RANDOM_NUM: int = random.randint(1,101)


def comparation_result(consult, num):
        # validamos que sean enteros
        # isinstance  entrega booleano
        if not isinstance(consult, int) or not isinstance(num, int):
                return "error"
        if (consult > num):
                return "mayor"
        elif (consult < num):
                return "menor"
        else:
                return "winner"


def player_validation(player_type, num, min_n, max_n):
    if player_type == "me":
        turn = int(input("Te toca jugar, por favor ingresa un numero\n"))
        player = ""
        
    elif player_type == "computadora":
        print("\nComputador jugando " + "-"*10)
        turn = random.randint(min_n, max_n)
        player = player_type.title()
        print(f"Computadora ha elegido el numero {turn}")

    comparar = comparation_result(turn, num)

    if comparar == "winner":
            print("Felicidades acertaste al numero correcto")
    else:
        if comparar == "menor":
            if player_type == "computadora":
                min_n = turn
            print(f"{player} El numero que elegiste es menor" )
        else:
            if player_type == "computadora":
                max_n = turn
            print(f"{player} El numero que elegiste es mayor")
    return comparar,min_n, max_n, turn
        