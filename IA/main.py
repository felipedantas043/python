from funcoes import *
import androidhelper

droid = androidhelper.Android()

print("[1] ver lista\n[2] escrever na lista\n[3] Apagar lista\n")
fazer = input("Digite aqui o número correspondente com a operação que deseja fazer: ")
msg = input("Qual é o seu nome? ")
escrever(msg)
f = open('Projeto_IA/text.txt', 'r')
leia = f.readlines()[0]
print("Olá, " +leia)