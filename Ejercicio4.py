import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

imagenSeleccionada = None
imagenTk = None

def abrirImagen():
    global imagenSeleccionada, imagenTk
    carpetaOrigen = filedialog.askdirectory(initialdir=os.getcwd(), title='Seleccionar una carpeta de imágenes')

    if carpetaOrigen:
        archivos = os.listdir(carpetaOrigen)
        archivosImagen = [archivo for archivo in archivos if archivo.endswith('.jpg')]
        if not archivosImagen:
            etiquetaResultado.config(text='No se encontraron imágenes en la carpeta.')
            return

        imagenSeleccionada = os.path.join(carpetaOrigen, archivosImagen[0])
        ventanaSecundaria = tk.Toplevel()
        ventanaSecundaria.title('Imagen y ruta')

        etiquetaRuta = tk.Label(ventanaSecundaria, text=f'Ruta de la imagen:\n{imagenSeleccionada}', font=("Helvetica", 14))
        etiquetaRuta.pack()

        imagen = Image.open(imagenSeleccionada)
        imagen.thumbnail((300, 300))
        imagenTk = ImageTk.PhotoImage(imagen)
        etiquetaImagen = tk.Label(ventanaSecundaria, image=imagenTk)
        etiquetaImagen.image = imagenTk
        etiquetaImagen.pack()

        botonGuardar = tk.Button(ventanaSecundaria, text='Guardar', command=guardarImagen)
        botonGuardar.pack()

def guardarImagen():
    if imagenSeleccionada:
        archivoGuardado = filedialog.asksaveasfile(defaultextension='.jpg', filetypes=[('Archivos de imagen', '*.jpg')])
        if archivoGuardado:
            imagenOriginal = Image.open(imagenSeleccionada)
            imagenOriginal.save(archivoGuardado.name)
            archivoGuardado.close()
            etiquetaResultado.config(text='Imagen guardada correctamente.')

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title('Abrir Imagen')

frame = ttk.Frame(ventanaPrincipal, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

botonAbrir = ttk.Button(frame, text='Abrir Imagen', command=abrirImagen)
botonAbrir.grid(column=0, row=0, columnspan=2, pady=10)

etiquetaResultado = ttk.Label(frame, text='', font=("Helvetica", 14))
etiquetaResultado.grid(column=0, row=1, columnspan=2)

ventanaPrincipal.geometry("400x200")  # Ajusta el tamaño de la ventana principal
ventanaPrincipal.update_idletasks()  # Actualiza la ventana principal para centrarla
ventanaPrincipal.mainloop()
