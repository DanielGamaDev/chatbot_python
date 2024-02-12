"""
    ARQUIVO DO TURISMO

    MADE BY DANIEL DOS SANTOS GAMA

    Basta apertar CTRL+F para buscar o termo necessário 
    
    CATEGORIAS E PONTOS TURÍSTICOS REGISTRADAS:

    *PONTOS TURÍSTICOS:
        PONTO1
        PONTO2
    *RESTAURANTES:
        RESTAURANTE1
        RESTAURANTE2
    *SHOPPINGS:
        SHOPPING CADIMA
        SHOPPING FRIBURGO

"""
# import pywhatkit as kit
import main
import menu
import varejo
import atacado
import verificador

def opcao_turismo():
    texto_turismo = """
    Você escolheu a opção TURISMO!
    Escolha uma das opções abaixo para conhecer:

    [1] - Pontos Turísticos.
    [2] - Restaurantes.
    [3] - Shoppings.
    [4] - Voltar para opções anteriores.\n"""

    print(texto_turismo)
    resposta = input("Qual a opção desejada? Resposta: ")
    if resposta == "1":
        opcoes_pontos_turisticos()
    elif resposta == "2":
        opcoes_restaurantes()
    elif resposta == "3":
        opcoes_shoppings()
    elif resposta == "4":
        print("OK! Vamos te retornar para as opções anteriores.")
        menu.menu_inicial()
    else:
        print("Não compreendi sua resposta... escolha uma opção válida.")
        print("Vamos começar de novo")

def opcoes_pontos_turisticos():
    print("Estas são as opcoes_pontos_turisticos")

def opcoes_restaurantes():
    print("Estas são as opcoes_restaurantes")
    return 0

def opcoes_shoppings():
    print("Estas são as opcoes_shoppings")