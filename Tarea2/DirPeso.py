from random import random
from math import sqrt, ceil

def punto(x1,y1):
    return(((x1[0] + y1[0])/2), ((x1[1] + y1[1])/2)+.005)

class Grafo:

    def __init__(self):
        self.nodos = []
        self.aristas= []
        self.dis = []
        self.dismin = []
        self.peso = []
        self.vector = []

    def agrega(self, n):
        with open("DirPesoNodos.dat", "w") as crear:
            for t in range(n):
                x=random()
                y=random()
                self.nodos.append((x,y))
                print (x,y,file=crear)

    def distancia(self):
        for (x1,y1) in self.nodos:
            for (x2,y2) in self.nodos:
                d=sqrt(((y2-y1)**2)+((x2-x1)**2))
                if d==0:
                    self.dis.append(d)
                else:
                    if d in self.dis:
                        self.dis.append(20)
                    else:
                        self.dis.append(d)

    def conecta(self):
        for (x1,y1) in self.nodos:
            self.dismin=[]
            for(x2,y2) in self.nodos:
                dm=sqrt(((y2-y1)**2)+((x2-x1)**2))
                if dm==0:
                    self.dismin.append(20)
                else:
                    if dm in self.dismin:
                        self.dismin.append(20)
                    else:
                        self.dismin.append(dm)
            if min(self.dismin) in self.dis:
                a1=self.nodos[self.dismin.index(min(self.dismin))][0]
                b1=self.nodos[self.dismin.index(min(self.dismin))][1]
                self.aristas.append((x1,y1,a1,b1))
                self.peso.append(ceil(random()*10))
                self.vector.append(punto((x1,y1),(a1,b1)))
                self.dis.remove(min(self.dismin))
        

    def graficar(self, di, pesos):
        with open("DirPeso.plot","w") as archivo:
             print("set term eps", file=archivo)
             print("set output 'DirPeso.eps'", file=archivo)
             print("set xrange [0:1]", file=archivo)
             print("set yrange [0:1]", file=archivo)
             print("set pointsize 1.5", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num=0
             for a in self.aristas:
                 (x1,y1,x2,y2)=a
                 if di is 1:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 else:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead filled lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 if pesos is 1:
                    p = self.peso[num]
                    (kp, rp) = self.vector[num]
                    print("set label font ',10' '{:d}' at {:f},{:f} tc rgb 'brown'".format(p, kp, rp),file = archivo)
                 num+=1
             print("show arrow", file=archivo)
             print("plot 'DirPesoNodos.dat' using 1:2 with points pt 7 lc 6", file=archivo)
             print("quit()",file=archivo)

             

i=10 #Cantidad de nodos que va a tener el grafo
G = Grafo()
G.agrega(i)
G.distancia()
G.conecta()
G.graficar(di=1, pesos=1) #Si di=0 el grafo va a ser sin direccion, si es 1 es dirigido
                          #Si pesos=0 el grafo no tendra ponderacion, si es 1 si lo tendra
