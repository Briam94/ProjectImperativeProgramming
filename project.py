import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox
import hashlib

regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,20}$"
__window_size = "450x400+400+200"

matriz_gestion_platos = []

# ________________________________________________________________________________________________#
# Funciones para eliminar platos


def eliminar_filas_seleccionadas():
    indices_seleccionados = []
    for i, var in enumerate(seleccion_vars):
        if var.get() == 1:
            indices_seleccionados.append(i)

    for index in sorted(indices_seleccionados, reverse=True):
        matriz_gestion_platos.pop(index)

    actualizar_tabla()


def actualizar_tabla():
    tabla.delete(*tabla.get_children())

    for row in matriz_gestion_platos:
        tabla.insert('', 'end', values=row)


# _____________________________________________________________________________________#

# Funciones de gestion de platos

def imprimir_matriz():
    for plato in matriz_gestion_platos:
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
        messagebox.showerror(
            "Error", "El campo precio debe ser un número mayor a 0")
        return

    # Validación del campo descripción
    if len(descripcion) > 100:
        messagebox.showerror(
            "Error", "El campo descripción no puede tener más de 100 caracteres")
        return

    # Validación del campo disponibilidad
    if disponibilidad.lower() not in ["si", "no"]:
        messagebox.showerror(
            "Error", "El campo disponibilidad solo puede ser 'si' o 'no'")
        return

    plato = [nombre, precio, descripcion, disponibilidad]
    matriz_gestion_platos.append(plato)

    messagebox.showinfo("Información", "Plato agregado correctamente")

    # Limpiar los campos de texto
    name__entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)
    disponibilidad_entry.delete(0, tk.END)

# _____________________________________________________________________________________#

# open and close screen/window


def close_and_open_screen(window_to_close, window_to_open):
    window_to_close.withdraw()
    window_to_open.deiconify()


def agregar_platos_screen():
    close_and_open_screen(gestion_platos, agregar_platos)


def eliminar_platos_screen():
    close_and_open_screen(gestion_platos, eliminar_platos)


def gestion_platos_screen():
    close_and_open_screen(menu_screen, gestion_platos)


def registry_screen():
    close_and_open_screen(home_scren, registry_user_screen)


def login_screen():
    close_and_open_screen(home_scren, init_sesion_screen)


def cancel_eliminar_platos():
    close_and_open_screen(eliminar_platos, gestion_platos)


def cancel_agregar_platos():
    close_and_open_screen(agregar_platos, gestion_platos)


def cancel_registry_user():
    close_and_open_screen(registry_user_screen, home_scren)


def cancel_gestion_platos():
    close_and_open_screen(gestion_platos, menu_screen)


def cancel_login():
    close_and_open_screen(init_sesion_screen, home_scren)


def registry_user():
    email = email_registry_user_entry.get()
    password = password_registry_user_entry.get()
    confirm_password = confirm_password_registry_user_entry.get()
    separator = '\n'
    if re.fullmatch(regex_email, email):
        if password == confirm_password:
            pat = re.compile(regex_password)
            mat = re.search(pat, password)
            if mat:
                password = hashlib.sha256(password.encode())
                users = [email + separator,
                         password.hexdigest() + separator]
                users_file = open("users.txt", "w")
                users_file.writelines(users)
                users_file.close()
                show_successful(
                    "EXITOSO", "el usuario fue guardado exitosamente")
                email_registry_user_entry.delete(0, tk.END)
                password_registry_user_entry.delete(0, tk.END)
                confirm_password_registry_user_entry.delete(0, tk.END)
            else:
                show_error(
                    'Contraseña', 'La contraseña debe contener 1 mayuscula, 1 numero, 1 minuscula, 1 caracter especial y minimo de 10 caracteres')
        else:
            show_error('Contraseña', 'Las contraseñas no coinciden.')
    else:
        show_error('Correo invalido',
                   'El correo ingresado no tiene la estructura correcta.')


def login():
    email = email_login_entry.get()
    password = hashlib.sha256(password_login_entry.get().encode())
    users_file = open("users.txt", "r")
    data = users_file.readlines()
    users = []
    print(data)
    for i in data:
        users.append(i.replace('\n', ''))
    print(users)
    try:
        index = users.index(email)
        if users[index] == email and users[index+1] == password.hexdigest():
            close_and_open_screen(init_sesion_screen, menu_screen)
        else:
            show_error('Usuario incorrecto', 'Usuario y/o correo invalidos')
    except:
        show_error('Usuario incorrecto', 'Usuario y/o correo invalidos')


def show_error(title_error, text_error):
    messagebox.showerror(title_error, text_error)


def show_successful(title, text):
    messagebox.showinfo(title, text)


def read_file():
    email = email_registry_user_entry.get()
    password = password_registry_user_entry.get()
    users_file = open("users.txt", "r")
    data = users_file.readlines()
    print('data', data)
    for i in range(0, data.length()):
        data_into_list = data.replace('\n', ' ')
    print('data_into_list', data_into_list)
    users_file.close()


# HOME PRINCIPAL
home_scren = tk.Tk()
home_scren.title("Proyecto final")

# LABELS
title = tk.Label(home_scren, text="Mi Restaurante",
                 font=("Arial", 18), pady=10)
title.pack()

title_description = tk.Label(home_scren,
                             text="Nuestro restaurante es un lugar donde ofrecemos\n una variedad de platos delicioso y recursos\n culinarios para el publico para satisfacer tus\n necesidades culinarias y hacerte disfrutar de una\n experiencia gastronómica excepcional",
                             font=("Arial", 10), justify="left", pady=10)
title_description.pack()


# Buttons
registry_button = tk.Button(
    home_scren, text="Registrarse", command=registry_screen)
registry_button.pack()

init_sesion_button = tk.Button(
    home_scren, text="Iniciar sesión", command=login_screen)
init_sesion_button.pack()


init_sesion_button.place(x=185, y=200)

# Generate window size
home_scren.geometry(__window_size)

# REGISTRY USER SCREEN
registry_user_screen = tk.Tk()
registry_user_screen.title("Registrar usuario")
registry_user_screen.withdraw()

title_user = tk.Label(registry_user_screen, text="Mi Restaurante",
                      font=("Arial", 18), pady=10)
title_user.pack()

# LABELS AND ENTRY
sub_title_registry_user = tk.Label(
    registry_user_screen, text="Registrarse", font=("Arial", 10), pady=10)
sub_title_registry_user.pack()

email_registry_user = tk.Label(
    registry_user_screen, text="Email", font=("Arial", 10), pady=10)
email_registry_user.pack()
email_registry_user_entry = tk.Entry(registry_user_screen)
email_registry_user_entry.pack()

password_registry_user = tk.Label(
    registry_user_screen, text="Contraseña", font=("Arial", 10), pady=10)
password_registry_user.pack()
password_registry_user_entry = tk.Entry(registry_user_screen, show="*")
password_registry_user_entry.pack()


confirm_password_registry_user = tk.Label(
    registry_user_screen, text="Cofirmar contraseña", font=("Arial", 10), pady=10)
confirm_password_registry_user.pack()
confirm_password_registry_user_entry = tk.Entry(
    registry_user_screen, show="*")
confirm_password_registry_user_entry.pack()

# BUTTON
registry_user_button = tk.Button(
    registry_user_screen, text="Registrar", command=registry_user)
registry_user_button.pack()

cancel_registry_user_button = tk.Button(
    registry_user_screen, text="Cancelar", command=cancel_registry_user)
cancel_registry_user_button.pack()

# PLACES
registry_user_button.place(x=170, y=280)
cancel_registry_user_button.place(x=250, y=280)

registry_user_screen.geometry(__window_size)
home_scren.withdraw()


# LOGIN SCREEN
init_sesion_screen = tk.Tk()
init_sesion_screen.title("Iniciar sesion")
init_sesion_screen.withdraw()


# LABELS AND ENTRY
sub_title_login = tk.Label(
    init_sesion_screen, text="Inicio sesion", font=("Arial", 10), pady=10)
sub_title_login.pack()

email_login = tk.Label(
    init_sesion_screen, text="Email", font=("Arial", 10), pady=10)
email_login.pack()
email_login_entry = tk.Entry(init_sesion_screen)
email_login_entry.pack()

password_login = tk.Label(
    init_sesion_screen, text="Contraseña", font=("Arial", 10), pady=10)
password_login.pack()
password_login_entry = tk.Entry(init_sesion_screen, show="*")
password_login_entry.pack()

# _______________________________________________________________________________________________________________#

# BUTTON
login_button = tk.Button(
    init_sesion_screen, text="INICIAR SESION", command=login)
login_button.pack()

cancel_login_button = tk.Button(
    init_sesion_screen, text="Cancelar", command=cancel_login)
cancel_login_button.pack()

# _______________________________________________________________________________________________________________#

# PLACES
login_button.place(x=120, y=280)
cancel_login_button.place(x=250, y=280)

init_sesion_screen.geometry(__window_size)

# _______________________________________________________________________________________________________________#

# MENU SCREEN
menu_screen = tk.Tk()
menu_screen.title("Data Entry Form")

etiqueta = tk.Label(menu_screen, text="Mi Restaurante",
                    font=("Arial", 18), pady=10)
etiqueta.pack()
frame = tk.Frame(menu_screen)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="Bienvenido",
                                font=("Arial", 14), pady=10)
user_info_frame.grid(row=0, column=0, padx=10, pady=10)

boton_gestion_platos = tk.Button(user_info_frame, text="Gestión platos", command=gestion_platos_screen,
                                 font=("Arial", 12), pady=10)

boton_gestion_platos.grid(row=1, column=0, sticky="news", padx=100, pady=10)

boton_gestion_mesas = tk.Button(user_info_frame, text="Gestión mesas",
                                font=("Arial", 12), pady=10)

boton_gestion_mesas.grid(row=2, column=0, sticky="news", padx=100, pady=10)

boton_gestion_pedidos = tk.Button(user_info_frame, text="Gestión pedidos",
                                  font=("Arial", 12), pady=10)

boton_gestion_pedidos.grid(row=3, column=0, sticky="news", padx=100, pady=10)

boton_cerrar_sesion = tk.Button(user_info_frame, text="Cerrar sesión",
                                font=("Arial", 12), pady=10)

boton_cerrar_sesion.grid(row=4, column=0, sticky="news", padx=100, pady=10)
menu_screen.withdraw()

menu_screen.geometry(__window_size)

# _______________________________________________________________________________________________________________#

# Gestion platos

gestion_platos = tk.Tk()
gestion_platos.title("Gestion platos")

etiqueta = tk.Label(gestion_platos, text="Mi Restaurante",
                    font=("Arial", 18), pady=10)
etiqueta.pack()
frame = tk.Frame(gestion_platos)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="Gestion de platos",
                                font=("Arial", 14), pady=20)

user_info_frame.grid(row=0, column=0, padx=10, pady=10)

# Botones
boton_gestion_platos = tk.Button(user_info_frame, text="Agregar", command=agregar_platos_screen,
                                 font=("Arial", 10), pady=10)

boton_gestion_platos.grid(row=1, column=0, sticky="news", padx=100, pady=10)

boton_gestion_mesas = tk.Button(user_info_frame, text="Eliminar", command=eliminar_platos_screen,
                                font=("Arial", 10), pady=10)

boton_gestion_mesas.grid(row=2, column=0, sticky="news", padx=100, pady=10)

boton_gestion_pedidos = tk.Button(user_info_frame, text="Actualizar",
                                  font=("Arial", 10), pady=10)

boton_gestion_pedidos.grid(row=3, column=0, sticky="news", padx=100, pady=10)

boton_gestion_pedidos = tk.Button(user_info_frame, text="Cancelar", command=cancel_gestion_platos,
                                  font=("Arial", 10), pady=10)

boton_gestion_pedidos.grid(row=4, column=0, sticky="news", padx=100, pady=10)


#gestion_platos.withdraw()
gestion_platos.geometry(__window_size)

# _______________________________________________________________________________________________________________#
# Agregar platos

agregar_platos = tk.Tk()
agregar_platos.title("Data Entry Form")

etiqueta = tk.Label(agregar_platos, text="Mi Restaurante",
                    font=("Arial", 18), pady=10)
etiqueta.pack()
frame = tk.Frame(agregar_platos)
frame.pack()

agregar_platos_frame = tk.LabelFrame(frame, text="Agregar platos",
                                     font=("Arial", 14), pady=10)

agregar_platos_frame.grid(row=0, column=0, padx=100, pady=10)

espacio_label = tk.Label(agregar_platos_frame, text="")
espacio_label.grid(row=0, column=0)
espacio_label = tk.Label(agregar_platos_frame, text="")
espacio_label.grid(row=0, column=1)

name_label = tk.Label(agregar_platos_frame, text="Nombre",
                      font=("Arial", 12), pady=10)
name_label.grid(row=1, column=0)
precio_label = tk.Label(agregar_platos_frame, text="Precio",
                        font=("Arial", 12), pady=10)
precio_label.grid(row=1, column=2)

name__entry = tk.Entry(agregar_platos_frame)
precio_entry = tk.Entry(agregar_platos_frame)
name__entry.grid(row=2, column=0)
precio_entry.grid(row=2, column=2)

espacio_label = tk.Label(agregar_platos_frame, text="")
espacio_label.grid(row=3, column=0)
espacio_label = tk.Label(agregar_platos_frame, text="")
espacio_label.grid(row=3, column=1)

descripcion_label = tk.Label(agregar_platos_frame, text="Descripción",
                             font=("Arial", 12), pady=10)

descripcion_label.grid(row=4, column=0)
disponibilidad_label = tk.Label(agregar_platos_frame, text="Disponibilidad",
                                font=("Arial", 12), pady=10)

disponibilidad_label.grid(row=4, column=2)

descripcion_entry = tk.Entry(agregar_platos_frame)
disponibilidad_entry = tk.Entry(agregar_platos_frame)
descripcion_entry.grid(row=5, column=0)
disponibilidad_entry.grid(row=5, column=2)

boton_agregar_platos = tk.Button(frame, text="Agregar", command=agregar_plato,
                                 font=("Arial", 12), pady=10)

boton_agregar_platos.grid(row=6, column=0, sticky="news", padx=30, pady=10)

boton_cancelar = tk.Button(frame, text="Imprimir",
                           command=cancel_agregar_platos)
boton_cancelar.grid(row=7, column=0, sticky="news", padx=30, pady=10)

agregar_platos.geometry(__window_size)
agregar_platos.withdraw()

# _______________________________________________________________________________________________________________#

# Crear la ventana principal eliminar platos
eliminar_platos = tk.Tk()
eliminar_platos.title("Tabla de Matriz")

etiqueta = tk.Label(eliminar_platos, text="Mi Restaurante",
                    font=("Arial", 18), pady=10)
etiqueta.pack()

# image = tk.PhotoImage(file="logo.png")

# lab = ttk.Label(image=image)
# lab.pack()

frame = tk.Frame(eliminar_platos)
frame.pack()

agregar_platos_frame = tk.LabelFrame(frame, text="Agregar platos",
                                     font=("Arial", 14), padx=50, pady=50)

agregar_platos_frame.grid(row=0, column=0, padx=100, pady=10)

# Crear la tabla
tabla = ttk.Treeview(agregar_platos_frame, columns=(
    "Nombre", "Precio", "Descripción", "Disponibilidad", "Selección"), show="headings")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Precio", text="Precio")
tabla.heading("Descripción", text="Descripción")
tabla.heading("Disponibilidad", text="Disponibilidad")
tabla.heading("Selección", text="Selección")

# Agregar los datos de la matriz a la tabla
for row in matriz_gestion_platos:
    tabla.insert('', 'end', values=row)

# Agregar un Checkbutton en la columna de selección
seleccion_vars = []
for i in range(len(matriz_gestion_platos)):
    var = tk.IntVar()
    seleccion_vars.append(var)
    tabla.set(tabla.get_children()[i], "Selección", "")
    tabla.tag_configure(i, foreground='black',
                        background='white', font='Arial 10')
    tabla.item(tabla.get_children()[i], tags=(i,))
    tabla.tag_bind(i, '<ButtonRelease-1>', lambda event,
                   i=i: toggle_seleccion(i))


def toggle_seleccion(i):
    seleccion_vars[i].set(not seleccion_vars[i].get())
    tabla.set(tabla.get_children()[i], "Selección",
              "X" if seleccion_vars[i].get() else "")


# Crear el botón de eliminar
boton_eliminar_platos = tk.Button(frame, text="Eliminar", background="red", command=eliminar_filas_seleccionadas,
                                  font=("Arial", 12), pady=0)

boton_eliminar_platos.grid(row=6, column=0, sticky="news", padx=10, pady=10)

boton_cancelar = tk.Button(frame, text="Cancelar", background="Blue", command=cancel_eliminar_platos,
                           font=("Arial", 12), pady=0)
boton_cancelar.grid(row=7, column=0, sticky="news", padx=10, pady=10)
# Mostrar la tabla y el botón en la ventana
tabla.pack()
eliminar_platos.withdraw()

# _______________________________________________________________________________________________________________#
home_scren.mainloop()
registry_user_screen.mainloop()
menu_screen.mainloop()
init_sesion_screen.mainloop()
gestion_platos.mainloop()
agregar_platos_frame.mainloop()
eliminar_platos.mainloop()
