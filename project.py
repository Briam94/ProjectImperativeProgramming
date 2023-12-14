import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox
import hashlib
import random

regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,20}$"
__window_size = "450x400+400+200"

matriz_gestion_platos = [['caldo', '5000', 'es un caldo', 'si'], ['arroz', '1300', 'es un arroz', 'no']]
lista_pedidos = []
tables =  [('1', '20/10/2023', '10:00', '4'), ('2', '20/10/2023', '14:00', '5'),('12', '12/10/1990','14:00','4')] 
# ________________________________________________________________________________________________#
# Funciones para eliminar platos


# _____________________________________________________________________________________#

# open and close screen/window



def close_and_open_screen(window_to_close, window_to_open):
    window_to_close.withdraw()
    window_to_open.deiconify()


def gestion_platos_screen():
    close_and_open_screen(menu_screen, gestion_platos)

def agregar_pedidos_screen():
    close_and_open_screen(menu_screen, agregar_pedidos)

def registry_screen():
    close_and_open_screen(home_scren, registry_user_screen)


def login_screen():
    close_and_open_screen(home_scren, init_sesion_screen)


def cancel_registry_user():
    close_and_open_screen(registry_user_screen, home_scren)


def cancel_gestion_platos():
    close_and_open_screen(gestion_platos, menu_screen)


def cancel_login():
    close_and_open_screen(init_sesion_screen, home_scren)

# _____________________________________________________________________________________#
    
def reservar_pedido():
    mesa_seleccionada = treeview_mesas.item(treeview_mesas.focus())['text']
    plato_seleccionado = treeview_platos.item(treeview_platos.focus())['text']
    
    numero_pedido = random.randint(1000, 9999)  # Generar un número aleatorio de pedido
    pedido_actual = {
        "ID": numero_pedido,
        "Mesa": mesa_seleccionada,
        "Plato": plato_seleccionado
    }
    lista_pedidos.append(pedido_actual)

def mostrar_pedidos():
    agregar_pedidos.withdraw()
    pedidos_window = tk.Tk()
    pedidos_window.title("Pedidos")
    pedidos_window.geometry(__window_size)

    def eliminar_pedido():
        selected_item = tree.focus()
        if selected_item:
            index = int(tree.item(selected_item, 'text'))
            tree.delete(selected_item)
            del lista_pedidos[index]

    tree = ttk.Treeview(pedidos_window, columns=("ID", "Mesa", "Plato"), selectmode="browse")
    tree.heading("#0", text="Índice")
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Mesa")
    tree.heading("#3", text="Plato")
    tree.column("#0", width=60)
    tree.column("#1", width=60)
    tree.column("#2", width=60)
    tree.column("#3", width=120)
    
    for i, pedido in enumerate(lista_pedidos):
        tree.insert("", "end", text=str(i), values=(pedido["ID"], pedido["Mesa"], pedido["Plato"]))

    tree.pack(padx=20, pady=10)

    btn_eliminar = tk.Button(
        pedidos_window, text="Eliminar Pedido", command=eliminar_pedido)
    btn_eliminar.pack(pady=5)

    btn_salir = tk.Button(pedidos_window, text="Salir", command=lambda: (
        pedidos_window.destroy(), agregar_pedidos.deiconify()))
    btn_salir.pack(pady=5)

    pedidos_window.mainloop()


# _____________________________________________________________________________________#

# Funciones de gestion de platos

def actualizar_datos():
    # Resto del código...
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showinfo("Error", "No se ha seleccionado ninguna fila.")
        return
    if seleccion:
        # Obtener los valores de la fila seleccionada
        valores = tree.item(seleccion)['values']

        actualizar_platos = tk.Tk()
        actualizar_platos.title("Data Entry Form")

        # Crear los campos de texto y mostrar los valores de la fila seleccionada
        
        etiqueta = tk.Label(actualizar_platos, text="Mi Restaurante",
                            font=("Arial", 18), pady=10)
        etiqueta.pack()
        frame = tk.Frame(actualizar_platos)
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

        descripcion_entry = tk.Entry(
            agregar_platos_frame)
        disponibilidad_entry = tk.Entry(
            agregar_platos_frame)
        descripcion_entry.grid(row=5, column=0)
        disponibilidad_entry.grid(row=5, column=2)

        name__entry.insert(0, valores[0])
        precio_entry.insert(0, valores[1])
        descripcion_entry.insert(0, valores[2])
        disponibilidad_entry.insert(0, valores[3])

    def actualizar_fila():
        # Obtener los nuevos valores de los campos de texto
        nuevo_nombre = name__entry.get()
        nuevo_precio = precio_entry.get()
        nueva_descripcion = descripcion_entry.get()
        nueva_disponibilidad = disponibilidad_entry.get()

    # Actualizar los valores en la tabla
        seleccion = tree.selection()
        if seleccion:
            tree.item(seleccion, values=(nuevo_nombre, nuevo_precio,
                      nueva_descripcion, nueva_disponibilidad))
            
            actualizar_platos.destroy()
            

        # Agregar el botón de actualizar
    boton_actualizar_platos = tk.Button(frame, text="Actualizar", command=actualizar_fila,
                                     font=("Arial", 12), pady=10)

    boton_actualizar_platos.grid(row=6, column=0, sticky="news", padx=20, pady=5)

    boton_cancelar = tk.Button(
        frame, text="Cancelar", command=actualizar_platos.destroy, font=("Arial", 12), pady=10)
    boton_cancelar.grid(row=7, column=0, sticky="news", padx=20, pady=5)

    actualizar_platos.geometry(__window_size)

def ingresar_datos():
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

    def agregar_fila():

        nombre = name__entry.get()
        precio = precio_entry.get()
        descripcion = descripcion_entry.get()
        disponibilidad = disponibilidad_entry.get()

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

        fila = [nombre, precio, descripcion, disponibilidad]
        matriz_gestion_platos.append(fila)
        actualizar_tabla()
        agregar_platos.destroy()

    boton_agregar_platos = tk.Button(frame, text="Agregar", command=agregar_fila,
                                     font=("Arial", 12), pady=10)

    boton_agregar_platos.grid(row=6, column=0, sticky="news", padx=20, pady=5)

    boton_cancelar = tk.Button(
        frame, text="Cancelar", command=agregar_platos.destroy, font=("Arial", 12), pady=10)
    boton_cancelar.grid(row=7, column=0, sticky="news", padx=20, pady=5)

    agregar_platos.geometry(__window_size)


def toggle_seleccion(event):
    selected_item = tree.selection()
    tree.tag_configure("seleccionada", foreground='black',
                       background='white', font='Arial 10')
    for item in tree.get_children():
        tags = tree.item(item, 'tags')
        if item == selected_item:
            tags += ("seleccionada",)
        tree.item(item, tags=tags)


def eliminar_filas_seleccionadas():
    selected_items = tree.selection()
    indices_seleccionados = [tree.index(item) for item in selected_items]

    for index in sorted(indices_seleccionados, reverse=True):
        matriz_gestion_platos.pop(index)

    actualizar_tabla()


def actualizar_tabla():
    tree.delete(*tree.get_children())

    for i, row in enumerate(matriz_gestion_platos):
        tree.insert('', 'end', values=row, tags=(f"row{i}",))


# ____________________________________________________________________________________________________________#

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
                                  font=("Arial", 12), pady=10, command=agregar_pedidos_screen)

boton_gestion_pedidos.grid(row=3, column=0, sticky="news", padx=100, pady=10)

boton_cerrar_sesion = tk.Button(user_info_frame, text="Cerrar sesión",
                                font=("Arial", 12), pady=10)

boton_cerrar_sesion.grid(row=4, column=0, sticky="news", padx=100, pady=10)


menu_screen.geometry(__window_size)
menu_screen.withdraw()

# _______________________________________________________________________________________________________________#


# _______________________________________________________________________________________________________________#

# Crear la ventana principal platos
gestion_platos = tk.Tk()
gestion_platos.title("Tabla de Matriz")

etiqueta = tk.Label(gestion_platos, text="Mi Restaurante",
                    font=("Arial", 18), pady=10)
etiqueta.pack()

# image = tk.PhotoImage(file="logo.png")

# lab = ttk.Label(image=image)
# lab.pack()

frame = tk.Frame(gestion_platos)
frame.pack()

agregar_platos_frame = tk.LabelFrame(frame, text="Agregar platos",
                                     font=("Arial", 14), padx=50, pady=50)

agregar_platos_frame.grid(row=0, column=0, padx=100, pady=10)


# Crear la tabla
tree = ttk.Treeview(agregar_platos_frame, columns=(
    "Nombre", "Precio", "Descripción", "Disponibilidad"), show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Precio", text="Precio")
tree.heading("Descripción", text="Descripción")
tree.heading("Disponibilidad", text="Disponibilidad")

# Configurar el evento de clic
tree.bind('<ButtonRelease-1>', toggle_seleccion)

# Mostrar la tabla en la ventana principal
tree.pack()


# Crear el botón de eliminar
boton_agregar_platos = tk.Button(frame, text="Ingresar Datos", command=ingresar_datos,
                                 font=("Arial", 12), pady=0)

boton_agregar_platos.grid(row=6, column=0, sticky="nsew",  padx=10, pady=10)


boton_eliminar_platos = tk.Button(frame, text="Eliminar",  command=eliminar_filas_seleccionadas,
                                  font=("Arial", 12), pady=0)

boton_eliminar_platos.grid(row=7, column=0, sticky="nsew",  padx=10, pady=10)

boton_actualizar_platos = tk.Button(frame, text="Actualizar", command=actualizar_datos,
                                    font=("Arial", 12), pady=0)

boton_actualizar_platos.grid(row=8, column=0, sticky="nsew",  padx=10, pady=10)

boton_cancelar = tk.Button(frame, text="Cancelar", command=cancel_gestion_platos,
                           font=("Arial", 12), pady=0)
boton_cancelar.grid(row=9, column=0, sticky="nsew", padx=10, pady=10)

actualizar_tabla()

gestion_platos.withdraw()



# Crear la ventana principal
agregar_pedidos = tk.Tk()
agregar_pedidos.title("Data Entry Form")

# Etiqueta para identificar el formulario
etiqueta = tk.Label(agregar_pedidos, text="Mi Restaurante", font=("Arial", 18), pady=5)
etiqueta.grid(row=0, column=0, columnspan=2)

# Crear un marco para el formulario
frame = tk.Frame(agregar_pedidos)
frame.grid(row=1, column=0, columnspan=2)

# Marco para agregar pedidos
agregar_pedidos_frame = tk.LabelFrame(frame, text="Agregar Pedidos", font=("Arial", 14), pady=10)
agregar_pedidos_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Marco para las mesas
frame_mesas = ttk.Frame(agregar_pedidos_frame)
frame_mesas.grid(row=0, column=0, padx=5, pady=5)

label_mesas = ttk.Label(frame_mesas, text="Mesas")
label_mesas.pack()

# Treeview para mostrar las mesas
treeview_mesas = ttk.Treeview(frame_mesas)
treeview_mesas.pack()

# Marco para los platos
frame_platos = ttk.Frame(agregar_pedidos_frame)
frame_platos.grid(row=0, column=1, padx=5, pady=5)

label_platos = ttk.Label(frame_platos, text="Platos")
label_platos.pack()

# Treeview para mostrar los platos
treeview_platos = ttk.Treeview(frame_platos)
treeview_platos.pack()

# Insertar mesas ficticias en el treeview de mesas
mesas_pedidos = []
for i in range(0,len(tables)):
    mesas_pedidos.append(tables[i][0])

for mesa in mesas_pedidos:
    treeview_mesas.insert('', 'end', text=mesa, values=("Mesa " + mesa))
 
# Lista de platos 
platos_pedidos = []
for i in range(0,len(matriz_gestion_platos)):
    platos_pedidos.append(matriz_gestion_platos[i][0])
    
# Insertar platos  en el treeview de platos
for plato in platos_pedidos:
    treeview_platos.insert('', 'end', text=plato, values=(plato))

# Botón para reservar un pedido
boton_reservar = ttk.Button(agregar_pedidos_frame, text="Reservar Pedido", command=reservar_pedido)
boton_reservar.grid(row=1, column=0, padx=10, pady=5, sticky="news")

# Botón para mostrar pedidos
boton_mostrar = ttk.Button(agregar_pedidos_frame, text="Mostrar Pedidos", command=mostrar_pedidos)
boton_mostrar.grid(row=1, column=1, padx=10, pady=5, sticky="news")
btn_salir = tk.Button(agregar_pedidos_frame, text="Salir", command = lambda: (agregar_pedidos.withdraw(), menu_screen.deiconify()))
btn_salir.grid(row=2, column=1, padx=10, pady=5, sticky="news")

# Configurar el tamaño de la ventana (reemplazar __window_size con el tamaño deseado)
agregar_pedidos.geometry(__window_size)
# Ocultar la ventana por defecto
agregar_pedidos.withdraw()

# Iniciar el bucle principal de la aplicación
# Natalia0506*
# _______________________________________________________________________________________________________________#
home_scren.mainloop()
registry_user_screen.mainloop()
menu_screen.mainloop()
init_sesion_screen.mainloop()
gestion_platos.mainloop()
agregar_platos_frame.mainloop()
boton_gestion_pedidos.mainloop()
agregar_pedidos_frame.mainloop()
