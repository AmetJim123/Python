def porcentaje_entre_dos_numeros():
    # Esta función dice que porcentaje representa un número con respecto al otro

    print("\nHolap, yo te wa sacar el procentaje que lleves de algo UwU")
    while True:
        try:
            numero = int(input("Ingrese el número que tiene →:"))
            numero_total = int(input("Ingrese el número total →:"))
        except ValueError:
            print("\nEy, ingresa bien los números, que yo hago el resto")
        else:
            break

    print("\nBien, hora de trabajar")
    porcentaje_final = numero / numero_total * 100
    print(f"Bueno, de {numero_total} llevas el: {porcentaje_final:.2f}%, o sea, {numero}/{numero_total}")


def porcentaje_de_numero():
    # Esta función dice que número representa el porcentaje
    print("\nHolap, yo te wa sacar a cuánto equivale el porcentaje que tienes UwU")
    while True:
        try:
            numero_total = int(input("Ingrese el número total →:"))
            porcentaje = int(input("Ingrese el porcentaje  →:"))
            print(f"{porcentaje}%")
        except ValueError:
            print("\nEy, ingresa bien los números, que yo hago el resto")
        else:
            break

    print("\nBien, hora de trabajar")
    numero_inicial = porcentaje / 100 * numero_total
    print(f"Bueno: {numero_inicial} es el {porcentaje}% de {numero_total}")


def preguntar():
    print("\n" + "*" * 52)
    print("""Bienvenido a tu calculadora de porcentajes :D  
Desplegaré mi menú:                                     
[1] Calcular que porcentaje representa un número         
[2] Calcular cuanto equivale el porcentaje 
   de un número""")
    print("*" * 52 + "\n")
    while True:
        try:
            menu = int(input("Ingrese su elección →: ").upper())
            [1, 2].index(menu)
        except ValueError:
            print("\nPor favor, ingrese una opción válida..")
        else:
            break

    if menu == 1:
        porcentaje_entre_dos_numeros()
    else:
        porcentaje_de_numero()


def inicio():

    while True:
        preguntar()
        try:
            pregunta = str(input("\nDesea seguir sacando procentajes?: [S]Sí [N]No →:").upper())
            ["S", "N"].index(pregunta)
        except ValueError:
            print("Por favor, elige una opción válida..")
        else:
            if pregunta == "N":
                print("Gracias, vuelva pronto UwU")
                break


inicio()
