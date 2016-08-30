import sys
import threading
import thread
import time

sys.path.append('/root/Desktop/Redes/practica2/server')
from c3 import Cliente
from s3 import FuncionS

class Corre:
    def __init__(self,puerto,mensaje):
        self.p=puerto
        self.m=mensaje
    
#servidor
    def Servi(self):
        print '----------------servidor'
        self.ser=FuncionS() 
        self.ser.abre(self.p)

#cliente
    def Cli(self):
        print '----------------cliente'
        c=Cliente()        
        c.crea(self.p,self.m)
        self.texto= c.respuesta()
        self.Pantalla(self.texto)
        

    def Pantalla(self,texto):
        
        print texto
        self.ser.cerrar()
        
class MisHilos:
    def Paquete(self,puerto,mensaje):
        x=Corre(puerto,mensaje)    
        
        #creo los hilos de servidor y cliente
        t1 = threading.Thread(target=x.Servi, args=())
        t = threading.Thread(target=x.Cli, args=())

        t1.start()
        time.sleep(1)
        t.start()
        
    
