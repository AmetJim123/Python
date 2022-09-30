#Importación de clase
import agenda


#Creación método de inicio
def inicio():
    contact = agenda.Agenda()
    s = True
    while s==True:
        print("\nBienvenido a su agenda.\n1)Añadir un contacto\n2)ver lista de contactos\n3)Buscar contacto\n4)Editar contacto\n5)Eliminar contacto\n6)Cerrar agenda")
        menu = int(input("\nElección ->: "))
        #Añadir contacto
        if menu==1:
            contact.añadirContacto()
        #Listar contactos
        elif menu==2:
            contact.listaContactos()
        #Buscar contacto
        elif menu==3:
            contact.buscarContacto()
        #Editar contacto
        elif menu==4:
            contact.editarContacto()
        #Eliminar contacto
        elif menu==5:
            contact.eliminarContacto()
        #Cerrar agenda
        elif menu==6:
            print("Oki, bai UwU")
            s = contact.cerrarAgenda()

#Iniciar el programa
inicio()