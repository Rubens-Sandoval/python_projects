import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(f'Verificando {ip}')
        os.system(f'ping -c 4 {ip}')
        print('-' * 60)
        time.sleep(5)