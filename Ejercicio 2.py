import os
import tkinter as tk
from PIL import ImageTk, Image

rutaDirectorio = "./imagenes"
listaImagenes = os.listdir(rutaDirectorio)

indiceActual = 0
photoImages = []
root = tk.Tk()
root.title("Visor de Imágenes")

root.configure(bg='#00CED1')

def mostrarImage():
    global indiceActual

    if hasattr(mostrarImage, "imagenFrame"):
        mostrarImage.imagenFrame.grid_forget()

    imagenPath = os.path.join(rutaDirectorio, listaImagenes[indiceActual])

    imagen = Image.open(imagenPath)
    photo = ImageTk.PhotoImage(imagen)
    photoImages.append(photo)

    mostrarImage.imagenFrame = tk.Frame(root, bg='#00CED1')  # Fondo azul turquesa
    mostrarImage.imagenFrame.grid(row=0, column=0, padx=10, pady=10)

    imagenLabel = tk.Label(mostrarImage.imagenFrame, image=photo)
    imagenLabel.grid(row=0, column=0, padx=10, pady=10)

    if indiceActual == 0:
        botonAnterior.config(state=tk.DISABLED)
    else:
        botonAnterior.config(state=tk.NORMAL)

    if indiceActual == len(listaImagenes) - 1:
        botonSiguiente.config(state=tk.DISABLED)
    else:
        botonSiguiente.config(state=tk.NORMAL)

    infoEtiqueta.config(text=f"Imagen {indiceActual + 1} de {len(listaImagenes)}")

def siguienteImagen():
    global indiceActual
    indiceActual += 1
    mostrarImage()

def imagenAnterior():
    global indiceActual
    indiceActual -= 1
    mostrarImage()

imagenFrame = tk.LabelFrame(root, text="Imagen", padx=10, pady=10)
imagenFrame.grid(row=0, column=0, padx=10, pady=10, rowspan=2, columnspan=3, sticky=tk.N+tk.E+tk.S+tk.W)

botonSiguiente = tk.Button(root, text="Siguiente Fotografía", command=siguienteImagen)
botonAnterior = tk.Button(root, text="Fotografía Anterior", command=imagenAnterior)
botonSalir = tk.Button(root, text="Salir", command=root.quit)

botonSiguiente.grid(row=1, column=1, padx=10, pady=10)
botonAnterior.grid(row=1, column=0, padx=10, pady=10)
botonSalir.grid(row=1, column=2, padx=10, pady=10)

infoEtiqueta = tk.Label(root, text="", bd=2, relief=tk.SUNKEN, anchor=tk.E)
infoEtiqueta.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)
infoEtiqueta.config(text=f"Imagen {indiceActual + 1} de {len(listaImagenes)}", anchor=tk.E)

mostrarImage()

root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("800x600")

root.mainloop()
