import tkinter as tk 
from tkinter import messagebox


ventana = tk.Tk()

ventana.title("CalculadoraYera")

#logo de app
icono = tk.PhotoImage(file='logo.png')
ventana.iconphoto(True, icono)
 
#color de fondo
ventana.configure(bg="light blue")

# Configuración de 5 filas y 4 columnas
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

#visor_texto
visor_texto = tk.StringVar()

#visor
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 23),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=4,
                 justify='right',
                 bg='light gray',
                 )
visor.grid(row=0,
           column=0,
           columnspan=4,
           sticky='nsew'
)

# Información de la botonera
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), (',', 4, 2), ('+', 4, 3),
]

# Crear botones en la ventana (excepto el igual)
for (texto, fila, columna) in botones:
    tk.Button(ventana, 
              text=texto, padx=20,
                pady=20).grid(row=fila, 
                                column=columna,
                                sticky='nsew',)
#boton de igual 
tk.Button(ventana,
          text="=", padx=20,
          pady=20,
          font=('Helvetica', 30)).grid(row=5,
                column=0,
                columnspan=4,
                sticky='nsew')

# Pantalla
ventana.mainloop()
