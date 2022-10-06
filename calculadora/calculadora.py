class Calculadora:
    operationCounter = 0
    #Creación del parametro historial
    def __init__(self):
        self.historial = []

    def pedirNumeros(self):
        numero1 = float(input("Ingrese su primer valor ->: "))
        numero2 = float(input("Ingrese su segundo valor valor ->: "))
        return numero1, numero2

    #Método Append
    def agregarHistorial(self, numero1, numero2, resultado, eleccion, id_antigua = False):
        if not id_antigua:
            if eleccion==1:
                self.historial.append({
                    'No. Operación' : self.operationCounter + 1,
                    'Número1' : numero1,
                    'Número2' : numero2,
                    'Suma = ' : resultado
                })
            elif eleccion==2:
                self.historial.append({
                    'No. Operación' : self.operationCounter + 1,
                    'Número1' : numero1,
                    'Número2' : numero2,
                    'Resta = ' : resultado
                })
            self.operationCounter += 1
        if id_antigua:
            if eleccion==1:
                self.historial.append({
                    'No. Operación' : id_antigua,
                    'Número1' : numero1,
                    'Número2' : numero2,
                    'Suma = ' : resultado
                })
            elif eleccion==2:
                self.historial.append({
                    'No. Operación' : id_antigua,
                    'Número1' : numero1,
                    'Número2' : numero2,
                    'Resta = ' : resultado
                })

    #Creación método de operaciones
    def operaciones(self,numero1=False, numero2=False, eleccion=False, id_antigua=False):
        if not eleccion:
            eleccion = int(input("Operación:\n1)Sumar\n2)Restar\nElección ->:"))
            numero1, numero2 = self.pedirNumeros()
            if eleccion==1:
                #Condición para nueva suma
                resultado = round((numero1 + numero2),2)
                print(f"{numero1} + {numero2} = {resultado}")
                self.agregarHistorial(numero1, numero2, resultado, eleccion)
            elif eleccion==2:
                #Condición para nueva resta
                resultado = round((numero1 - numero2),2)
                print(f"{numero1} - {numero2} = {resultado}")
                self.agregarHistorial(numero1,numero2,resultado, eleccion)
        elif eleccion:
            if eleccion==1:
                #Condición para suma existente
                resultado =round((numero1+numero2),2)
                print(f"{numero1} + {numero2} = {resultado}")
                self.agregarHistorial(numero1, numero2, resultado, eleccion,id_antigua)
            elif eleccion==2:
                #Condición para resta existente
                resultado = round((numero1-numero2),2)
                print(f"{numero1} - {numero2} = {resultado}")
                self.agregarHistorial(numero1, numero2, resultado, eleccion, id_antigua)

    #Método para mostrar historial
    def mostrarHistorial(self):
        if len(self.historial) <= 0:
            return print("No tiene nada guardado")
        else:
            print("Historial de operaciones:")
            for operacion in self.historial:
                print(operacion)

    #Método para buscar dentro del historial
    def buscarHistorial(self, busqueda = False):
        if len(self.historial) <= 0:
            return print("\nNo hay historial de operaciones\n")
        else:
            if not busqueda:
                busqueda = int(input("\nIngrese el identificador de la operación->: "))
            found = False
            for i,operacion in enumerate(self.historial):
                if busqueda == operacion['No. Operación']:
                    found = i,operacion
            if not found:
                print("\nOperación inexistente\n")

            return found

    #Método de edición de operaciones
    def editarOperación(self):
        if len(self.historial) <= 0:
            return print("\nNo hay historial de operaciones\n")
        else:
            busqueda = self.buscarHistorial()
            if busqueda: 
                print("\nDesea repetir operación la operación o editarla:\n1)Repetir operación\n2)Editar operación")
                editar = int(input("Elección->: "))
                if editar == 1:
                    if 'Suma = ' in busqueda[1]:
                        eleccion = 1
                        self.operaciones(busqueda[1]['Número1'], busqueda[1]['Número2'], eleccion)
                    elif 'Resta = ' in busqueda[1]:
                        eleccion = 2
                        self.operaciones(busqueda[1]['Número1'],busqueda[1]['Número2'],eleccion)
                elif editar ==2:
                    numero1,numero2 = self.pedirNumeros()
                    if 'Suma = ' in busqueda[1]:
                        eleccion = 1
                        resultado=round((numero1+numero2),2)
                        print(f"{numero1} + {numero2} = {resultado}")
                        self.historial[busqueda[0]]={
                            'No. Operación' : busqueda[1]['No. Operación'],
                            'Número1': numero1,
                            'Número2': numero2,
                            'Suma = ': resultado
                        }
                    elif 'Resta = ' in busqueda[1]:
                        eleccion = 2
                        resultado=round((numero1-numero2),2)
                        print(f"{numero1} - {numero2} = {resultado}")
                        self.historial[busqueda[0]]={
                            'No. Operación' : busqueda[1]['No. Operación'],
                            'Número1': numero1,
                            'Número2': numero2,
                            'Resta = ': resultado
                        }
            else:
                print("\nOperación NO identificada")

    #Método de eliminación del historial
    def eliminar(self):
        if len(self.historial) <= 0:
            return print("\nNo hay historial de operaciones\n")
        else:
            #Menú de elección de eliminación
            eleccion = int(input("\n)Menú de eliminación:\n1)Eliminar todo el historial\n2)Eliminar una operación del historial\n\nElección->: "))
            if eleccion == 1:
                self.mostrarHistorial()
                confirmacion = str(input("\nDesea eliminar todo el historial?\n (Sí)/(No)\n\nElección->:")).lower()
                if confirmacion == 'no':
                    print("No se eliminó el historial")
                else:
                    #Eliminar historial completo
                    self.historial.clear()
                    print("\nHistorial eliminado")
            elif eleccion ==2:
                busqueda = self.buscarHistorial()
                if busqueda:
                    confirmacion = str(input("\nDesea eliminar esta operación del historial?\n (Sí)/(No)->:")).lower()
                    if confirmacion == 'no':
                        print("No se eliminó la operación")
                    else:
                        #Eliminar una operación del historial
                        del self.historial[busqueda[0]]
                        print("\nOperación eliminada")
            else:
                print("\nOperación inexistente")

    #Método de salir
    def salir(self):
        return False


