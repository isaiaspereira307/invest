import json
import os

def calculo(self):
    meta = float(input('valor da meta: ')) # 1000000
    valorinicial = float(input('valor inicial: ')) # 5637.99
    valormensal = float(input('investimento mensal: ')) # 150
    dividendos = float(input('dividendos: ')) # 16.86
    meta = meta - valorinicial - valormensal - dividendos
    i = 0
    while i < meta:
        meta = meta - valormensal - dividendos
        print(meta)
        dividendos = dividendos + 1.37
        i = i + 1 
        print (i)
    return i

def viver_de_renda_hglg():
    preco = 194
    div = 0.78
    magic_number = int(preco/div)
    valor = preco * magic_number
    rmd = 1000 #renda mensal desejada
    valor_nescessario = magic_number*rmd
    return valor_nescessario

def viver_de_renda_knri(self):
    preco = 185
    div = 0.74
    magic_number = int(preco/div)
    valor = preco * magic_number
    rmd = 10000 #renda mensal desejada
    valor_nescessario = magic_number*rmd
    return valor_nescessario

def viver_de_renda_bcff(self):
    preco = 99
    div = 0.53
    magic_number = int(preco/div)
    valor = preco * magic_number
    rmd = 10000 #renda mensal desejada
    valor_nescessario = magic_number*rmd
    return valor_nescessario

def vdrFII():
    preco = 478
    div = 2.05
    rmd = 10000
    magic_number = int(preco/div)
    valor_nescessario = magic_number*rmd
    print(valor_nescessario)

def sair():
    print("\nObrigado por utilizar a calculadora. Até logo!")
    exit()


def chamarMenu():
    #os.system('clear')
    escolha = int(input("##### INVESTPY #####"
    "\nDigite: "
    "\n<1> adicionar ação"
    "\n<2> exibir ações"
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
        dicionario[input("Digite o nome da ação: ")] = [
            input("Digite o valor da ação: "),
            input("Digite o valor do dividendo: "),
            input("Digite a quantidade de cotas:")]
        resp = input("Digite <S> para continuar.").upper()
        gravar_arquivo(dicionario,arquivo)
        return "JSON gerado!!!!"
        
def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Ação.........: ", chave)
        print("Valor........: ", dado[0])
        print("Dividendos...: ", dado[1])
        print("Cotas........: ", dado[2])


acoes = ler_arquivo("acoes.json")
opcao=chamarMenu()
while opcao > 0 and opcao < 5:
    if opcao == 1:
        print(registrar(acoes, "acoes.json"))
    elif opcao == 2:
        exibir("acoes.json")
    elif opcao == 3:
        sair()
    opcao = chamarMenu()