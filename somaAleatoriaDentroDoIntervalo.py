from itertools import combinations
import random
valorTotal = int(input('Digite um valor total: '))
tamanhoItens = int(input('digite o tamanho da lista: '))
valFinal = int(input('Digite a quantidade a ser somada: '))
lista = random.sample(range(0, valorTotal), tamanhoItens)
print(lista)

for i in (valFinal, len(lista)):
    for lista in combinations(lista, i):
        if sum(lista) <= valorTotal:
            print('{} = {}'.format(lista, sum(lista)))

""""
lista = [randint(0, valor)]
total = int(input('Digite o tamanho da lista: '))
for i in range(0, total):
    elem = str(input())

    print(sum(lista))
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = str(input())

    lst.append(ele)  # adding the element

print(lst)
print((lst[2]))
"""