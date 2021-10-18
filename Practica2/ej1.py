import random
import math
import sys
from timeit import timeit

print("***** Practica 2 ***")
print("N = 5000")
print("Este es uno de los mejores casos")


#funcion para obtener el tiempo de ejecucion
def measure_time(func, *args, **kwargs):
    globals_ = {'func': func, 'args': args, 'kwargs': kwargs}
    time = timeit('func(*args, **kwargs)',
                  number=1,
                  globals=globals_)
    return f"{time} seconds"

#funcion para intercambiar dos valores en un arreglo
def SwitchElements(arr,i,j):
    aux = arr[i]
    arr[i]=arr[j]
    arr[j]= aux

def QuickSortPartition(arr,idxIni,idxFin):
    x=arr[idxFin]
    i = idxIni - 1
    for j in range(idxIni,idxFin):
        if (x>=arr[j]):
            i = i + 1
            SwitchElements(arr,i,j)
    SwitchElements(arr,i+1,idxFin)
    return i+1

def Quicksort(arr, idxIni,idxFin):
    if(idxIni<idxFin):
        q = QuickSortPartition(arr,idxIni,idxFin)
        Quicksort(arr, idxIni, q-1) 
        Quicksort(arr, q+1,idxFin)

def RandomQuickSort(arr, idxIni , idxFin):
    if(idxIni < idxFin):
        pivotindex =  RandomPartition(arr,idxIni, idxFin)
        RandomQuickSort(arr , idxIni , pivotindex-1)
        RandomQuickSort(arr, pivotindex + 1, idxFin)

def RandomPartition(arr , idxIni, idxFin):
    randpivot = random.randrange(idxIni, idxFin)   
    arr[idxIni], arr[randpivot] = arr[randpivot], arr[idxIni]
    return RandomQuicksortPartition(arr, idxIni, idxFin)
 
def RandomQuicksortPartition(arr,idxIni,idxFin):
    pivot = idxIni 
    i = idxIni + 1
    for j in range(idxIni + 1, idxFin + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)

def MaxHeapify(arr, i, tamHeap):
    idxIzq = 2*i+1
    idxDer = 2*i+2

    idxMax = i

    if (idxIzq < tamHeap) and (arr[idxIzq] > arr[i]):
        idxMax = idxIzq

    if (idxDer < tamHeap) and (arr[idxDer] > arr[idxMax]):
        idxMax = idxDer

    if (idxMax != i):
        arr[i], arr[idxMax] = arr[idxMax], arr[i]
        MaxHeapify(arr, idxMax, tamHeap)

def construirHeapMaxIni(arr,tamHeap):
    for i in range((tamHeap - 1) // 2, -1, -1):
        MaxHeapify(arr, i, tamHeap)

def HeapSort(arr,tamHeap):
    construirHeapMaxIni(arr,tamHeap)
    for i in range(tamHeap-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        tamHeap -= 1
        MaxHeapify(arr, 0, tamHeap)

def Ascendente(arr,n):
  i = 0
  for i in range(n):
    arr.append(i)
  return arr

def Descendente(arr, n):
  j = n
  while j > 0:
    arr.append(j)
    j -= 1
  return arr

def Aleatoria(arr,n):
  #llenar la lista aleatoriamente con numeros entre 0 y 9
  for i in range(n):
  #para el peor caso tomamos este ultimo rango n*1000
  #para el mejor caso tomamos k << n 
  #para el caso promedio tomamos k aprox a n(k + 100)
    A.append(random.randint(0,10))

n = 1000 # longitud arreglo
A = [] # arreglo original
sys.setrecursionlimit(n*4)

#definir los casos segun el arreglo

A = Ascendente(A,n)
#A = Descendente(A,n)
#A = Aleatoria(A,n)

#copias del arreglo
a1 = A[:]
a2 = A[:]
a3 = A[:]

#ordenacion en cada copia
Quicksort(a1,0,n-1)
RandomQuickSort(a2,0,n-1)
HeapSort(a3,n)

#imprimir en consola el tiempo de cada metodo
print("El tiempo de ejecucion de Quicksort es: \n",measure_time(Quicksort,a1,0,n-1))
print("El tiempo de ejecucion del Random Quicksort es: \n",measure_time(RandomQuickSort,a2,0,n-1))
print("El tiempo de ejecucion de HeapSort es: \n",measure_time(HeapSort,a3,n))
