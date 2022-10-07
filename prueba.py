from dotenv import load_dotenv
import requests
from decouple import config

load_dotenv()



#----------------------------------- Code ----------------------------------------
#Obteniendo la url de la api

api_url = config("url_api")

class Pokeapi:


    def __init__(self):
        self.data = []

    def consultarCampo(self):
        print("Ingrese el campo que quiera ver:\n1)Bayas\n2)Evoluciones\n3)Juegos\n4)Pokedex\n5)Movimientos\n6)Pokemones")
        eleccion=int(input("\n->:"))
        if eleccion==1:
            campo = 'berry/'
        elif eleccion==2:
            campo = 'evolution-chain/'
        elif eleccion==3:
            campo = 'pokedex/'
        elif eleccion==4:
            campo = 'move/'
        elif eleccion==5:
            campo = 'pokemon/'

        return api_url + campo



    def get_pokemon_data(self, url_pokemon=''):
        pokemon_data = {
        }

        response = requests.get(url_pokemon)
        data = response.json()


    def main(self):

        pokemon_name = str(input('Ingresar ID del area ->: ')).lower()
        pokemon_url = api_url + pokemon_name
        data = self.get_pokemon_data(pokemon_url)

        print("{}\nEste es toda la información disponible\nPara más información, vaya a: {}".format(data, pokemon_url))

    # print(data)

