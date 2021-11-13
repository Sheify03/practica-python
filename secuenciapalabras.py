""" Escriba un programa que acepte una sequencia de palabras separadas por coma como input y que print las palabras en una sequencia separada por comas despues de ser ordenadas alfabeticamente"""


sec = input('Introduce una secuencia de palabras > ')
print(', '.join(sorted(set(sec.split(' ')))))