import random
import math
from timeit import timeit

print("***** Practica 2 ***")
print("\tEste es el segundo programa\n")


def RadixSortLexicografico(arr):
    # Se calcula la cadena mas larga de la lista original y se le asigna a k 
    cadenaLarga = max(arr, key=len)
    # Se Calcula la longitud de la variable k y se le asigna a d    
    d = len(cadenaLarga)
    contador = 0              

    for i in range(len(arr)): 
        while len(arr[i]) < d:
            arr[i] += ' ' #para agregar un espacio a aquellas palabras que no sean de la misma longitud que la más larga
    
    for i in range(d-1,-1,-1): 
         #el ordenamiento de arr según el digito
        arr = CountingSortForRadixSort(arr, len(arr), i)   

    #FOR dedicado a contabilizacion de espacios
    for cadena in arr: #para cada cadena del arreglo
        
        i=len(cadena) - 1   
        contadorEspacios = 0

        while i > -1:    
            if cadena[i] == ' ': 
                contadorEspacios += 1  
            else:   
                break #salir del ciclo cuando esta la separación   
            i -= 1  

        if contadorEspacios >= 1: 
            auxCadena = cadena[:-1*contadorEspacios]  #para obtener la cadena al reves
            arr[contador] = auxCadena 
        
        contador += 1

    return arr

def CountingSortForRadixSort(arr,b,i):
    
    C = [0]*255   # Arreglo temporal basado en el sistema ASCII
    B = [0]*len(arr)  #arreglo para hacer una copia del original pero ya ordenado 
    for j in range(len(arr)):
        cadena = arr[j]         
        valor = ord(cadena[i])
        print(cadena[i])           
        C[valor] += 1    #sumatoria de valores en arreglo de contabilizacion

    for j in range(1, len(C)):
        C[j] = C[j] + C[j-1]  #frecuencia acumulada
    
    for j in range(len(arr)-1,-1,-1):
        cadena = arr[j]               
        valor = ord(cadena[i])
        posicion = C[valor]   
        
        B[posicion - 1] = cadena  
        C[valor] -= 1   

    return B


arr = ["Adan","Nati","Sofia","Frida","Miguel","Olivia",
           "Angel","Raquel","Sara","Ernesto"]


print("\nArreglo Desordenado:\n", arr)

#llamar a la funcion pasando como argumento el arreglo, 
#se iguala ya que al final la funcion retorna el arreglo ordenado
arr = RadixSortLexicografico(arr)

print("\nArreglo Ordenado:\n", arr) 