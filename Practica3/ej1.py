import random
import math
from timeit import timeit

print("***** Practica 2 ***")
print("Este es el primer programa ")
print("Este es uno de los mejores casos ")

#funcion para obtener el tiempo de ejecucion
def measure_time(func, *args, **kwargs):
    globals_ = {'func': func, 'args': args, 'kwargs': kwargs}
    time = timeit('func(*args, **kwargs)',
                  number=1,
                  globals=globals_)
    return f"{time} seconds"

def CountingSort(A):
  #obtenemos el valor maximo del arreglo
  k = max(A)
  print("el elemento maximo del arreglo es: ",k)  
  #creamos un arreglo de k+1 elementos
  C = [0]*(k+1) 
  for i in range(len(A)):
    #para empezar el conteo de los elementos en el arreglo C
    valor = A[i]
    C[valor] += 1

  for i in range(1,len(C)-1):
    #para empezar el conteo incrementado
    C[i] = C[i] + C[i - 1]
  
  #creamos el arreglo B que tendra el arreglo original ordenado  
  B = [0]*len(A)

  for j in range(len(A)-1,-1,-1):
    #colocaremos los valores en su respectiva posicion respeto a la cuenta tomada en C
    valor = A[j]
    posicion = C[valor]
    B[posicion] = valor

    C[valor] -= 1 

  return B
  


def RadixSort(arr):
  #almacenamos el elemento maximo del arreglo
  k = max(arr)
  #obtenemos el numero de digitos basado en k
  d = math.floor(math.log10(k))+1
  print("el elemento maximo del arreglo es: ",k)

  for i in range(d):
    arr = CountingSortForRadixSort(arr,10,i)
  return arr

def CountingSortForRadixSort(arr, b, i):
  k = b - 1
  C = [0]*(k+1)
  for j in range(len(arr)):

    valor = arr[j]
    digito = math.floor(valor/math.pow(b,i)) % b #representar el valor según el digito que representa
    #conteo de valor del digito
    C[digito] += 1

  for j in range(1, len(C)):
    #comenzamos con el conteo incrementado de los valores
    C[j] = C[j] + C[j-1]

  B = [0]*len(arr) #el arreglo copia que representa el arreglo original ordenado

  for j in range(len(arr)-1,-1,-1):
    valor = arr[j]
    digito = math.floor(valor/math.pow(b,i)) % b
    #copiando los valores ordenados en B
    posicion = C[digito]
    B[posicion - 1] =valor
    C[digito] -= 1
  return B

#n sera el numero de elementos del arreglo A
n = 10000
A = []
#llenar la lista aleatoriamente con numeros entre 0 y 9
for i in range(n):
  #para el peor caso tomamos este ultimo rango n*1000
  #para el mejor caso tomamos k << n 
  #para el caso promedio tomamos k aprox a n(k + 100)
    A.append(random.randint(0,10000))


a1 = A[:]
a2 = A[:]
#lista original
#print(A)
#A = CountingSort(A)
#A = RadixSort(A)
#print("El tiempo de ejecucion de Counting Sort es: \n",measure_time(CountingSort,a1))
print("El tiempo de ejecucion de Radix Sort es: \n",measure_time(RadixSort,a2))
#print(A)
#imprimir lista ordenada
#print(CountingSort(A))
