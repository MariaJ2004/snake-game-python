from turtle import *

posiciones = [(0, 0), (-20, 0), (-40, 0)]

up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.segmentos = []        # ← atributo real
        self.color = "white"       # ← atributo real
        self.shape = "square"      # ← atributo real
        self.crear_snake()
        self.move()
    def crear_snake(self):
        for pos in posiciones:
            self.agregar_segmento(pos)

    def agregar_segmento(self, pos):
        segmento = Turtle(shape=self.shape)
        segmento.color(self.color)
        segmento.penup()
        segmento.goto(pos)
        self.segmentos.append(segmento)

    def extend(self):
        self.agregar_segmento(self.segmentos[-1].position())

    def move(self):
        for i in range(len(self.segmentos)-1, 0, -1):
            new_x = self.segmentos[i-1].xcor()
            new_y = self.segmentos[i-1].ycor()
            self.segmentos[i].goto(new_x, new_y)
        self.segmentos[0].forward(20)
    def up(self):
        if self.segmentos[0].heading()!=down:
            self.segmentos[0].setheading(90)

    def down(self):
        if self.segmentos[0].heading()!=up:
            self.segmentos[0].setheading(270)
    def left(self):
        if self.segmentos[0].heading() != right:
            self.segmentos[0].setheading(180)
    def right(self):
        if self.segmentos[0].heading() != left:
            self.segmentos[0].setheading(0)

    def reset(self):
        for seg in self.segmentos:
            seg.goto(1000,1000)

        self.segmentos.clear()
        self.color = "white"  # ← atributo real
        self.shape = "square"  # ← atributo real
        self.crear_snake()
        self.move()


