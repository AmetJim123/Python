"""Se necesita un programa que le pregunte el nombre al usuario. Luego enviar un mensaje al
   usuario que tiene que adivinar un número entre el 1 y 100 y solo tendrá 8 intentos para adivinar.

   Casos:
   -Si el número es menor que 1 o mayor que 100, enviar un mensaje que comunique que el número no es permitido
   -Si el número es menor al número secreto, comunicar que el número es menor que el elegido
   -Si el número es mayor al número secreto, comunicar que el número es mayor que el elegido
   -Si el usuario acierta, se le dirá que ganó el juego y que tomó n número de intentos para lograrlo"""

from random import *


nombre = input("Hola qué tal?, Por favor: Indique su nombre →: ")
print(f"""\nBienvenid@ {nombre} al juego de adivinar un número. Dispondrá de 8 intentos para
 adivinar un número entre 1 y 100. Buena suerte y que acierte al primer intento\n 
 [SI EN ALGÚN MOMENTO USTED QUIERE DETENER EL JUEGO, escriba '666']\n""")


jugar = 's'
while jugar == 's':

    intentos = 1
    numero_secreto = randint(1, 100)
    while intentos <= 8:

        numero = int(input(f"""Bueno, este es su intento número {intentos}. 
Digite un número para intentar adivinar el número secreto →: """))
        if numero == 666:
            print("\n Veo que ya no quiere jugar, está bien. Adios, cobarde")
            break
        elif numero < 1 or numero > 100:
            intentos += 1
            print("\nEl número que usted eligió no es válido, ha perdido un intento por ignorante\n")

        elif numero < numero_secreto:
            intentos += 1
            print("\nEl número que usted digitó es menor que el número secreto, vuelva a intentar\n")

        elif numero > numero_secreto:
            intentos += 1
            print("\nEl número que usted digitó es mayor que el número secreto, vuelva a intentar\n")

        else:

            print(f"""\nFELICIDADES {nombre}! Su número {numero} es igual a el número secreto {numero_secreto}.
Ganó el juego!\n""")
            break

    else:
        print(f"Usted agotó todos sus intentos. GAME OVER. El número secreto era {numero_secreto} ")
    jugar = input("\nEl juego se terminó, ¿Desea volver a jugar?, (S) para sí, (N) para no →: ").lower()
    if jugar == 'n':
        print("\nMuchas gracias, vuelva pronto a intentar adivinar el número secreto :D ")
