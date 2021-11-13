""" Escriba un programa para calcular la frecuencia de las palabras de la entrada. La salida debería aparecer después de ordenar la clave alfanuméricamente.
Suponga que se proporciona la siguiente entrada al programa:
¿Es nuevo en Python o elige entre Python 2 y Python 3? Leer Python 2 o Python 3.
"""


Palabras = input('Ingrese la secuencia de palabras:>')


listaPalabras = Palabras.split() 

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + Palabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencia\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab)))) 