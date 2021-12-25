func = str(input('Digite o nome do funcionario: '))
salario = float(input('Digite o salario do funcionario: R$'))
salarioNovo = salario + (salario * 15 / 100)
print('O funcionario {}'.format(func))
print('Tinha um salario de R${}\n'
      'Salario com aumento é igual de R${:.2f}'.format(salario, salarioNovo))