import pygame
import pygame_gui
from pygame import *
import sys
import os
from carta import Carta 
from pygame.locals import *
from Pila import Pila
from arbolBinario import binary_search_tree
from dropdown import DropDown
from grafito import *
grafo = Grafica()
grafo.read_json()
listica = []    
combo = None 
main_window= None
clock= time.Clock()
corde_y = 400
radio = 30
#botones 
pila1 = Rect (800, 500,150,50)
arboles = Rect (800, 550,150,50)
grafos = Rect (800, 600,150,50)
añadir = Rect (400, 250, 150, 50)
nuevoNodo = Rect (800, 100, 150, 50)
rect_nodo =pygame.Rect((650, 180), (300, 50))
pila4 = Pila(pygame.Rect((90, 0), (210, 650)))
pila3 = Pila(pygame.Rect((250, 0), (470, 650)))
pila2= Pila(pygame.Rect((470, 0), (630, 650)))
pila = Pila(pygame.Rect((630, 0), (1000, 650)))
seleccionarCiudades = Rect((150,50),(150,50))
cambiarValorConexion = pygame.Rect(800, 50, 400, 30)
cambio = Rect(850,150,150, 50)
verConnecciones = Rect(850,400,200,50)

#banderas 
bandera= False

init()

# asignar puntos en el mapa para las ciudades 
listaPuntos = [(250,110),(395,285), (450,110), (470,230), (450,290), (370,310), (410,120), (495,170),(590,520),(420,210),(390,160),(400,270),(390,270),(330,380),(500,90),(450,110),(480,140),(500,310)]
i=0
for item in grafo.vertices:
    if i < len(listaPuntos):
        grafo.vertices[item].x = listaPuntos[i][0]
        grafo.vertices[item].y = listaPuntos[i][1]
    i+=1

dropRecorridos = DropDown(["white", "red"],
                          ["white", "red"],
                          150,50,150,50,    
                          pygame.font.SysFont(None, 30),
                          "Recorridos", ["postorder", "inorder","amplitud", "preorder"]  )
dd = DropDown(
    ["green", "red"],
    ["white", "white"],
    50, 50, 150, 30, 
    pygame.font.SysFont(None, 20), 
    "Ciudad origen", ["San Andres", "Armenia", "Barranquilla","Bucaramanga","Bogota","Cali","Cartagena","Cucuta","Leticia","Medellin","Monteria","Neira","Pasto","Riohacha","Santa Marta","Valledupar","Villavicencio"])
ddestino = DropDown(
    ["green", "red"],
    ["white", "white"],
    200, 50, 300, 30, 
    pygame.font.SysFont(None, 20), 
    "Ciudad destino", ["San Andres", "Armenia", "Barranquilla","Bucaramanga","Bogota","Cali","Cartagena","Cucuta","Leticia","Medellin","Monteria","Neira","Pasto","Riohacha","Santa Marta","Valledupar","Villavicencio"])
ciudad1 = DropDown(
    ["green", "red"],
    ["white", "white"],
    1150, 100, 150, 30, 
    pygame.font.SysFont(None, 20), 
    "ciudad 1", ["San Andres", "Armenia", "Barranquilla","Bucaramanga","Bogota","Cali","Cartagena","Cucuta","Leticia","Medellin","Monteria","Neira","Pasto","Riohacha","Santa Marta","Valledupar","Villavicencio"])
ciudad2 = DropDown(
    ["green", "red"],
    ["white", "white"],
    1000, 100, 150, 30, 
    pygame.font.SysFont(None, 20), 
    "Ciudad 2", ["San Andres", "Armenia", "Barranquilla","Bucaramanga","Bogota","Cali","Cartagena","Cucuta","Leticia","Medellin","Monteria","Neira","Pasto","Riohacha","Santa Marta","Valledupar","Villavicencio"])

#listas 
cartas = [ ]
listapilas = [ ]
pilas =[]
cartas = [ ]
nodosDibujar=[]
recorridos= []
WIDTH, HEIGHT = 1400, 650
dimension=300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poker")
myFont = font.SysFont('Roboto' ,30 )
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
manager2 = pygame_gui.UIManager((WIDTH, HEIGHT))
text_input = pygame_gui.elements.UITextEntryLine(rect_nodo, manager=manager,
                                               object_id='#valornodo')
input_cambio = pygame_gui.elements.UITextEntryLine(cambio, manager=manager2,
                                               object_id='#inputcambio')
miFuente = pygame.font.Font(None, 50)
carpeta_juego = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_juego, "imagenes")
arbol = binary_search_tree()
global primeraCiudad
global segundaCiudad
primeraCiudad = None
segundaCiudad = None

      #CARTAS
      
carta1= Carta(pygame.transform.scale(pygame.image.load("imagenes/2-trebol.jpg"), (100,200)), 700,50,2)
carta2 = Carta(pygame.transform.scale(pygame.image.load("imagenes/3-trebol.jpg"), (100,200)), 700, 80,3)
carta3 = Carta(pygame.transform.scale(pygame.image.load("imagenes/4-trebol.jpg"), (100,200)), 700, 110,4)
carta4 = Carta(pygame.transform.scale(pygame.image.load("imagenes/5-trebol.jpg"), (100,200)), 700, 140,5)
carta8 = Carta(pygame.transform.scale(pygame.image.load("imagenes/6-trebol.jpg"), (100,200)), 500,50,6)
carta7 = Carta(pygame.transform.scale(pygame.image.load("imagenes/7-trebol.jpg"), (100,200)), 500, 80,7)
carta6 = Carta(pygame.transform.scale(pygame.image.load("imagenes/8-trebol.jpg"), (100,200)),500,110,8)
carta5 = Carta(pygame.transform.scale(pygame.image.load("imagenes/9-trebol.jpg"), (100,200)), 500,140,9)
carta11 = Carta(pygame.transform.scale(pygame.image.load("imagenes/10-trebol.jpg"), (100,200)), 300,50,10)
carta10 = Carta(pygame.transform.scale(pygame.image.load("imagenes/11-trebol.jpg"), (100,200)), 300,80,11)
carta9 = Carta(pygame.transform.scale(pygame.image.load("imagenes/12-trebol.jpg"), (100,200)),300,110,12)
carta12 = Carta(pygame.transform.scale(pygame.image.load("imagenes/13-trebol.jpg"), (100,200)),100,80,13)
carta13 = Carta(pygame.transform.scale(pygame.image.load("imagenes/14-trebol.jpg"), (100,200)), 100,50,14)
carta14 = Carta(pygame.transform.scale(pygame.image.load("imagenes/15-trebol.jpg"), (100,200)), 730,180,15)
pila.push(carta1)
pila.push(carta2)
pila.push(carta3)
pila.push(carta4) 
pila2.push(carta8)
pila2.push(carta7)
pila2.push(carta6)
pila2.push(carta5)
pila3.push(carta11)
pila3.push(carta10)
pila3.push(carta9)
pila4.push(carta13) 
pila4.push(carta12)
#pila4.push(carta14)
pilas.append(pila)
pilas.append(pila2)
pilas.append(pila3)
pilas.append(pila4)
textonodo= ""
textopadre =""
banderaAñadir = False 
nodos = []
a=1

def show_selection():
    # Obtener la opción seleccionada.
    selection = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )

#PARA LISTA DESPLEGABLE DE CIUDADES
#GRAFOS
def showComboBox():
    global main_window
    global combo 
    main_window = tk.Tk()
    main_window.config(width=400, height=50)
    main_window.title("ciudad origen")
    
    combo2 = ttk.Combobox(
        state="readonly",
        values=["Python", "C", "C++", "Java"]
    )
    combo = ttk.Combobox(
        state="readonly",
        values=["Python", "C", "C++", "Java"]
    )
    combo.place(x=10, y=10)
    combo2.place(x= 150,y=10)
    button = ttk.Button(text="Mostrar selección", command=show_selection)
    button.place(x=250, y=10)
    main_window.mainloop()
    
def showComboOrden():
    main_window = tk.Tk()
    main_window.config(width=400, height=50)
    main_window.title("ciudad origen")
    
    combo = ttk.Combobox(
        state="readonly",
        values=["Inorder", "Posorder", "Preorder", "Amplitud"]
    )
    combo.place(x=10, y=10)
    button = ttk.Button(text="Mostrar selección", command=show_selection)
    button.place(x=250, y=10)
    main_window.mainloop()
    

#GRAFOS
def generateGraphs(bandera, texto, banderaConecciones):
    if bandera:
        imagen =pygame.transform.scale(pygame.image.load("imagenes/Mapa.jpg"), (600,500))
        SCREEN.blit(imagen, (200,100))
        dibujar(cambiarValorConexion, "cambiar valor conexion")
        manager2.draw_ui(SCREEN)
        draw_button(SCREEN, verConnecciones, "verConnecciones")
        for item in grafo.vertices:
                dibujarPuntico(grafo.vertices[item].x, grafo.vertices[item].y)
        if listaGrafos != None:
            banderaConecciones = False 
            print(listaGrafos)
            unirPuntos(listaGrafos)
        if banderaConecciones:
            mostrarConexiones()
        if texto != "" and primeraCiudad >-1 and segundaCiudad >-1:
            #la info que me llegue de ciudad, de los dropbox
            i=0
            aux= None
            for item in grafo.vertices:
                    if i == segundaCiudad:
                        aux = item
                        break
                    i+=1
            i=0
            for item in grafo.vertices:
                        if i == primeraCiudad:
                            print (grafo.vertices[item].vecinos)
                            for vecino in grafo.vertices[item].vecinos:
                                if vecino[0] == aux:
                                    vecino[1] = int(texto)
                                    break
                            print (grafo.vertices[item].vecinos)
                        i+=1
        
	                
def hacerDijkstra(ciudadOrigen, ciudadDestino):
    if ciudadOrigen != None and ciudadDestino != None:
            global grafo 
            print(ciudadOrigen, ciudadDestino)
            i =0
            aux = None
            for item in grafo.vertices:
                if ciudadDestino == i:
                    aux = item 
                    break
                i+=1
            i=0
            for item in grafo.vertices:
                if ciudadOrigen == i:
                    eliminarRepetidos(grafo.vertices[item].vecinos)
                    grafo.dijkstra(item)
                    print(item, aux)
                    respuesta= grafo.camino(item,aux)
                    respuesta2 = grafo.camino('ADZ', 'BGA')
                    print(respuesta, respuesta2)
                    return respuesta 
                i+=1

def unirPuntos(lista):
    for i in range(len(lista[0])-1):
        tupla = buscarVertice(lista[0][i])
        tupla2 = buscarVertice(lista[0][i+1])
        pygame.draw.line(SCREEN, "black", tupla, tupla2, width=5)

def buscarVertice(elemento):
    tupla = ()
    for item in grafo.vertices:
        if elemento == item:
            tupla = (grafo.vertices[item].x+10, grafo.vertices[item].y+50)
            return tupla 
                   

        #san andres
      #  dibujarPuntico(250,110)
        #armenia 
      #  dibujarPuntico(395,285)
        #barranquilla 
      #  dibujarPuntico(450,110)
        #bucaramanga
      #  dibujarPuntico(470,230)
        #bogota
      #  dibujarPuntico(450,290)
        #cali
      #  dibujarPuntico(370,310)
        #cartagena
      #  dibujarPuntico(410,120)
        #cucuta 
      #  dibujarPuntico(495,170)
        #leticia 
      #  dibujarPuntico(590,520)
        # medellin
     #   dibujarPuntico(420,210)
        #monteria
       # dibujarPuntico(390,160)
        #neira replace to neiva 
        #dibujarPuntico(400,270)
        #pereira 
       # dibujarPuntico(390,270)
        #pasto
       # dibujarPuntico(330,380)
        #rioacha
       # dibujarPuntico(500,90)
        # santamarta 
       # dibujarPuntico(450,110)
        #valledupar
      #  dibujarPuntico(480,140)
        #villavicencio
      #  dibujarPuntico(500,310)
    
def eliminarRepetidos(lista):
    for item in lista:
        for item2 in lista:
            if item [0] == item2[0]:
                lista.remove(item2)

fuenteGrande =font.SysFont('Roboto' ,100)
def dibujarPuntico(x,y):
    puntico=fuenteGrande.render(".", 0, "red")
    SCREEN.blit(puntico,(x,y))

#PILAS 
def revisarCarta(pila,cartica):
    #va a devolver un booleano
    cartaEvaluar = pila.cabeza 
    if cartaEvaluar.valor.jerarquia > cartica.jerarquia:
        return True

def mostrarGano(banderaGano):
    if banderaGano:
        fuente = pygame.font.Font(None, 50)
        texto_gano = fuente.render ("FELICIDADES, GANASTE ", 0, (255,255,255))
        SCREEN.blit(texto_gano, [ 300,300] )


def generarPilas(bandera):
    if bandera:
        for pila in pilas:
            draw.rect(SCREEN, "black", pila.rect, 0)
        for pila in pilas:
            carta = pila.cola
            while carta != None:
                SCREEN.blit(carta.valor.imagen, (carta.valor.x, carta.valor.y))
                carta = carta.nodo_anterior 
    
def mostrarConexiones():
    for item in grafo.vertices:
        vecinos = grafo.vertices[item].vecinos
        for i in range(len(vecinos)-1):
            tupla = buscarVertice(vecinos[i][0])
            tupla2 = buscarVertice(vecinos[i+1][0])
            pygame.draw.line(SCREEN, "black", tupla, tupla2, width=1)

#ARBOLES 

def generate_tree (a):
    if banderaArbol:
        fuente = pygame.font.Font(None, 30)
        texto_cant_nodos = fuente.render ("cantidad de nodos: ", 0, (200, 60,80))
        texto_max_nodos= fuente.render ("cantidad maxima de nodos: 15",0, (200, 60,80))
        SCREEN.blit (texto_max_nodos,[650,150])
        SCREEN.blit(texto_cant_nodos,  [ 100,150])
        cantidad = fuente.render(f'{a:01d}',0, (200, 60, 80) )
        SCREEN.blit(cantidad,  [ 300,150])
        texto_valor_nodo = fuente.render ("Ingrese los valores del arbol, separados por comas ", 0, (200, 60,80))
        SCREEN.blit(texto_valor_nodo, [ 100,200] )
        draw_button(SCREEN, añadir, "crear")
        manager.draw_ui(SCREEN)
        dropRecorridos.active = True 
        dropRecorridos.draw(SCREEN,dropRecorridos.active)
        mostrarRecorrido(opcion)
    if banderaAñadir and banderaArbol:
        if arbol.length != None:
            estructuraArbol(arbol.length)
        
def crearArbol(texto):
    arboles = texto.split(',')
    for item in arboles:
        if item.isdigit():
            arbol.insert(item)
        else:
            return False 
    return True 
        
def estructuraArbol (numero):
    #colocar que se pueden tener maximo 15 nodos 
    global a
    lista = arbol.breadth_first_search()
    niveles = arbol.levels()
    lista2 =[]
    for item in lista:
        if item != None:
            lista2.append(item)
    
    eliminarUltimosNone(lista)
    print(lista)
    print(lista2)
    a = len(lista2)
    for item in lista:
        nodosDibujar.append(miFuente.render(item, 0, (200,60,80)))
    for i in range(len(lista)):
        listaCirculos =[(100,320), (0,400), (200,400), (-50,480),(25,480),(150,480),(250,480),(-100,560),(50,560),(-25,560),(25,560),(75,560),(130,560),(250,560),(400,560) ]
        print(i)
        
        if lista[i] != None:
            dibujarNodo(listaCirculos[i][0], listaCirculos[i][1])
            SCREEN.blit (nodosDibujar[i], (listaCirculos[i][0]+300, listaCirculos[i][1]))
            
def eliminarUltimosNone(lista):
    item = lista[len(lista)-1] 
    while item == None:
        lista.pop()
        item = lista[len(lista)-1]
opcion = -1 
def mostrarRecorrido(opcion):
    recorridos = Rect (300,50,650,50)
    if opcion == -1:
        draw_button(SCREEN, recorridos,"")
    if arbol != None:
        if opcion == 0:
            Str = " ".join(arbol.postorder())
            draw_button(SCREEN, recorridos, Str)
        if opcion == 1:
            Str = " ".join(arbol.inorder())
            draw_button(SCREEN, recorridos, Str)
        if opcion == 2:
            Str = " ".join(arbol.amplitud())
            draw_button(SCREEN, recorridos, Str)
        if opcion == 3:
            Str = " ".join(arbol.preorder())
            draw_button(SCREEN, recorridos, Str)

def dibujarCarta(bandera, cartica):
    if cartica != None and bandera== False :
        cartica.x, cartica.y = mouse.get_pos()
        SCREEN.blit(cartica.imagen, (cartica.x, cartica.y))

def dibujarNodo(i, j):
    pygame.draw.circle (SCREEN, "white", (i+dimension+(radio/2),j+(radio/2)),radio, 5)
textocambio = ""



#INTERFAZ 
def dibujar(button, word):
    draw.rect(SCREEN, (70, 189, 34), button, 0)
    text= myFont.render(word, True, "black")
    SCREEN.blit(text, (button.x +(button.width-text.get_width())/2,
                button.y + (button.height - text.get_height())/2))
def draw_button(screen, button, word):
    if button.collidepoint(mouse.get_pos()):
        draw.rect(screen, (237, 128, 19), button, 0)
    else:
        draw.rect(screen, (70, 189, 34), button, 0)
    text= myFont.render(word, True, "black")
    screen.blit(text, (button.x +(button.width-text.get_width())/2,
                 button.y + (button.height - text.get_height())/2))
banderaGano = False 
seleccion = True
cartica = None
tengoCarta =False
banderaArbol = False 
banderaGrafos = False 
ci1= None
ci2 = None
banderaConecciones = False 
ciudadOrigen = None
ciudadDestino = None
listaGrafos = None 
while True:
    SCREEN.fill("black")
    eventos = event.get()
    for e in eventos:
        UI_REFRESH_RATE = clock.tick(60)/1000
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        if (e.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                e.ui_object_id == '#valornodo' and banderaArbol):
                    textonodo = e.text
        manager.process_events(e)
        if (e.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                e.ui_object_id == '#inputcambio' and banderaGrafos):
                    textocambio = e.text
        else:
            textocambio =""
        manager2.process_events(e)
        
        if e.type== MOUSEBUTTONDOWN and e.button== 1:
            if arboles.collidepoint(mouse.get_pos()):
                bandera =False
                banderaArbol=True
                banderaGano= False 
                banderaGrafos = False 
            if banderaArbol and añadir.collidepoint(mouse.get_pos()):
                if crearArbol(textonodo):
                    banderaAñadir = True 
                else:
                    print('error')
            if nuevoNodo.collidepoint(mouse.get_pos()):
                text_input.enable()
            if grafos.collidepoint(mouse.get_pos()):
                print("raro ")
                banderaGrafos = True
                banderaArbol = False
                bandera= False 
            if banderaGrafos:
                    if verConnecciones.collidepoint(mouse.get_pos()):
                        banderaConecciones = True 
                    banderaArbol = False
                    dd.active = True
                    ddestino.active = True
                    ciudad1.active= True
                    ciudad2.active= True 
                    selected_option = dd.update(eventos)
                    destino =ddestino.update(eventos)
                    ci1= ciudad1.update(eventos)
                    ci2= ciudad2.update(eventos)
                    if selected_option >= 0:
                        dd.main = dd.options[selected_option]
                        ciudadOrigen = selected_option
                    if destino >= 0:
                        ddestino.main = ddestino.options[destino]
                        ciudadDestino = destino
                        if ciudadOrigen != None and ciudadOrigen != -1:
                            listaGrafos =hacerDijkstra(ciudadOrigen, ciudadDestino)
                        destino = -1
                        ciudadOrigen = -1
                    if ci1 >= 0:
                        ciudad1.main = ciudad1.options[ci1]
                        primeraCiudad= ci1
                    if ci2 >= 0:
                        ciudad2.main = ciudad2.options[ci2]
                        print("ci2 jksdjfk"+str(ci2))
                        segundaCiudad= ci2
            if banderaArbol:
                    dd.active = False
                    ddestino.active = False
                    selected_option = dropRecorridos.update(eventos)
                    if selected_option >= 0:
                        dropRecorridos.main = dropRecorridos.options[selected_option]
                        opcion = selected_option
                    ciudad1.active = False
                    ciudad2.active= False 
            if bandera:
                    dd.active = False
                    ddestino.active = False
                    ciudad1.active = False
                    ciudad2.active = False 
                    dropRecorridos.active = False 
                    banderaArbol= False 
                    for pila in pilas:
                            if pila.rect.collidepoint(mouse.get_pos()) :
                                if seleccion:
                                    cartica =pila.pop()
                                    seleccion = False
                                    tengoCarta= True 
                                    break
                                else:
                                    if cartica != None and pila.cabeza != None :
                                        if revisarCarta(pila,cartica):
                                            pila.push(cartica)
                                            if pila.tamaño>= 13:
                                                banderaGano= True 
                                            cartica = None 
                                            seleccion = True 
                                            break
                                        else:
                                            print('no puede')
                                            break 
            if pila1.collidepoint(mouse.get_pos()):
                bandera=True
                banderaArbol= False
                
             
    generateGraphs(banderaGrafos,textocambio, banderaConecciones)
    generate_tree(a)
    generarPilas(bandera)
    dd.draw(SCREEN, dd.active)   
    ddestino.draw(SCREEN, ddestino.active)
    ciudad1.draw(SCREEN, ciudad1.active)
    ciudad2.draw(SCREEN, ciudad2.active)
    dibujarCarta(seleccion, cartica )  
    mostrarGano(banderaGano)   
    manager.update(UI_REFRESH_RATE)   
    manager2.update(UI_REFRESH_RATE)                         
    draw_button(SCREEN, pila1, "pilas")
    draw_button(SCREEN, arboles, "arboles")
    draw_button(SCREEN, grafos, "grafos")
    
   
    display.update()
    


#24,23,12,1,56
#23,12,15,24,50
#23,12,25,46
#50,56,54,57,45,44,46