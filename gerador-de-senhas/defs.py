import random
import time
import pyperclip
def gerarSenha(lenghtPass):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    lower = alfabeto.lower()
    upper = alfabeto.upper()

    numeros = "0123456789"
    simbolos = "[]{}(),.-*%$#@!"

    all = lower+upper+numeros+simbolos
    password = "".join(random.sample(all, lenghtPass))
    pyperclip.copy(password)
    
    id = "30" #str(random.randrange(100))
    data = str(time.asctime())
    
    with open("gerador-de-senhas/senhas.txt", 'r')as senhas:
        senha = senhas.readline()
        while senha =senhas.rea:


        for linha in senhas:
            palavras = linha.split(",")
            compararid = palavras[0]
            if(compararid == id):
                print("Já existe!")

            else:
                with open("gerador-de-senhas/senhas.txt", "a") as senhas:
                    texto = ("\n"+id+", " +password+", "+data)
                    senhas.write(texto)

                print("sua senha é: ", password)
                print("\n>>>Sua senha foi copiada para sua área de transferência!<<<")



def salvando():
    # senhas = open("gerador-de-senhas/senhas.txt", "r")
    # conteudo = senhas.read()
    # print(conteudo)
    # senhas.close()

    # Método seguro que evita que o arquivo seja esquecido de ser fechado
    # try:
    #     senhas = open("gerador-de-senhas/senhas.txt", "r")
    #     conteudo = senhas.read()
    #     print(conteudo)
    # finally:    
    #     senhas.close()


    #with é pra facilitar a vida. Ele fecha o arquivo automaticamente, sem precisa do comando '[str].close()'
    with open("gerador-de-senhas/senhas.txt", "r") as senhas:
        textos = senhas.readlines()
        for texto in textos:
            print(texto, end='')

def procurar(id):
    with open("gerador-de-senhas/senhas.txt", 'r')as senhas:
        senha = senhas.readline()
        for linha in senhas:
            palavras = linha.split(",")
            if(palavras[0] == id):
                print(palavras[0])
        #print(senha)


gerarSenha(5)