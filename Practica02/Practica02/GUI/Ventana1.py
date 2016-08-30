from Tkinter import * 
import sys
import threading
import thread
import time

sys.path.append('/root/Desktop/Redes/practica2/Principal')
from Main import Plantica

class Ventana:
    def hacer_click():
        
    def mostrar(self,ventana):
        ventana.deiconify()

    def ocultar(ventana):
        ventana.withdraw()

    def ejecutar(self,f):
        ventanaInicio.affter(200,f)
                
    #def aceptar(self):
        #botonIngresar=Button(self.ventanaInicio,text="Acceder",command=lambda:
        #self.puertos(self.textoentry_1,self.miPuerto)).pack()
        ##botonIngresar.pack()
    
    def puertos(self,texto,StringVar1,texto1,StringVar2,ventanaInicio):
        #StringVar1.set(texto)
        #StringVar2.set(texto1)
        z=Plantica()
        z.algo(int(texto),int(texto1))
      
        z.Con
        ventanaChat = Toplevel(self.ventanaInicio)
        ventanaChat.protocol("WM_DELETE_WINDOW", "onexit")
        
        ventanaChat.resizable(0,0)
        
        scrollbar = Scrollbar(ventanaChat)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        ventanaChat.geometry("300x500")
        
        self.ejecutar(self.mostrar(ventanaInicio))  
        
        comentario = Listbox(ventanaChat)
        comentario.pack()
        miTexto = StringVar()
        e1 = Entry(ventanaChat, textvar = miTexto).pack()
        
        comentario.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=comentario.yview)
        
        ventanaChat.withdraw()
        
        

        from Tkinter import *
import sys
import threading
import thread
import time

sys.path.append('C:\Users\Aaron\practica2\Principal')
from Main import Plantica

ventanaInicio = Tk()
ventanaChat = Toplevel(ventanaInicio)
ventanaChat.protocol("WM_DELETE_WINDOW", "onexit")

# Evita que la ventana se pueda cambiar de tamaño
ventanaInicio.resizable(0,0)
ventanaChat.resizable(0,0)

# Scrollbar
scrollbar = Scrollbar(ventanaChat)
scrollbar.pack(side=RIGHT, fill=Y)

    def puertos(self,texto,StringVar1,texto1,StringVar2,ventanaInicio):

        z=Plantica()
        z.algo(int(texto),int(texto1))
      
        z.Con
        ventanaChat = Toplevel(self.ventanaInicio)
        ventanaChat.protocol("WM_DELETE_WINDOW", "onexit")
        
        ventanaChat.resizable(0,0)
        
        scrollbar = Scrollbar(ventanaChat)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        ventanaChat.geometry("300x500")
        
        self.ejecutar(self.mostrar(ventanaInicio))  
        
        comentario = Listbox(ventanaChat)
        comentario.pack()
        miTexto = StringVar()
        e1 = Entry(ventanaChat, textvar = miTexto).pack()
        
        comentario.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=comentario.yview)
        
        ventanaChat.withdraw()

    def mostrar(self,ventana):
        ventana.deiconify()

    def ocultar(ventana):
        ventana.withdraw()

    def ejecutar(self,f):
        ventanaInicio.affter(200,f)

# Inserta en los comentarios
def insertar_comentario():
    if miTexto.get() != "":
        comentario.insert(END,miTexto.get())
        comentario.insert(END,"RESPUESTA")
    else:
        w = Message(ventanaChat, text= "Escribe algo" ).pack()

# Cambia el tamaño de la ventana
ventanaInicio.geometry("400x200")
ventanaChat.geometry("300x500")


# VENTANA LOGIN
# declaramos Variable
miPuerto=StringVar()
textoentry_1=StringVar()
puertoContacto=StringVar()
textoentry_2=StringVar()
# Etiqueta 1
LabelMiPuerto = Label(ventanaInicio, text="Cual es mi puerto?").pack()
# Guardamos el puerto
entry1=Entry(ventanaInicio,textvar=textoentry_1).pack()
label1=Label(ventanaInicio,textvar=LabelMiPuerto).pack()
# Etiqueta 2
LabelMiPuerto = Label(ventanaInicio, text="Cuál es el puerto del contacto?").pack()
# Guardamos el puerto

entry1=Entry(ventanaInicio,textvar=textoentry_2).pack()
label1=Label(ventanaInicio,textvar=puertoContacto).pack()

# Creamos el boton de ingresar
botonIngresar=Button(ventanaInicio,text="Acceder",command=lambda:ejecutar(mostrar(ventanaChat)))
botonIngresar.pack()





# VENTANA CHAT
comentario = Listbox(ventanaChat)
comentario.pack()
miTexto = StringVar()
e1 = Entry(ventanaChat, textvar = miTexto).pack()

comentario.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=comentario.yview)

# Creamos el boton de Responde
botonResponde=Button(ventanaChat,text="Responde", command = insertar_comentario)
botonResponde.pack()


# oculta la ventada de chat
ventanaChat.withdraw()
# inicializar 
ventanaInicio.mainloop()

    def LoginV(self):
        self.ventanaInicio = Tk()
        self.ventanaInicio.resizable(0,0)
        self.ventanaInicio.geometry("400x200")
        
        self.miPuerto=StringVar()
        self.textoentry_1=StringVar()
        
        self.puertoContacto=StringVar()
        self.textoentry_2=StringVar()
        
        self.LabelMiPuerto = Label(self.ventanaInicio, text="Cual es mi puerto?").pack()
        
        self.entry1=Entry(self.ventanaInicio,textvar=self.textoentry_1).pack()
        self.label1=Label(self.ventanaInicio,textvar=self.miPuerto).pack()

        self.LabelMiPuerto = Label(self.ventanaInicio, text="Cual es el puerto del contacto?").pack()

        self.entry2=Entry(self.ventanaInicio,textvar=self.textoentry_2).pack()
        self.label2=Label(self.ventanaInicio,textvar=self.puertoContacto).pack()
        
        
        botonIngresar=Button(self.ventanaInicio,text="Acceder",command=lambda:
                                 command=hacer_click).pack()
        self.puertos(self.textoentry_1.get(),self.miPuerto,self.textoentry_2.get(),self.puertoContacto,self.ventanaInicio)).pack()
        
        
        self.ventanaInicio.mainloop()
        
    #def ChatV(self,ventanaInicio):
        
    def insertar_comentario():
        if miTexto.get() != "":
            comentario.insert(END,miTexto.get())
            comentario.insert(END,"RESPUESTA")
        else:
            w = Message(ventanaChat, text= "Escribe algo" ).pack()
                
z=Ventana()
z.LoginV()
#z.ChatV()
