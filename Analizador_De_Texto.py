""" Analizador de texto
Se necesita un programa que le pida al usuario que ingrese un texto (puede ser párrafo, informe, lo que desee
pero que sea un texto) y que luego pida al usuario que se ingrese 3 (tres) letras a su libre elección. Con es-
to procederemos a entregarle al usuario 5 tipos de información que serán:

1) Cuántas veces aparece cada letra suministrada por el usuario
2) Cuántas palabras hay en el texto
3) Informar cuál es la primera y última letra del texto
4) Mostrar el texto con el orden de las palabras invertidas
5) Mostrar si la palabra "Python" se encuentra dentro del texto

"""

mi_texto = input("Por favor, ingrese un texto cualquiera: ")
letras = []

mi_texto = mi_texto.lower()

letras.append(input("Por favor, ingrese la primera letra al azar de su preferencia: ").lower())
letras.append(input("Por favor, ingrese la segunda letra al azar de su preferencia: ").lower())
letras.append(input("Por favor, ingrese la tercera letra al azar de su preferencia: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
count_letras1 = mi_texto.count(letras[0])
count_letras2 = mi_texto.count(letras[1])
count_letras3 = mi_texto.count(letras[2])

print(f"Se econctró la letra {letras[0]} <{count_letras1}> veces")
print(f"Se econctró la letra {letras[1]} <{count_letras2}> veces")
print(f"Se econctró la letra {letras[2]} <{count_letras3}> veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = mi_texto.split()
print(f"Se encontró {len(palabras)} palabras en el texto")

print("\n")
print("LETRA INICIAL Y FINAL")
letra_inicial = mi_texto[0]
letra_final = mi_texto[-1]
print(f"La letra inicial de su texto es '{letra_inicial[0]}' y la letra final es  '{letra_final[-1]}'")

print("\n")
print("Orden de las palabras invertidas")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos el texto de forma invertida va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in mi_texto
dic = {True: "sí", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
