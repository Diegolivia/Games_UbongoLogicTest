import random as rand
import os

class Tablero:
    def __init__(self,numP):
        self.tabMtx = []
        self.numPlayer=numP
        self.arrP=['A','B','C','D']
        self.FillTablero()
        
    #El tablero debe ser de 6 x 12+4
    #Hay 6 tipos de gemas y 12 de cada tipo, maximo 4 jugadores
    def FillTablero(self):
        LogGem=[0,0,0,0,0,0]
        for x in range(6):
            t=[]
            #Genera las columnas para los jugadores
            for i in range(self.numPlayer):
                t.append(0)
            #Generador de gemas por fila (AGREGAR ALGORITMO DE COMPROBACION)
            prev=-1
            for y in range(12):               
                gem=True
                while gem:
                    g=rand.randint(1,6)
                    #if(LogGem[g-1]<12 and g!=prev): //No funciona aun//
                    if(LogGem[g-1]<12):
                        t.append(g)
                        LogGem[g-1]+=1
                        prev=g
                        gem=False
                        print("nice")
            self.tabMtx.append(t)
        #Generador de personajes
        for p in range(self.numPlayer):
            self.tabMtx[1+p][p]=self.arrP[p]

    #Dibujar el tablero
    def Dibujar(self):
        for x in self.tabMtx:
            for y in x:
                print(y, end =" ")
            print()

    #Mover al jugador actual, limpia la posicon actual y luego recoloca al jugador
    def MovePlayer(self,player,mov):
        self.tabMtx[player.Position][player.Turn]=0
        player.UpdatePosition(mov)
        self.tabMtx[player.Position][player.Turn]=self.arrP[player.Color]
        self.ComerPiezas(player)
    
    #Cada jugador come las dos primeras piezas de la posicon donde se encuentra
    def ComerPiezas(self,player):
        i=self.numPlayer
        while i<=10+self.numPlayer:
            if(self.tabMtx[player.Position][i]!=0):
                player.AgregarGema(self.tabMtx[player.Position][i])
                player.AgregarGema(self.tabMtx[player.Position][i+1])
                self.tabMtx[player.Position][i]=0
                self.tabMtx[player.Position][i+1]=0
                i=16
            else:
                i+=2
        pass

class Player:
    def __init__(self,turn,position,color):
        self.Turn = turn
        self.Position = position
        self.Color = color
        self.Mochila=[0,0,0,0,0,0]
    
    #La mochila esta ordenada de 1 a 6 segun el color de la gema(el numero de la gema)
    def AgregarGema(self,gem):
        self.Mochila[gem-1]+=1

    #Actualiza la posicion del jugador dentro del arreglo
    def UpdatePosition(self,mov):
        if(self.Position+mov<0 or self.Position+mov>5):
            pass
        else:
            self.Position+=mov

    def ShowPlayerState(self):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Jugador del Turno " + str(self.Turn)+":")
        print("Jugador Posicion " + str(self.Position)+":")
        print("Jugador color " + str(self.Color)+":")
        print("Jugador maximo " + str(self.MaximoGemas())+":")
        print(self.Mochila)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def MaximoGemas(self):
        max = 0;
        geM=0;
        for i in range(6):
            if(self.Mochila[i]>max):
                max=self.Mochila[i];
                geM=i;
        return [geM,max];


class AIPlayer(Player):
    def __init__(self, turn, position, color,diff):
        self.Difficulty = diff;
        self.Buscar=[0,0]
        Player.__init__(self,turn,position,color);

    def DefinirBusqueda(self):
        pass

    def DecidirMovimiento(self):
        pass

    def ShowPlayerState(self):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Jugador AI del Turno " + str(self.Turn)+":")
        print("Jugador AI Posicion " + str(self.Position)+":")
        print("Jugador AI color " + str(self.Color)+":")
        print("Jugador AI Buscara " + str(self.Buscar)+":")
        print("Jugador maximo " + str(self.MaximoGemas())+":")
        print(self.Mochila)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

#Los turnos de los jugadores se crean dentro de un arreglo de jugadores
def Game():
    #default values
    GameLoop=True;  
    numPlayers=69
    numAI=-69
    mov=99
    Turn=0
    #Preguntar por la cantidad de jugadores
    while numPlayers>4 or numPlayers<2:
        numPlayers = int(input("Ingrese el numero de jugadores: "));
    while numAI>numPlayers-1 or numAI<0:
        numAI = numPlayers-int(input("Ingrese el numero de humanos: "))
    #Crea el tablero con las gemas y los jugadores
    tab=Tablero(numPlayers)
    #Agregar los jugadores al sistema de turnos
    arrPlayers = []
    for i in range(numPlayers-numAI):
        arrPlayers.append(Player(i,i+1,i))
    for i in range(numAI):
        arrPlayers.append(AIPlayer(numPlayers-numAI+i,numPlayers-numAI+i+1,numPlayers-numAI+i,1))

    #Bucle del juego
    while GameLoop :
        #Imprimir tablero
        tab.Dibujar()
        for i in range(numPlayers):
            arrPlayers[i].ShowPlayerState();
            if(type(arrPlayers[i])==AIPlayer):
                print("Es un robot");
            else : 
                if(type(arrPlayers[i])==Player):
                    print("Es un manito");
        #Manejador de Turnos, turno final regresa al turno 0
        if(Turn==numPlayers):
            Turn=0

        #Movimiento de los jugadores
        while(mov!=0 and mov!=1 and mov!=-1):
            mov=int(input("Ingrese el movimiento para el player " + str(chr(65+Turn))+" (0, close)(1, abajo)(-1, arriba): "))
        if(mov==0):
            GameLoop=False
            break
        else:
            tab.MovePlayer(arrPlayers[Turn],mov)
            Turn+=1
            mov=99

Game()