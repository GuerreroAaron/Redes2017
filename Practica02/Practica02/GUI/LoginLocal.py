# Importa el modulo
from Tkinter import * 
# Creamos las ventanas
ventanaInicio = Tk()
# Evita que la ventana se pueda cambiar de tamano
ventanaInicio.resizable(0,0)
# Muestra una ventana
def mostrar(ventana):
    ventana.deiconify()
# Oculta una ventana
def ocultar(ventana):
    ventana.withdraw()
# Una forma de ejecutar las funciones
def ejecutar(f):
    ventanaInicio.affter(200,f)


# Cambia el tamano de la ventana
ventanaInicio.geometry("400x200")

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
LabelMiPuerto = Label(ventanaInicio, text="Cual es el puerto del contacto?").pack()
# Guardamos el puerto
entry1=Entry(ventanaInicio,textvar=textoentry_2).pack()
label1=Label(ventanaInicio,textvar=puertoContacto).pack()
# Creamos el boton de ingresar
botonIngresar=Button(ventanaInicio,text="Acceder",command=lambda:
ejecutar(mostrar(ventanaChat)))
botonIngresar.pack()


# inicializar 
)


