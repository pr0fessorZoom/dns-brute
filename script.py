import os
from datetime import datetime

# Crear la carpeta 'scripts' si no existe
if not os.path.exists('scripts'):
    os.makedirs('scripts')

# Solicitar al usuario el nombre del archivo .sh
output_script = input("Escribe el nombre del archivo .sh (sin extensión): ") + ".sh"
top_1m = '../dicts/subdomains-top1million-110000.txt'
raft = '../dicts/raft-large-words-lowercase-cleanned.txt' # Hay que poner la ruta del diccionario limpio
letter = '../dicts/letter.txt'
diccionarios = [top_1m, raft, letter]

# Ruta completa donde se guardará el archivo .sh
output_path = os.path.join('scripts', output_script)

# Crear o limpiar el archivo .sh si ya existe
with open(output_path, 'w') as file:
    file.write("#!/bin/bash\n\n")

while True:
    # Solicitar al usuario la acción a realizar
    accion = input("¿Desea agregar o eliminar un dominio? (escribe 'agregar', 'eliminar' o 'salir'): ").lower()

    if accion == 'salir':
        print(f"Script guardado en {output_path}")
        break
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Generar una cadena de texto con la fecha y hora actual
    if accion == 'agregar':
        # Solicitar el nombre del dominio
        dominio_base = input("Escribe el nombre del dominio (sin '.com' o '.cl'): ")

        # Solicitar al usuario el tipo de dominio
        tipo_dominio = input("¿Es un dominio .com o .cl? (escribe 'com' o 'cl'): ").lower()

        if tipo_dominio not in ['com', 'cl']:
            print("Tipo de dominio no válido. Intenta nuevamente.")
            continue

        # Generar el dominio completo
        dominio = f"{dominio_base}.{tipo_dominio}"
        resultado_dominio = f"{dominio_base}"

        # Generar el comando con los parámetros dados
        for diccionario in diccionarios:
            comando = f"dnsrecon -d {dominio} -t brt -D {diccionario} -c {resultado_dominio}_{timestamp}_result.csv"
            with open(output_path, 'a') as file:
                file.write(comando + "\n")
            print(f"Comando añadido: {comando}")


        # Guardar el comando en el archivo .sh
        with open(output_path, 'a') as file:
            file.write(comando + "\n")

        print(f"Comando añadido: {comando}")

    elif accion == 'eliminar':
            # Solicitar el nombre del dominio
            dominio_base = input("Escribe el nombre del dominio a eliminar (sin '.com' o '.cl'): ")

            # Solicitar al usuario el tipo de dominio
            tipo_dominio = input("¿Es un dominio .com o .cl? (escribe 'com' o 'cl'): ").lower()

            if tipo_dominio not in ['com', 'cl']:
                print("Tipo de dominio no válido. Intenta nuevamente.")
                continue

            # Generar el dominio completo
            dominio = f"{dominio_base}.{tipo_dominio}"
            resultado_dominio = f"{dominio_base}"

            # Leer el archivo y filtrar los comandos
            with open(output_path, 'r') as file:
                lineas = file.readlines()

            # Filtrar las líneas que no coinciden con el comando a eliminar
            with open(output_path, 'w') as file:
                for linea in lineas:
                    eliminar = False
                    for diccionario in diccionarios:
                        comando_a_eliminar = f"dnsrecon -d {dominio} -t brt -D {diccionario} -c {resultado_dominio}_result.csv"
                        if linea.strip() == comando_a_eliminar:
                            eliminar = True
                            print(f"Comando eliminado: {comando_a_eliminar}")
                            break
                    if not eliminar:
                        file.write(linea)

                else:
                    print("Acción no válida. Intenta nuevamente.")

print("¡Operación finalizada!")
