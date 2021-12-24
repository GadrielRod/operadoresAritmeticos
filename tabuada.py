multiplicador = int(input('Digite um numero para ser multiplicado: '))
multiplicando = 0
for multiplicando in range (11):
    produto = multiplicador * multiplicando
    print('{} X {} = {}'.format(multiplicador, multiplicando, produto))