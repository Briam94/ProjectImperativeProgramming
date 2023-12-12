import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

matriz = []
def imprimir_matriz():
    for plato in matriz:
        print(plato)



def agregar_plato():
    nombre = name__entry.get()
    precio = precio_entry.get()
    descripcion = descripcion_entry.get()
    disponibilidad = disponibilidad_entry.get()
    
    # Validación del campo nombre
    if not nombre:
        messagebox.showerror("Error", "El campo nombre es obligatorio")
        return
    
    # Validación del campo precio
    if not precio.isdigit() or int(precio) <= 0:
        messagebox.showerror("Error", "El campo precio debe ser un número mayor a 0")
        return
    
    # Validación del campo descripción
    if len(descripcion) > 100:
        messagebox.showerror("Error", "El campo descripción no puede tener más de 100 caracteres")
        return
    
    # Validación del campo disponibilidad
    if disponibilidad.lower() not in ["si", "no"]:
        messagebox.showerror("Error", "El campo disponibilidad solo puede ser 'si' o 'no'")
        return
    
    plato = [nombre, precio, descripcion, disponibilidad]
    matriz.append(plato)
    
    messagebox.showinfo("Información", "Plato agregado correctamente")
    
    # Limpiar los campos de texto
    name__entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)
    disponibilidad_entry.delete(0, tk.END)

agregar_platos = tk.Tk()
agregar_platos.title("Data Entry Form")

etiqueta = tk.Label(agregar_platos, text="Mi Restaurante",
                    font=("Arial", 18), pady=10)
etiqueta.pack()
frame = tk.Frame(agregar_platos)
frame.pack()

agregar_platos_frame = tk.LabelFrame(frame, text="Agregar platos")
agregar_platos_frame.grid(row=0, column=0, padx=150, pady=10)

espacio_label = tk.Label(agregar_platos_frame, text="")
espacio_label.grid(row=0, column=0)
espacio_label = tk.Label(agregar_platos_frame, text="")
espacio_label.grid(row=0, column=1)

name_label = tk.Label(agregar_platos_frame, text="Nombre")
name_label.grid(row=1, column=0)
precio_label = tk.Label(agregar_platos_frame, text="Precio")
precio_label.grid(row=1, column=2)

name__entry = tk.Entry(agregar_platos_frame)
precio_entry = tk.Entry(agregar_platos_frame)
name__entry.grid(row=2, column=0)
precio_entry.grid(row=2, column=2)

espacio_label = tk.Label(agregar_platos_frame, text="")
espacio_label.grid(row=3, column=0)
espacio_label = tk.Label(agregar_platos_frame, text="")
espacio_label.grid(row=3, column=1)

descripcion_label = tk.Label(agregar_platos_frame, text="Descripción")
descripcion_label.grid(row=4, column=0)
disponibilidad_label = tk.Label(agregar_platos_frame, text="Disponibilidad")
disponibilidad_label.grid(row=4, column=2)

descripcion_entry = tk.Entry(agregar_platos_frame)
disponibilidad_entry = tk.Entry(agregar_platos_frame)
descripcion_entry.grid(row=5, column=0)
disponibilidad_entry.grid(row=5, column=2)

boton_agregar_platos = tk.Button(frame ,text="Agregar", command=agregar_plato)
boton_agregar_platos.grid(row=6, column=0, sticky="news", padx=30, pady=10)

# boton_imprimir = tk.Button(frame, text="Imprimir", command=imprimir_matriz)
# boton_imprimir.grid(row=7, column=0, sticky="news", padx=30, pady=10)

agregar_platos_frame.mainloop()
