
def escrever(msg):
     folder = open("Projeto_IA/text.txt", "r")
     read = folder.readlines()
     read.append(msg+"\n")
            
     folder = open("Projeto_IA/text.txt","w")
     folder.writelines(read)
     folder.close()
     print("mensagem salva!\n")
def mostrarTxt():
    f = open("Projeto_IA/text.txt")
    r = f.read()
    print(r)
