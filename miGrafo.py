import json
import heapq
import math
import random 
class Graph:
    class Vertex:

        def __init__(self, key, info):
            self.id = key
            self.connectedTo = {}
            self.info = info 
            self.x =0
            self.y =0
            self.aristas =[]
        def addArista(self, arista, peso = random.randint(0,50)):
            self.connectedTo[self.id]= self.aristas.append((arista, peso))
        def __str__(self):
            return f"{str(self.id)} connected to: {str(self.aristas)} nombre: {str(self.info)}, x: {self.x}, y: {self.y}"
        def getConnections(self):
            return self.connectedTo.keys
        def idConnections(self):
            lista =[]
            for item in self.connectedTo.values():
                lista.append(item[0].getId())
            print(lista)
            return lista
        def getId(self):
            return self.id
      #  def getWeight(self, nbr):
      #      return self.connectedTo.get(nbr)

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.vertices =[]
    

    def addVertex(self, key, info):
        #añade un vertice al grafo con el id como llave
        self.numVertices += 1
        #instantiate a new Vertex class
        newVertex = self.Vertex(key, info)

        #add the vertex with the key to the vertList dictionary
        self.vertList[key] = newVertex
        #return the NewVertex created
        return newVertex

    def getVertex(self, key):
        """
        If vertex with key is in Graph then return the Vertex
        """
        #use the get method to return the Vertex if it exists
        #otherwise it will return None
        return self.vertList[key]
    def getId(self, key):
        return self.vertList.keys()
    def verInfoConnectios(self, id):
        self.getVertex(id).getConnections()


    def __contains__(self, key):
        """
        Check whether vertex with key is in the Graph
        """
        return key in self.vertList

    def añadirArista(self, f, t, weight = 0):
        """
        Add an edge to connect two vertices of t and f with weight
        assuming directed graph
        """
        #add vertices if they do not exist
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        #then add Neighbor from f to t with weight
        self.vertList[f].addArista(self.vertList[t])
        self.vertList[t].addArista(self.vertList[f])
    
    def getVertices(self):
        return self.vertList.keys()
    def getVerticesCuerpo(self):
        return self.vertList
    def valoresVertices(self):
        return self.vertList.values()
    def getCount(self):
        return self.numVertices
    

    def read_json(self):
        with open('ciudades.json') as data:
            ciudades = json.load(data)
            for ciudad in ciudades:
                self.addVertex(ciudad.get('id'), ciudad.get('name'))
            for ciudad in ciudades:
                for destino in ciudad.get('destinations'):
                    self.añadirArista(ciudad.get('id'), destino)

    def lazy_dijkstras(self,graph, root):
        n = self.numVertices#numVertices
        # set up "inf" distances
        dist = [math.inf for _ in range(n)]
        # set up root distance
        dist[root] = 0
        # set up visited node list
        visited = [False for _ in range(n)]
        # set up priority queue
        pq = [(0, root)]
        # while there are nodes to process
        while len(pq) > 0:
            # get the root, discard current distance
            _, u = heapq.heappop(pq)
            # if the node is visited, skip
            if visited[u]:
                continue
            # set the node to visited
            visited[u] = True
            # check the distance and node and distance
            for v, l in graph[u]:
                # if the current node's distance + distance to the node we're visiting
                # is less than the distance of the node we're visiting on file
                # replace that distance and push the node we're visiting into the priority queue
                if dist[u] + l < dist[v]:
                    dist[v] = dist[u] + l
                    heapq.heappush(pq, (dist[v], v))
        return dist
        
    def bfs(self,id): #function for BFS
        visited = [] # List for visited nodes.
        queue = [] 
        visited.append(id)
        queue.append(id)
        while queue:          # Creating loop to visit each node
            m = queue.pop(0) 
            print (m, end = " ") 
            for neighbour in self.getVertex(id).getConnections():
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour.id)
    
    def getAllSimplePaths(self,originNode, targetNode): 
        return self.helpGetAllSimplePaths(targetNode, 
                                    [originNode], 
                                    [originNode], 
                                    list()) 
 
    def helpGetAllSimplePaths(self,targetNode, 
                            currentPath, 
                            usedNodes, 
                            answerPaths): 
        print(currentPath,usedNodes )
        lastNode = currentPath[-1] 
        if lastNode == targetNode: 
            answerPaths.append(list(currentPath)) 
        else: 
            for neighbor in self.getVerticesCuerpo()[lastNode].idConnections(): 
                if neighbor not in usedNodes: 
                    currentPath.append(neighbor) 
                    usedNodes.append(neighbor) 
                    self.helpGetAllSimplePaths(targetNode, 
                                        currentPath, 
                                        usedNodes, 
                                        answerPaths) 
                    usedNodes.remove(neighbor) 
                    currentPath.pop() 
        return answerPaths 
