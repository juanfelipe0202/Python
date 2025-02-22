import random

datos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("que larga quieres tu contraseña:"))

contrasena = ""

for i in range(longitud):
    p = random.choice(datos)
    contrasena += p
print(contrasena)