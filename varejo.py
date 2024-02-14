"""
    ARQUIVO DO VAREJO

    MADE BY DANIEL DOS SANTOS GAMA

    Basta apertar CTRL+F para buscar o termo necessário 
    
    CATEGORIAS E LOJAS DE VAREJO REGISTRADAS:
    
    *LINGERIE:
        LOJA1
        LOJA2
    *PIJAMAS:
        LOJA1
        LOJA2
    *CUECAS:
        LOJA1
        LOJA2
    *PRESENTES:
        LOJA1
        LOJA2

"""
# import pywhatkit as kit
import menu

def opcao_varejo():
    texto_varejo = """
    Você escolheu a opção VAREJO!
    Escolha uma das opções abaixo para conhecer:

    [1] - Lingerie.
    [2] - Pijamas.
    [3] - Cuecas.
    [4] - Presentes.
    [5] - Voltar para opções anteriores.\n"""

    print(texto_varejo)
    resposta = input("Qual a opção desejada? Resposta: ")
    if resposta == "1":
        opcoes_lingerie()
    elif resposta == "2":
        opcoes_pijamas()
    elif resposta == "3":
        opcoes_cuecas()
    elif resposta == "4":
        opcoes_presentes()    
    elif resposta == "5":
        print("OK! Vamos te retornar para as opções anteriores.")
        menu.menu_inicial()
    else:
        print("Não compreendi sua resposta... escolha uma opção válida.")
        print("Vamos começar de novo")

def opcoes_lingerie():
    print("Estas são as opcoes_lingerie")

def opcoes_pijamas():
    print("Estas são as opcoes_pijamas")

def opcoes_cuecas():
    print("Estas são as opcoes_cuecas")

def opcoes_presentes():
    print("Estas são as opcoes_presentes")