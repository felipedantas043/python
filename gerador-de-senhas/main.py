import defs

acao = str(input("o que deseja fazer? \n\n buscar senha\n gerar nova senha\n ver lista de senhas \n\n\n").lower())

gerar_senha = ["gerar senha", "gerar", "nova senha", "fazer senha", "primeira opção", "1"]
buscar_senha = ["buscar senha"," procurar senha", "buscar", "encontrar","procurar"]
ver_senhas_geradas = ["ver lista", "ver senhas", "ver"]
opcoes = ["gerar senha", "gerar", "nova senha", "fazer senha", "primeira opção", "1", "buscar senha"," procurar senha", "buscar", "encontrar","procurar","ver lista", "ver senhas", "ver"]

while(not acao in opcoes):
    print("Não entendi. \n\n")
    acao = str(input("o que deseja fazer? \n\n buscar senha\n gerar nova senha\n ver lista de senhas \n\n\n").lower())


if(acao in gerar_senha):
    print("gerar senhas")
    length = int(input("Qual o tamanho da senha? (somente números)"))
    defs.gerarSenha(length)

if(acao in buscar_senha):
    print("buscar senhas")

if(acao in ver_senhas_geradas):
    print("listar senhas")

