multiplicador = int(input('Digite um numero para ser multiplicado: '))
multiplicando = 0
print('-'*12)
for multiplicando in range (11):
    produto = multiplicador * multiplicando
    print('{} X {:2} = {}'.format(multiplicador, multiplicando, produto))

print('-'*12)