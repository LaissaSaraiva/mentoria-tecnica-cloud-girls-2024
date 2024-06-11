# Exercícios
# 1 - Imprima a frase: Python na Escola de Programação da Alura.

print('Python na Escola de Programação da Alura \n')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = input('Informe o seu nome:')
idade = input('Informe a sua idade:')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')
print('\n')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

print('A')
print('L')
print('U')
print('R')
print('A')
print('\n')
print('A','L','U','R','A',sep='\n')

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:

pi = 3.14159

pi_arredondado = round(pi, 2)
print('\n')
print(f'O valor arredondado de pi é: {pi_arredondado} ')