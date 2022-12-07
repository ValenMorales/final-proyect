
class Carta():
    def __init__(self, imagen, x,y, jerarquia):
        self.imagen= imagen
        self.rect= imagen.get_rect()
        self.x= x
        self.y =y
        self.jerarquia = jerarquia


    