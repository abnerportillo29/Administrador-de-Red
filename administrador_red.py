import json
import csv
from datetime import datetime

RUTA_ARCHIVO = "/Users/macbook/Documents/Archivos_Python/dispositivos.json"

dispositivos = []

def guardar_datos():
    with open(RUTA_ARCHIVO, "w") as archivo:
        json.dump(dispositivos, archivo, indent=4)

def cargar_datos():
    global dispositivos

    try:
        with open(RUTA_ARCHIVO, "r") as archivo:
            dispositivos = json.load(archivo)

    except FileNotFoundError: dispositivos = []

cargar_datos()

def validar_ip(ip):
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for parte in partes:
        if not parte.isdigit():
            return False
        
        numero = int(parte)

        if numero < 0 or numero > 255:
            return False
    
    return True

print("Datos Cargados:", dispositivos)

def mostrar_resumen():
    activos = 0
    inactivos = 0
    tipos = []

    for dispositivo in dispositivos:
        if dispositivo["estado"].lower() == "activo":
            activos += 1
        else:
            inactivos += 1

        if dispositivo["tipo"] not in tipos:

            tipos.append(dispositivo["tipo"])

        if len(dispositivos) > 0:
            ultimo = dispositivos[-1]["nombre"]
        else:
            ultimo = "Ninguno"

def guardar_log(evento):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("historial.log", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {evento}\n")

while True:
    print("\n= * = * = * = * = * = * = * = * = * A D M I N I S T R A D O R   D E   R E D = * = * = * = * = * = * = * = * = *")
    
    print("\n" + "=" * 55)
    print("* = * = HORIZONTE IT SUITE = * = *")
    print("Mi Camino, Mi Codigo, Mi Futuro")
    print("=" * 55)
    print("Version: 0.2 Alpha")
    print("Desarrolladores Abner y Zero")

    print("Bienvenido al Sistema de Adminstracion de IT")
    print("=" * 55)
    
    print("1. Ver dispositivos")
    print("2. Agregar dispositivo")
    print("3. Buscar dispositivos por IP")
    print("4. Buscar dispositivos por nombre")
    print("5. Eliminar dispositivo")
    print("6. Ver Estadisticas")
    print("7. Editar Dispositivo")
    print("8. Ver dispositivos activos")
    print("9. Ver dispositivos inactivos")
    print("10. Exportar inventario a TXT")
    print("11. Exportar inventario a CSV")
    print("12. Filtrar dispositivos por tipo")
    print("13. Ordenar dispositivos por nombre")
    print("14. Mostrar porcentaje de dispositivos")
    print("15. Ver historial de eventos")
    print("16. Buscar en historial")
    print("17. Salir")

    opcion = input("\n Selecciona una opcion: ")

    if opcion == "1":
        if len(dispositivos) == 0:
            print("No hay dispositivos registrados.")
        else:
            print("\n=== DISPOSITIVOS REGISTRADOS ===")
            print("=" * 130)
            print(f"{'ID':<5}{'NOMBRE':<20}{'IP':<18}{'TIPO':<15}{'SISTEMA':<18}{'ESTADO':<12}{'REGISTRO':<20}{'ULTIMA MODIFICACION':<25}")
            print("=" * 130)

            for i, dispositivo in enumerate(dispositivos, start=1):
                print(
                    f"{i:<5}"
                    f"{dispositivo['nombre']:<20}"
                    f"{dispositivo['ip']:<18}"
                    f"{dispositivo['tipo']:<15}"
                    f"{dispositivo['sistema']:<18}"
                    f"{dispositivo['estado']:<12}"
                    f"{dispositivo['fecha_registro']:<22}"
                    f"{dispositivo['ultima_modificacion']:<22}"
                )
                print("=" * 130)

    elif opcion == "2":
        print("\n=== AGREGAR DISPOSITIVO ===")

        while True:
            ip = input("Direccion IP: ").strip()

            if not validar_ip(ip):
                print("Direccion IP no valida")
                continue

            if any(dispositivo["ip"] == ip for dispositivo in dispositivos):
                print("Esa IP ya esta registrada.")
                continue
            break

        while True:
            nombre = input("Nombre del Dispositivo: ").strip()

            if nombre == "":
                print("El nombre no puede estar vacio.")
                continue

            if any(dispositivo["nombre"].lower() == nombre.lower()
                   for dispositivo in dispositivos):
                print("Ese nombre ya esta registrado.")
                continue
            break
        
        tipo = input("Tipo: ").strip()
        sistema = input("Sistema Operativo: ").strip()

        while True:
            estado = input("Estado (activo/inactivo): ").strip().lower()

            if estado in ("activo", "inactivo"):
                break
            
            print("El estado debe ser 'activo' o 'inactivo'.")

        fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        ultima_modificacion = fecha_registro

        dispositivo = {
            "nombre": nombre,
            "ip": ip,
            "tipo": tipo,
            "sistema": sistema,
            "estado": estado,
            "fecha_registro": fecha_registro,
            "ultima_modificacion": ultima_modificacion
        }

        dispositivos.append(dispositivo)
        guardar_datos()

        guardar_log(f"Se agrego el dispositivo: {nombre} ({ip})")

        print("\n Dispositivo agregado correctamente.")

    elif opcion == "3":
        ip_buscar = input("Ingrese la IP a buscar: ")

        encontrado = False

        for dispositivo in dispositivos:
            if dispositivo["ip"] == ip_buscar:
                print("\n=== DISPOSITIVO ENCONTRADO ===")
                print(f"Nombre: {dispositivo['nombre']}")
                print(f"IP: {dispositivo['ip']}")
                print(f"Tipo: {dispositivo['tipo']}")
                print(f"Sistema Operativo: {dispositivo['sistema']}")
                print(f"Estado: {dispositivo['estado']}")

                encontrado = True
                break

        if not encontrado:
            print("No se encontro ningun dispositivo con esa IP.")

    elif opcion == "4":
        nombre_buscar = input("Ingrese el nombre del dispositivo: ")

        for dispositivo in dispositivos:
            if dispositivo["nombre"].lower() == nombre_buscar.lower():

                print("\n=== DISPOSITIVO ENCONTRADO ===")
                print(f"Nombre: {dispositivo['nombre']}")
                print(f"IP: {dispositivo['ip']}")
                print(f"Tipo: {dispositivo['tipo']}")
                print(f"Sistema Operativo: {dispositivo['sistema']}")
                print(f"Estado: {dispositivo['estado']}")

                encontrado = True
                break
        if not encontrado:
            print("Dispositivo no encontrado.")

    elif opcion == "5":
        ip_eliminar = input("Ingrese la IP del dispositivo a eliminar: ")
        
        encontrado = False

        for dispositivo in dispositivos:
            if dispositivo["ip"] == ip_eliminar:

                guardar_log(f"Se elimino el dispositivo: {dispositivo['nombre']} ({dispositivo['ip']})")

                dispositivos.remove(dispositivo)
                
                guardar_datos()

                print("Dispositivo eliminado correctamente.")
                
                encontrado = True
                break
        
        if not encontrado:
            print("No se encontro ningun dispositivo con esa IP")

    elif opcion == "6":
        total = len(dispositivos)

        activos = 0
        inactivos = 0

        laptops = 0
        celulares = 0
        routers = 0
        pcs = 0
        tablets = 0
        smart_tvs = 0

        for dispositivo in dispositivos:
            if dispositivo["estado"].lower() == "activo":
                activos += 1
            else:
                inactivos += 1

            if dispositivo["tipo"].lower() == "laptop":
                laptops += 1

            elif dispositivo["tipo"].lower() == "celular":
                celulares += 1

            elif dispositivo["tipo"].lower() == "router":
                routers += 1

            elif dispositivo["tipo"].lower() == "pc":
                pcs += 1

            elif dispositivo["tipo"].lower() == "tablet":
                tablets += 1

            elif dispositivo["tipo"].lower() == "smart tv":
                smart_tvs += 1

        print("\n=== ESTADISTICAS ===")
        print(f"Total de dispositivos: {total}")
        print(f"Dispositivos activos: {activos}")
        print(f"Dispositivos Inactivos: {inactivos}")
        print(f"Laptops: {laptops}")
        print(f"Celulares: {celulares}")
        print(f"Routers: {routers}")
        print(f"PCs: {pcs}")
        print(f"Tablets: {tablets}")
        print(f"Smart TVs: {smart_tvs}")

    elif opcion == "7":
        ip_editar = input("Ingrese la IP del dispositivo a editar: ")

        encontrado = False

        for dispositivo in dispositivos:
            if dispositivo["ip"] == ip_editar:

                print("\n=== EDITANDO DISPOSITIVO ===")

                dispositivo["nombre"] = input(f"Nuevo nombre ({dispositivo['nombre']}): ")

                dispositivo["tipo"] = input(f"Nuevo tipo ({dispositivo['tipo']}): ")

                dispositivo["sistema"] = input(f"Nuevo sistema operativo ({dispositivo['sistema']}): ")

                dispositivo["estado"] = input(f"Nuevo estado ({dispositivo['estado']}): ")

                dispositivo["ultima_modificacion"] = datetime.now().strftime("%d/%m/Y %H:%M:%S")

                guardar_datos()

                guardar_log(f"Se edito el dispositivo: {dispositivo['nombre']} ({dispositivo['ip']})")

                print("Dispositivo actualizado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print("No se encontro ningun dispositivo con esa IP")

    elif opcion == "8":
        print("\n=== DISPOSITIVOS ACTIVOS ===")

        encontrado = False

        for dispositivo in dispositivos:
            if dispositivo["estado"].lower() == "activo":
                print(f"Nombre: {dispositivo['nombre']}")
                print(f"IP: {dispositivo['ip']}")
                print(f"Tipo: {dispositivo['tipo']}")
                print(f"Sistema Operativo: {dispositivo['sistema']}")
                print(f"Estado: {dispositivo['estado']}")

                print("\n--------------------------------------------------------------------")
                
                encontrado = True

        if not encontrado:
            print("No hay dispositivos activos.")

    elif opcion == "9":
        print("\n=== DISPOSITIVOS INACTIVOS ===")

        encontrado = False

        for dispositivo in dispositivos:
            if dispositivo["estado"].lower() == "inactivo":
                print(f"Nombre: {dispositivo['nombre']}")
                print(f"IP: {dispositivo['ip']}")
                print(f"Tipo: {dispositivo['tipo']}")
                print(f"Sistema Operativo: {dispositivo['sistema']}")
                print(f"Estado: {dispositivo['estado']}")

                print("\n--------------------------------------------------------------------")
        
                encontrado = True

        if not encontrado:
            print("No hay dispositivos inactivos.")  

    elif opcion == "10":
        
        with open("invenatario_red.txt", "w", encoding="utf-8") as archivo:

            archivo.write("\n\n=== INVENTARIO DE RED ===\n\n")

            for dispositivo in dispositivos:
                archivo.write(f"Nombre: {dispositivo['nombre']} \n")
                archivo.write(f"IP: {dispositivo['ip']} \n")
                archivo.write(f"Tipo: {dispositivo['tipo']} \n")
                archivo.write(f"Sitema Operativo: {dispositivo['sistema']} \n")
                archivo.write(f"Estado: {dispositivo['estado']} \n")

                archivo.write(
                    f"Fecha de registro: "
                    f"{dispositivo.get('fecha_registro', 'No registrada')}\n"
                )

                archivo.write("-" * 30 + "\n")

        print("Invenatario exportado correctamente.")

    elif opcion == "11":

        with open("inventario_red.csv", "w", newline="", encoding="utf-8") as archivo:

            escritor = csv.writer(archivo)
            
            escritor.writerow([
                "Nombre",
                "IP",
                "Tipo",
                "Sistema Operativo",
                "Estado",
                "Fecha de Registro"
            ])

            for dispositivo in dispositivos:
                escritor.writerow ([
                    dispositivo["nombre"],
                    dispositivo["ip"],
                    dispositivo["tipo"],
                    dispositivo["sistema"],
                    dispositivo["estado"],
                    dispositivo.get("fecha_registrada", "No registrada")
                ])

        print("Inventario exportado correctamente a CSV.")

    elif opcion == "12":
        tipo_buscado = input(
            "Ingrese el tipo de dispositivos buscar: ").lower()

        encontrados = False

        for dispositivo in dispositivos:

            if dispositivo["tipo"].lower() == tipo_buscado:

                print("\n === DISPOSITIVO ENCONTRADO ===")
                print(f"Nombre: {dispositivo['nombre']}")
                print(f"IP: {dispositivo['ip']}" )
                print(f"Tipo: {dispositivo['tipo']}")
                print(f"Sistema Operativo: {dispositivo['sistema']}")
                print(f"Estado: {dispositivo['estado']}")
                print(
                    f"Fecha de registro: "
                    f"{dispositivo.get('fecha_registro', 'No registrada')}"
                    )

                encontrados = True

        if not encontrados:
            print("No se encontraron dispositivo con ese tipo")

    elif opcion == "13":

        dispositivos_ordenados = sorted(
            dispositivos,
        key=lambda dispositivo: dispositivo["nombre"].lower()
        )

        print("\n=== DISPOSITIVOS ORDENADOS POR NOMBRE ===")

        for dispositivo in dispositivos_ordenados:
            
            print(f"\nNombre: {dispositivo['nombre']}")
            print(f"IP: {dispositivo['ip']}")
            print(f"Tipo: {dispositivo['tipo']}")
            print(f"Sistema Operativo: {dispositivo['sistema']}")
            print(f"Estado: {dispositivo['estado']}")
            print(
                f"Fecha de regsitro: "
                f"{dispositivo.get('fecha_registrada', 'No registrada')}"
            )

    elif opcion == "14":
        total_dispositivos = len(dispositivos)

        if total_dispositivos == 0:
            print("No hay dispositivos registrados.")

        else:
            activos = 0
            inactivos = 0

            for dispositivo in dispositivos:
                if dispositivo["estado"].lower() == "activo":
                    activos += 1

                elif dispositivo["estado"].lower() == "inactivo":
                    inactivos += 1

            porcentaje_activos = (activos / total_dispositivos) * 100
            porcentaje_inactivos = (inactivos / total_dispositivos) * 100

            print("\n=== PORCENTAJE DE LA RED ===")
            print(f"Total de dispositivos: {total_dispositivos}")
            print(f"Activos: {porcentaje_activos: 2f}%")
            print(f"Inactivos: {porcentaje_inactivos: 2f}%")

    elif opcion == "15":
        print("\n=== HISTORIAL DE EVENTOS ===\n")

        try:
            with open("historial.log", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

                if contenido.strip() == "":
                    print("No hay eventos registrados.")

                else:
                    print(contenido)

        except FileNotFoundError:
            print("El archivo del histrial.log no existe.")

    elif opcion == "16":

        palabra = input("Buscar en historial: ").lower()

        encontrado = False

        try:
            with open ("historial.log", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if palabra in linea.lower():
                        print(linea, end="")
                        encontrado = True

            if not encontrado:
                print("No se encontradron concidencias.")

        except FileExistsError:
            print("No existe historial.")

    elif opcion == "17":
        print("\nGracias por utilizar Horizonte IT Suite.\n")
        print("\nMi Camino, Mi Codigo, Mi Futuro.\n")
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida")