import tkinter as tk
from tkinter import messagebox

# Defino tres funciones que mostrarán ventanas emergentes con diferentes opciones.
# Cada función recopila la respuesta del usuario y actualiza una etiqueta con el resultado.

def mostrarVentanaDePregunta():
    respuesta = messagebox.askquestion('Pregunta', '¿Quieres continuar?')
    etiquetaResultado.config(text=f'Has clicado {"Sí" if respuesta == "yes" else "No"}')

def mostrarVentanaOkCancel():
    respuesta = messagebox.askokcancel('Pregunta', '¿Estás seguro de que quieres hacer esto?')
    etiquetaResultado.config(text=f'Has clicado {"Sí" if respuesta else "No"}')

def mostrarVentanaYesNo():
    respuesta = messagebox.askyesno('Pregunta', '¿Estás de acuerdo?')
    etiquetaResultado.config(text=f'Has clicado {"Sí" if respuesta else "No"}')

# Creo una ventana principal de tkinter y le doy un título y dimensiones.
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title('Ventanas Emergentes')
ventanaPrincipal.geometry('400x200')

# Creo una etiqueta para mostrar el resultado de las ventanas emergentes.
etiquetaResultado = tk.Label(ventanaPrincipal, text="", pady=10)
etiquetaResultado.pack()

# Defino colores para la ventana y botones.
color_fondo = "lightblue"
color_boton = "lightgreen"

# Configuro los colores de la ventana principal.
ventanaPrincipal.configure(bg=color_fondo)

# Creo un marco para los botones con un espaciado de 10 píxeles.
marco_botones = tk.Frame(ventanaPrincipal, bg=color_fondo)
marco_botones.pack(pady=10)

# Creo tres botones, cada uno asociado a una función de ventana emergente.
botonPregunta = tk.Button(marco_botones, text='Pregunta', command=mostrarVentanaDePregunta, bg=color_boton)
botonOkCancel = tk.Button(marco_botones, text='OK/Cancelar', command=mostrarVentanaOkCancel, bg=color_boton)
botonYesNo = tk.Button(marco_botones, text='SI/NO', command=mostrarVentanaYesNo, bg=color_boton)

# Añado los botones en el marco y los pongo en el posicion que quiera.
botonPregunta.pack(side=tk.LEFT, padx=10)
botonOkCancel.pack(side=tk.LEFT, padx=10)
botonYesNo.pack(side=tk.LEFT)

ventanaPrincipal.mainloop()
