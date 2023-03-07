from threading import Thread
import time

def carro(velocidade, carro):
    trajeto = 0
    while trajeto <= 100:
        print(f'{carro}: {trajeto}\n')
        trajeto+=velocidade
        time.sleep(0.5)

#carro(10, 'carro1')
#carro(10, 'carro2')

t_carro1 =  Thread(target=carro, args=[10, 'carro1'])
t_carro2 =  Thread(target=carro, args=[20, 'carro2'])

t_carro1.start()
t_carro2.start()