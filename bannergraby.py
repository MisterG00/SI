import socket
import sys
import argparse

def banner_grabbing(dominio, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((dominio, int(puerto)))
        sock.settimeout(5)
        banner = sock.recv(1024)
        
        print(f"Banner recibido desde {dominio}:{puerto}:\n{banner.decode().strip()}")
    
    except socket.timeout:
        print(f"Timeout: No se pudo recibir el banner desde {dominio}:{puerto}.")
    
    except socket.gaierror:
        print(f"Error: Dominio '{dominio}' no válido.")
    
    except ValueError:
        print(f"Error: Puerto '{puerto}' no válido. Debe ser un número.")
    
    except Exception as e:
        print(f"Error al conectar con {dominio}:{puerto}. Detalles: {e}")
    
    finally:
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Script para realizar banner grabbing.")
    parser.add_argument('-t', '--target', help="El dominio objetivo", required=True)
    parser.add_argument('-p', '--port', type=int, help="El puerto objetivo", required=True)
    args = parser.parse_args()

    # Verificamos que el puerto esté dentro del rango válido
    if args.port < 1 or args.port > 65535:
        print("Error: El puerto debe estar entre 1 y 65535.")
        sys.exit(1)

    banner_grabbing(args.target, args.port)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Ejecución interrumpida.")
        sys.exit(1)
