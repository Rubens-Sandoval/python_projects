import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as err:
        print("A conexão falhou!!")
        print(f"Erro: {err}")
        sys.exit()

    print("Conexão bem sucessida")

    hostAlvo = input("Digite o host ou IP para conectar: ")
    portaAlvo = input("Digite a porta a ser conectada:")

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso!")
        print("Host: ", hostAlvo, "\nPorta: ", portaAlvo)
        s.shutdown(2)

    except socket.error as err:
        print("Não foi possível conectar!!")
        print(f"Erro: {err}")
        sys.exit()

if __name__ == "__main__":
    main()