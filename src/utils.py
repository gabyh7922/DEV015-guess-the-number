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
