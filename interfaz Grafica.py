import tkinter as tk
from tkinter import ttk, messagebox
import json

dispositivos = []

def guardar_dispositivos():
    with open("dispositivos.json", "w") as archivo:
        json.dump(dispositivos, archivo, indent=4)

def cargar_dispositivos():
    global dispositivos

    try:
        with open("dispositivos.json", "r") as archivo:
            dispositivos = json.load(archivo)
            
            for dispositivo in dispositivos:
                tabla.insert(
                 "",
                 "end",
                 values=(
                    dispositivo["nombre"],
                    dispositivo["ip"],
                    dispositivo["tipo"],
                    dispositivo["estado"]
                 )
                )
    except FileNotFoundError:
            dispositivos = []

def agregar_dispositivo():
    tabla.insert(
        "",
        "end",
        values=("Nuevo Equipo", "192.168.1.100", "PC", "Activo")
    )

def abrir_ventana_agregar():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Dispositivo")
    ventana_agregar.geometry("350x250")

    tk.Label(ventana_agregar, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana_agregar, width=30)
    entry_nombre.pack()

    tk.Label(ventana_agregar, text="Direccion IP:").pack(pady=5)
    entry_ip = tk.Entry(ventana_agregar, width=30)
    entry_ip.pack()

    tk.Label(ventana_agregar, text="Tipo:").pack(pady=5)
    entry_tipo = tk.Entry(ventana_agregar, width=30)
    entry_tipo.pack()

    tk.Label(ventana_agregar, text="Estado:").pack(pady=5)
    entry_estado = tk.Entry(ventana_agregar, width=30)
    entry_estado.pack()

    def guardar():
        nombre = entry_nombre.get()
        ip = entry_ip.get()
        tipo = entry_tipo.get()
        estado = entry_estado.get()

        if not nombre or not ip or not tipo or not estado:
            messagebox.showerror(
                "Error",
                "Todos los campos son obligatorios"
            )
            return
        
        nuevo_dispositivo = {
            "nombre": nombre,
            "ip": ip,
            "tipo": tipo,
            "estado": estado
        }
        
        dispositivos.append(nuevo_dispositivo)

        guardar_dispositivos()

        tabla.insert(
            "",
            "end",
            values=(nombre, ip, tipo, estado)
        )

        messagebox.showinfo(
            "Exito",
            "Dispositivo agregado correctamente"
        )

        ventana_agregar.destroy()

    btn_guardar = tk.Button(
        ventana_agregar,
        text="Guardar",
        command=guardar
        )
    btn_guardar.pack(pady=10)

ventana = tk.Tk()

ventana.title("Administrador de Redes")
ventana.geometry("800x600")


titulo = tk.Label (
    ventana,
    text="Administrador de Redes",
    font="Arial, 20"
)
titulo.pack(pady=20)

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=20)


btn_agregar = tk.Button(
    marco_botones,
    text="Agregar Dispositivo",
    width=20,
    command=abrir_ventana_agregar
)
btn_agregar.grid(row=0, column=0, padx=10, pady=10)

btn_mostrar = tk.Button(
    marco_botones,
    text="Mostrar Dispositivos",
    width=20
)
btn_mostrar.grid(row=0, column=1, padx=10, pady=10)

btn_buscar = tk.Button(
    marco_botones,
    text="Buscar Dispositivos",
    width=20
)
btn_buscar.grid(row=1, column=0, padx=10, pady=10)

btn_eliminar = tk.Button(
    marco_botones,
    text="Eliminar Dispositivo",
    width=20
)
btn_eliminar.grid(row=1, column=1, padx=10, pady=10)

tabla = ttk.Treeview(
    ventana,
    columns=("nombre", "ip", "tipo", "estado"),
    show="headings"
)

tabla.heading("nombre", text="Nombre")
tabla.heading("ip", text="Direccion IP")
tabla.heading("tipo", text="Tipo")
tabla.heading("estado", text="Estado")

tabla.column("nombre", width=150)
tabla.column("ip", width=150)
tabla.column("tipo", width=150)
tabla.column("estado", width=100)

tabla.pack(pady=20, fill="both", expand=True)

cargar_dispositivos()

ventana.mainloop()