"""
    ARQUIVO PRINCIPAL
    
    MADE BY DANIEL DOS SANTOS GAMA 
    
    Basta apertar CTRL+F para buscar o termo necessário

"""
# import pywhatkit as kit
import menu
import turismo
import varejo
import atacado
import verificador

def start():
    # APRESENTA O FRIBOT
    texto_apresentacao = """
        Olá, eu sou o FriBot!
        Um robô virtual criado para te ajudar a se locomover por Nova Friburgo.
        Vamos conhecer a cidade?\n"""
    print(texto_apresentacao)

    nome_usuario = 0
    continuar = True
    while (continuar == True): 
        # PEDE O NOME DO USUÁRIO SE ELE AINDA NÃO TIVER FORNECIDO
        if nome_usuario == 0:
            nome_usuario = verificador.confirma_nome()
            print("\nOlá {}!".format(nome_usuario))
            print("\nSe você quiser cancelar a conversa use as opções para voltar ao menu inicial")
        # MOSTRA O MENU INICIAL DE OPÇÕES
        resposta_inicial = menu.menu_inicial()
        if resposta_inicial == "4":
            continuar = False
            print("X----- CONVERSA ENCERRADA -----X")
            continue

    texto_despedida = """
        Obrigado por se informar com o FRIBOT!
        Caso queira saber mais sobre Nova Friburgo basta iniciar outra conversa.
        Tchau tchau ;)"""
    print(texto_despedida)


if __name__ == "__main__":
    start()
