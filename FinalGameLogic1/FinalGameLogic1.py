import random as rand
import os

class Player:
    def __init__(self,position,color):
        self.Position = position
        self.Color = color
        self.Mochila=[0,0,0,0,0]
    
    #La mochila esta ordenada de 1 a 6 segun el color de la gema(el numero de la gema)
    def AgregarGema(self,gem):
        self.Mochila[gem-1]+=1

    def ShowPlayerState(self):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Jugador color " + str(self.color)+":")
        print(Mochila)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


#El tablero debe ser de 6 x 12+4
#Hay 6 tipos de gemas y 12 de cada tipo, maximo 4 jugadores
def FillTablero(tab,numPlayer):
    LogGem=[0,0,0,0,0,0]
    arrP=['A','B','C','D']
    for x in range(6):
        t=[]
        for i in range(numPlayer):
            t.append(0)
        for y in range(12):            
            #Generador de gemas por fila (AGREGAR ALGORITMO DE COMPROBACION)
            gem=True
            while gem:
                g=rand.randint(1,6)
                if(LogGem[g-1]<12):
                    t.append(g)
                    LogGem[g-1]+=1
                    gem=False
        tab.append(t)

    #Generador de personajes
    for p in range(numPlayer):
        tab[1+p][p]=arrP[p]

    
def PlayerMovement(tab,PlayerTurn,move):
    msg = "El jugador " + str(PlayerTurn) + " se movio " + str(move)
    print(msg)

def PrintTab(tab):
    for x in tab:
        for y in x:
            print(y, end =" ")
        print()


#Los turnos de los jugadores se crean dentro de un arreglo de jugadores
def Game():
    GameLoop=True;
    
    tabMtx = []
    numPlayers=2
    FillTablero(tabMtx,numPlayers)
    mov=99

    arrPlayers = []
    for i in range(numPlayers):
        arrPlayers.append(Player(i+1,i))

    while GameLoop :
        PrintTab(tabMtx)
        while(mov!=0 and mov!=1 and mov!=2):
            mov=int(input("Ingrese el movimiento para el player 1 (0, close)(1, arriba)(2, abajo): "))
        if(mov==0):
            GameLoop=False
        else:
            #PlayerMovement(1,mov)
            mov=99

Game()