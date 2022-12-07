# Pila Lista enlazada simple - Stack Single linked list

class Pila:
    class _Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.nodo_siguiente = None
            self.nodo_anterior = None 
    def __init__(self, rect):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0
        self.rect = rect
        self.activate = False 
    def __str__(self):
        # Muestra los elementos de la Stack
        array = []
        nodo_actual = self.cabeza
        while nodo_actual != None:
            array.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente
        return str(array) + " Tamaño: " + str(self.tamaño)

        
    def push(self, valor):
        # Agrega un elemento al principio de la Stack
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.tamaño += 1
            return True
        else:
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cabeza.nodo_anterior = nuevo_nodo 
            self.cabeza = nuevo_nodo
            self.tamaño += 1
            return True
        
    def pop(self):
        # Saca el primer elemento de la Stack
        if self.tamaño == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
            nodo_eliminado.nodo_siguiente = None
            self.tamaño -= 1
            return nodo_eliminado.valor

