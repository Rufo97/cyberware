# # Ejercicio 1
# # Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

# nombre = input("escribe tu nombre: ")
# n = input("escribe un numero entero: ")
# print ((nombre + "\n") * int(n))



# Ejercicio 2

# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

# nombre = input("escribe tu nombre: ")

# print(nombre.lower())
# print(nombre.upper())
# print(nombre.title())


# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

# nombre = input("pon tu nombre: ")
# print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

# tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
# print('El número de teléfono es ', tel[4:-3])

# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.


# frase = input("Introduce una frase: ")
# print(frase[::-1])

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("escriba una frase: ")
vocal = input("escriba una vocal: ")
print(frase.replace(vocal, vocal.upper()))

# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("escribe tu correo electronic: ")
print() 