"""
    MADE BY DANIEL DOS SANTOS GAMA

    Basta apertar CTRL+F para buscar o termo necessário 
    Para se localizar no código deixarei as explicações abaixo:
    
    def confirma_nome é onde o usuário declara seu nome e o confirma
    def menu_inicial tem as primeiras opções
    def verifica_menu_inicial valida a primeira resposta do usuário

      *PONTOS TURÍSTICOS:
            CAO SENTADO
      *RESTAURANTES:
            SERRA BELLA
      *SHOPPINGS:
            CADIMA SHOPPING
      *

"""

import pywhatkit as kit


def confirma_nome():
    print("Antes de te passar as opções preciso do seu nome.")
    nome = input("Digite o seu nome aqui: ")
    print("")
    print("Seu nome é {}.".format(nome))
    validador = int(
        input(
            "Se o nome estiver correto digite 1 para confirmar, caso deseje mudar o nome digite 2: "
        )
    )
    if validador == 1:
        return nome
    while validador != 1:
        if validador != 2:
            print("Esta NÃO é uma opção válida! Vou mudar para a opção 2: mudar nome.")
            validador = 2
        print("Vamos mudar o nome escrito anteriormente.")
        nome = input("Digite o seu nome aqui: ")
        print("")
        print("Seu nome é {}.".format(nome))
        validador = int(
            input(
                "Se o nome estiver correto digite 1 para confirmar, caso deseje mudar o nome digite 2: "
            )
        )
        if validador == 1:
            return nome


def menu_inicial():
    texto_menu_inicial = """
    Escolha uma das opções abaixo digitando apenas o número:
    [1] - Turismo (pontos turisticos, restaurantes, shoppings etc.)
    [2] - Comprar em lojas de varejo.
    [3] - Comprar em lojas de atacado.
    [4] - Cancelar conversa.\n """
    print(texto_menu_inicial)

    resposta = input("Qual a opção desejada? Resposta: ")
    if resposta == '1':
        opcao_turismo()
    elif resposta == '2':
        opcao_varejo()
    elif resposta == '3':
        opcao_atacado()
    elif resposta == '4':
        print("OK! Vamos cancelar esta conversa.")
        return 911
    else:
        print("Não compreendi sua resposta... escolha uma opção válida.")
        print("Vamos começar de novo")
        start()
    
    return resposta 

def opcao_turismo():
    texto_turismo = ("""
    Você escolheu a opção TURISMO!
    Escolha uma das opções abaixo para conhecer:

    [1] - Pontos Turísticos.
    [2] - Restaurantes.
    [3] - Shoppings.
    [4] - Voltar para opções anteriores.\n""")
    
    print (texto_turismo)
    resposta = input("Qual a opção desejada? Resposta: ")
    if resposta == '1':
        opcoes_pontos_turisticos()
    elif resposta == '2':
        opcoes_restaurantes()
    elif resposta == '3':
        opcoes_shoppings()
    elif resposta == '4':
        print("OK! Vamos te retornar para as opções anteriores.")
        menu_inicial()
    else:
        print("Não compreendi sua resposta... escolha uma opção válida.")
        print("Vamos começar de novo")

def opcao_varejo(nome):
    print("Olá {}, você quer saber sobre varejo.".format(nome))
    return 0

def opcao_atacado(nome):
    print("Olá {}, você quer saber sobre atacado.".format(nome))
    return 0

def start():
    # APRESENTA O FRIBOT
    texto_apresentacao = """
        Olá, eu sou o FriBot!
        Um robô virtual criado para te ajudar a se locomover por Nova Friburgo.
        Vamos conhecer a cidade?\n"""
    print(texto_apresentacao)

    continuar = "SIM"
    while continuar.upper() == "SIM": # VERIFICA SE O USUÁRIO DESEJA CONTINUAR COM A CONVERSA
        # PEDE O NOME DO USUÁRIO
        nome_usuario = confirma_nome()

        # MOSTRA O MENU INICIAL DE OPÇÕES
        print("\nOlá {}!".format(nome_usuario))
        resposta_usuario = menu_inicial()
        cancelar = verifica_menu_inicial(resposta_usuario)
        if cancelar == 911:
            continue
        texto_despedida = """
        Obrigado por se informar com o FRIBOT!
        Caso queira saber mais sobre Nova Friburgo basta iniciar outra conversa.
        Tchau tchau ;)"""
        print(texto_despedida)

if __name__ == "__main__":
    start()
