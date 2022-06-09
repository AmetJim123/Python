import numeros


def preguntar():

    print("\nBuen día, cómo está?, Bienvenido a FarmaCos SA.\n")

    while True:
        print('''Hacia dónde se dirige?: 
[P] Perfumería
[F] Farmacia
[C] Cosméticos\n''')

        try:
            mi_rubro = input("Elija una sección →: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break
    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quiere sacar otro turno? [S] [N] →: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("No eligió bien, usuario ¬¬")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()
