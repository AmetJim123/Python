class Agenda:

    def __init__(self):
        self.directorio = []

    def añadirContacto(self):
        nombre = str(input("Ingrese nombre de contacto ->: "))
        telefono = int(input("Ingrese número de contacto ->: "))
        email = str(input("Ingrese email de contacto ->: "))
        self.directorio.append({
            'id' : len(self.directorio) + 1, 
            'nombre' : nombre,
            'telefono' : telefono,
            'email' : email
        })
        print("Contacto guardado\n")

    def listaContactos(self):
        if  len(self.directorio) <= 0:
            print("\nUsted no tiene contactos\n")
        else:
            print("\nLista de contactos:")
            print(self.directorio)

    def buscarContacto(self, busqueda = False):
        if len(self.directorio) <= 0:
            return print("\nNo tienes contactos\n")
        else:
            if not busqueda:
                busqueda = int(input("\nIngrese el identificador del contacto ->: "))
            found = False
            for i,contact in enumerate(self.directorio):
                if busqueda == contact['id']:
                    found = contact,i
            if found:
                print("\nContacto: ", found[0])
            else:
                print("El contacto no existe")
            return found

    def editarContacto(self):
        if len(self.directorio) <= 0:
            return print("\nNo tienes contactos\n")
        else:
            busqueda = self.buscarContacto()
            print(busqueda)
            if busqueda: 
                nombre = str(input("Ingrese el nuevo nombre de contacto ->: "))
                telefono = int(input("Ingrese el nuevo número de contacto ->: "))
                email = str(input("Ingrese el nuevo email de contacto ->: "))
                self.directorio[busqueda[1]] = {
                    'id' : busqueda[0]['id'],
                    'nombre' : nombre,
                    'telefono': telefono,
                    'email' : email
                }
                
            else:
                print("\nContacto con el identificador ingresado NO existe")

    def eliminarContacto(self):
        if len(self.directorio) <= 0:
            return print("\nNo tienes contactos\n")
        else:
            busqueda = self.buscarContacto()
            if busqueda:
                confirmacion = str(input("\nDesea eliminar este contacto)\n (Sí)/(No)->:")).lower()
                if confirmacion == 'no':
                    print("No se eliminó el contacto")
                else:
                    del self.directorio[busqueda[1]] # No sé si esto sirva
                    print("\nContacto eliminado")
            else:
                print("\nContacto con el identificador ingresado NO existe")

    def cerrarAgenda(self):
        return False
