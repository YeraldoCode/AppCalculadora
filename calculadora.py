import tkinter as tk 
from tkinter import messagebox

ventana = tk.Tk()

ventana.title("Calculadora")

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

#visor 
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 23),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=4,
                 justify='right'
                 )
visor.grid(row=0,
           column=0,
           columnspan=4
)



# Pantalla
ventana.mainloop()