from typing import List
from Database_12K import Usuario
import collections

def CrearTablaHash(m):
	t = [None]*m
	for i in range(m):
		t[i] = list()

	#crear listas ligadas vacias para cada indice de t
	return t

def CalcularHash(cadena, m, j):
	sum = 0
	for i in range(len(cadena)):
		sum += (i + 1)*ord(cadena[i])

	#hash por metodo de division
	hash = (sum + j) % n
	return hash 