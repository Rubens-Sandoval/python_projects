import ipaddress

ip = '192.168.0.1'
rede_ip = '192.168.0.110/29'

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(rede_ip, strict=False)

#print(endereco)
#print(rede)

for ip in rede:
    print(ip)
