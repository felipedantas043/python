import random

alfabeto = "abcdefghijklmnopqrstuvwxyz"

acao = input("o que deseja fazer? \n buscar senha\n gerar nova senha\n ver lista de senhas")


lower = alfabeto.lower()
upper = alfabeto.upper()

numeros = "0123456789"
simbolos = "[]{}(),.-*%$#@!"
lenght = int(input("Digite o tamanho da senha: (somente números) "))

all = lower+upper+numeros+simbolos
password = "".join(random.sample(all, lenght))