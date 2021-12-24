n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divInteira = n1 // n2
resto = n1 % n2
raizQuadrada = n1 ** (1/2)
raizCubica = n1 ** (1/3)

print(f'A soma dos valores foi: {soma}\n'
      f'A subtração dos valores foi: {subtracao}\n'
      f'A multiplicação dos valores foi: {multiplicacao}\n'
      f'A divisão dos valores foi: {divisao}\n'
      f'O quadrado dos valores foi: {potencia}\n'
      f'A divisão inteira dos valores foi: {divInteira}\n'
      f'O resto dos valores foi: {resto}\n'
      f'A raiz quadrada do valor 1 é: {raizQuadrada}\n'
      f'A raiz cubica do valor 1 é: {raizCubica}')

#forma alternativa de fazer potencai
#print(pow(5,5))

#Ordem de precendecia:
#1 - '()'
#2 - '**'
#3 - '*' '/' '//' '%'
#4 - '+' '-'

alinhamento = str(input('digite algo para ser alinhado: '))
print('Estou te alinhando a direita em 20 espaços: {:>20}'.format(alinhamento))
print('Estou te centralizando em 20 espaços: {:=^20}'.format(alinhamento))
print('Estou te centralizando em 20 espaços: {:^20}'.format(alinhamento))
print('Estou te alinhando a esquerda em 20 espaços: {:<20}'.format(alinhamento))
