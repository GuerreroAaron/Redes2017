from Tkinter import *


ventanaInicio = Tk()
ventanaChat = Toplevel(ventanaInicio)
ventanaChat.protocol("WM_DELETE_WINDOW", "onexit")

# Evita que la ventana se pueda cambiar de tamanio
ventanaInicio.resizable(0,0)
ventanaChat.resizable(0,0)

# Scrollbar
scrollbar = Scrollbar(ventanaChat)
scrollbar.pack(side=RIGHT, fill=Y)

def mostrar(self,ventana):
    ventana.deiconify()

def ocultar(ventana):
    ventana.withdraw()

def ejecutar(self,f):
    ventanaInicio.affter(200,f)


# Inserta en los comentarios
def insertar_comentario(miComentario):
    if miComentario != "":
        comentario.insert(END,miComentario)
    else:
        w = Message(ventanaChat, text= "Escribe algo" ).pack()

# Cambia el tamanio de la ventana
ventanaInicio.geometry("400x200")
ventanaChat.geometry("300x500")


# VENTANA LOGIN
# declaramos Variable
miPuerto=StringVar()
textoentry_1=StringVar()
puertoContacto=StringVar()
textoentry_2=StringVar()

# Etiqueta 1
LabelMiPuerto = Label(ventanaInicio, text="Cual es mi puerto?")
LabelMiPuerto.pack()
entry1 = Entry(ventanaInicio,textvar=textoentry_1).pack()
label1 = Label(ventanaInicio,textvar=LabelMiPuerto).pack()

# Etiqueta 2
LabelPuertoContacto = Label(ventanaInicio, text="Cual es el puerto del contacto?")
LabelPuertoContacto.pack()

# Guardamos el puerto

entry2 = Entry(ventanaInicio,textvar=textoentry_2).pack()
label2 = Label(ventanaInicio,textvar=puertoContacto).pack()

# Creamos el boton de ingresar
botonIngresar=Button(ventanaInicio,text="Acceder",command=lambda:ejecutar(mostrar(ventanaChat)))
botonIngresar.pack()

# Creamos el boton de ocultar
botonOcultar=Button(ventanaInicio,text="Ocultar",command=lambda:ejecutar(ocultar(ventanaChat)))
botonOcultar.pack()





# VENTANA CHAT
comentario = Listbox(ventanaChat)
comentario.pack()
miTexto = StringVar()
e1 = Entry(ventanaChat, textvar = miTexto).pack()

comentario.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=comentario.yview)

# Creamos el boton de Responde
botonResponde=Button(ventanaChat,text="Responde", command = insertar_comentario(e1))
botonResponde.pack()


# oculta la ventada de chat
ventanaChat.withdraw()
# inicializar 
ventanaInicio.mainloop()
