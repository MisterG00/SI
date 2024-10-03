import socket
import sys
import argparse

# Configurar argumentos
parser = argparse.ArgumentParser(description="Obtener la IP de un dominio.")
parser.add_argument("-t", "--target", help="Ingresa la URL sin HTTP o HTTPS", required=True)
args = parser.parse_args()

def obtener_ip(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        print(f"La dirección IP de {dominio} es: {ip}")
    except socket.gaierror:
        print(f"No se pudo obtener la IP de {dominio}. Verifica el nombre del dominio.")

def main():
    if args.target:
        obtener_ip(args.target)
    else:
        print("Por favor, ingrese una dirección válida.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nEjecución interrumpida por el usuario.")
