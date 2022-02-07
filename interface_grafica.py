from distutils import command
from tarfile import PAX_FIELDS
from tkinter import *
from matplotlib import image

# importamos toda la libreria, todas las clases de tkinter

root = Tk() # creamos la raiz instancia de la clase Tk

# metodo title para cambiar el titulo de la ventana
root.title("Ventana uno")

# booleano width (ancho), height(alto)
# 0 es False, no se puede redimensionar la ventana
'''root.resizable(0,0)'''

# size de la ventana seteado
'''root.geometry("650x350")'''

# color de fondo
'''root.config(bg="orange")'''

# imagen .ico para icono de la ventana
root.iconbitmap("study.ico")

# cuando se ejecuta desde windows ejecuta la consola tambien,
# si se cambia la extension a pyw, ya no lo ejecuta al cmd

# creamos el frame
myFrame = Frame(root, width=650, height=350)

# le damos color al fondo pero no se ve hasta que no redimensionamos el mismo
'''myFrame.config(bg="blue")'''

# redimension del frame
'''myFrame.config(width="650", height="350")'''

# empaquetamos el Frame creado
myFrame.pack()

# caracteristicas del borde: groove, sunken
'''myFrame.config(relief="sunken")'''

# cambiar cursor
'''myFrame.config(cursor="hand2")'''

# tamaño el borde
'''myFrame.config(bd=35)'''

## WIDGETS ##

# Entry: cuadros para insertar texto
'''textInsert = Entry(myFrame)
textInsert.place(x=100, y=100)'''

# para crear un campo con nombre y caja de texto
# primer poner el inputText y luego la Label
'''nombreLabel = Label(myFrame, text="Nombre: ").place(x=100, y=100)'''

# Se aconseja trabajar con el metodo grid() para evitar problemas de coordenadas
# divide nuestra interfaz grafica en una grilla para poder colocar los elementos
# Este metodo usa dos datos: row y column
# Con grid pasa lo mismo que con pack, no respeta las dimensiones dadas
# cuando creamos el frame

# Sticky coloca las labels segun coordenadas: n, s, e, w, ne, nw, se, sw.
# Pady (vertical), Padx (horizontal) es espacio de separacion

# creo una variable con la que voy a cambiar el texto del textInsert1 por medio de la funcion funcionBoton
nombre = StringVar()

nombreLabel = Label(myFrame, text="Nombre: ", bg="gray").grid(row=0, column=0, sticky="e", pady=6, padx=6)
textInsert1 = Entry(myFrame,textvariable=nombre) # le asigno la variable nombre al Entry

textInsert1.grid(row=0, column=1)
textInsert1.config(fg="blue", justify="center")

apellidoLabel = Label(myFrame, text="Apellido: ", bg="gray").grid(row=1, column=0, sticky="w", pady=6, padx=6)
textInsert2 = Entry(myFrame)
textInsert2.grid(row=1, column=1)

direccionLabel = Label(myFrame, text="Dirección: ", bg="gray").grid(row=2, column=0, pady=6, padx=6)
textInsert3 = Entry(myFrame)
textInsert3.grid(row=2, column=1)

passLabel = Label(myFrame, text="Password: ", bg="gray").grid(row=3, column=0, pady=6, padx=6)
textInsert4 = Entry(myFrame)
textInsert4.grid(row=3, column=1)
textInsert4.config(show="*")
# con show se muestra un caracter a la hora de escribir en el campo de texto


# Text: introducir texto largo

comentariosLabel = Label(myFrame, text="Comentarios: ", bg="gray").grid(row=4, column=0, pady=6, padx=6)
textInsert5 = Text(myFrame, width=16, height=5)
textInsert5.grid(row=4, column=1, padx=6, pady=6)
# hay que redimensionar el Text porque por default es muy grande
# esto se hace con width y height

# Podemos crear una scrollbar para agregar al Text
# declaramos un objeto de tipo scrollbar y le indicamos donde se va a encontrar
# luego con command le decimos a quien pertenece, en este caso a nuestro Text
# y le decimos que va a ser la vista de scroll para la coordenada y

scrollV= Scrollbar(myFrame,command=textInsert5.yview)

# luego se coloca el scrollbar utilizando el grid

scrollV.grid(row=4, column=2,sticky="ns",)
# con sticky, el tamaño de la scrollbar se adapta al Text

# para agregarle el posicionamiento correcto al Text le agregamos config
# con el seteo de la scrollbar

textInsert5.config(yscrollcommand=scrollV.set)


# Label: es texto estatico, no se puede modificar
# variableLabel = Label(contenedor, opciones)
# algunas opciones: Text, Anchor, Bg, Bitmap, Bd, Font, Fg (color de fuente), Width, Height, Image, justify.
'''myLabel = Label(myFrame, text="Hello World")'''

# meter el frame dentro de la raiz, empaquetarlo
# Packer Options
# Podemos indicar donde se va a colocar el frame dentro de la raiz con el parametro side,
# pasandole por parametro le direccion: right, left, top, bottom
'''myFrame.pack(fill="both", expand="True")'''

# Otro parametro es anchor, que maneja puntos cardinales (n, s, e, w), si o agreamos a side,
# podemos ubicar el frame en algun vertice
'''myFrame.pack(side="top", anchor="e")'''

# otra opcion es el metodo de rellenado o fill
# puede rellenar x, y (para y hay que agregar expand = "True")
# para rellenar en ambas direcciones debemos poner fill = "both" y expand = "True"
'''myFrame.pack(fill="x")'''

# empaquetamos la Label creada
# Cuando se usa el pack con el Label, adapta el tamaño del contenedor al tamaño del Label
'''myLabel.pack()'''

# Para evitar que tome el tamaño de la Label, usamos place (coordenadas x e y)
'''myLabel.place(x=100, y=200)'''

# Si no vamos a volver a usar la variable myLabel, podemos avreviar todo asi
# Usar con Texto
'''Label(myFrame, text="Hello World", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)'''

# para insertar una foto usamos la clase PjotoImage
myImage = PhotoImage(file="favicon.png") # imagen sola
Label(myFrame, image=myImage).grid(rowspan=4, row=0,column=2)
# con rowspan coloco la foto para que ocupe todas las rows que coloque hasta ahora

# Button: botones, en este caso colocamos el boton en el root
# la funcion funcionBoton
def funcionBoton():
    nombre.set("Belen") # set o get

botonUpdate = Button(root, text="Nombre", command=funcionBoton)
botonUpdate.pack()

# Se pueden aplicar estilos del Frame en la Raiz tambien.
root.mainloop() # metodo mainloop para que se ejecute en bucle infinito