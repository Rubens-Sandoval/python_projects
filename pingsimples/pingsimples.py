import os

print("#" *  60)

ip = input("Digite o ip: ")

print("-" * 60)

os.system(f'ping -c 6 {ip}')

