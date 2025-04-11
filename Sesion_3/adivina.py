
import random   

while(True):
    numero_secreto = random.randint(1, 10) 

    numero_usario = int(input("Dime un numero del 1 al 10: "))

    if(numero_secreto == numero_usario):
        print(f"¡Felicidades, te has ganado 10 puntos extras: {numero_secreto}!")
        break
    else:
        print("Sigue intentando.")
        if(numero_usario > numero_secreto):
            print("El numero secreto es menor.")
        else:
            print("El numero secreto es mayor.")
        print("Lo siento, el numero secreto era: ", numero_secreto)

