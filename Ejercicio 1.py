import tkinter as tk

# Defino una función que agrega un caracter al campo de entrada de texto.
def agregar_caracter(caracter):
    # Obtengo el texto actual en el campo de entrada.
    texto_actual = entrada_texto.get()

    # Si el texto es "0" y el caracter es un dígito y no hay un punto en el texto,
    # borro el "0" inicial.
    if texto_actual == "0" and caracter.isdigit() and '.' not in texto_actual:
        entrada_texto.delete(0, tk.END)

    # Inserto el caracter en el campo de entrada.
    entrada_texto.insert(tk.END, caracter)

# Defino una función que borra el último caracter en el campo de entrada.
def borrar_caracter():
    entrada_texto.delete(len(entrada_texto.get()) - 1)

# Defino una función que borra el texto en el campo de entrada.
def clear():
    entrada_texto.delete(0, tk.END)

# Defino una función que calcula el resultado de la expresión en el campo de entrada.
def calcular():
    try:
        expresion = entrada_texto.get()
        resultado = round(eval(expresion), 2)  # Evalúo la expresión y redondeo el resultado a 2 decimales.
        entrada_texto.delete(0, tk.END)  # Borro el contenido actual en el campo de entrada.
        entrada_texto.insert(tk.END, str(resultado))  # Inserto el resultado en el campo de entrada.
    except Exception as e:
        entrada_texto.delete(0, tk.END)  # En caso de error, borro el contenido actual.
        entrada_texto.insert(tk.END, 'Error')  # Muestro "Error" en el campo de entrada.

# Creo una ventana de Tkinter.
ventana = tk.Tk()
ventana.title('Calculadora')
ventana.geometry("750x750")  # Establezco el tamaño de la ventana

# Establezco un color de fondo amarillo
ventana.configure(bg="#FFFF99")

# Agrego una etiqueta para el título "Calculadora".
titulo_label = tk.Label(ventana, text="Calculadora", font=('Arial', 24), bg="#FFFF99", pady=10)
titulo_label.pack()

# Creo un campo de entrada de texto.
entrada_texto = tk.Entry(ventana, font=('Arial', 20))
entrada_texto.pack()

# Defino una lista de botones para la calculadora.
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', 'C'
]

fila = 0
columna = 0

frame = tk.Frame(ventana, bg="#FFFF99")  # Color de fondo amarillo suave
frame.pack()

# Creo los botones en la interfaz gráfica.
for boton in botones:
    if boton == '=':
        tk.Button(frame, text=boton, font=('Arial', 20), width=3, height=1, command=calcular).grid(row=fila, column=columna)
    elif boton == 'C':
        tk.Button(frame, text=boton, font=('Arial', 20), width=3, height=1, command=clear).grid(row=fila, column=columna)
    else:
        # Utilizo una función lambda para pasar el carácter al hacer clic en el botón.
        tk.Button(frame, text=boton, font=('Arial', 20), width=3, height=1,
                  command=lambda b=boton: agregar_caracter(b)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

ventana.mainloop()
