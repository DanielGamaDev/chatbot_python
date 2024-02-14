"""
    ARQUIVO DE VERIFICADORES

    MADE BY DANIEL DOS SANTOS GAMA

    Basta apertar CTRL+F para buscar o termo necessário 

"""

# import pywhatkit as kit
import menu


def confirma_nome():
    print("Antes de te passar as opções preciso do seu nome.")
    nome = input("Digite o seu nome aqui: ")
    print("")
    print("Seu nome é {}.".format(nome))
    validador = int(
        input(
            """Está correto? Digite apenas o número da opção desejada:
    [1] Confirmar
    [2] Mudar nome\n
    Resposta: """
        )
    )
    if validador == 1:
        return nome
    while validador != 1:
        if validador != 2:
            print(
                "Esta NÃO é uma opção válida! Vou mudar para a opção [2] Mudar nome.\n"
            )
            validador = 2
        print("Vamos mudar o nome escrito anteriormente.")
        nome = input("Digite o seu nome aqui: ")
        print("")
        print("Seu nome é {}.".format(nome))
        validador = int(
            input(
                """Está correto? Digite apenas o número da opção desejada:
    [1] Confirmar
    [2] Mudar nome\n
    Resposta: """
            )
        )
        if validador == 1:
            return nome


def continuar_conversa():
    continuar = "S"
    while continuar.upper() != "S" or continuar.upper() != "N":
        continuar = input("\nDeseja continuar conversa? Resposta[S/N]: ")
        if continuar.upper() == "S":
            menu.menu_inicial()
        elif continuar.upper() == "N":
            return False
        else:
            print(
                "\nNão compreendi sua resposta, digite apenas 'S' para sim ou 'N' para não"
            )
