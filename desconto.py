produto = str(input('Digite o nome do produto: '))
preco = float(input('Digite o preço do produto: R$'))
precoComDesconto = preco - (preco * 5 / 100)

print('O produto {} tem um desconto de 5%'.format(produto))
print('Preço original: {} R$ \n'
      'Preço com desconto de 5%: {} R$'.format(preco, precoComDesconto))