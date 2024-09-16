from Main import  compara, ordenador, end_game, start, random_number
from turn_play import system
from game_user import user_turn, validate_number


"""Implementa un bucle que solicite a la jugadora que adivine el número. Usa la función input para obtener la entrada de la jugadora."""
user_list = []
system_list = []

def game():
 
    start()

    number = random_number()
    
    while True:
        print("----Tu turno----")
        user_number = user_turn()
        validate_number(user_number)
        record_user = ordenador(user_number, user_list)

        if user_number == number:
           end_game('Usuario', record_user)
           break

        else: comparison(user_number, number)

        print("------------system turn--------------")
        system = turn_play()
        record_system = record_numbers(system , system_list)

        if system_number == number:
            end_game('Sistema', record_system)
            break
        
        else: compara(system, number)

      
if __name__ == '__main__':
    game()


