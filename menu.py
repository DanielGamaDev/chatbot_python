"""
    ARQUIVO DE MENUS

    MADE BY DANIEL DOS SANTOS GAMA

    Basta apertar CTRL+F para buscar o termo necessário 

"""
# import pywhatkit as kit
import main
import turismo
import varejo
import atacado
import verificador

def menu_inicial():
    texto_menu_inicial = """
    Escolha uma das opções abaixo digitando apenas o número:
    [1] - Turismo (pontos turisticos, restaurantes, shoppings etc.)
    [2] - Comprar em lojas de varejo.
    [3] - Comprar em lojas de atacado.
    [4] - Cancelar conversa.\n """
    print(texto_menu_inicial)

    resposta = input("Qual a opção desejada? Resposta: ")
    if resposta == "1":
        turismo.opcao_turismo()
    elif resposta == "2":
        varejo.opcao_varejo()
    elif resposta == "3":
        atacado.opcao_atacado()
    elif resposta == "4":
        print("OK! Vamos cancelar esta conversa.")
        return resposta
    else:
        print("Não compreendi sua resposta... escolha uma opção válida.")
        print("Vamos começar de novo")
        main.start()
    
    return resposta