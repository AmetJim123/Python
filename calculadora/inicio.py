import calculadora

#Creación método de inicio
def inicio():
    print("\n\n................Iniciando calculadora.................")
    calcular = calculadora.Calculadora()
    s = True
    while s==True:
        menu = int(input("\n\nMenu de opciones:\n1)Operar números\n2)Ver historial de operaciones\n3)Editar operaciones\n4)Eliminar\n5)Salir\n\nElección ->: "))
        if menu==1:
            calcular.operaciones()
        elif menu==2:
            calcular.mostrarHistorial()
        elif menu==3:
            calcular.editarOperación()
        elif menu==4:
            calcular.eliminar()
        elif menu==5:
            print("\nOki, bai UwU")
            print("\n\n................Finalizando calculadora.................\n\n")
            s = calcular.salir()


#Iniciar la calculadora
inicio()