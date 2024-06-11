import os

# print('Hello World\n')
def exibir_nome_do_programa():
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

# Exibir Informação
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

# Input do usuário
#Convenção Python snake-case nome de variáveis, funções e métodos
# Python é fortemente tipado. Recebe inputs como string, se necessario, converter para Inteiro


# opcao_escolhida = int(opcao_escolhida)
# print('Você escolheu a opção:', opcao_escolhida)
# print(f'Você escolheu a opção: {opcao_escolhida}')

# No python, Strings é versátil. 'aspas simples' / "aspas duplas" / """ aspas triplas para eventuais quebras de linhas"""são usadas para criar strings que abrangem várias linhas. Elas são úteis quando você precisa incluir quebras de linha e manter o formato do texto.

#Interpolação = string + variáveis



# print('Opção escolhida',opcao_escolhida == 1)
# print(type(opcao_escolhida))
# print(type(1))

def finalizar_app():
    os.system('cls')
    print('Finalizando o App!\n')

# If else
def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: ')) # int() converte string para Inteiro
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()


# Defininado arquivo principal

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
        
if __name__ == '__main__': # Convenção
    main()

