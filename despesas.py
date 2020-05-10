import json
import os

def chamarMenu():
    escolha = int(input("Digite: "
    "\n<1> adicionar despesa"
    "\n<2> exibir despesas"
    "\n<3> sair\n> "))
    return escolha

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario=json.load(arq_json)
    else:
        dicionario = {}
    return dicionario

def gravar_arquivo(dicionario,arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)

def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o nome da despesa: ")] = [
            input("Digite a data da despesa: "),
            input("Digite o valor: "), input("Digite a categoria: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravar_arquivo(dicionario,arquivo)
        return "JSON gerado!!!!"
        
def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Despesa......: ", chave)
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2])

def sair():
    print("\nObrigado por utilizar a calculadora. Até logo!")
    exit()

despesas = ler_arquivo("despesas.json")
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        print(registrar(despesas, "despesas.json"))
    elif opcao==2:
        exibir("despesas.json")
    elif opcao==3:
        sair()
    opcao = chamarMenu()