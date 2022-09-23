class Jugador:
    goles = 0

    #Parámetros del objeto
    def __init__(self, nombre, apellido, numero):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.nombre_completo = self.full_name

    #Creación del nombre completo
    def full_name(self):
        return self.nombre + " " + self.apellido

    #Suma de goles
    def sumarGoles(self, goles):
        self.goles += goles

    #Resta de goles
    def restarGoles(self, goles):
        self.goles -= goles

    #Todos los goles del jugador
    def totalGoles(self):
        return self.goles 

    #Retorno de la infomación del jugador en un json
    def retu_json(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "numero": self.numero,
            "goles": self.goles
            }
