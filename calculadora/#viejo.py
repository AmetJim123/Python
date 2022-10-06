#viejo
class Calculadora:
    
    #Creación del parametro historial
    def __init__(self):
        self.historial = []

    #Creación método sumar
    def sumar(self,numero1=False, numero2=False):
        #Condición para repetir la operación
        if numero1 and numero2:
            resultado =round((numero1+numero2),2)
            print(f"{numero1} + {numero2} = {resultado}")
            #Adición de la operación al historial
            self.historial.append({
                'No. Operación' : len(self.historial) + 1,
                'Número1' : numero1,
                'Número2' : numero2,
                'Suma = ' : resultado
            })
        elif not numero1 and not numero2:
            numero1 = float(input("Ingrese su primer valor ->: "))
            numero2 = float(input("Ingrese su segundo valor valor ->: "))
            resultado = round((numero1 + numero2),2)
            #Impresion del resultado
            print(f"{numero1} + {numero2} = {resultado}")
            #Adición de la operación al historial
            self.historial.append({
                'No. Operación' : len(self.historial) + 1,
                'Número1' : numero1,
                'Número2' : numero2,
                'Suma = ' : resultado
            })

    #Creación método Restar
    def restar(self, numero1=False, numero2=False):
        #Condición para repetir la operación
        if numero1 and numero2:
            resultado = round((numero1-numero2),2)
            print(f"{numero1} - {numero2} = {resultado}")
            #Adición de la operación al historial
            self.historial.append({
                'No. Operación' : len(self.historial) + 1,
                'Número1' : numero1,
                'Número2' : numero2,
                'resta = ' : resultado
            })
        elif not numero1 and not numero2:
            numero1 = float(input("Ingrese su primer valor ->: "))
            numero2 = float(input("Ingrese su segundo valor valor ->: "))
            resultado = round((numero1 - numero2),2)
            #Impresion del resultado
            print(f"{numero1} - {numero2} = {resultado}")
            #Adición de la operación al historial
            self.historial.append({
                'No. Operación' : len(self.historial) + 1,
                'Número1' : numero1,
                'Número2' : numero2,
                'Resta = ' : resultado
            })

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
                eleccion = int(input("Elección->: "))
                if eleccion == 1:
                    if 'Suma = ' in busqueda[1]:
                        numero1 = busqueda[1]['Número1']
                        numero2 = busqueda[1]['Número2']
                        self.sumar(numero1,numero2)
                    elif 'Resta = ' in busqueda[1]:
                        numero1 = busqueda[1]['Número1']
                        numero2 = busqueda[1]['Número2']
                        self.restar(numero1,numero2)
                elif eleccion ==2:
                    if 'Suma = ' in busqueda[1]:
                        numero1 = float(input("Ingrese su primer valor ->: "))
                        numero2 = float(input("Ingrese su segundo valor valor ->: "))
                        resultado = round((numero1 + numero2),2)
                        self.historial[busqueda[0]]={
                            'No. Operación' : busqueda[1]['No. Operación'],
                            'Número1' : numero1,
                            'Número2' : numero2,
                            'Suma = ' : resultado
                        }
                    elif 'Resta = ' in busqueda[1]:
                        numero1 = float(input("Ingrese su primer valor ->: "))
                        numero2 = float(input("Ingrese su segundo valor valor ->: "))
                        resultado = round((numero1 - numero2),2)
                        self.historial[busqueda[0]]={
                            'No. Operación' : busqueda[1]['No. Operación'],
                            'Número1' : numero1,
                            'Número2' : numero2,
                            'Resta = ' : resultado
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