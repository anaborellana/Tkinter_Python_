import datetime
import os
from tkinter import *
import csv
import os
from tkinter import filedialog

# ------------------------------------- FUNCTIONS -------------------------------------#

def opcion_1(in_nombre, csv_clientes, coincidencias):

    for Nombre, Dirección, Documento, Fecha, Correo, Empresa in csv_clientes:
        if in_nombre.lower() in Nombre.lower():
            error_text.set("")            
            result_text.set("---- Search by customer ----\nCliente: {}\nDirección: {}\nDNI: {}\nFecha de alta: {}\nCorreo Electrónico: {}\nEmpresa: {}\n".format(Nombre, Dirección, Documento, Fecha, Correo, Empresa))
            addLines(text_result, result_text.get())
            coincidencias = True
    if coincidencias == False:
        error_text.set("No se encontraron coincidencias")

def opcion_2(in_valor, lista_empresa_actual, coincidencias):
    contador = 0

    for Nombre, Dirección, Documento, Fecha, Correo, Empresa in lista_empresa_actual:

        if len(lista_empresa_actual) > 1 and Nombre != "Nombre":
            coincidencias = True
            if coincidencias == True:
                contador += 1
                if contador == 1:
                    result_text.set("---- Search by User ----\n Empresa: {}.\n Total Usuarios: {}\n".format(in_valor, (len(lista_empresa_actual))-1))
                    addLines(text_result, result_text.get())
                result_text.set("{} - {}, {}, {}, {}, {}, {}\n".format(contador, Nombre, Dirección, Documento, Fecha, Correo, Empresa))
                addLines(text_result, result_text.get())
        elif coincidencias == False:
            error_text.set("No se encontraron coincidencias")

def opcion_3(csv_viaticos, lista_empresa_actual, in_valor):
    total = 0
    contador = 0
    next(csv_viaticos)
    
    try:
        for viaje in csv_viaticos:
            monto = (viaje[2]).replace(",", "")
            f_monto = float(monto)
            for cliente in lista_empresa_actual:
                if viaje[0] == cliente[0] and cliente[1] == in_valor:
                    contador += 1
                    if contador == 1:
                        result_text.set("---- Search Total Travel Expenses ----")
                        addLines(text_result, result_text.get())
                    result_text.set(" Viaje {} - ${}".format(contador, f_monto))
                    addLines(text_result, result_text.get())
                    total += f_monto
                else:
                    pass
    except ValueError:
        error_text.set("ERROR: No se pudo hacer el cálculo")
        pass
    
    if contador >= 1:

        result_text.set("{}. ${:.2f} \n".format(in_valor, total))
        addLines(text_result, result_text.get())
    else:
        error_text.set("No se encontraron coincidencias")

def opcion_4(lista_cliente, csv_viaticos, in_valor, cabecera_viajes):

    total = 0
    cantidad = 0
    viajes = []

    if len(lista_cliente) == 0:
        error_text.set("No se encontraron coincidencias")
    else:
        for viaje in csv_viaticos:
            Documento, fecha, monto = viaje
            if Documento == in_valor:
                viajes.append(viaje)
                monto_aux = (monto).replace(",", "")
                f_monto = float(monto_aux)
                cantidad += 1
                total += f_monto
        
        total = float('{:.2f}'.format(total))
                                
        for cliente in lista_cliente:
            Nombre, Dirección, Documento, Fecha, Correo, Empresa = cliente.rstrip("\n").split(',')
            result_text.set("Nombre: {}\nE-mail: {}\nEmpresa: {}".format(Nombre, Correo, Empresa))
            addLines(text_result, result_text.get())
                    
        for Documento, fecha, monto in cabecera_viajes:
            result_text.set("\nDetalle de viajes\n{}, {}".format(fecha, monto))
            addLines(text_result, result_text.get())
            
        for Documento, fecha, monto in viajes:
            result_text.set("{} - ${}".format(fecha, monto))
            addLines(text_result, result_text.get())
        
        result_text.set("Total viajes: {}, Monto: ${}\n".format(cantidad, total))
        addLines(text_result, result_text.get())

def escribir_log(tipo_log, input):
    nombre_log = "sys_clientes.log"
    ct = datetime.datetime.now()
    now = "{}/{}/{} - {}:{}:{} //".format(ct.day, ct.month, ct.year, ct.hour, ct.minute, ct.second)
    
    try:
        open(nombre_log)
        with open(nombre_log, "a", newline="") as f_log:
            csv_log = csv.writer(f_log)
            nuevo_log = " " + tipo_log
            input =" Input: " + input
            csv_log.writerow([now,nuevo_log, input])

    except FileNotFoundError:
        with open(nombre_log, "w", newline="") as f_log:
            csv_log = csv.writer(f_log)
            cabecera = "Acción"
            csv_log.writerow([cabecera])
            csv_log.writerow(["Menú"])
            error_text.set("Archivo log creado con exito en ", os.path.abspath(nombre_log))     
        
def busqueda(archivo_clientes, archivo_viaticos, opcion, in_valor):
    
    try:
        with open(archivo_clientes, 'r', encoding="utf-8") as f_clientes:
            csv_clientes = csv.reader(f_clientes, delimiter=",")
            coincidencias = False

            if opcion == 1:
                tipo_log = "Busqueda de cliente por nombre"
                next(csv_clientes)
                
                if in_valor == "":
                    error_text.set("No se acepta un ingreso vacío\nIngrese un nombre para buscar")
                else:
                    opcion_1(in_valor, csv_clientes, coincidencias)               
                    escribir_log(tipo_log, in_valor)
                    
            elif opcion == 2:
                tipo_log = "Busqueda total usuarios por empresa"
                                   
                if in_valor == "":
                    error_text.set("No se acepta un ingreso vacío\nIngrese un nombre para buscar")
                else:

                    lista_empresas = list(csv_clientes)         
                    lista_empresa_actual = [[Nombre, Dirección, Documento, Fecha, Correo, Empresa] for Nombre, Dirección, Documento, Fecha, Correo, Empresa in lista_empresas if Empresa == in_valor or Nombre == "Nombre"]
                    opcion_2(in_valor, lista_empresa_actual, coincidencias)
                    escribir_log(tipo_log, in_valor)
                    
            elif opcion == 3:
                
                tipo_log = "Busqueda total viaticos por empresa"
                
                with open(archivo_viaticos, 'r', encoding="utf-8") as f_viaticos:
                    csv_viaticos = csv.reader(f_viaticos, delimiter=",")
                    
                    lista_empresas = list(csv_clientes)
                    lista_empresa_actual = [[ Documento, Empresa] for Nombre, Dirección, Documento, Fecha, Correo, Empresa in lista_empresas if Nombre != "Nombre"]
                    lista_empresa_actual.sort()    
                    
                    if in_valor == "":
                        error_text.set("No se acepta un ingreso vacío\nIngrese un nombre para buscar")
                    else:
                        opcion_3(csv_viaticos, lista_empresa_actual, in_valor)
                        escribir_log(tipo_log, in_valor)
                
            elif opcion == 4:
                
                tipo_log = "Busqueda total viaticos por cliente"
                
                with open(archivo_viaticos, 'r', encoding="utf-8") as f_viaticos:
                    csv_viaticos = csv.reader(f_viaticos, delimiter=",")                    
                    cabecera_viajes = [next(csv_viaticos, None)]
                    
                    if in_valor == "":
                        error_text.set("No se acepta un ingreso vacío\nIngrese un nombre para buscar")
                    else:
                        lista_empresas = list(csv_clientes)
                        lista_cliente = [', '.join([Nombre, Direccion, Documento, Fecha, Correo, Empresa]) for Nombre, Direccion, Documento, Fecha, Correo, Empresa in lista_empresas if Documento == in_valor]
                        opcion_4(lista_cliente, csv_viaticos, in_valor, cabecera_viajes)
                        escribir_log(tipo_log, in_valor)
    except RuntimeError:
        error_text.set("Ingrese un valor para su busqueda")
    except FileNotFoundError:
        error_text.set("Por favor seleccionar los archivos de\nclientes y viajes para poder procesar")

def browseFiles(lbl_root,text):
    global path_client, path_viati
    path = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
    )
    lbl_root.configure(text=path)
    if text == "client":
        path_client = path
    elif text == "viati":
        path_viati = path

def addLines(variable, line):
    variable.insert(END, line + '\n')

# ------------------------------------- WINDOW -------------------------------------#

root = Tk()
root.title("File admin")
myframe = Frame(root)
myframe.pack()
path_client = ""
path_viati = ""
result_text = StringVar()
error_text = StringVar()

# ------------------- ROW 0 -------------------- #
lbl_title = Label(myframe, text="Search System",width=50, height=1, pady=10)
lbl_title.grid(columnspan=4, row=0)
lbl_title.config(font='Century 18 bold', bg="orange")

text_result = Text(myframe)
text_result.grid(row=2, rowspan=8, column=2, sticky='e')

scr=Scrollbar(myframe, orient=VERTICAL, command=text_result.yview)
scr.grid(row=2, column=3, rowspan=8, sticky='nsw', pady=30)

text_result.config(font='Century 9', bg="white", yscrollcommand=scr.set, width=50, height=12)

# ------------------- ROW 1 -------------------- #
lbl_root_client = Label(myframe, height=1, pady=10, text=path_client)
lbl_root_client.grid(column=0, row=1)

lbl_root_viati = Label(myframe, height=1, pady=10, text=path_viati)
lbl_root_viati.grid(column=1, row=1)

text_error = Label(myframe, width=44, height=3, pady=10, textvariable=error_text)
text_error.grid(row=1, column=2, sticky='e')
text_error.config(relief='flat',  background='#F0F0F0')

# ------------------- ROW 2 -------------------- #

button_client = Button(myframe, text="Browse file customer", command=lambda:browseFiles(lbl_root_client,"client"))
button_client.grid(column=0, row=2)

button_viati = Button(myframe, text="Browse file travel expenses", command=lambda:browseFiles(lbl_root_viati,"viati"))
button_viati.grid(column=1, row=2)

# ------------------- ROW 3 -------------------- #
lbl_title = Label(myframe, text="Menu",width=30, height=2)
lbl_title.grid(columnspan=2, row=3)
lbl_title.config(font='Helvetica 12 bold')

# ------------------- ROW 4 -------------------- #
search_client_text = Entry(myframe, width=30)
search_client_text.grid(column=0, row=4, pady=7, padx=7, sticky='e')

search_client = Button(myframe, text="Search by customer", command=lambda:busqueda(path_client, path_viati, 1, str(search_client_text.get())))
search_client.grid(column=1, row=4, pady=7, padx=7, sticky='w')

# ------------------- ROW 5 -------------------- #
search_usu_text = Entry(myframe, width=30)
search_usu_text.grid(column=0, row=5, pady=7, padx=7, sticky='e')

search_usu = Button(myframe, text="Search for users by company", command=lambda:busqueda(path_client, path_viati, 2, str(search_usu_text.get())))
search_usu.grid(column=1, row=5, pady=7, padx=7, sticky='w')

# ------------------- ROW 6 -------------------- #
search_tr_exp_text = Entry(myframe, width=30)
search_tr_exp_text.grid(column=0, row=6, pady=7, padx=7, sticky='e')

total_tr_exp = Button(myframe, text="Total travel expenses per company", command=lambda:busqueda(path_client, path_viati, 3, str(search_tr_exp_text.get())))
total_tr_exp.grid(column=1, row=6, pady=7, padx=7, sticky='w')

# ------------------- ROW 7 -------------------- #
search_tr_cust_text = Entry(myframe, width=30)
search_tr_cust_text.grid(column=0, row=7, pady=7, padx=7, sticky='e')

tr_customer = Button(myframe, text="Travel per customer", command=lambda:busqueda(path_client, path_viati, 4, str(search_tr_cust_text.get())))
tr_customer.grid(column=1, row=7, pady=7, padx=7, sticky='w')

# ------------------- ROW 8 -------------------- #
button_exit = Button(myframe, text="Exit", command=exit)
button_exit.grid(columnspan=2, row=8, pady=7)

root.mainloop()