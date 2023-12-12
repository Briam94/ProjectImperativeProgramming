import tkinter as tk
import re
from tkinter import messagebox
import hashlib

regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,20}$"
__window_size = "450x400+400+200"

# open and close screen/window


def close_and_open_screen(window_to_close, window_to_open):
    window_to_close.withdraw()
    window_to_open.deiconify()


def registry_screen():
    close_and_open_screen(home_scren, registry_user_screen)


def login_screen():
    close_and_open_screen(home_scren, init_sesion_screen)


def cancel_registry_user():
    close_and_open_screen(registry_user_screen, home_scren)


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


# BUTTON
login_button = tk.Button(
    init_sesion_screen, text="INICIAR SESION", command=login)
login_button.pack()

cancel_login_button = tk.Button(
    init_sesion_screen, text="Cancelar", command=cancel_login)
cancel_login_button.pack()


# PLACES
login_button.place(x=120, y=280)
cancel_login_button.place(x=250, y=280)

init_sesion_screen.geometry(__window_size)

# MENU SCREEN
menu_screen = tk.Tk()
menu_screen.geometry("200x300")
menu_screen.title("Mi Restaurante")

etiqueta = tk.Label(menu_screen, text="Mi Restaurante",
                 font=("Arial", 18), pady=10)
etiqueta.pack(side=tk.TOP, pady=10)


campo_menu_screen = tk.Frame(menu_screen, background="red")
campo_menu_screen.pack(pady=20)

# Configurar el campo1 para que se expanda correctamente
campo_menu_screen.columnconfigure(0, weight=1)
campo_menu_screen.rowconfigure(0, weight=1)

# Etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(
    campo_menu_screen, text="Bienvenido", background="red")
etiqueta_bienvenida.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# # Botones
boton_gestion_platos = tk.Button(campo_menu_screen, text="Gestión platos")
boton_gestion_platos.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

boton_gestion_mesas = tk.Button(campo_menu_screen, text="Gestión mesas")
boton_gestion_mesas.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

boton_gestion_pedidos = tk.Button(campo_menu_screen, text="Gestión pedidos")
boton_gestion_pedidos.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

boton_cerrar_sesion = tk.Button(campo_menu_screen, text="Cerrar sesión")
boton_cerrar_sesion.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

menu_screen.withdraw()

home_scren.mainloop()
registry_user_screen.mainloop()
menu_screen.mainloop()
init_sesion_screen.mainloop()
