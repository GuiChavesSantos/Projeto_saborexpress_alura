import os


restaurantes = [{'nome': 'Praça', 'categoria' : 'japonesa', 'ativo': False}, {'nome' : 'Pizza Suprema', 'categoria': 'italiana', 'ativo': True}]


def exibir_nome_do_programa():
    print('Sabor express\n')

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def finalizar_app():
    exibir_subtitulo('finalizando o APP')
   

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def opcao_invalida():
    print('opcao inavalida\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastra_novo_restaurante():
    exibir_subtitulo(' Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome' : nome_do_restaurante, 'categoria' : categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurente {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()
    


def listar_restaurantes():
    
    exibir_subtitulo('Listando Restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo} ')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante q deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurente in restaurantes:
        if nome_restaurante == restaurantes['nome']:
            restaurente_encontrado = True
            restaurente['ativo'] = not restaurente ['ativo']
            mensagem = f'o restaurante{nome_restaurante} foi ativado com sucesso' if restaurente['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurente_encontrado:
        print('O restaurante não foi encontrado')

def escolher_opcao():
    try:

        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastra_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        
        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()