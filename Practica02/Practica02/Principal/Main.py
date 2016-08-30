import sys
import threading
import thread
import time

sys.path.append('/root/Desktop/Redes/practica2/hilos')
from h1 import MisHilos


class Plantica:
    def algo(self,p,p1):
        print 'chat'
        self.puerto1=p
        self.puerto2=p1
        

    def Conversa(self,m):
        y=MisHilos()
        #m=raw_input('mensaje:')
        y.Paquete(int(self.puerto2),m)
        return m
    def Conversa1(self,m1):
        x=MisHilos()
        #m1=raw_input('mensaje1:')
        x.Paquete(int(self.puerto1),m1)
        return m1
#z=Plantica()
#z.Conversa()
#z.Conversa1()
