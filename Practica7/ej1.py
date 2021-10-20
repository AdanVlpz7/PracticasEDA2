class Nodo():
    def __init__(self,nombre):       
        self.nombre = nombre
        self.vecinos = []
        self.color = 'blanco'
        self.distancia = -1 #no ha sido explorado
        self.padre = None

    def agregarVecino(self,nodo):
        #if self.vecinos
        for v in self.vecinos:
            if v == nodo:
                #print('Ya existe el nodo como vecino bro')
                return
        self.vecinos.append(nodo)

    def __str__(self):
        return self.nombre 

    def __repr__(self) -> str:
        return self.nombre


class Grafo():
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self,nombreNodo):
        nuevoNodo = Nodo(nombreNodo)
        self.vertices[nombreNodo] = nuevoNodo

    def agregarArista(self,nombreNodo1,nombreNodo2):
        
        if nombreNodo1 in self.vertices:
            nodo1 = self.vertices[nombreNodo1]
            
        
        else: 
            print("Error no existe el nodo1 con nombre: ", nombreNodo1)
            return

        if nombreNodo2 in self.vertices:
            nodo2 = self.vertices[nombreNodo2]
            
        
        else: 
            print("Error no existe el nodo2 con nombre: ", nombreNodo2)
            return

        nodo1 = self.vertices[nombreNodo1]
        nodo2 = self.vertices[nombreNodo2]

        nodo1.agregarVecino(nodo2)
        nodo2.agregarVecino(nodo1)

    def bfs(self,nodoInicial):
        for u in self.vertices.values():
            u.color = 'blanco'
            u.distancia = -1
            u.padre = None

        self.vertices[nodoInicial].color = 'gris'
        self.vertices[nodoInicial].distancia = 0
        self.vertices[nodoInicial].padre = None


        Q = []
        Q.append(self.vertices[nodoInicial]) #encolar Q
        while len(Q) > 0:
            u = Q.pop()
            for v in u.vecinos:
                if v.color == 'blanco':
                    v.color = 'gris'
                    v.distancia = u.distancia + 1
                    v.padre = u
                    print(u.nombre)
                    print(u.color)
                    print(u.distancia)
                    print(u.padre)
                    Q.append(v)
            
            u.color = 'Negro'

    def __str__(self):
        s = ''
        for v in self.vertices:
            s += self.vertices[v].nombre + '-'
            for i in self.vertices[v].vecinos:
                s += i.nombre + ','
            s += '\n'
        return s

    def __repr__(self):
        s = ''
        for v in self.vertices:
            s += self.vertices[v].nombre + ','
        return s

g = Grafo()
g.agregarVertice('1')
g.agregarVertice('2')
g.agregarVertice('3')
g.agregarVertice('4')
g.agregarVertice('5')
g.agregarVertice('6')

g.agregarArista('1','1') 
g.agregarArista('1','2') 
g.agregarArista('1','5') 

g.agregarArista('2','1')
g.agregarArista('2','3')
g.agregarArista('2','5')

g.agregarArista('3','2')
g.agregarArista('3','4')

g.agregarArista('4','3')
g.agregarArista('4','4')
g.agregarArista('4','5')

g.agregarArista('5','1')
g.agregarArista('5','2')
g.agregarArista('5','4')

g.agregarArista('6','4')            

g.bfs('1')
g.bfs('2')
print('Mi grafo es: \n', g)
#cola = []
#cola.append('a')

#cola.append('b')

#cola.append('c')

#cola.pop(0) #para sacar el primer elemento, como en una cola