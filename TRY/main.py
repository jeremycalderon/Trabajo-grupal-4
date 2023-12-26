import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

import numpy as np
from numpy import pi, sin, cos, sqrt, arccos, arctan2

from calcular import calcular_resultados

# Función para actualizar el valor en los Label
def update_slider_value1(val):
    integer_val = int(float(val))
    value_label1.config(text=f"{integer_val} °")
    return(integer_val)

def update_slider_value2(val):
    integer_val = int(float(val))
    value_label2.config(text=f"{integer_val} °")
    return(integer_val)

def update_slider_value3(val):
    integer_val = int(float(val))
    value_label3.config(text=f"{integer_val} °")
    return(integer_val)

def get_O2x():
    integer_val = float(O2x_input.get())
    return(integer_val)

def get_O2y():
    integer_val = float(O2y_input.get())
    return(integer_val)

def get_O4x():
    integer_val = float(O4x_input.get())
    return(integer_val)

def get_O4y():
    integer_val = float(O4y_input.get())
    return(integer_val)

def get_P2x():
    integer_val = float(P2x_input.get())  # Convertir el valor a entero
    return(integer_val)

def get_P2y():
    integer_val = float(P2y_input.get())
    return(integer_val)

def get_P3x():
    integer_val = float(P3x_input.get())
    return(integer_val)

def get_P3y():
    integer_val = float(P3y_input.get())
    return(integer_val)

def get_t1():
    integer_val = int(slider1.get())
    return(integer_val)

def get_t2():
    integer_val = int(slider2.get())
    return(integer_val)

def get_t3():
    integer_val = int(slider3.get())
    return(integer_val)

def update():
    t1 = get_t1()
    t2 = get_t2()
    t3 = get_t3()
    O2x = get_O2x()
    O2y = get_O2y()
    O4x = get_O4x()
    O4y = get_O4y()
    P2x = get_P2x()
    P2y = get_P2y()
    P3x = get_P3x()
    P3y = get_P3y()
    resultados = calcular_resultados(P2x, P2y, P3x, P3y, O2x, O2y, O4x, O4y,  t1, t2, t3)
    return l1.set(round(resultados[0],3)), l2.set(round(resultados[1],3)), l3.set(round(resultados[2],3)), l4.set(round(resultados[3],3)), b2.set(round(resultados[4],2)), b3.set(round(resultados[5],2)), g2.set(round(resultados[6],2)), g3.set(round(resultados[7],2))

#INTERFAZ
#Ventana principal
root = tk.Tk()
root.title("TAREA 4 - TEORÍA DE MÁQUINAS Y MECANISMOS")
root.configure(bg="#99fa73")
root.option_add('*TButton*Font', 'CenturyGothic 12')
root.geometry("1100x500")
root.resizable(False, False)

#Marcos
left_frame = tk.Frame(root, bg="#29eaff")
left_frame.place(x=15, y=15)

middle_frame = tk.Frame(root, bg="#29eaff")
middle_frame.place(x=375, y=35)

right_frame = tk.Frame(root, bg="#29eaff")
right_frame.place(x=720, y=80)

#COLOCAR LOGOS E INFORMACIÓN EN EL MARCO MIDDLE
universidad = tk.Label(middle_frame, text="UNIVERSIDAD NACIONAL DE TRUJILLO", bg="#29eaff", fg="black")
universidad.grid(row=0, column=0, padx=55, pady=(10, 2))
facultad = tk.Label(middle_frame, text="FACULTAD DE INGENIERÍA", bg="#29eaff", fg="black")
facultad.grid(row=1, column=0, padx=55, pady=(2, 2))
escuela = tk.Label(middle_frame, text="ESCUELA DE INGENIERÍA MECATRÓNICA", bg="#29eaff", fg="black")
escuela.grid(row=2, column=0, padx=55, pady=(2, 2))

image1_path = "unt.png"
image1 = Image.open(image1_path)
unt = ImageTk.PhotoImage(image1)
image1_label = tk.Label(middle_frame, image=unt, width=125, height=101)
image1_label.grid(row=3, column=0, padx=40, pady=(10, 5))

image2_path = "mecatronica.png"
image2 = Image.open(image2_path)
mec = ImageTk.PhotoImage(image2)
image2_label = tk.Label(middle_frame, image=mec, width=113, height=113)
image2_label.grid(row=4, column=0, padx=40, pady=(5, 10))

integrantes = tk.Label(middle_frame, text="Integrantes:", bg="#29eaff", fg="black")
integrantes.grid(row=5, column=0, padx=20, pady=(10, 5))
integrante1 = tk.Label(middle_frame, text="-Calderón Alvarado, Jeremy Lorenzo", bg="#29eaff", fg="black")
integrante1.grid(row=6, column=0, padx=20, pady=(2, 2))
integrante2 = tk.Label(middle_frame, text="-Carrillo Guevara, Abigail Bibiana", bg="#29eaff", fg="black")
integrante2.grid(row=7, column=0, padx=20, pady=(2, 10))

#CONFIGURAR ENTRADAS EN EL MARCO LEFT
# Coordenada x de O2
O2x_label = tk.Label(left_frame, text="Coordenada x de O2", bg="#114045", fg="white")
O2x_label.grid(row=0, column=0, padx=10, pady=(10, 5))
O2x_input = tk.Entry(left_frame, bg="white", fg="black", width=20)
O2x_input.grid(row=1, column=0, padx=10, pady=(0, 10))

# Coordenada y de O2
O2y_label = tk.Label(left_frame, text="Coordenada y de O2", bg="#114045", fg="white")
O2y_label.grid(row=0, column=1, padx=10, pady=(10, 5))
O2y_input = tk.Entry(left_frame, bg="white", fg="black", width=20)
O2y_input.grid(row=1, column=1, padx=10, pady=(0, 10))

# Coordenada x de O4
O4x_label = tk.Label(left_frame, text="Coordenada x de O4", bg="#114045", fg="white")
O4x_label.grid(row=2, column=0, padx=10, pady=(10, 5))
O4x_input = tk.Entry(left_frame, bg="white", fg="black", width=20)
O4x_input.grid(row=3, column=0, padx=10, pady=(0, 10))

# Coordenada y de O4
O4y_label = tk.Label(left_frame, text="Coordenada y de O4", bg="#114045", fg="white")
O4y_label.grid(row=2, column=1, padx=10, pady=(10, 5))
O4y_input = tk.Entry(left_frame, bg="white", fg="black", width=20)
O4y_input.grid(row=3, column=1, padx=10, pady=(0, 10))

# Coordenada x de P2
P2x_label = tk.Label(left_frame, text="Coordenada x de P2", bg="#114045", fg="white")
P2x_label.grid(row=4, column=0, padx=10, pady=(10, 5))
P2x_input = tk.Entry(left_frame, bg="white", fg="black", width=20)
P2x_input.grid(row=5, column=0, padx=10, pady=(0, 10))

# Coordenada y de P2
P2y_label = tk.Label(left_frame, text="Coordenada y de P2", bg="#114045", fg="white")
P2y_label.grid(row=4, column=1, padx=10, pady=(10, 5))
P2y_input = tk.Entry(left_frame, bg="white", fg="black", width=20)
P2y_input.grid(row=5, column=1, padx=10, pady=(0, 10))

# Coordenada x de P3
P3x_label = tk.Label(left_frame, text="Coordenada x de P3", bg="#114045", fg="white")
P3x_label.grid(row=6, column=0, padx=10, pady=(10, 5))
P3x_input = tk.Entry(left_frame, bg="white", fg="black", width=20)
P3x_input.grid(row=7, column=0, padx=10, pady=(0, 10))

# Coordenada y de P3
P3y_label = tk.Label(left_frame, text="Coordenada y de P3", bg="#114045", fg="white")
P3y_label.grid(row=6, column=1, padx=10, pady=(10, 5))
P3y_input = tk.Entry(left_frame, bg="white", fg="black", width=20)
P3y_input.grid(row=7, column=1, padx=10, pady=(0, 10))

# Slider "t1"
slider_label1 = tk.Label(left_frame, text="Ángulo del acoplador en P1", bg="#114045", fg="white")
slider_label1.grid(row=8, column=0, padx=10, pady=(10, 5))
style = ttk.Style()
style.configure("TScale", sliderrelief="flat", sliderthickness=20)
slider1 = ttk.Scale(left_frame, from_=0, to=360, orient="horizontal", style="TScale", command=update_slider_value1)
slider1.grid(row=9, column=0, padx=10, pady=(0, 10), sticky="nsew")
value_label1 = tk.Label(left_frame, text="0 °", bg="#114045", fg="white", width=6)
value_label1.grid(row=10, column=0, padx=10, pady=(0, 10), sticky="nsew")

# Slider "t2"
slider_label2 = tk.Label(left_frame, text="Ángulo del acoplador en P2", bg="#114045", fg="white")
slider_label2.grid(row=8, column=1, padx=10, pady=(10, 5))
style = ttk.Style()
style.configure("TScale", sliderrelief="flat", sliderthickness=20)
slider2 = ttk.Scale(left_frame, from_=0, to=360, orient="horizontal", style="TScale", command=update_slider_value2)
slider2.grid(row=9, column=1, padx=10, pady=(0, 10), sticky="nsew")
value_label2 = tk.Label(left_frame, text="0 °", bg="#114045", fg="white", width=6)
value_label2.grid(row=10, column=1, padx=10, pady=(0, 10), sticky="nsew")

# Slider "t3"
slider_label3 = tk.Label(left_frame, text="Ángulo del acoplador en P3", bg="#114045", fg="white")
slider_label3.grid(row=11, column=0, padx=10, pady=(10, 5))
style = ttk.Style()
style.configure("TScale", sliderrelief="flat", sliderthickness=20)
slider3 = ttk.Scale(left_frame, from_=0, to=360, orient="horizontal", style="TScale", command=update_slider_value3)
slider3.grid(row=12, column=0, padx=10, pady=(0, 10), sticky="nsew")
value_label3 = tk.Label(left_frame, text="0 °", bg="#114045", fg="white", width=6)
value_label3.grid(row=13, column=0, padx=10, pady=(0, 10), sticky="nsew")

# Botón "Calcular"
configurar_button = tk.Button(left_frame, text="Calcular", bg="#2a808d", fg="white", width=15, relief="flat", command=update)
configurar_button.grid(row=11, column=1, padx=10, pady=(10, 0))

#CONFIGURAR EL MARCO RIGHT CON LAS SALIDAS/RESULTADOS
#Configurar Título
resultados_label = tk.Label(right_frame, text="RESULTADOS", bg="#114045", fg="white")
resultados_label.grid(row=0, column=0, padx=100, pady=(10, 5))

#Crear variables para los resultados
l1 = tk.DoubleVar()
l2 = tk.DoubleVar()
l3 = tk.DoubleVar()
l4 = tk.DoubleVar()
b2 = tk.DoubleVar()
b3 = tk.DoubleVar()
g2 = tk.DoubleVar()
g3 = tk.DoubleVar()

#Configurar resultado "Longitud del eslabón 1"
l1_label = tk.Label(right_frame, text="Longitud del eslabón 1 (g):", bg="#114045", fg="white")
l1_label.grid(row=1, column=0, padx=20, pady=(10, 5))
value_l1_label = tk.Label(right_frame, textvariable=l1, bg="#114045", fg="white")
value_l1_label.grid(row=1, column=1, padx=10, pady=(10, 5))

#Configurar resultado "Longitud del eslabón 2"
l2_label = tk.Label(right_frame, text="Longitud del eslabón 2 (w):", bg="#114045", fg="white")
l2_label.grid(row=2, column=0, padx=20, pady=(10, 5))
value_l2_label = tk.Label(right_frame, textvariable=l2, bg="#114045", fg="white")
value_l2_label.grid(row=2, column=1, padx=10, pady=(10, 5))

#Configurar resultado "Longitud del eslabón 3"
l3_label = tk.Label(right_frame, text="Longitud del eslabón 3 (v):", bg="#114045", fg="white")
l3_label.grid(row=3, column=0, padx=20, pady=(10, 5))
value_l3_label = tk.Label(right_frame, textvariable=l3, bg="#114045", fg="white")
value_l3_label.grid(row=3, column=1, padx=10, pady=(10, 5))

#Configurar resultado "Longitud del eslabón 4"
l4_label = tk.Label(right_frame, text="Longitud del eslabón 4 (u):", bg="#114045", fg="white")
l4_label.grid(row=4, column=0, padx=20, pady=(10, 5))
value_l4_label = tk.Label(right_frame, textvariable=l4, bg="#114045", fg="white")
value_l4_label.grid(row=4, column=1, padx=10, pady=(10, 5))

#Configurar resultado "Beta 2"
b2_label = tk.Label(right_frame, text="Beta 2:", bg="#114045", fg="white")
b2_label.grid(row=5, column=0, padx=20, pady=(10, 5))
value_b2_label = tk.Label(right_frame, textvariable=b2, bg="#114045", fg="white")
value_b2_label.grid(row=5, column=1, padx=10, pady=(10, 5))

#Configurar resultado "Beta 3"
b3_label = tk.Label(right_frame, text="Beta 3:", bg="#114045", fg="white")
b3_label.grid(row=6, column=0, padx=20, pady=(10, 5))
value_b3_label = tk.Label(right_frame, textvariable=b3, bg="#114045", fg="white")
value_b3_label.grid(row=6, column=1, padx=10, pady=(10, 5))

#Configurar resultado "Gamma 2"
g2_label = tk.Label(right_frame, text="Gamma 2:", bg="#114045", fg="white")
g2_label.grid(row=7, column=0, padx=20, pady=(10, 5))
value_g2_label = tk.Label(right_frame, textvariable=g2, bg="#114045", fg="white")
value_g2_label.grid(row=7, column=1, padx=10, pady=(10, 5))

#Configurar resultado "Gamma 3"
g3_label = tk.Label(right_frame, text="Gamma 3:", bg="#114045", fg="white")
g3_label.grid(row=8, column=0, padx=20, pady=(10, 5))
value_g3_label = tk.Label(right_frame, textvariable=g3, bg="#114045", fg="white")
value_g3_label.grid(row=8, column=1, padx=10, pady=(10, 5))

#Ejecutar la interfaz
root.mainloop()