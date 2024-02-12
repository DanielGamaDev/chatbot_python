"""
    ARQUIVO DE VERIFICADORES

    MADE BY DANIEL DOS SANTOS GAMA

    Basta apertar CTRL+F para buscar o termo necessário 

"""
# import pywhatkit as kit
import main
import menu
import turismo
import varejo
import verificador

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