"""
En una empresa los vendedores reciben una comisión del 13% por el valor total
de sus ventas. Se necesita un programa que les calcule su nombre y cuanto han
vendido para calcular la comisión que le toca a cada trabajador.
"""

Nombre = input("¿Cuál es su nombre?: ")
Ventas = int(input("¿Cuánto vendió en el evento?: "))
comision = round(Ventas * 13 / 100, 2)
print(f"Estimado {Nombre}, su comisión es de ${comision} que es el 13% de sus ventas que fueron ${Ventas}")
