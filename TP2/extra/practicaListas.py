#!/usr/bin/env python3
#-*-coding:utf-8-*-


# Creación de la matriz
lista = [ [2,2,5,6],[0,3,7,4],[8,8,5,2],[1,5,6,1] ]

print('Matriz original')
for elemento in lista:
    print(elemento)


# Selecciona fila 2
print('\nSelección de fila 2')
fila2 = lista[2]
print(fila2)


# Seteo de diagonal en 0
print('\nSetea la diagonal en 0')
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if(i==j):
            lista[i][j] = 0

for elemento in lista:
    print(elemento)


#Suma todos los elementos
print('\nLa suma de todos los elementos es:', end=' ')
suma = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        suma += int(lista[i][j])

print(suma)


# Diferencia elementos pares e impares
print('\nLa matriz con los valores pares en 0 e impares en 1 es')
for i in range(len(lista)):
    for j in range(len(lista[i])):
        suma += int(lista[i][j])
        if(lista[i][j]%2 == 0): 
            lista[i][j] = 0
        else:
            lista[i][j] = 1

for elemento in lista:
    print(elemento)
