# dns-brute scripting tool
Este manual describe cómo utilizar el script en Python para gestionar la creación y eliminación de comandos dnsrecon en un archivo `.sh`. 
El archivo generado podrá ser ejecutado como un script de shell para realizar escaneos de DNS.

## Requisitos
- Python 3.9 o superior
- dnsrecon

## Uso
```bash
python script.py
```
- El programa permite agregar, modificar y eliminar comandos dnsrecon en un archivo `.sh`. El archivo `.sh` se creará en la carpeta `scripts` si no existe.
- El archivo `.sh` se puede utilizar como un script de shell para realizar escaneos de DNS.
- **Agregar Dominios:**
Selecciona la opción "agregar" para añadir un dominio.
Ingresa el nombre base del dominio (sin .com o .cl).
Selecciona si el dominio es .com o .cl.
El comando correspondiente se agregará al archivo .sh.
- **Eliminar Dominios:**
Selecciona la opción "eliminar" para quitar un dominio.
Ingresa el nombre base del dominio que deseas eliminar.
Selecciona si el dominio es .com o .cl.
El comando correspondiente será eliminado del archivo .sh si existía.
- **Salir del Script:**
Escribe "salir" para finalizar y guardar los cambios en el archivo .sh.

## Uso del script.sh
- Otorgar permisos de ejecución al archivo:
```bash
chmod 766 script.sh # El owner tiene permiso de lectura, escritura y ejecución
``` 
- Ejecutar el script:
```bash
./script.sh
```