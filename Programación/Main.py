import tkinter as tk
import csv
import os
import tkinter.messagebox
from os import system

def correlacion():
    # Código para abrir el locker
    system(f"python3 correlacion.py")
    pass

def ft2():
    # Código para abrir el script de registro de nuevo usuario
    system(f"python3 FT2.py")
    pass

def filtros():
    # Código para abrir el script de registro de nuevo usuario
    system(f"python3 filtros.py")
    pass


ventana = tk.Tk()
ventana.title("Menú principal")
ventana.geometry("400x300")

correlacion_b = tk.Button(ventana, text="Correlción", command=correlacion)
correlacion_b.pack()

ft2_b = tk.Button(ventana, text="Detección de filtro", command=ft2)
ft2_b.pack()

filtros_b = tk.Button(ventana, text="Conversión de filtros", command=filtros)
filtros_b.pack()

ventana.mainloop()