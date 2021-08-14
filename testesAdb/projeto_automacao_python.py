import time
from ppadb.device import Device
from teste_scrcpy import connectAdb

device, client = connectAdb.connect()

def rolar_tela_vertical(vezes):

    #variaveis que armazenam onde começa a rolagem na tela, termina e a duração.
    start_x = 500
    start_y = 1500
    end_x = 500
    end_y = 700
    duration_ms = 300

    
    #loop para rolar a tela varias vezes
    contador = 0
    while contador < vezes:
        device.shell(f'input swipe {start_x} {start_y} {end_x} {end_y} {duration_ms}')#aqui são passado os valores  das variaveis acima
        print(f'Rolou a tela {contador +1} vezes')
        contador = contador + 1
    
def rolar_tela_horizontal(vezes, start_x, start_y, end_x):

    # start_x = 250
    # start_y = 1300
    # end_x = 1000
    end_y = start_y
    duration_ms = 200

    contador = 0 
    while contador < vezes:
        device.shell(f'input swipe {start_x} {start_y} {end_x} {end_y} {duration_ms}')
        print(f'Rolou a tela {contador +1} vezes')
        contador = contador + 1

def abrir_insta():

    device.shell("input keyevent 3")
    time.sleep(5)

    rolar_tela_vertical(1)
    rolar_tela_horizontal(2, 250, 1300, 1000)
    rolar_tela_horizontal(1, 1000, 1300, 250)

    cordenada_icone_insta = "333 696" # x y
    device.shell(f'input tap {cordenada_icone_insta}')

    time.sleep(3)

    cordenada_home = "110 2270"
    device.shell(f'input tap {cordenada_home}')

    time.sleep(4)

    rolar_tela_vertical(5)

    time.sleep(5)
    device.shell("input keyevent 3")

def abir_navegador(url):

    time.sleep(2)

    device.shell('input keyevent 64')#abrir o navegador
    print("Navegador aberto!")
    barra_pesquisa = '550 100' # x y
    
    device.shell(f'input tap {barra_pesquisa}')#aperta na barar de pesquisa
    print("Barra de pesquisa clicada!")

    time.sleep(2)#respira por 5 segundos
    print("Respirou.")
    
    device.shell(f'input text "{url}"')# insere o texto à ser pesquisado
    print("escrevendo...")

    device.shell('input keyevent 66')# aperta enter
    print("enter")

abrir_insta()