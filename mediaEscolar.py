aluno = str(input('Digite o nome do aluno(a): '))
n1 = float(input('Digite a 1º nota do aluno(a): '))
n2 = float(input('Digite a 2º nota do aluno(a): '))
media = (n1 + n2) / 2
if media >= 7:
    print('O aluno(a) {} tirou "{}" na N1 e "{}" na N2\n'
          'O aluno(a) passou com {}'.format(aluno, n1, n2, media))
else:
    print('O aluno(a) {} tirou "{}" na N1 e "{}" na N2\n'
          'O aluno(a) reprovou com {}'.format(aluno, n1, n2, media))