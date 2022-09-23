from jugador import Jugador

import json

#Instanciamiento del Json
data = {}
with open('jugadores.json', 'r') as f:
    data = f.read()
    data = json.loads(data)

    #Creación de la función que recibe los parámetros
    def jugador_vs_jugador(data):
        #Asignación de parámetros de jugadores
        jugadores = []
        for jugador in data["jugadores"]:
            jugadores.append(Jugador(jugador["nombre"], jugador["apellido"], jugador["numero"]))

        #Instanciamiento de jugadores
        jugador1 = jugadores[0]
        jugador2 = jugadores[1]

        s = True

        #Ejecución de la suma y resta
        print("""Bienvenido a la comparación de jugadores.""")
        while s==True:
            #Elección de jugador
            jugador_actual = str(input(f"""Ingerese el nombre del jugador desea elegir:
1){jugador1.nombre_completo()} con el número {jugador1.numero}
2){jugador2.nombre_completo()} con el número {jugador2.numero}
->: """)).lower()

            seguir = True
            #Suma y resta de goles
            while seguir ==True:
                if jugador_actual=='kevin':
                    accion = input("Sumar o restar goles? s para sumar, r para restar ->:").lower()
                    if accion == 's':
                        jugador1.sumarGoles(1)
                    elif accion =='r':
                        jugador1.restarGoles(1)
                elif jugador_actual=='ronaldo':
                    accion = input("Sumar o restar goles? s para sumar, r para restar ->").lower()
                    if accion == 's':
                        jugador2.sumarGoles(1)
                    elif accion =='r':
                        jugador2.restarGoles(1)
                else:
                    print("por favor, ingrese el nombre del jugador")
                detener = input("Desea continuar con el jugador? Sí o No ->: ").lower()
                if detener == 'no':
                    seguir = False
            romper = input("Desea salir? Sí o No ->: ").lower()
            if romper=='si':
                break
        
        #Retorno del json con la nueva información
        print(jugador1.retu_json())
        print(jugador2.retu_json())

    jugador_vs_jugador(data)


