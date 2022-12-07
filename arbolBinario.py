
import collections
class binary_search_tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left_branch = None
            self.rigth_branch = None
    def __init__(self):
        self.root = None
        self.length = 0
    def insert(self, value):
        new_node = self.Node(value)
        if self.root == None:
            self.root = new_node
            self.length += 1
        else:
            def tree_route(value, node):
                if value == node.value:
                    return "El elemento ya existe"
                elif value < node.value:
                    if node.left_branch == None:
                        node.left_branch = new_node
                        self.length +=1
                        return True
                    else:
                        return tree_route(value, node.left_branch)
                elif value > node.value:
                    if node.rigth_branch == None:
                        node.rigth_branch = new_node
                        self.length +=1 
                        return True
                    else:
                        return tree_route(value, node.rigth_branch)
            tree_route(value, self.root)
    def find(self, value):
        def tree_route(value, node):
            if value == node.value:
                return node.value
            elif value < node.value:
                if node.left_branch == None:
                    return "No existe el elemento buscado"
                else:
                    return tree_route(value, node.left_branch)
            else:
                if node.rigth_branch == None:
                    return "No existe el elemento buscado"
                else:
                    return tree_route(value, node.rigth_branch)
        node_find = tree_route(value, self.root)
        return print(node_find)
    def delete(self, value):
        def tree_route(value, node, previous_node):
            if value == node.value:
                if node.left_branch == None and node.rigth_branch == None:
                    if previous_node.left_branch != None:
                        if previous_node.left_branch.value == node.value:
                            previous_node.left_branch = None
                    if previous_node.rigth_branch != None:
                        if previous_node.rigth_branch.value == node.value:
                            previous_node.rigth_branch = None
                    node = None
                elif node.left_branch == None and node.rigth_branch != None:
                    if previous_node.left_branch != None:
                        if previous_node.left_branch.value == node.value:        
                            previous_node.left_branch = node.rigth_branch
                    if previous_node.rigth_branch != None:
                        if previous_node.rigth_branch.value == node.value:
                            previous_node.rigth_branch = node.rigth_branch
                elif node.rigth_branch == None and node.left_branch != None:
                    if previous_node.left_branch != None:
                        if previous_node.left_branch.value == node.value:
                            previous_node.left_branch = node.left_branch
                    if previous_node.rigth_branch != None:
                        if previous_node.rigth_branch.value == node.value:
                            previous_node.rigth_branch = node.left_branch
                else:
                    node_comodin = None
                    previous_node = node
                    node = node.rigth_branch
                    #--Codigo agregado aun no explicado Inicio--
                    if node.left_branch == None and node.rigth_branch != None:
                        previous_node.value = node.value
                        previous_node.rigth_branch = node.rigth_branch
                    elif node.left_branch == None and node.rigth_branch == None:
                        previous_node.value = node.value
                        previous_node.rigth_branch = None
                    #--Codigo agregado aun no explicado Fin--
                    else:
                        while node.left_branch != None:
                            node_comodin = node
                            node = node.left_branch
                        previous_node.value = node.value
                        if node.rigth_branch != None:
                            node_comodin.left_branch = node.rigth_branch
                        else:
                            node_comodin.left_branch = None
                    node = None
            elif value < node.value:
                if node.left_branch == None:
                    return "No existe el elemento buscado"
                else:
                    return tree_route(value, node.left_branch, node)
            else:
                if node.rigth_branch == None:
                    return "No existe el elemento buscado"
                else:
                    return tree_route(value, node.rigth_branch, node)
        tree_route(value, self.root, self.root)
  
    def preorder(self):
        contenedor = []
        def tree_route(node):
            contenedor.append(node.value)
            if node.left_branch != None:
                tree_route(node.left_branch)
            if node.rigth_branch != None:
                tree_route(node.rigth_branch)
        tree_route(self.root)
        return contenedor
   
    def inorder(self):
        contenedor = []
        def tree_route(node):
            if node.left_branch != None:
                tree_route(node.left_branch)
            contenedor.append(node.value)
            if node.rigth_branch != None:
                tree_route(node.rigth_branch)
        tree_route(self.root)
        return contenedor
  
    def postorder(self):
        contenedor = []
        if self.root != None:
            def tree_route(node):
                if node.left_branch != None:
                    tree_route(node.left_branch)
                if node.rigth_branch != None:
                    tree_route(node.rigth_branch)
                contenedor.append(node.value)
            tree_route(self.root)
        return contenedor
        
    def breadth_first_search(self):
        contenedor_1 = [self.root]
        contenedor_2 = [self.root.value]
        while len(contenedor_1) != 0:
            node = contenedor_1.pop(0)
            if node.left_branch != None:
                contenedor_1.append(node.left_branch)
                contenedor_2.append(node.left_branch.value)
            else:
                contenedor_2.append(None)
            if node.rigth_branch != None:
                contenedor_1.append(node.rigth_branch)
                contenedor_2.append(node.rigth_branch.value)
            else:
                contenedor_2.append(None)
        return contenedor_2

    def amplitud(self):
        contenedor_1 = [self.root]
        contenedor_2 = [self.root.value]
        while len(contenedor_1) != 0:
            node = contenedor_1.pop(0)
            if node.left_branch != None:
                contenedor_1.append(node.left_branch)
                contenedor_2.append(node.left_branch.value)
            if node.rigth_branch != None:
                contenedor_1.append(node.rigth_branch)
                contenedor_2.append(node.rigth_branch.value)
        return contenedor_2


    def levels (self):
        resList = []
        q = collections.deque()
        if self.root:
            q.append(self.root)
        while q:
            level = []
            qLen = len(q)
            for node in range(qLen):
                cur = q.popleft()
                if cur.left_branch:
                    q.append(cur.left_branch)
                if cur.rigth_branch:
                    q.append(cur.rigth_branch)
                level.append(cur.value)
            resList.append(level)
        
        return resList

   