# progrma que le el numero del suario y cre la tabla de multiplicar
import time
numero_usuario = int(input('Tabla del... \n'
                           '----> '))
for n in range(1, 11):
    print(f'{numero_usuario} * {n} = {numero_usuario * n}')
time.sleep(20)