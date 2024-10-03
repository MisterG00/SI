import subprocess
import sys
import argparse

# Configuración del parser de argumentos
parser = argparse.ArgumentParser(description="Obtén la IP de un dominio objetivo usando nslookup")
parser.add_argument('-t', '--target', help='Introduce la dirección IP o dominio de la víctima', required=True)
args = parser.parse_args()

def get_ip(target):
    try:
        # Usar subprocess para capturar la salida del comando
        result = subprocess.run(['nslookup', target], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Resultado de nslookup para {target}:\n")
            print(result.stdout)
        else:
            print(f"Error al ejecutar nslookup en {target}.\nDetalles: {result.stderr}")
    except subprocess.SubprocessError as e:
        print(f"[-] No se pudo obtener la IP: {e}")
        sys.exit(1)

def main():
    if args.target:
        get_ip(args.target)
    else:
        print('[-] Debes indicar una URL o dirección IP con el argumento -t.')
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Proceso interrumpido por el usuario.")
        sys.exit(1)
