import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox
import hashlib

regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,20}$"
__window_size = "450x400+400+200"

matriz_gestion_platos = []
table_management_columns = ('mesa', 'fecha', 'hora', 'n.personas')

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


def gestion_platos_screen():
    close_and_open_screen(menu_screen, gestion_platos)


def registry_screen():
    close_and_open_screen(home_scren, registry_user_screen)


def login_screen():
    close_and_open_screen(home_scren, init_sesion_screen)


def cancel_registry_user():
    close_and_open_screen(registry_user_screen, home_scren)


def cancel_login():
    close_and_open_screen(init_sesion_screen, home_scren)


def table_management():
    close_and_open_screen(menu_screen, table_management_screen)


def cancel_registry_table():
    close_and_open_screen(table_management_screen, menu_screen)


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
                users_file = open("users.txt", "r")
                data = users_file.readlines()
                users_file.close()
                print(data)
                try:
                    index = data.index(email+separator)
                except ValueError:
                    index = -1
                if index >= 0:
                    show_error(
                        'Error', 'Ya existe un usuario registrado con ' + email)
                else:
                    password = hashlib.sha256(password.encode())
                    data.append(email + separator)
                    data.append(password.hexdigest() + separator)
                    print(data)
                    users_file = open("users.txt", "w")
                    users_file.writelines(data)
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


def registry_table():
    tables = []
    separator = '\n'
    table_number = registry_table_entry.get()
    table_date = registry_table_date_entry.get()
    table_time = registry_table_time_entry.get()
    table_number_persons = registry_table_number_persons_entry.get()
    if table_number != '' and table_date != '' and table_time != '' and table_number_persons != '':
        tables_file = open(
            "D:/univalle/programacion imperativa/ejercicios de clase/proyecto/tables.txt", "r")
        data = tables_file.readlines()
        tables_file.close()
        print('data', data)
        table_status = validate_table(
            data, table_number, table_date, table_time)
        if table_status == True:
            tables.append((f'{table_number}',
                           f'{table_date}',
                           f'{table_time}',
                           f'{table_number_persons}'))
            data.append(table_number + separator)
            data.append(table_date + separator)
            data.append(table_time + separator)
            data.append(table_number_persons + separator)
            tables_file = open(
                "D:/univalle/programacion imperativa/ejercicios de clase/proyecto/tables.txt", "w")
            tables_file.writelines(data)
            tables_file.close()
            print('tables', tables)
            for table in tables:
                print('table', table)
                table_management_table.insert('', tk.END, values=table)
            registry_table_entry.delete(0, tk.END)
            registry_table_date_entry.delete(0, tk.END)
            registry_table_time_entry.delete(0, tk.END)
            registry_table_number_persons_entry.delete(0, tk.END)
        else:
            show_error('Mesa no disponible',
                       'La mesa seleccionada no esta disponible en la fecha y hora seleccionada')
    else:
        show_error('Informacion incompleta', 'Faltan campos por diligenciar')


def validate_table(tables, table_number, table_date, table_time):
    tables_to_validate = []
    print(data)
    counter = 0
    table = ''
    for i in tables:
        print('i', i)
        table = table + i.replace('\n', ',')
        counter += 1
        if counter == 4:
            counter = 0
            table = table.split(',')
            print('table', table)
            tables_to_validate.append((f'{table[0]}', f'{table[1]}',
                                       f'{table[2]}', f'{table[3]}'))
            table = ''
    print('table to validate', tables_to_validate)
    for table in tables_to_validate:
        print('table data', table)
        if (table[0] == table_number
            and table[1] == table_date
                and table[2] == table_time):
            return False
    return True


def delete_table():
    table_number = registry_table_entry.get()
    table_date = registry_table_date_entry.get()
    table_time = registry_table_time_entry.get()
    tables_file = open(
        "D:/univalle/programacion imperativa/ejercicios de clase/proyecto/tables.txt", "r")
    data = tables_file.readlines()
    tables = format_table(data)
    tables_file.close()
    for table in tables:
        if table[0] == table_number and table[1] == table_date and table[2] == table_time:
            tables.remove(table)
            clear_data_table(table)


def inser_data_table(tables):
    for table in tables:
        table_management_table.insert('', tk.END, values=table)


def clear_data_table(table):
    table_management_table.delete(table)


def format_table(data):
    tables = []
    counter = 0
    table = ''
    for i in data:
        print('i', i)
        table = table + i.replace('\n', ',')
        counter += 1
        if counter == 4:
            counter = 0
            table = table.split(',')
            print('table', table)
            tables.append((f'{table[0]}', f'{table[1]}',
                           f'{table[2]}', f'{table[3]}'))
            table = ''
    return tables


def show_error(title_error, text_error):
    messagebox.showerror(title_error, text_error)


def show_successful(title, text):
    messagebox.showinfo(title, text)


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
                                font=("Arial", 12), pady=10, command=table_management)

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

boton_gestion_mesas = tk.Button(user_info_frame, text="Eliminar",
                                font=("Arial", 10), pady=10)

boton_gestion_mesas.grid(row=2, column=0, sticky="news", padx=100, pady=10)

boton_gestion_pedidos = tk.Button(user_info_frame, text="Actualizar",
                                  font=("Arial", 10), pady=10)

boton_gestion_pedidos.grid(row=3, column=0, sticky="news", padx=100, pady=10)


gestion_platos.withdraw()
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

boton_imprimir = tk.Button(frame, text="Imprimir", command=imprimir_matriz)
boton_imprimir.grid(row=7, column=0, sticky="news", padx=30, pady=10)

agregar_platos.geometry(__window_size)
agregar_platos.withdraw()

# MANAGEMENT TABLE
table_management_screen = tk.Tk()
table_management_screen.title("Gestión mesas")

table_management_table = ttk.Treeview(table_management_screen,
                                      columns=table_management_columns, show='headings')

table_management_table.heading('mesa', text='Mesa')
table_management_table.heading('fecha', text='Fecha')
table_management_table.heading('hora', text='Hora')
table_management_table.heading('n.personas', text='N.personas')

tables_file = open(
    "D:/univalle/programacion imperativa/ejercicios de clase/proyecto/tables.txt", "r")
data = tables_file.readlines()
tables = []
print(data)
counter = 0
table = ''
for i in data:
    print('i', i)
    table = table + i.replace('\n', ',')
    counter += 1
    if counter == 4:
        counter = 0
        table = table.split(',')
        print('table', table)
        tables.append((f'{table[0]}', f'{table[1]}',
                      f'{table[2]}', f'{table[3]}'))
        table = ''
print('tables', tables)
tables_file.close()
for table in tables:
    table_management_table.insert('', tk.END, values=table)

table_management_table.grid(row=0, column=0, sticky='nsew')
scrollbar = ttk.Scrollbar(table_management_screen,
                          orient=tk.VERTICAL, command=table_management_table.yview)
table_management_table.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# LABELS
registry_table_num = tk.Label(
    table_management_screen, text="Mesa", font=("Arial", 10), pady=10)
registry_table_num.grid(row=10, column=0)
registry_table_entry = tk.Entry(table_management_screen)
registry_table_entry.grid(row=15, column=0)

registry_table_date = tk.Label(
    table_management_screen, text="Fecha", font=("Arial", 10), pady=10)
registry_table_date.grid()
registry_table_date_entry = tk.Entry(table_management_screen)
registry_table_date_entry.grid()

registry_table_time = tk.Label(
    table_management_screen, text="Hora", font=("Arial", 10), pady=10)
registry_table_time.grid()
registry_table_time_entry = tk.Entry(table_management_screen)
registry_table_time_entry.grid()

registry_table_number_persons = tk.Label(
    table_management_screen, text="N. personas", font=("Arial", 10), pady=10)
registry_table_number_persons.grid()
registry_table_number_persons_entry = tk.Entry(table_management_screen)
registry_table_number_persons_entry.grid()

registry_table_button = tk.Button(
    table_management_screen, text="Registrar", command=registry_table)
registry_table_button.grid()

delete_registry_table_button = tk.Button(
    table_management_screen, text="Eliminar", command=delete_table)
delete_registry_table_button.grid()

update_table_button = tk.Button(
    table_management_screen, text="Actualizar",)
update_table_button.grid()

cancel_registry_table_button = tk.Button(
    table_management_screen, text="Cancelar", command=cancel_registry_table)
cancel_registry_table_button.grid()

registry_table_num.place(x=200, y=280)
registry_table_entry.place(x=250, y=290)

registry_table_date.place(x=500, y=280)
registry_table_date_entry.place(x=560, y=290)

registry_table_time.place(x=200, y=350)
registry_table_time_entry.place(x=250, y=360)

registry_table_number_persons.place(x=500, y=350)
registry_table_number_persons_entry.place(x=560, y=360)


registry_table_button.place(x=200, y=450)
delete_registry_table_button.place(x=300, y=450)
update_table_button.place(x=400, y=450)
cancel_registry_table_button.place(x=500, y=450)

table_management_screen.withdraw()
table_management_screen.geometry('830x500+300+100')
# _______________________________________________________________________________________________________________#
home_scren.mainloop()
registry_user_screen.mainloop()
menu_screen.mainloop()
init_sesion_screen.mainloop()
gestion_platos.mainloop()
table_management_screen.mainloop()
agregar_platos_frame.mainloop()
