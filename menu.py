import os
import subprocess

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
        print(resultado.stdout)
        return resultado
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {comando}")
        print(f"Detalles: {e}")

def procesar_comando(script, victima, puerto=None):
    comando = f"python3 {script} -t {victima}"
    if puerto:
        comando += f" -p {puerto}"
    ejecutar_comando(comando)
    input("Presione Enter para continuar...")
    limpiar_pantalla()

print("Sistema para pruebas de seguridad informatica")
print("Version 1.0")
print("Desarrollado por: Diego Lopez")

x = True
limpiar_pantalla()

while x:
    print("\nOpciones disponibles:")
    print("Opcion 1: Encontrar IP (Socket).")
    print("Opcion 2: Encontrar IP (Python).")
    print("Opcion 3: Encontrar subdominios.")
    print("Opcion 4: Banner Grabbing.")
    print("Opcion 5: Escaneo de Puertos.")
    print("Opcion 6: Salir.")

    try:
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            victima = input("Obtener IP (Socket): ")
            procesar_comando('getip.py', victima)

        elif opcion == 2:
            victima = input("Obtener IP (Python): ")
            procesar_comando('getip2.py', victima)

        elif opcion == 3:
            victima = input("Ingrese el dominio: ")
            procesar_comando('subdominios.py', victima)

        elif opcion == 4:
            victima = input("Ingrese el dominio: ")
            puerto = input("Ingrese el puerto: ")
            procesar_comando('bannergraby.py', victima, puerto)

        elif opcion == 5:
            victima = input("Ingrese el dominio para escanear puertos: ")
            procesar_comando('portscanner.py', victima)

        elif opcion == 6:
            limpiar_pantalla()
            print("Saliendo del sistema...")
            x = False

        else:
            print("Opcion no valida, intenta de nuevo.")
    
    except ValueError:
        print("Error: Ingrese un numero valido.")
