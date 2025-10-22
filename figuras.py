import tkinter as tk
import math
from tkinter import PhotoImage  # ← agregado para cargar imágenes

#---------------- FUNCIONES DE PERÍMETRO ----------------#

def cp_cuadrado():
    lado = float(entrada_ladopc.get())
    perimetro = 4 * lado
    label_resultado.config(text=f"El perímetro es: {perimetro} u", font=("Courier", 11), background="#ffffcc")

def perimetro_cuadrado():
    cuadrado = tk.Toplevel(aplicacion)
    cuadrado.configure(background="#ffffee")
    cuadrado.geometry("300x200+450+150")
    cuadrado.title("Perímetro Cuadrado")
    tk.Label(cuadrado, text="Ingrese el lado del cuadrado:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_ladopc
    entrada_ladopc = tk.Entry(cuadrado)
    entrada_ladopc.pack(pady=10)
    tk.Button(cuadrado, text="Calcular", command=cp_cuadrado, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(cuadrado, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

def cp_circulo():
    radio = float(entrada_radiopci.get())
    perimetro = 2 * math.pi * radio
    label_resultado.config(text=f"El perímetro es: {perimetro} u", font=("Courier", 10), background="#ffffcc")

def perimetro_circulo():
    circulo = tk.Toplevel(aplicacion)
    circulo.configure(background="#ffffee")
    circulo.geometry("300x200+450+150")
    circulo.title("Perímetro Círculo")
    tk.Label(circulo, text="Ingrese el radio del círculo:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_radiopci
    entrada_radiopci = tk.Entry(circulo)
    entrada_radiopci.pack(pady=10)
    tk.Button(circulo, text="Calcular", command=cp_circulo, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(circulo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

def cp_triangulo():
    lado = float(entrada_ladopt.get())
    perimetro = lado * 3
    label_resultado.config(text=f"El perímetro es: {perimetro} u", font=("Courier", 11), background="#ffffcc")

def perimetro_triangulo():
    triangulo = tk.Toplevel(aplicacion)
    triangulo.configure(background="#ffffee")
    triangulo.geometry("300x200+450+150")
    triangulo.title("Perímetro Triángulo")
    tk.Label(triangulo, text="Ingrese el lado del triángulo:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_ladopt
    entrada_ladopt = tk.Entry(triangulo)
    entrada_ladopt.pack(pady=10)
    tk.Button(triangulo, text="Calcular", command=cp_triangulo, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(triangulo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

#---------------- FUNCIONES DE ÁREA ----------------#

def ca_cuadrado():
    lado = float(entrada_ladoac.get())
    area = lado * lado
    label_resultado.config(text=f"El área es: {area} u²", font=("Courier", 11), background="#ffffcc")

def area_cuadrado():
    cuadrado = tk.Toplevel(aplicacion)
    cuadrado.configure(background="#ffffee")
    cuadrado.geometry("300x200+450+150")
    cuadrado.title("Área Cuadrado")
    tk.Label(cuadrado, text="Ingrese el lado del cuadrado:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_ladoac
    entrada_ladoac = tk.Entry(cuadrado)
    entrada_ladoac.pack(pady=10)
    tk.Button(cuadrado, text="Calcular", command=ca_cuadrado, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(cuadrado, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

def ca_circulo():
    radio = float(entrada_radioaci.get())
    area = math.pi * radio**2
    label_resultado.config(text=f"El área es: {area} u²", font=("Courier", 10), background="#ffffcc")

def area_circulo():
    circulo = tk.Toplevel(aplicacion)
    circulo.configure(background="#ffffee")
    circulo.geometry("300x200+450+150")
    circulo.title("Área Círculo")
    tk.Label(circulo, text="Ingrese el radio del círculo:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_radioaci
    entrada_radioaci = tk.Entry(circulo)
    entrada_radioaci.pack(pady=10)
    tk.Button(circulo, text="Calcular", command=ca_circulo, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(circulo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

def ca_triangulo():
    base = float(entrada_baseat.get())
    altura = float(entrada_alturaat.get())
    area = (base * altura) / 2
    label_resultado.config(text=f"El área es: {area} u²", font=("Courier", 11), background="#ffffcc")

def area_triangulo():
    triangulo = tk.Toplevel(aplicacion)
    triangulo.configure(background="#ffffee")
    triangulo.geometry("300x265+450+150")
    triangulo.title("Área Triángulo")
    tk.Label(triangulo, text="Ingrese la base del triángulo:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_baseat
    entrada_baseat = tk.Entry(triangulo)
    entrada_baseat.pack(pady=10)
    tk.Label(triangulo, text="Ingrese la altura del triángulo:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_alturaat
    entrada_alturaat = tk.Entry(triangulo)
    entrada_alturaat.pack(pady=10)
    tk.Button(triangulo, text="Calcular", command=ca_triangulo, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(triangulo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

#---------------- FUNCIONES DE VOLUMEN ----------------#

def cv_cubo():
    lado = float(entrada_ladovc.get())
    volumen = lado ** 3
    label_resultado.config(text=f"El volumen es: {volumen} u³", font=("Courier", 11), background="#ffffcc")

def volumen_cubo():
    cubo = tk.Toplevel(aplicacion)
    cubo.configure(background="#ffffee")
    cubo.geometry("300x200+450+150")
    cubo.title("Volumen Cubo")
    tk.Label(cubo, text="Ingrese el lado del cubo:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_ladovc
    entrada_ladovc = tk.Entry(cubo)
    entrada_ladovc.pack(pady=10)
    tk.Button(cubo, text="Calcular", command=cv_cubo, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(cubo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

def cv_esfera():
    radio = float(entrada_radiove.get())
    volumen = (4 * math.pi * radio**3) / 3
    label_resultado.config(text=f"El volumen es: {volumen} u³", font=("Courier", 10), background="#ffffcc")

def volumen_esfera():
    esfera = tk.Toplevel(aplicacion)
    esfera.configure(background="#ffffee")
    esfera.geometry("300x200+450+150")
    esfera.title("Volumen Esfera")
    tk.Label(esfera, text="Ingrese el radio de la esfera:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_radiove
    entrada_radiove = tk.Entry(esfera)
    entrada_radiove.pack(pady=10)
    tk.Button(esfera, text="Calcular", command=cv_esfera, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(esfera, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

def cv_cilindro():
    radio = float(entrada_radiovci.get())
    altura = float(entrada_alturavci.get())
    volumen = (math.pi * radio**2) * altura
    label_resultado.config(text=f"El volumen es: {volumen} u³", font=("Courier", 11), background="#ffffcc")

def volumen_cilindro():
    cilindro = tk.Toplevel(aplicacion)
    cilindro.configure(background="#ffffee")
    cilindro.geometry("350x265+450+150")
    cilindro.title("Volumen Cilindro")
    tk.Label(cilindro, text="Ingrese el radio del cilindro:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_radiovci
    entrada_radiovci = tk.Entry(cilindro)
    entrada_radiovci.pack(pady=10)
    tk.Label(cilindro, text="Ingrese la altura del cilindro:", bg="#ffffee", font=("Courier", 10), foreground="#3B3636").pack(pady=10)
    global entrada_alturavci
    entrada_alturavci = tk.Entry(cilindro)
    entrada_alturavci.pack(pady=10)
    tk.Button(cilindro, text="Calcular", command=cv_cilindro, font=("Verdana", 11), background="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(cilindro, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

#---------------- VENTANAS PRINCIPALES ----------------#

def ventana_perimetro():
    v = tk.Toplevel(aplicacion)
    v.configure(background="#ffffee")
    v.geometry("500x350+450+150")
    v.title("Perímetro")

    tk.Label(v, text="Perímetros", bg="#ffffee", font=("Courier", 24, "bold"), foreground="#3B3636").place(x=50, y=35, anchor='nw')

    # 🔹 Imagen general solo dentro de la ventana de perímetro
    try:
        img_perimetro = tk.PhotoImage(file="img/perimetrogeneral.png").subsample(4, 6)
        tk.Label(v, image=img_perimetro, bg="#ffffee").place(x=100, y=100)
        v.img_perimetro = img_perimetro  # mantener referencia para que no se borre
    except Exception as e:
        print("⚠️ No se pudo cargar la imagen del perímetro:", e)

    # 🔹 Botones
    tk.Button(v, text="Cuadrado", font=("Verdana", 11), background="#ffffcc", command=perimetro_cuadrado).place(x=430, y=110, anchor="ne")
    tk.Button(v, text="Círculo", font=("Verdana", 11), background="#ffffcc", command=perimetro_circulo).place(x=418, y=190, anchor="ne")
    tk.Button(v, text="Triángulo Equilátero", font=("Verdana", 11), background="#ffffcc", command=perimetro_triangulo).place(x=465, y=270, anchor="ne")

#---------------- APLICACIÓN PRINCIPAL ----------------#

aplicacion = tk.Tk()
aplicacion.geometry("500x350+450+150")
aplicacion.configure(background="#ffffee")
aplicacion.title("Perímetro, área y volumen")

tk.Label(aplicacion, text="Calculadora", bg="#ffffee", font=("Courier", 24, "bold"), foreground="#3B3636").place(x=50, y=35, anchor='nw')

# 🔹 Aquí se carga y muestra la imagen general del perímetro
try:
    img_perimetro = PhotoImage(file="img/perimetro.png").subsample(2, 2)
    tk.Label(aplicacion, image=img_perimetro, bg="#ffffee").place(x=30, y=80)
except Exception as e:
    print("⚠️ No se pudo cargar la imagen del perímetro:", e)

tk.Button(aplicacion, text="Perímetro", font=("Verdana", 11), background="#ffffcc", command=ventana_perimetro).place(x=430, y=110, anchor="ne")
tk.Button(aplicacion, text="Volumen", font=("Verdana", 11), background="#ffffcc", command=volumen_cubo).place(x=425, y=190, anchor="ne")
tk.Button(aplicacion, text="Área", font=("Verdana", 11), background="#ffffcc", command=area_cuadrado).place(x=410, y=270, anchor="ne")

aplicacion.mainloop()
