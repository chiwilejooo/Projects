import time

# El for tiene peculiaridades parecidas al while mientras siga habiendo un valor verdadero se repetira hasta que sea
# falso y dentro de el se pueden usar funciones como "item" el cual va sucediendo al for
lista_de_la_compra = ["leche", "arroz", "jamon"]
for item in lista_de_la_compra:
    print(f'Hoy voy a comprar {item}')

# El for se puede utilizar para conseguir dentro de variables datos como letras sucediendo el for por la palabra
# "letra"
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
frase = input('\n\n\n\nEscriba su frase:\n'
              '----> ')
vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        vocales_encontradas += 1

print(f'Se han encontrado {vocales_encontradas} vocales en la frase:\n'
      f'>>> "{frase}" <<<')
time.sleep(len(frase))
