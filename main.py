"""
    ARQUIVO PRINCIPAL
    
    MADE BY DANIEL DOS SANTOS GAMA 
    
    Basta apertar CTRL+F para buscar o termo necessário

"""

import pywhatkit
import menu
import verificador


def start():
    # APRESENTA O FRIBOT
    texto_apresentacao = """
        Olá, eu sou o FriBot!
        Um robô virtual criado para te ajudar a se locomover por Nova Friburgo.
        Vamos conhecer a cidade?\n"""
    print(texto_apresentacao)
    pywhatkit.sendwhatmsg('+5522981092450', texto_apresentacao, 13, 21)

    nome_usuario = 0
    continuar = True
    while continuar == True:
        # PEDE O NOME DO USUÁRIO SE ELE AINDA NÃO TIVER FORNECIDO
        if nome_usuario == 0:
            nome_usuario = verificador.confirma_nome()
            print("\nOlá {}!".format(nome_usuario))
            print(
                "\nSe você quiser cancelar a conversa use as opções para voltar à este menu e selecione a opção 4."
            )
        # MOSTRA O MENU INICIAL DE OPÇÕES
        resposta_inicial = menu.menu_inicial()
        if resposta_inicial == "4" or resposta_inicial == False:
            continuar = menu.menu_final()
            print("------------------------ CONVERSA ENCERRADA ------------------------\n")
            break


if __name__ == "__main__":
    start()
