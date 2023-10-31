import sqlite3
import tkinter as tk
from tkinter import messagebox

# Defino una función para crear la tabla "jugadores" si no existe
def crearTablaJugadores():
    # Establezco una conexión con la base de datos (o la creo si no existe)
    conexionBD = sqlite3.connect('data/basquet.db')
    cursorDN = conexionBD.cursor()  # Creo un cursor para ejecutar comandos SQL

    # Especifico la sentencia SQL para crear la tabla "jugadores" con los campos: nombre, apellido, altura y edad
    tabla_jugadores = '''
    CREATE TABLE IF NOT EXISTS jugadores (
        nombre TEXT,
        apellido TEXT,
        altura REAL,
        edad INTEGER
    )
    '''

    cursorDN.execute(tabla_jugadores)  # Ejecuto la sentencia SQL
    conexionBD.commit()  # Guardo los cambios en la base de datos
    conexionBD.close()  # Cierro la conexión con la base de datos

# Defino una función para insertar datos en la tabla
def insertarDatos():
    # Establezco una conexión con la base de datos
    conexionBD = sqlite3.connect('data/basquet.db')
    cursorDN = conexionBD.cursor()  # Creo un cursor para ejecutar comandos SQL

    # Obtengo los datos ingresados
    nombre = entryNombre.get()
    apellido = entryApellido.get()
    altura = entryAltura.get()
    edad = entryEdad.get()

    # Ejecuto una sentencia SQL para insertar datos en la tabla "jugadores"
    cursorDN.execute('INSERT INTO jugadores (nombre, apellido, altura, edad) VALUES (?, ?, ?, ?)',
                     (nombre, apellido, altura, edad))

    conexionBD.commit()  # Guardo los cambios en la base de datos
    conexionBD.close()  # Cierro la conexión

    # Limpio los campos de entrada después de la inserción
    entryNombre.delete(0, tk.END)
    entryApellido.delete(0, tk.END)
    entryAltura.delete(0, tk.END)
    entryEdad.delete(0, tk.END)
    messagebox.showinfo('Éxito', 'Los datos se han insertado correctamente.')

# Creo la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title('Inserción de Datos')

# Creo los elementos de la interfaz gráfica
labelNombre = tk.Label(ventana, text='Nombre:')
entryNombre = tk.Entry(ventana)

labelApellido = tk.Label(ventana, text='Apellido:')
entryApellido = tk.Entry(ventana)

labelAltura = tk.Label(ventana, text='Altura:')
entryAltura = tk.Entry(ventana)

labelEdad = tk.Label(ventana, text='Edad:')
entryEdad = tk.Entry(ventana)

botonInsertar = tk.Button(ventana, text='Insertar Datos', command=insertarDatos)  # Creo el botón

# Coloco los elementos en la ventana con una cuadrícula
labelNombre.grid(row=0, column=0)
entryNombre.grid(row=0, column=1)

labelApellido.grid(row=1, column=0)
entryApellido.grid(row=1, column=1)

labelAltura.grid(row=2, column=0)
entryAltura.grid(row=2, column=1)

labelEdad.grid(row=3, column=0)
entryEdad.grid(row=3, column=1)

botonInsertar.grid(row=4, column=0, columnspan=2)  # El botón ocupa dos columnas

crearTablaJugadores()

ventana.mainloop()
