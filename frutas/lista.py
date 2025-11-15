# Lista é uma variável que comporta vários tipos de dados.

# Quando eu crio a variável frutas = [], eu estou criando uma variável vazia.

# Nessa atividade o usuário terá 4 opções:
# 1 - Adicionar um item a lista de frutas.
# 2 - Excluir a lista.
# 3 - Visualizar a lista de frutas.
# 4 - Sair da lista.

# Acompanhe o código abaixo:

frutas = []

print('--- Bem-vindas(os) ao Varejão de Frutas da Gen ---')
print('Hoje suas opções são:')
print('1 - Adicionar uma fruta. \n2 - Excluir uma fruta. \n3 - Visualizar lista de frutas. \n4 - SAIR!')

escolha = int(input('Qual a opção desejada: '))

if escolha < 1 or escolha > 4:
    print('Escolha não reconhecida, finalizando sistema.')
else:
    while escolha >= 1:
        if escolha == 1: # Caso 1: Adicionar uma fruta.
            nova_fruta = (input('Qual fruta quer adicionar: '))
            frutas.append(nova_fruta) # Para adicionar um elemento na lista eu devo chamar a lista e dar o atributo ".append", anexando assim, o novo valor.
            print(f'Fruta {frutas[-1]} adicionada')
            escolha = int(input('Qual opção desejada: '))
        elif escolha == 2: # Caso 2: Excluir uma fruta.
            for posicao, cada_fruta in enumerate(frutas, start=1):
                print(posicao,' - ', cada_fruta)
            print('Agora você pode excluir uma fruta da lista,')
            posicao_fruta = int(input('Digite o número da fruta que deseja excluir: '))
            frutas.pop(posicao_fruta - 1) # O comando pop exclui um elemento da lista, baseado em sua posição.
            print('Fruta excluída com sucesso!')
            escolha = int(input('Qual opção desejada: '))
        elif escolha == 3: # Caso 3: Visualizar a lista de frutas.
            for posicao, nome_frutas in enumerate(frutas, start = 1):
                print(posicao, '-', nome_frutas)
            escolha = int(input('Qual opção desejada: '))
        else: #Caso 4: SAIR
            print('Obrigado. Volte sempre!')    
            break 