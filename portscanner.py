import socket
import sys
import argparse
from os import path

#conf
parser = argparse.ArgumentParser(description="Script para buscar puertos.")
parser.add_argument('-t', '--target', help='Indica el dominio objetivo', required=True)
args = parser.parse_args()

def main():
    if path.exists('puertos.txt'):
        with open('puertos.txt', 'r') as wordlist:
            puertos = wordlist.read().splitlines()

        if not puertos:
            print("No hay noni")
            return

        for puerto in puertos:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            resultado = s.connect_ex((args.target, int(puerto)))
            if resultado == 0:
                print(f"El puerto: {puerto} esta abierto y vulnerable 😈")

            s.close()
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
