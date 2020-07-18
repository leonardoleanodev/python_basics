def numero_magico(numero):
    magico = 3
    if type(numero) != int:
        return 'nao valido'
    elif numero == magico:
        return 'magico'
    elif magico/2 < numero and numero < magico:
        return 'menor'
    elif numero < 2*magico  and numero > magico :
        return 'maior'
    elif numero > 2*magico:
        return 'muito maior'
    elif numero < magico/2:
        return 'muito menor'
    

    
