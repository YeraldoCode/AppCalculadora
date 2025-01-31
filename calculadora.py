import tkinter as tk 
from tkinter import messagebox

#creacion de ventana principal
ventana = tk.Tk()
ventana.title("CalculadoraYera")

#logo de app
icono = tk.PhotoImage(file='logo.png')
ventana.iconphoto(True, icono)

#variable para almacenar el valor de la expresion
expresion = ""

#variable para almcenar el estado del visor 
resultado_mostrado = False


#funcion para actualizar la expresion en el cuadro de texto 
def pulsar_tecla(tecla):
    global expresion, resultado_mostrado
    #evaluar si se ha calculado y mostrado un resultado
    if resultado_mostrado:
    #evaluar si se presiono numero o punto 
        if tecla.isdigit() or tecla == ".":
             expresion = str(tecla)
        else:
            expresion += str(tecla)
        resultado_mostrado = False
    else:
        expresion += str(tecla)

    visor_texto.set(expresion)


#funcion para limpiar
def limpiar():
    global expresion
    global resultado_mostrado
    expresion = ""
    visor_texto.set(expresion)    
    resultado_mostrado = False

#funcion para evaluar la expresion y mostrar el resultado
def evaluar():
    global expresion, resultado_mostrado 
    try:
        resultado = eval(expresion)
        #verificar es un numero entero
        if resultado == int(resultado):
            resultado = int(resultado)
        visor_texto.set(str(resultado))
        expresion = str(resultado)
        resultado_mostrado = True
    
    except:
        visor_texto.set("Error")
        expresion = ""
        resultado_mostrado = False

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
                 borderwidth=2,
                 justify='right',
                 bg='light gray',
                 relief='sunken',
                 background="#e8f0fe"
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

#colores almacenados en variables
color_fondo_numero = "light blue"
color_fondo_operacion = "purple"
color_fondo_especial = "blue"
color_fondo_calcular = "#f0f0f0"
color_fondo_presionado = "#f0f0f0"
color_fondo_calcular_presionado = "#f0f0f0"
color_texto_numero = "#333333"
color_texto_especial = "#000000"

# Crear botones en la ventana (excepto el igual)
for (texto, fila, columna) in botones:
    if texto in ['/', '*', '-', '+']:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_operacion
        color_texto = color_texto_especial
    elif texto == 'C':
        comando = lambda x=texto: limpiar()
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial
    elif texto == ',':
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial
    else:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_numero
        color_texto = color_texto_numero




    tk.Button(ventana, 
                text=texto, 
                padx=20,
                pady=20,
                font=('Helvetica', 20, 'bold'),
                bg=color_fondo,
                fg=color_texto,
                activeforeground=color_texto_especial,
                activebackground=color_fondo_presionado,
                bd=1,
                relief="raised",
                command=comando
                ).grid(row=fila, 
                                column=columna,
                                sticky='nsew',
                                padx=2,
                                pady=2)
#boton de igual 
tk.Button(ventana,
          text="=", padx=20,
          pady=20,
          font=('Helvetica', 30),
          bg='light green',
          command=evaluar
          ).grid(row=5,
            
                column=0,
                columnspan=4,
                sticky='nsew')
# Pantalla
ventana.mainloop()
