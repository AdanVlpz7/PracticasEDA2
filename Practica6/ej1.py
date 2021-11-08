class Nodo():
    #al crear un objeto Nodo lo inicializamos con ciertos valores y el nombre pasado por el usuario.
    def __init__(self,nombre):       
        self.nombre = nombre
        self.vecinos = [] #tendra varios vecinos pero aún no estan definidos
        self.color = 'blanco' 
        self.distancia = -1 #no ha sido explorado
        self.padre = None #no tiene establecido un padre aún

    #metodo para agregarle un objeto nodo como vecino al nodo referido.
    def agregarVecino(self,nodo):
        
        for v in self.vecinos:
            if v == nodo:
                print('Ya existe el nodo como vecino bro')
                return

        #en caso que nuestro nodo no tenga el nodo del parametro como vecino
        self.vecinos.append(nodo)

    #para cuando se refiera a un objeto nodo se devuelva el nombre del nodo referido.
    def __str__(self):
        return self.nombre 

    def __repr__(self) -> str:
        return self.nombre


class Grafo():
    #al inicializar un objeto grafo le decimos que debe tener en la instancia un diccionario de vertices
    def __init__(self):
        self.vertices = {}

    #funcion para agregar un vertice al grafo definiendo el nombre dado por el usuario
    def agregarVertice(self,nombreNodo):
        for u in self.vertices.values():
            if u.nombre == nombreNodo:
                print('Ya existe en el grafo el nodo: ', nombreNodo)
                return
        nuevoNodo = Nodo(nombreNodo)
        self.vertices[nombreNodo] = nuevoNodo

    #funcion para definir una arista entre dos nodos, dichos nodos son dados con sus nombres
    def agregarArista(self,nombreNodo1,nombreNodo2):
        
        if nombreNodo1 in self.vertices:
            nodo1 = self.vertices[nombreNodo1]
            
        #en caso que el primer nodo pasado como parametro no exista
        else: 
            print("Error no existe el nodo1 con nombre: ", nombreNodo1)
            return

        if nombreNodo2 in self.vertices:
            nodo2 = self.vertices[nombreNodo2]
            
        #en caso que el segundo nodo pasado como parametro no exista
        else: 
            print("Error no existe el nodo2 con nombre: ", nombreNodo2)
            return

        nodo1 = self.vertices[nombreNodo1] 
        nodo2 = self.vertices[nombreNodo2]

        nodo1.agregarVecino(nodo2) #al nodo1 se le asigna como vecino al nodo2
        nodo2.agregarVecino(nodo1) #al nodo2 se le asigna como vecino al nodo1

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

    #funcion base para imprimir un grafo como lista de adyacencia diferenciando cada vertice y sus vecinos
    def __str__(self):
        #creamos un string que tiene un salto de linea para evitar un espacio en el primer vertice
        s = '\n'
        #recorremos los vertices
        for v in self.vertices:
            s += self.vertices[v].nombre + '-> [' # agregar vertice -> [
            for i in self.vertices[v].vecinos:
                s += i.nombre + ',' # agregar el nombre del vecino y una coma
            s += ']' #vertice -> [vecinos]
            s += '\n'

        
        return s

    def __repr__(self):
        s = ''
        for v in self.vertices:
            s += self.vertices[v].nombre + ','
        return s

g = Grafo()
g.agregarVertice('0')
g.agregarVertice('1')
g.agregarVertice('2')
g.agregarVertice('3')
g.agregarVertice('4')
g.agregarVertice('5')
g.agregarVertice('6')
g.agregarVertice('7')
g.agregarVertice('0')

g.agregarArista('9','1')
g.agregarArista('0','1') 
g.agregarArista('0','2') 
g.agregarArista('0','3') 

g.agregarArista('1','2') 

g.agregarArista('2','1')
g.agregarArista('2','3')

g.agregarArista('3','2')
g.agregarArista('3','4')

g.agregarArista('4','3')
g.agregarArista('4','5')
g.agregarArista('4','6')

g.agregarArista('5','6')      

print('Mi grafo es: \n', g)