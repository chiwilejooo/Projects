# Solo saque los multiplos de dos de la tabla de multiplicar



numero_usuario = int(input('Tabla del... \n'
                           '----> '))
for n in range(1, 11):
    if n % 2 == 0:
        print(f'{numero_usuario} * {n} = {numero_usuario * n}')