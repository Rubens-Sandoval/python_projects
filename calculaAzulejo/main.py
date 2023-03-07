from Retangulo import Retangulo
import math

while True:
    piso_a = float(input("Digite um lado do piso: "))
    piso_b = float(input("Digite outro lado do piso: "))

    piso = Retangulo(piso_a, piso_b)

    az_a = float(input("Digite um lado do azulejo: "))
    az_b = float(input("Digite outro lado do azulejo: "))

    az = Retangulo(az_a, az_b)

    area_piso = piso.area()
    area_az = az.area()

    qntd_az = area_piso / area_az

    if area_piso % area_az == 0:
        print(f'A quantidade de azulejos para preencher o piso é: {qntd_az}')
    else:
        print(f'A quantidade mínima de azulejos para preencher o piso é: {math.ceil(qntd_az)}')


