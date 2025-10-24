from PIL import Image, ImageTk
import os
import tkinter as tk
import math
import os
import sys
from tkinter import PhotoImage  # agregado para cargar imágenes

# Ruta base del proyecto (para localizar imágenes)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#---------------- FUNCIONES DE PERÍMETRO ----------------#

def cp_cuadrado():
    try:
        lado = float(entrada_ladopc.get())
        perimetro = 4 * lado
        label_resultado.config(text=f"El perímetro es: {perimetro} u", font=("Courier", 11), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido", bg="#ffcccc")

def perimetro_cuadrado():
    cuadrado = tk.Toplevel(aplicacion)
    cuadrado.configure(background="#ffffee")
    cuadrado.geometry("500x350+450+150")
    cuadrado.title("Perímetro Cuadrado")
    tk.Label(cuadrado, text="Ingrese el lado del cuadrado:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=10)
    global entrada_ladopc
    entrada_ladopc = tk.Entry(cuadrado)
    entrada_ladopc.pack(pady=10)
    tk.Button(cuadrado, text="Calcular", command=cp_cuadrado, font=("Verdana", 11), bg="#ffffcc").pack(pady=10)
    global label_resultado

    img = Image.open("img/square_perimeter.png")
    img = img.resize((130, 130), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(img)
    parent_bg = cuadrado.cget("background")
    image_label = tk.Label(cuadrado, image=tk_image, bg=parent_bg)
    image_label.pack(pady=10)
    image_label.image = tk_image

    label_resultado = tk.Label(cuadrado, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

def cp_circulo():
    try:
        radio = float(entrada_radiopci.get())
        perimetro = 2 * math.pi * radio
        label_resultado.config(text=f"El perímetro es: {perimetro:.2f} u", font=("Courier", 10), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido", bg="#ffcccc")

def perimetro_circulo():
    circulo = tk.Toplevel(aplicacion)
    circulo.configure(background="#ffffee")
    circulo.geometry("400x390+450+150")
    circulo.title("Perímetro Círculo")
    tk.Label(circulo, text="Ingrese el radio del círculo:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=10)
    global entrada_radiopci
    entrada_radiopci = tk.Entry(circulo)
    entrada_radiopci.pack(pady=10)
    tk.Button(circulo, text="Calcular", command=cp_circulo, font=("Verdana", 11), bg="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(circulo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

    #-------------Imagen agregada por Raul Contreras -------------
    global img_circulo
    img_circulo = PhotoImage(file="img/Circulo.png")
    img_circulo = img_circulo.subsample(3, 3) 
    tk.Label(circulo, image=img_circulo, bg="#ffffee").pack(pady=10)

def cp_triangulo():
    try:
        lado = float(entrada_ladopt.get())
        perimetro = lado * 3
        label_resultado.config(text=f"El perímetro es: {perimetro} u", font=("Courier", 11), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido", bg="#ffcccc")

def perimetro_triangulo():
    triangulo = tk.Toplevel(aplicacion)
    triangulo.configure(background="#ffffee")
    triangulo.geometry("300x200+450+150")
    triangulo.title("Perímetro Triángulo")
    tk.Label(triangulo, text="Ingrese el lado del triángulo:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=10)
    global entrada_ladopt
    entrada_ladopt = tk.Entry(triangulo)
    entrada_ladopt.pack(pady=10)
    tk.Button(triangulo, text="Calcular", command=cp_triangulo, font=("Verdana", 11), bg="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(triangulo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)
    img = Image.open("img/tri_perimeter.png")
    img = img.resize((130, 130), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(img)
    parent_bg = triangulo.cget("background")
    image_label = tk.Label(triangulo, image=tk_image, bg=parent_bg)
    image_label.pack(pady=10)
    image_label.image = tk_image
    label_resultado = tk.Label(triangulo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

#---------------- FUNCIONES DE ÁREA ----------------#

def ca_cuadrado():
    try:
        lado = float(entrada_ladoac.get())
        area = lado ** 2
        label_resultado.config(text=f"El área es: {area} u²", font=("Courier", 11), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido", bg="#ffcccc")

def area_cuadrado():
    cuadrado = tk.Toplevel(aplicacion)
    cuadrado.configure(background="#ffffee")
    cuadrado.geometry("300x300+450+150")
    cuadrado.title("Área Cuadrado")
    tk.Label(cuadrado, text="Ingrese el lado del cuadrado:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=10)
    global entrada_ladoac
    entrada_ladoac = tk.Entry(cuadrado)
    entrada_ladoac.pack(pady=10)
    tk.Button(cuadrado, text="Calcular", command=ca_cuadrado, font=("Verdana", 11), bg="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(cuadrado, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

    # Imagen del cuadrado debajo
    path_img = os.path.join(os.path.dirname(__file__), "img/cuadrado.png")
    if os.path.exists(path_img):
        img = Image.open(path_img).resize((80, 80))
        imagen_cuadrado = ImageTk.PhotoImage(img)
        label_imagen = tk.Label(cuadrado, image=imagen_cuadrado, bg="#ffffee")
        label_imagen.image = imagen_cuadrado
        label_imagen.pack(pady=5)

def ca_circulo():
    try:
        radio = float(entrada_radioaci.get())
        area = math.pi * radio**2
        label_resultado.config(text=f"El área es: {area:.2f} u²", font=("Courier", 10), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido", bg="#ffcccc")

def area_circulo():
    circulo = tk.Toplevel(aplicacion)
    circulo.configure(background="#ffffee")
    circulo.geometry("340x360+450+150")
    circulo.title("Área Círculo")

    tk.Label(circulo, text="Ingrese el radio del círculo:", bg="#ffffee",
             font=("Courier", 10), fg="#3B3636").pack(pady=(10, 4))

    try:
        path = os.path.join(BASE_DIR, "img", "circulo.png")
        photo = tk.PhotoImage(file=path).subsample(2, 2)
        img_label = tk.Label(circulo, image=photo, bg="#ffffee")
        img_label.image = photo
        img_label.pack(pady=(0, 6))
    except Exception as e:
        tk.Label(circulo, text="(No se pudo cargar imagen del círculo)", bg="#ffffee", fg="#aa0000").pack()

    global entrada_radioaci
    entrada_radioaci = tk.Entry(circulo)
    entrada_radioaci.pack(pady=10)
    tk.Button(circulo, text="Calcular", command=ca_circulo, font=("Verdana", 11), bg="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(circulo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

def ca_triangulo():
    try:
        base = float(entrada_baseat.get())
        altura = float(entrada_alturaat.get())
        area = (base * altura) / 2
        label_resultado.config(text=f"El área es: {area} u²", font=("Courier", 11), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese valores válidos", bg="#ffcccc")

def area_triangulo():
    triangulo = tk.Toplevel(aplicacion)
    triangulo.configure(background="#ffffee")
    triangulo.geometry("330x400+450+150")
    triangulo.title("Área Triángulo")

    try:
        path = os.path.join(BASE_DIR, "img", "triangle.png")
        photo = tk.PhotoImage(file=path).subsample(3, 3)
        tk.Label(triangulo, image=photo, bg="#ffffee").pack(pady=10)
        triangulo.img_ref = photo
    except Exception as e:
        tk.Label(triangulo, text="(No se pudo cargar imagen del triángulo)", bg="#ffffee", fg="#aa0000").pack()

    tk.Label(triangulo, text="Ingrese la base del triángulo:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=6)
    global entrada_baseat
    entrada_baseat = tk.Entry(triangulo)
    entrada_baseat.pack(pady=6)
    tk.Label(triangulo, text="Ingrese la altura del triángulo:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=6)
    global entrada_alturaat
    entrada_alturaat = tk.Entry(triangulo)
    entrada_alturaat.pack(pady=6)
    tk.Button(triangulo, text="Calcular", command=ca_triangulo, font=("Verdana", 11), bg="#ffffcc").pack(pady=8)
    global label_resultado
    label_resultado = tk.Label(triangulo, text="", bg="#ffffee")
    label_resultado.pack(pady=8)

#---------------- FUNCIONES DE VOLUMEN ----------------#

def cv_cubo():
    try:
        lado = float(entrada_ladovc.get())
        volumen = lado ** 3
        label_resultado.config(text=f"El volumen es: {volumen} u³", font=("Courier", 11), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido", bg="#ffcccc")

def volumen_cubo():
    cubo = tk.Toplevel(aplicacion)
    cubo.configure(background="#ffffee")
    cubo.geometry("300x300+450+150")
    cubo.title("Volumen Cubo")
    tk.Label(cubo, text="Ingrese el lado del cubo:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=10)
    global entrada_ladovc
    entrada_ladovc = tk.Entry(cubo)
    entrada_ladovc.pack(pady=10)
    tk.Button(cubo, text="Calcular", command=cv_cubo, font=("Verdana", 11), bg="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(cubo, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

    path_img = os.path.join(os.path.dirname(__file__), "img/cubo.png")
    if os.path.exists(path_img):
        img = Image.open(path_img).resize((80, 80))
        imagen_cubo = ImageTk.PhotoImage(img)
        label_imagen = tk.Label(cubo, image=imagen_cubo, bg="#ffffee")
        label_imagen.image = imagen_cubo
        label_imagen.pack(pady=5)

def cv_esfera():
    try:
        radio = float(entrada_radiove.get())
        volumen = (4 * math.pi * radio**3) / 3
        label_resultado.config(text=f"El volumen es: {volumen:.2f} u³", font=("Courier", 10), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido", bg="#ffcccc")

def volumen_esfera():
    esfera = tk.Toplevel(aplicacion)
    esfera.configure(background="#ffffee")
    esfera.geometry("300x300+450+150")
    esfera.title("Volumen Esfera")
    tk.Label(esfera, text="Ingrese el radio de la esfera:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=10)
    global entrada_radiove
    entrada_radiove = tk.Entry(esfera)
    entrada_radiove.pack(pady=10)
    tk.Button(esfera, text="Calcular", command=cv_esfera, font=("Verdana", 11), bg="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(esfera, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

    path_img = os.path.join(os.path.dirname(__file__), "img/esfera.png")
    if os.path.exists(path_img):
        img = Image.open(path_img).resize((80, 80))
        imagen_esfera = ImageTk.PhotoImage(img)
        label_imagen = tk.Label(esfera, image=imagen_esfera, bg="#ffffee")
        label_imagen.image = imagen_esfera
        label_imagen.pack(pady=5)

def cv_cilindro():
    try:
        radio = float(entrada_radiovci.get())
        altura = float(entrada_alturavci.get())
        volumen = (math.pi * radio**2) * altura
        label_resultado.config(text=f"El volumen es: {volumen:.2f} u³", font=("Courier", 11), background="#ffffcc")
    except ValueError:
        label_resultado.config(text="Ingrese valores válidos", bg="#ffcccc")

def volumen_cilindro():
    cilindro = tk.Toplevel(aplicacion)
    cilindro.configure(background="#ffffee")
    cilindro.geometry("350x380+450+150")
    cilindro.title("Volumen Cilindro")
    tk.Label(cilindro, text="Ingrese el radio del cilindro:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=10)
    global entrada_radiovci
    entrada_radiovci = tk.Entry(cilindro)
    entrada_radiovci.pack(pady=10)
    tk.Label(cilindro, text="Ingrese la altura del cilindro:", bg="#ffffee", font=("Courier", 10), fg="#3B3636").pack(pady=10)
    global entrada_alturavci
    entrada_alturavci = tk.Entry(cilindro)
    entrada_alturavci.pack(pady=10)
    tk.Button(cilindro, text="Calcular", command=cv_cilindro, font=("Verdana", 11), bg="#ffffcc").pack(pady=10)
    global label_resultado
    label_resultado = tk.Label(cilindro, text="", bg="#ffffee")
    label_resultado.pack(pady=10)

    path_img = os.path.join(os.path.dirname(__file__), "img/cilindro.png")
    if os.path.exists(path_img):
        img = Image.open(path_img).resize((80, 80))
        imagen_cilindro = ImageTk.PhotoImage(img)
        label_imagen = tk.Label(cilindro, image=imagen_cilindro, bg="#ffffee")
        label_imagen.image = imagen_cilindro
        label_imagen.pack(pady=5)

#---------------- VENTANAS PRINCIPALES ----------------#

def ventana_perimetro():
    v = tk.Toplevel(aplicacion)
    v.configure(background="#ffffee")
    v.geometry("500x350+450+150")
    v.title("Perímetro")
    tk.Label(v, text="Perímetros", bg="#ffffee", font=("Courier", 24, "bold"), fg="#3B3636").place(x=50, y=35, anchor='nw')

    try:
        img_path = os.path.join(BASE_DIR, "img", "perimetrogeneral.png")
        img_perimetro = tk.PhotoImage(file=img_path).subsample(4, 4)
        tk.Label(v, image=img_perimetro, bg="#ffffee").place(x=100, y=100)
        v.img_ref = img_perimetro
    except:
        tk.Label(v, text="(No se pudo cargar imagen del perímetro)", bg="#ffffee", fg="#aa0000").place(x=100, y=100)

    tk.Button(v, text="Cuadrado", font=("Verdana", 11), bg="#ffffcc", command=perimetro_cuadrado).place(x=430, y=110, anchor="ne")
    tk.Button(v, text="Círculo", font=("Verdana", 11), bg="#ffffcc", command=perimetro_circulo).place(x=418, y=190, anchor="ne")
    tk.Button(v, text="Triángulo Equilátero", font=("Verdana", 11), bg="#ffffcc", command=perimetro_triangulo).place(x=465, y=270, anchor="ne")

def ventana_area():
   

    v = tk.Toplevel(aplicacion)
    v.configure(background="#ffffee")
    v.geometry("500x350+450+150")
    v.title("Área")
    tk.Label(v, text="Áreas", bg="#ffffee", font=("Courier", 24, "bold"), fg="#3B3636").place(x=50, y=35, anchor='nw')
    tk.Button(v, text="Cuadrado", font=("Verdana", 11), bg="#ffffcc", command=area_cuadrado).place(x=430, y=110, anchor="ne")
    tk.Button(v, text="Triángulo", font=("Verdana", 11), bg="#ffffcc", command=area_triangulo).place(x=428, y=190, anchor="ne")
    tk.Button(v, text="Círculo", font=("Verdana", 11), bg="#ffffcc", command=area_circulo).place(x=418, y=270, anchor="ne")


def ventana_volumen():
    v = tk.Toplevel(aplicacion)
    v.configure(background="#ffffee")
    v.geometry("500x350+450+150")
    v.title("Volumen")
    tk.Label(v, text="Volúmenes", bg="#ffffee", font=("Courier", 24, "bold"), fg="#3B3636").place(x=50, y=35, anchor='nw')
    tk.Button(v, text="Cubo", font=("Verdana", 11), bg="#ffffcc", command=volumen_cubo).place(x=400, y=110, anchor="ne")
    tk.Button(v, text="Esfera", font=("Verdana", 11), bg="#ffffcc", command=volumen_esfera).place(x=405, y=190, anchor="ne")
    tk.Button(v, text="Cilindro", font=("Verdana", 11), bg="#ffffcc", command=volumen_cilindro).place(x=410, y=270, anchor="ne")

#---------------- APLICACIÓN PRINCIPAL ----------------#

aplicacion = tk.Tk()
aplicacion.geometry("500x350+450+150")
aplicacion.configure(background="#ffffee")
aplicacion.title("Perímetro, área y volumen")

tk.Label(aplicacion, text="Calculadora", bg="#ffffee", font=("Courier", 24, "bold"), fg="#3B3636").place(x=50, y=35, anchor='nw')

try:
    IMG_PATH = os.path.join(BASE_DIR, "img", "bimo.png")
    foto_principal = tk.PhotoImage(file=IMG_PATH)
    max_w, max_h = 200, 200
    w, h = foto_principal.width(), foto_principal.height()
    if w > max_w or h > max_h:
        factor = max(1, math.ceil(max(w / max_w, h / max_h)))
        foto_principal = foto_principal.subsample(factor, factor)
    aplicacion.foto_principal = foto_principal
    tk.Label(aplicacion, image=foto_principal, bg="#ffffee").place(x=50, y=90, anchor="nw")
except:
    tk.Label(aplicacion, text="(No se pudo cargar imagen principal)", bg="#ffffee", fg="#aa0000").place(x=50, y=90, anchor="nw")

# Botones principales
tk.Button(aplicacion, text="Perímetro", font=("Verdana", 11), bg="#ffffcc", command=ventana_perimetro).place(x=430, y=110, anchor="ne")
tk.Button(aplicacion, text="Volumen", font=("Verdana", 11), bg="#ffffcc", command=ventana_volumen).place(x=425, y=190, anchor="ne")
tk.Button(aplicacion, text="Área", font=("Verdana", 11), bg="#ffffcc", command=ventana_area).place(x=410, y=270, anchor="ne")

aplicacion.mainloop()

