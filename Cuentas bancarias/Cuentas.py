class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = str(titular)
        self.cantidad = int(cantidad)

    def Mostrar(self):
        print(f"Titular: {self.titular}\nCantidad: {self.cantidad}")


class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = int(plazo)
        self.interes = float(interes)


    def importeInteres(self):
        porcentaje = float(self.interes/100)
        resu = float(self.cantidad * porcentaje)
        self.importe = float(resu/100)

    def Mostrar(self):
        print(f"Titular: {self.titular}\nPlazo: {self.plazo} meses\nInterés: {self.interes}%\nTotal Interés: {self.importe}")



cuenta1 = Cuenta('Amet Jimenez', 200000)
cuenta1.Mostrar()
cuenta2 = CajaAhorro("Ronaldo Pardo", 500000)
cuenta2.Mostrar()
cuenta3 = PlazoFijo('Ernesto Cabana', 24000000, 8, 25)
cuenta3.importeInteres()
cuenta3.Mostrar()