# import tkinter as tk
# from tkinter import ttk

# matriz_gestion_platos = [['caldo', '5000', 'es un caldo', 'si'], ['arroz', '1300', 'es un arroz', 'no']]

# def eliminar_filas_seleccionadas():
#     indices_seleccionados = []
#     for i, var in enumerate(seleccion_vars):
#         if var.get() == 1:
#             indices_seleccionados.append(i)
    
#     for index in sorted(indices_seleccionados, reverse=True):
#         matriz_gestion_platos.pop(index)
    
#     actualizar_tabla()

# def actualizar_tabla():
#     tabla.delete(*tabla.get_children())
    
#     for row in matriz_gestion_platos:
#         tabla.insert('', 'end', values=row)

# # Crear la ventana principal
# eliminar_platos = tk.Tk()
# eliminar_platos.title("Tabla de Matriz")

# etiqueta = tk.Label(eliminar_platos, text="Mi Restaurante",
#                     font=("Arial", 18), pady=10)
# etiqueta.pack()

# # image = tk.PhotoImage(file="logo.png")

# # lab = ttk.Label(image=image)
# # lab.pack()

# frame = tk.Frame(eliminar_platos)
# frame.pack()

# agregar_platos_frame = tk.LabelFrame(frame, text="Agregar platos",
#                                  font=("Arial", 14),padx=50, pady=50)

# agregar_platos_frame.grid(row=0, column=0, padx=100, pady=10)

# # Crear la tabla
# tabla = ttk.Treeview(agregar_platos_frame, columns=("Nombre", "Precio", "Descripción", "Disponibilidad", "Selección"), show="headings")
# tabla.heading("Nombre", text="Nombre")
# tabla.heading("Precio", text="Precio")
# tabla.heading("Descripción", text="Descripción")
# tabla.heading("Disponibilidad", text="Disponibilidad")
# tabla.heading("Selección", text="Selección")

# # Agregar los datos de la matriz a la tabla
# for row in matriz_gestion_platos:
#     tabla.insert('', 'end', values=row)

# # Agregar un Checkbutton en la columna de selección
# seleccion_vars = []
# for i in range(len(matriz_gestion_platos)):
#     var = tk.IntVar()
#     seleccion_vars.append(var)
#     tabla.set(tabla.get_children()[i], "Selección", "")
#     tabla.tag_configure(i, foreground='black', background='white', font='Arial 10')
#     tabla.item(tabla.get_children()[i], tags=(i,))
#     tabla.tag_bind(i, '<ButtonRelease-1>', lambda event, i=i: toggle_seleccion(i))

# def toggle_seleccion(i):
#     seleccion_vars[i].set(not seleccion_vars[i].get())
#     tabla.set(tabla.get_children()[i], "Selección", "X" if seleccion_vars[i].get() else "")

# # Crear el botón de eliminar
# boton_eliminar_platos = tk.Button(frame ,text="Eliminar",background="red", command=eliminar_filas_seleccionadas,
#                                  font=("Arial", 12), pady=0)

# boton_eliminar_platos.grid(row=6, column=0, sticky="news", padx=10, pady=10)

# boton_cancelar = tk.Button(frame, text="Cancelar",background="Blue",
#                                  font=("Arial", 12), pady=0)
# boton_cancelar.grid(row=7, column=0, sticky="news", padx=10, pady=10)
# # Mostrar la tabla y el botón en la ventana
# tabla.pack()

# # Iniciar el bucle principal de la aplicación
# eliminar_platos.mainloop()

# # Mostrar la tabla y

# # haz una tabla para mostrar la informacion de la matriz, en la columna 1
# # nombre
# # 2 precio
# # 3 descripcion
# # 4 disponibilidad
# # 5 seleccion, en seleccion debe haber un Checkbutton por cada valor que se toma desde la matriz

# # ademas de esto debe haber un boton de eliminar el cual eliminara de la matriz las filas seleccionadas







# import tkinter as tk
# from tkinter import ttk

# matriz = [['caldo', '5000', 'es un caldo', 'si'], ['arroz', '1300', 'es un arroz', 'no']]

# def toggle_seleccion(i):
#     for j, var in enumerate(seleccion_vars):
#         if i == j:
#             var.set(not var.get())
#             tree.set(tree.get_children()[j], "Selección", "X" if var.get() else "")
#         else:
#             var.set(0)
#             tree.set(tree.get_children()[j], "Selección", "")

# def eliminar_filas_seleccionadas():
#     indices_seleccionados = [i for i, var in enumerate(seleccion_vars) if var.get()]
    
#     for index in sorted(indices_seleccionados, reverse=True):
#         matriz.pop(index)
    
#     actualizar_tabla()

# def actualizar_tabla():
#     tree.delete(*tree.get_children())
    
#     for row in matriz:
#         tree.insert('', 'end', values=row)

# # Crear la ventana principal
# root = tk.Tk()
# root.title("Tabla de Matriz")

# # Crear la tabla
# tree = ttk.Treeview(root, columns=("Nombre", "Precio", "Descripción", "Disponibilidad", "Selección"), show="headings")
# tree.heading("Nombre", text="Nombre")
# tree.heading("Precio", text="Precio")
# tree.heading("Descripción", text="Descripción")
# tree.heading("Disponibilidad", text="Disponibilidad")
# tree.heading("Selección", text="Selección")

# # Agregar los datos de la matriz a la tabla
# for row in matriz:
#     tree.insert('', 'end', values=row)

# # Agregar un Checkbutton en la columna de selección
# seleccion_vars = []
# for i in range(len(matriz)):
#     var = tk.IntVar()
#     seleccion_vars.append(var)
#     tree.set(tree.get_children()[i], "Selección", "")
#     tree.tag_configure(i, foreground='black', background='white', font='Arial 10')
#     tree.item(tree.get_children()[i], tags=(i,))
#     tree.tag_bind(i, '<ButtonRelease-1>', lambda event, i=i: toggle_seleccion(i))

# # Crear el botón de eliminar
# eliminar_button = tk.Button(root, text="Eliminar", command=eliminar_filas_seleccionadas)

# # Mostrar la tabla y el botón en la ventana
# tree.pack()
# eliminar_button.pack()



#_______________________________________________________________________________________#

# # Iniciar el bucle principal de la aplicación
# root.mainloop()
# import tkinter as tk
# from tkinter import ttk

# def ingresar_datos():
#     global matriz
#     matriz = []  # Reinicia la matriz
#     num_filas = int(entry_num_filas.get())

#     for _ in range(num_filas):
#         nombre = entry_nombre.get()
#         precio = entry_precio.get()
#         descripcion = entry_descripcion.get()
#         disponibilidad = entry_disponibilidad.get()
#         fila = [nombre, precio, descripcion, disponibilidad]
#         matriz.append(fila)

#     actualizar_tabla()

# def toggle_seleccion(event):
#     selected_item = tree.selection()
#     tree.tag_configure("seleccionada", foreground='black', background='white', font='Arial 10')
#     for item in tree.get_children():
#         tags = tree.item(item, 'tags')
#         if item == selected_item:
#             tags += ("seleccionada",)
#         tree.item(item, tags=tags)

# def eliminar_filas_seleccionadas():
#     selected_items = tree.selection()
#     indices_seleccionados = [tree.index(item) for item in selected_items]
    
#     for index in sorted(indices_seleccionados, reverse=True):
#         matriz.pop(index)
    
#     actualizar_tabla()

# def actualizar_tabla():
#     tree.delete(*tree.get_children())
    
#     for i, row in enumerate(matriz):
#         tree.insert('', 'end', values=row, tags=(f"row{i}",))

# # Crear la ventana principal
# root = tk.Tk()
# root.title("Tabla de Matriz")

# # Entradas para ingresar datos
# tk.Label(root, text="Número de filas:").pack()
# entry_num_filas = tk.Entry(root)
# entry_num_filas.pack()

# tk.Label(root, text="Nombre:").pack()
# entry_nombre = tk.Entry(root)
# entry_nombre.pack()

# tk.Label(root, text="Precio:").pack()
# entry_precio = tk.Entry(root)
# entry_precio.pack()

# tk.Label(root, text="Descripción:").pack()
# entry_descripcion = tk.Entry(root)
# entry_descripcion.pack()

# tk.Label(root, text="Disponibilidad:").pack()
# entry_disponibilidad = tk.Entry(root)
# entry_disponibilidad.pack()

# # Botón para ingresar datos
# tk.Button(root, text="Ingresar Datos", command=ingresar_datos).pack()

# # Crear la tabla
# tree = ttk.Treeview(root, columns=("Nombre", "Precio", "Descripción", "Disponibilidad"), show="headings")
# tree.heading("Nombre", text="Nombre")
# tree.heading("Precio", text="Precio")
# tree.heading("Descripción", text="Descripción")
# tree.heading("Disponibilidad", text="Disponibilidad")

# # Configurar el evento de clic
# tree.bind('<ButtonRelease-1>', toggle_seleccion)

# # Crear el botón de eliminar
# eliminar_button = tk.Button(root, text="Eliminar", command=eliminar_filas_seleccionadas)

# # Mostrar la tabla y el botón en la ventana
# tree.pack()
# eliminar_button.pack()

# # Iniciar el bucle principal de la aplicación
# root.mainloop()



import tkinter as tk
from tkinter import ttk

def ingresar_datos():
    ventana_datos = tk.Toplevel(root)
    ventana_datos.title("Ingresar Datos")

    tk.Label(ventana_datos, text="Número de filas:").pack()
    entry_num_filas = tk.Entry(ventana_datos)
    entry_num_filas.pack()

    tk.Label(ventana_datos, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana_datos)
    entry_nombre.pack()

    tk.Label(ventana_datos, text="Precio:").pack()
    entry_precio = tk.Entry(ventana_datos)
    entry_precio.pack()

    tk.Label(ventana_datos, text="Descripción:").pack()
    entry_descripcion = tk.Entry(ventana_datos)
    entry_descripcion.pack()

    tk.Label(ventana_datos, text="Disponibilidad:").pack()
    entry_disponibilidad = tk.Entry(ventana_datos)
    entry_disponibilidad.pack()

    def agregar_fila():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        descripcion = entry_descripcion.get()
        disponibilidad = entry_disponibilidad.get()
        fila = [nombre, precio, descripcion, disponibilidad]
        matriz.append(fila)
        actualizar_tabla()
        ventana_datos.destroy()

    tk.Button(ventana_datos, text="Agregar Fila", command=agregar_fila).pack()

def toggle_seleccion(event):
    selected_item = tree.selection()
    tree.tag_configure("seleccionada", foreground='black', background='white', font='Arial 10')
    for item in tree.get_children():
        tags = tree.item(item, 'tags')
        if item == selected_item:
            tags += ("seleccionada",)
        tree.item(item, tags=tags)

def eliminar_filas_seleccionadas():
    selected_items = tree.selection()
    indices_seleccionados = [tree.index(item) for item in selected_items]
    
    for index in sorted(indices_seleccionados, reverse=True):
        matriz.pop(index)
    
    actualizar_tabla()

def actualizar_tabla():
    tree.delete(*tree.get_children())
    
    for i, row in enumerate(matriz):
        tree.insert('', 'end', values=row, tags=(f"row{i}",))

# Crear la ventana principal
root = tk.Tk()
root.title("Tabla de Matriz")

# Crear la tabla
tree = ttk.Treeview(root, columns=("Nombre", "Precio", "Descripción", "Disponibilidad"), show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Precio", text="Precio")
tree.heading("Descripción", text="Descripción")
tree.heading("Disponibilidad", text="Disponibilidad")

# Configurar el evento de clic
tree.bind('<ButtonRelease-1>', toggle_seleccion)

# Crear el botón para ingresar datos
tk.Button(root, text="Ingresar Datos", command=ingresar_datos).pack()

# Crear el botón de eliminar
eliminar_button = tk.Button(root, text="Eliminar", command=eliminar_filas_seleccionadas)
eliminar_button.pack()

# Mostrar la tabla en la ventana principal
tree.pack()

# Matriz inicial
matriz = [['caldo', '5000', 'es un caldo', 'si'], ['arroz', '1300', 'es un arroz', 'no']]
actualizar_tabla()

# Iniciar el bucle principal de la aplicación
root.mainloop()




