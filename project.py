import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox
import hashlib
import random

__window_size = "450x400+400+100"
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,20}$"

matrix_management_dishes = [['caldo', '5000', 'es un caldo', 'si'], [
    'arroz', '1300', 'es un arroz', 'no']]
order_list = []
table_management_columns = ('table', 'date', 'hour', 'n.personas')
tables = [('1', '20/10/2023', '10:00', '4'), ('2', '20/10/2023',
                                              '14:00', '5'), ('12', '12/10/1990', '14:00', '4')]


def close_and_open_screen(window_to_close, window_to_open):
    window_to_close.withdraw()
    window_to_open.deiconify()


def management_plates_screen():
    close_and_open_screen(menu_screen, dish_management)


def add_orders_screen():
    update_board1()
    close_and_open_screen(menu_screen, add_orders)


def registry_screen():
    close_and_open_screen(home_scren, registry_user_screen)


def login_screen():
    close_and_open_screen(home_scren, init_sesion_screen)


def cancel_registry_user():
    close_and_open_screen(registry_user_screen, home_scren)


def cancel_gestion_dishes():
    close_and_open_screen(dish_management, menu_screen)


def cancel_login():
    close_and_open_screen(init_sesion_screen, home_scren)


def cancel_table_management():
    close_and_open_screen(table_management_screen, menu_screen)


def table_management():
    close_and_open_screen(menu_screen, table_management_screen)


def log_out():
    close_and_open_screen(menu_screen, home_scren)


def update_board1():
    treeview_dishes.delete(*treeview_dishes.get_children())
    treeview_tables.delete(*treeview_tables.get_children())
    tables_orders = []
    for i in range(0, len(tables)):
        tables_orders.append(tables[i][0])

    for table in tables_orders:
        treeview_tables.insert('', 'end', text=table,
                               values=("table " + table))

    # Lista de dishes
    dishes_orders = []
    for i in range(0, len(matrix_management_dishes)):
        dishes_orders.append(matrix_management_dishes[i][0])

    # Insertar dishes  en el treeview de dishes
    for plato in dishes_orders:
        treeview_dishes.insert('', 'end', text=plato, values=(plato))


# _____________________________________________________________________________________#

# Order management features

def reserve_order():
    selected_table = treeview_tables.item(treeview_tables.focus())['text']
    dish_selected = treeview_dishes.item(treeview_dishes.focus())['text']

    # Generar un número aleatorio de order
    asked_number = random.randint(1000, 9999)
    current_order = {
        "ID": asked_number,
        "Table": selected_table,
        "Dish": dish_selected
    }
    order_list.append(current_order)

# Function to show the orders


def show_orders():
    add_orders.withdraw()
    orders_window = tk.Tk()
    orders_window.title("orders")
    orders_window.geometry(__window_size)

    def eliminate_order():
        selected_item = tree.focus()
        if selected_item:
            index = int(tree.item(selected_item, 'text'))
            tree.delete(selected_item)
            del order_list[index]

    tree = ttk.Treeview(orders_window, columns=(
        "ID", "Table", "Dish"), selectmode="browse")
    tree.heading("#0", text="Índice")
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Table")
    tree.heading("#3", text="Dish")
    tree.column("#0", width=60)
    tree.column("#1", width=60)
    tree.column("#2", width=60)
    tree.column("#3", width=120)

    for i, order in enumerate(order_list):
        tree.insert("", "end", text=str(i), values=(
            order["ID"], order["Table"], order["Dish"]))

    tree.pack(padx=20, pady=10)

    btn_eliminate = tk.Button(
        orders_window, text="eliminate order", command=eliminate_order)
    btn_eliminate.pack(pady=5)

    btn_go_out = tk.Button(orders_window, text="go_out", command=lambda: (
        orders_window.destroy(), add_orders.deiconify()))
    btn_go_out.pack(pady=5)

    orders_window.mainloop()


# _____________________________________________________________________________________#

# Funciones de gestion de dishes

def update_data():
    # Resto del código...
    selection = tree.selection()
    if not selection:
        messagebox.showinfo("Error", "No row has been selected.")
        return
    if selection:
        # Get the values ​​of the selected row
        values = tree.item(selection)['values']

        update_dishes = tk.Tk()
        update_dishes.title("Data Entry Form")

        # Create the text fields and show the values ​​of the selected row

        label = tk.Label(update_dishes, text="Grill House",
                         font=("Arial", 18), pady=10)
        label.pack()
        frame = tk.Frame(update_dishes)
        frame.pack()

        add_dishes_frame = tk.LabelFrame(frame, text="add dishes",
                                         font=("Arial", 14), pady=10)

        add_dishes_frame.grid(row=0, column=0, padx=100, pady=10)

        space_label = tk.Label(add_dishes_frame, text="")
        space_label.grid(row=0, column=0)
        space_label = tk.Label(add_dishes_frame, text="")
        space_label.grid(row=0, column=1)

        name_label = tk.Label(add_dishes_frame, text="name",
                              font=("Arial", 12), pady=10)
        name_label.grid(row=1, column=0)
        price_label = tk.Label(add_dishes_frame, text="price",
                               font=("Arial", 12), pady=10)
        price_label.grid(row=1, column=2)

        name__entry = tk.Entry(add_dishes_frame)
        price_entry = tk.Entry(add_dishes_frame)
        name__entry.grid(row=2, column=0)
        price_entry.grid(row=2, column=2)

        space_label = tk.Label(add_dishes_frame, text="")
        space_label.grid(row=3, column=0)
        space_label = tk.Label(add_dishes_frame, text="")
        space_label.grid(row=3, column=1)

        description_label = tk.Label(add_dishes_frame, text="Description",
                                     font=("Arial", 12), pady=10)

        description_label.grid(row=4, column=0)
        availability_label = tk.Label(add_dishes_frame, text="availability",
                                      font=("Arial", 12), pady=10)

        availability_label.grid(row=4, column=2)

        description_entry = tk.Entry(
            add_dishes_frame)
        availability_entry = tk.Entry(
            add_dishes_frame)
        description_entry.grid(row=5, column=0)
        availability_entry.grid(row=5, column=2)

        name__entry.insert(0, values[0])
        price_entry.insert(0, values[1])
        description_entry.insert(0, values[2])
        availability_entry.insert(0, values[3])

    def update_row():
        # Get the news values ​​of the text fields
        new_name = name__entry.get()
        new_price = price_entry.get()
        new_description = description_entry.get()
        new_availability = availability_entry.get()

    # update the values ​​in the table
        selection = tree.selection()
        if selection:
            tree.item(selection, values=(new_name, new_price,
                      new_description, new_availability))

            update_dishes.destroy()

        # add el botón de update
    button_update_dishes = tk.Button(frame, text="update", command=update_row,
                                     font=("Arial", 12), pady=10)

    button_update_dishes.grid(
        row=6, column=0, sticky="news", padx=20, pady=5)

    button_cancel = tk.Button(
        frame, text="cancel", command=update_dishes.destroy, font=("Arial", 12), pady=10)
    button_cancel.grid(row=7, column=0, sticky="news", padx=20, pady=5)

    update_dishes.geometry(__window_size)

# Enter data into the dishes table


def enter_data():
    add_dishes = tk.Tk()
    add_dishes.title("Data Entry Form")

    label = tk.Label(add_dishes, text="Grill House",
                     font=("Arial", 18), pady=10)
    label.pack()
    frame = tk.Frame(add_dishes)
    frame.pack()

    add_dishes_frame = tk.LabelFrame(frame, text="add dishes",
                                     font=("Arial", 14), pady=10)

    add_dishes_frame.grid(row=0, column=0, padx=100, pady=10)

    space_label = tk.Label(add_dishes_frame, text="")
    space_label.grid(row=0, column=0)
    space_label = tk.Label(add_dishes_frame, text="")
    space_label.grid(row=0, column=1)

    name_label = tk.Label(add_dishes_frame, text="name",
                          font=("Arial", 12), pady=10)
    name_label.grid(row=1, column=0)
    price_label = tk.Label(add_dishes_frame, text="price",
                           font=("Arial", 12), pady=10)
    price_label.grid(row=1, column=2)

    name__entry = tk.Entry(add_dishes_frame)
    price_entry = tk.Entry(add_dishes_frame)
    name__entry.grid(row=2, column=0)
    price_entry.grid(row=2, column=2)

    space_label = tk.Label(add_dishes_frame, text="")
    space_label.grid(row=3, column=0)
    space_label = tk.Label(add_dishes_frame, text="")
    space_label.grid(row=3, column=1)

    description_label = tk.Label(add_dishes_frame, text="Description",
                                 font=("Arial", 12), pady=10)

    description_label.grid(row=4, column=0)
    availability_label = tk.Label(add_dishes_frame, text="availability",
                                  font=("Arial", 12), pady=10)

    availability_label.grid(row=4, column=2)

    description_entry = tk.Entry(add_dishes_frame)
    availability_entry = tk.Entry(add_dishes_frame)
    description_entry.grid(row=5, column=0)
    availability_entry.grid(row=5, column=2)

# Función para add una row a la board de dishes
    def add_row():

        name = name__entry.get()
        price = price_entry.get()
        description = description_entry.get()
        availability = availability_entry.get()

        if not name:
            messagebox.showerror("Error", "The name field is required")
            return

        # Validación del campo price
        if not price.isdigit() or int(price) <= 0:
            messagebox.showerror(
                "Error", "The price field must be a number greater than 0")
            return

        # Validación del campo Description
        if len(description) > 100:
            messagebox.showerror(
                "Error", "The description field cannot be more than 100 characters")
            return

        # Validación del campo availability
        if availability.lower() not in ["si", "no"]:
            messagebox.showerror(
                "Error", "The availability field can only be 'si' or 'no'")
            return

        row = [name, price, description, availability]
        matrix_management_dishes.append(row)
        update_board()
        add_dishes.destroy()

    button_add_dishes = tk.Button(frame, text="add", command=add_row,
                                  font=("Arial", 12), pady=10)

    button_add_dishes.grid(row=6, column=0, sticky="news", padx=20, pady=5)

    button_cancel = tk.Button(
        frame, text="cancel", command=add_dishes.destroy, font=("Arial", 12), pady=10)
    button_cancel.grid(row=7, column=0, sticky="news", padx=20, pady=5)

    add_dishes.geometry(__window_size)

# Function to change the color of the selected row


def toggle_selection(event):
    selected_item = tree.selection()
    tree.tag_configure("selected", foreground='black',
                       background='white', font='Arial 10')
    for item in tree.get_children():
        tags = tree.item(item, 'tags')
        if item == selected_item:
            tags += ("selected",)
        tree.item(item, tags=tags)

# Function to eliminate a row from the dishes table


def eliminate_rows_selecteds():
    selected_items = tree.selection()
    indices_selected = [tree.index(item) for item in selected_items]

    for index in sorted(indices_selected, reverse=True):
        matrix_management_dishes.pop(index)

    update_board()

# Function to update the dishes table


def update_board():
    tree.delete(*tree.get_children())

    for i, row in enumerate(matrix_management_dishes):
        tree.insert('', 'end', values=row, tags=(f"row{i}",))


# ____________________________________________________________________________________________________________#


# Table management functions


def update_data_table():
    selection = table_management_table.selection()
    if not selection:
        messagebox.showinfo("Error", "No row has been selected.")
        return
    if selection:
        # getting values of the selected table
        values = table_management_table.item(selection)['values']

        update_table = tk.Tk()
        update_table.title("update table")

        tag = tk.Label(update_table, text="Grill House",
                       font=("Arial", 18), pady=10)
        tag.pack()
        frame = tk.Frame(update_table)
        frame.pack()

        update_table_frame = tk.LabelFrame(frame, text="add table",
                                           font=("Arial", 14), pady=10)

        update_table_frame.grid(row=0, column=0, padx=100, pady=10)

        label_space = tk.Label(update_table_frame, text="")
        label_space.grid(row=0, column=0)
        label_space = tk.Label(update_table_frame, text="")
        label_space.grid(row=0, column=1)

        table_label = tk.Label(update_table_frame, text="Table",
                               font=("Arial", 12), pady=10)
        table_label.grid(row=1, column=0)
        date_label = tk.Label(update_table_frame, text="date",
                              font=("Arial", 12), pady=10)
        date_label.grid(row=1, column=2)

        table__entry = tk.Entry(update_table_frame)
        date_entry = tk.Entry(update_table_frame)
        table__entry.grid(row=2, column=0)
        date_entry.grid(row=2, column=2)

        label_space = tk.Label(update_table_frame, text="")
        label_space.grid(row=3, column=0)
        label_space = tk.Label(update_table_frame, text="")
        label_space.grid(row=3, column=1)

        time_label = tk.Label(update_table_frame, text="Hour",
                              font=("Arial", 12), pady=10)

        time_label.grid(row=4, column=0)
        number_person_label = tk.Label(update_table_frame, text="N. personas",
                                       font=("Arial", 12), pady=10)

        number_person_label.grid(row=4, column=2)

        time_entry = tk.Entry(
            update_table_frame)
        number_person_entry = tk.Entry(
            update_table_frame)
        time_entry.grid(row=5, column=0)
        number_person_entry.grid(row=5, column=2)

        table__entry.insert(0, values[0])
        date_entry.insert(0, values[1])
        time_entry.insert(0, values[2])
        number_person_entry.insert(0, values[3])

    def update_row():
        # Get new values
        new_table = table__entry.get()
        new_date = date_entry.get()
        new_time = time_entry.get()
        new_number_person = number_person_entry.get()

        table_status = validate_table(new_table, new_date, new_time)

        # Update values of the table
        if table_status == True:
            selection = table_management_table.selection()
            if selection:
                table_management_table.item(selection, values=(new_table, new_date,
                                                               new_time, new_number_person))

                update_table.destroy()
        else:
            show_error('Table not available',
                       'The table selected is not available on the date selected')

    update_table_button = tk.Button(frame, text="update", command=update_row,
                                    font=("Arial", 12), pady=10)

    update_table_button.grid(
        row=6, column=0, sticky="news", padx=20, pady=5)

    button_cancel = tk.Button(
        frame, text="cancel", command=update_table.destroy, font=("Arial", 12), pady=10)
    button_cancel.grid(row=7, column=0, sticky="news", padx=20, pady=5)

    update_table.geometry(__window_size)


def validate_table(new_table, date, time):
    for table in tables:
        if table[0] == new_table and table[1] == date and table[2] == time:
            return False
    return True


def regitry_table():
    regitry_table_screen = tk.Tk()
    regitry_table_screen.title("Registrar tables")

    title_regitry_table_screen = tk.Label(regitry_table_screen, text="Grill House",
                                          font=("Arial", 18), pady=10)
    title_regitry_table_screen.pack()
    frame = tk.Frame(regitry_table_screen)
    frame.pack()

    regitry_table_screen_frame = tk.LabelFrame(frame, text="add tables",
                                               font=("Arial", 14), pady=10)

    regitry_table_screen_frame.grid(row=0, column=0, padx=100, pady=10)

    label_space = tk.Label(regitry_table_screen_frame, text="")
    label_space.grid(row=0, column=0)
    label_space = tk.Label(regitry_table_screen_frame, text="")
    label_space.grid(row=0, column=1)

    table_label = tk.Label(regitry_table_screen_frame, text="Table",
                           font=("Arial", 12), pady=10)
    table_label.grid(row=1, column=0)
    date_label = tk.Label(regitry_table_screen_frame, text="date",
                          font=("Arial", 12), pady=10)
    date_label.grid(row=1, column=2)

    table__entry = tk.Entry(regitry_table_screen_frame)
    date_entry = tk.Entry(regitry_table_screen_frame)
    table__entry.grid(row=2, column=0)
    date_entry.grid(row=2, column=2)

    label_space = tk.Label(regitry_table_screen_frame, text="")
    label_space.grid(row=3, column=0)
    label_space = tk.Label(regitry_table_screen_frame, text="")
    label_space.grid(row=3, column=1)

    time_label = tk.Label(regitry_table_screen_frame, text="Hour",
                          font=("Arial", 12), pady=10)

    time_label.grid(row=4, column=0)
    number_person_label = tk.Label(regitry_table_screen_frame, text="N.personas",
                                   font=("Arial", 12), pady=10)

    number_person_label.grid(row=4, column=2)

    time_entry = tk.Entry(regitry_table_screen_frame)
    number_person_entry = tk.Entry(regitry_table_screen_frame)
    time_entry.grid(row=5, column=0)
    number_person_entry.grid(row=5, column=2)

    def add_new_record():
        table = table__entry.get()
        date = date_entry.get()
        time = time_entry.get()
        number_person = number_person_entry.get()
        table_status = validate_table(table, date, time)
        if table_status == True:
            if not table or not date or not time or not number_person:
                return show_error("Error", "All fields are required")

            new_record = [table, date, time, number_person]
            tables.append(new_record)
            update_table()
            regitry_table_screen.destroy()
        else:
            show_error('Table not available',
                       'The table selected is not available on the date selected')

    add_table = tk.Button(frame, text="add", command=add_new_record,
                          font=("Arial", 12), pady=10)

    add_table.grid(row=6, column=0, sticky="news", padx=20, pady=5)

    button_cancel = tk.Button(
        frame, text="cancel", command=regitry_table_screen.destroy, font=("Arial", 12), pady=10)
    button_cancel.grid(row=7, column=0, sticky="news", padx=20, pady=5)

    regitry_table_screen.geometry(__window_size)


def toggle_selection_table(event):
    selected_item = table_management_table.selection()
    table_management_table.tag_configure("selected", foreground='black',
                                         background='white', font='Arial 10')
    for item in table_management_table.get_children():
        tags = table_management_table.item(item, 'tags')
        if item == selected_item:
            tags += ("selected",)
        table_management_table.item(item, tags=tags)


def delete_row_seleted_table():
    selected_items = table_management_table.selection()
    indices_selected = [table_management_table.index(
        item) for item in selected_items]

    for index in sorted(indices_selected, reverse=True):
        tables.pop(index)

    update_table()


def update_table():
    table_management_table.delete(*table_management_table.get_children())

    for i, row in enumerate(tables):
        table_management_table.insert('', 'end', values=row, tags=(f"row{i}",))

# ____________________________________________________________________________________________________________#


# Funtion REGISTRY USER SCREEN
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
                try:
                    index = data.index(email+separator)
                except ValueError:
                    index = -1
                if index >= 0:
                    show_error(
                        'Error', 'There is already a registered user with ' + email)
                else:
                    password = hashlib.sha256(password.encode())
                    data.append(email + separator)
                    data.append(password.hexdigest() + separator)
                    users_file = open("users.txt", "w")
                    users_file.writelines(data)
                    users_file.close()
                    show_successful(
                        "SUCCESSFUL", "the user was saved successfully")
                    email_registry_user_entry.delete(0, tk.END)
                    password_registry_user_entry.delete(0, tk.END)
                    confirm_password_registry_user_entry.delete(0, tk.END)
            else:
                show_error(
                    'Password', 'The password must contain 1 uppercase letter, 1 number, 1 lowercase letter, 1 special character and a minimum of 10 characters.')
        else:
            show_error('Password', 'Passwords do not match.')
    else:
        show_error('Correo invalido',
                   'The email entered does not have the correct structure.')

# Funtion LOGIN SCREEN


def login():
    email = email_login_entry.get()
    password = hashlib.sha256(password_login_entry.get().encode())
    users_file = open("users.txt", "r")
    data = users_file.readlines()
    users = []
    for i in data:
        users.append(i.replace('\n', ''))
    try:
        index = users.index(email)
        if users[index] == email and users[index+1] == password.hexdigest():
            email_login_entry.delete(0, tk.END)
            password_login_entry.delete(0, tk.END)
            close_and_open_screen(init_sesion_screen, menu_screen)
        else:
            show_error('Usuario incorrecto', 'Usuario y/o correo invalidos')
    except:
        show_error('Usuario incorrecto', 'Usuario y/o correo invalidos')


def show_error(title_error, text_error):
    messagebox.showerror(title_error, text_error)


def show_successful(title, text):
    messagebox.showinfo(title, text)


# HOME PRINCIPAL
home_scren = tk.Tk()
home_scren.title("Proyecto final")

# LABELS
title = tk.Label(home_scren, text="𝑮𝑹𝑰𝑳𝑳 𝑯𝑶𝑼𝑺𝑬",
                 font=("Arial", 30), pady=10)
title.pack()

image = tk.PhotoImage(file="logo.png")

lab = ttk.Label(image=image)
lab.pack()

title_description = tk.Label(home_scren,
                             text="𝙾𝚞𝚛 𝚛𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝 𝚒𝚜 𝚊 𝚙𝚕𝚊𝚌𝚎 𝚠𝚑𝚎𝚛𝚎 𝚠𝚎 𝚘𝚏𝚏𝚎𝚛 𝚊 𝚟𝚊𝚛𝚒𝚎𝚝𝚢 𝚘𝚏\n𝚍𝚎𝚕𝚒𝚌𝚒𝚘𝚞𝚜 𝚍𝚒𝚜𝚑𝚎𝚜 𝚊𝚗𝚍 𝚌𝚞𝚕𝚒𝚗𝚊𝚛𝚢 𝚛𝚎𝚜𝚘𝚞𝚛𝚌𝚎𝚜 𝚝𝚘 𝚝𝚑𝚎 𝚙𝚞𝚋𝚕𝚒𝚌\n𝚌𝚞𝚕𝚒𝚗𝚊𝚛𝚢 𝚗𝚎𝚎𝚍𝚜 𝚊𝚗𝚍 𝚖𝚊𝚔𝚎 𝚢𝚘𝚞 𝚎𝚗𝚓𝚘𝚢 𝚊𝚗 𝚎𝚡𝚌𝚎𝚙𝚝𝚒𝚘𝚗𝚊𝚕 \n𝚐𝚊𝚜𝚝𝚛𝚘𝚗𝚘𝚖𝚒𝚌 𝚎𝚡𝚙𝚎𝚛𝚒𝚎𝚗𝚌𝚎.",
                             font=("Arial", 12), justify="left", pady=8)
title_description.pack()


# Buttons
registry_button = tk.Button(
    home_scren, text="𝐂𝐇𝐄𝐂𝐊 𝐈𝐍", command=registry_screen)
registry_button.pack()

init_sesion_button = tk.Button(
    home_scren, text="𝐋𝐎𝐆 𝐈𝐍", command=login_screen)
init_sesion_button.pack()


# Generate window size
home_scren.geometry(__window_size)

# REGISTRY USER SCREEN
registry_user_screen = tk.Tk()
registry_user_screen.title("Registrar usuario")
registry_user_screen.withdraw()

title_user = tk.Label(registry_user_screen, text="Grill House",
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
    registry_user_screen, text="Password", font=("Arial", 10), pady=10)
password_registry_user.pack()
password_registry_user_entry = tk.Entry(registry_user_screen, show="*")
password_registry_user_entry.pack()


confirm_password_registry_user = tk.Label(
    registry_user_screen, text="Cofirmar Password", font=("Arial", 10), pady=10)
confirm_password_registry_user.pack()
confirm_password_registry_user_entry = tk.Entry(
    registry_user_screen, show="*")
confirm_password_registry_user_entry.pack()

# BUTTON
registry_user_button = tk.Button(
    registry_user_screen, text="Registrar", command=registry_user)
registry_user_button.pack()

cancel_registry_user_button = tk.Button(
    registry_user_screen, text="cancel", command=cancel_registry_user)
cancel_registry_user_button.pack()

# PLACES
registry_user_button.place(x=170, y=280)
cancel_registry_user_button.place(x=250, y=280)

registry_user_screen.geometry(__window_size)


# LOGIN SCREEN
init_sesion_screen = tk.Tk()
init_sesion_screen.title("Log in")
init_sesion_screen.withdraw()


# LABELS AND ENTRY
sub_title_login = tk.Label(
    init_sesion_screen, text="Login", font=("Arial", 10), pady=10)
sub_title_login.pack()

email_login = tk.Label(
    init_sesion_screen, text="Email", font=("Arial", 10), pady=10)
email_login.pack()
email_login_entry = tk.Entry(init_sesion_screen)
email_login_entry.pack()

password_login = tk.Label(
    init_sesion_screen, text="Password", font=("Arial", 10), pady=10)
password_login.pack()
password_login_entry = tk.Entry(init_sesion_screen, show="*")
password_login_entry.pack()

# _______________________________________________________________________________________________________________#

# BUTTON LOGIN
login_button = tk.Button(
    init_sesion_screen, text="Log in", command=login)
login_button.pack()

cancel_login_button = tk.Button(
    init_sesion_screen, text="cancel", command=cancel_login)
cancel_login_button.pack()

# _______________________________________________________________________________________________________________#

# PLACES
# Ubicacion de los botones en la pantalla de inicio de sesion
login_button.place(x=120, y=280)
cancel_login_button.place(x=250, y=280)

init_sesion_screen.geometry(__window_size)

# _______________________________________________________________________________________________________________#

# MENU SCREEN
menu_screen = tk.Tk()
menu_screen.title("Data Entry Form")

label = tk.Label(menu_screen, text="Grill House",
                 font=("Arial", 18), pady=10)
label.pack()
frame = tk.Frame(menu_screen)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="Welcome",
                                font=("Arial", 14), pady=10)
user_info_frame.grid(row=0, column=0, padx=10, pady=10)


# creacion de los botones de la pantalla de menu
button_dish_management = tk.Button(user_info_frame, text="Management dishes", command=management_plates_screen,
                                   font=("Arial", 12), pady=10)

button_dish_management.grid(row=1, column=0, sticky="news", padx=100, pady=10)

button_gestion_tables = tk.Button(user_info_frame, text="Management tables",
                                  font=("Arial", 12), pady=10, command=table_management)

button_gestion_tables.grid(row=2, column=0, sticky="news", padx=100, pady=10)

button_gestion_orders = tk.Button(user_info_frame, text="Management orders",
                                  font=("Arial", 12), pady=10, command=add_orders_screen)

button_gestion_orders.grid(row=3, column=0, sticky="news", padx=100, pady=10)

button_cerrar_sesion = tk.Button(user_info_frame, text="Sign off",
                                 font=("Arial", 12), pady=10, command=log_out)

button_cerrar_sesion.grid(row=4, column=0, sticky="news", padx=100, pady=10)


menu_screen.geometry(__window_size)
menu_screen.withdraw()

# _______________________________________________________________________________________________________________#


# _______________________________________________________________________________________________________________#

# Crear la ventana principal gestion de dishes
dish_management = tk.Tk()
dish_management.title("board de Matrix")

label = tk.Label(dish_management, text="Grill House",
                 font=("Arial", 18), pady=10)
label.pack()

# image = tk.PhotoImage(file="logo.png")

# lab = ttk.Label(image=image)
# lab.pack()

frame = tk.Frame(dish_management)
frame.pack()

add_dishes_frame = tk.LabelFrame(frame, text="add dishes",
                                 font=("Arial", 14), padx=50, pady=50)

add_dishes_frame.grid(row=0, column=0, padx=100, pady=10)


# Crear la board
tree = ttk.Treeview(add_dishes_frame, columns=(
    "name", "price", "Description", "availability"), show="headings")
tree.heading("name", text="name")
tree.heading("price", text="price")
tree.heading("Description", text="Description")
tree.heading("availability", text="availability")

# Configurar el evento de clic
tree.bind('<ButtonRelease-1>', toggle_selection)

# show la board en la ventana principal
tree.pack()


# Crear los botones para add, eliminate y update
button_add_dishes = tk.Button(frame, text="Enter Data", command=enter_data,
                              font=("Arial", 12), pady=0)

button_add_dishes.grid(row=6, column=0, sticky="nsew",  padx=10, pady=10)


button_eliminate_dishes = tk.Button(frame, text="eliminate",  command=eliminate_rows_selecteds,
                                    font=("Arial", 12), pady=0)

button_eliminate_dishes.grid(row=7, column=0, sticky="nsew",  padx=10, pady=10)

button_update_dishes = tk.Button(frame, text="update", command=update_data,
                                 font=("Arial", 12), pady=0)

button_update_dishes.grid(row=8, column=0, sticky="nsew",  padx=10, pady=10)

button_cancel = tk.Button(frame, text="cancel", command=cancel_gestion_dishes,
                          font=("Arial", 12), pady=0)
button_cancel.grid(row=9, column=0, sticky="nsew", padx=10, pady=10)

update_board()

dish_management.withdraw()

# _______________________________________________________________________________________________________________#


# _______________________________________________________________________________________________________________#

# Crear la ventana principal


add_orders = tk.Tk()
add_orders.title("Data Entry Form")

# label para identificar el formulario
label = tk.Label(add_orders, text="Grill House",
                 font=("Arial", 18), pady=5)
label.grid(row=0, column=0, columnspan=2)

# Crear un marco para el formulario
frame = tk.Frame(add_orders)
frame.grid(row=1, column=0, columnspan=2)

# Marco para add orders
add_orders_frame = tk.LabelFrame(
    frame, text="add orders", font=("Arial", 14), pady=10)
add_orders_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Marco para las tables
frame_tables = ttk.Frame(add_orders_frame)
frame_tables.grid(row=0, column=0, padx=5, pady=5)

label_tables = ttk.Label(frame_tables, text="Tables")
label_tables.pack()

# Treeview para show las tables
treeview_tables = ttk.Treeview(frame_tables)
treeview_tables.pack()

# Marco para los dishes
frame_dishes = ttk.Frame(add_orders_frame)
frame_dishes.grid(row=0, column=1, padx=5, pady=5)

label_dishes = ttk.Label(frame_dishes, text="dishes")
label_dishes.pack()

# Treeview para show los dishes
treeview_dishes = ttk.Treeview(frame_dishes)
treeview_dishes.pack()


# Insertar tables ficticias en el treeview de tables
tables_orders = []
for i in range(0, len(tables)):
    tables_orders.append(tables[i][0])

for table in tables_orders:
    treeview_tables.insert('', 'end', text=table, values=("table " + table))

# Lista de dishes
dishes_orders = []
for i in range(0, len(matrix_management_dishes)):
    dishes_orders.append(matrix_management_dishes[i][0])

# Insertar dishes  en el treeview de dishes
for plato in dishes_orders:
    treeview_dishes.insert('', 'end', text=plato, values=(plato))

# Botón para Reserve un order
button_reserve = ttk.Button(add_orders_frame,
                            text="Reserve order", command=reserve_order)
button_reserve.grid(row=1, column=0, padx=10, pady=5, sticky="news")

# Botón para show orders
button_show = ttk.Button(add_orders_frame,
                         text="Show orders", command=show_orders)
button_show.grid(row=1, column=1, padx=10, pady=5, sticky="news")
btn_go_out = tk.Button(add_orders_frame, text="go_out", command=lambda: (
    add_orders.withdraw(), menu_screen.deiconify()))
btn_go_out.grid(row=2, column=1, padx=10, pady=5, sticky="news")

# Set the window size (replace __window_size with the desired size)
#
# Hide the window by default

add_orders.withdraw()
# Start the main application loop
# Natalia0506*
# _______________________________________________________________________________________________________________#


# table management
table_management_screen = tk.Tk()
table_management_screen.title("Table management")

label = tk.Label(table_management_screen, text="Grill House",
                 font=("Arial", 18), pady=10)
label.pack()

table_management_frame = tk.Frame(table_management_screen)
table_management_frame.pack()

add_dishes_frame = tk.LabelFrame(table_management_frame, text="List of tables",
                                 font=("Arial", 14), padx=50, pady=50)

add_dishes_frame.grid(row=0, column=0, padx=100, pady=10)


# table_to_show
table_management_table = ttk.Treeview(
    add_dishes_frame, columns=table_management_columns, show="headings")
table_management_table.heading("table", text="table")
table_management_table.heading("date", text="date")
table_management_table.heading("hour", text="Hour")
table_management_table.heading("n.personas", text="N.personas")

table_management_table.bind('<ButtonRelease-1>', toggle_selection_table)

table_management_table.pack()

# buttons
add_tables_button = tk.Button(table_management_frame, text="Registrar table", command=regitry_table,
                              font=("Arial", 12), pady=0)

add_tables_button.grid(row=6, column=0, sticky="nsew",  padx=10, pady=10)


delete_tables_button = tk.Button(table_management_frame, text="eliminate",  command=delete_row_seleted_table,
                                 font=("Arial", 12), pady=0)

delete_tables_button.grid(row=7, column=0, sticky="nsew",  padx=10, pady=10)

update_tables_button = tk.Button(table_management_frame, text="update", command=update_data_table,
                                 font=("Arial", 12), pady=0)

update_tables_button.grid(row=8, column=0, sticky="nsew",  padx=10, pady=10)

cancel_tables_button = tk.Button(table_management_frame, text="cancel", command=cancel_table_management,
                                 font=("Arial", 12), pady=0)
cancel_tables_button.grid(row=9, column=0, sticky="nsew", padx=10, pady=10)

update_table()

table_management_screen.withdraw()

if __name__ == '__main__':

    home_scren.mainloop()
    registry_user_screen.mainloop()
    menu_screen.mainloop()
    init_sesion_screen.mainloop()
    dish_management.mainloop()
    add_dishes_frame.mainloop()
    button_gestion_orders.mainloop()
    add_orders_frame.mainloop()
    table_management_screen.mainloop()
    table_management_frame.mainloop()
