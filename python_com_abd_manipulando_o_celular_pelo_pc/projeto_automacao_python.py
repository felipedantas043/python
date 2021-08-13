import time
from ppadb.client import Client as AdbClient

def connect():
    
    client = AdbClient(host='127.0.0.1', port=5037)

    devices = client.devices()

    if len(devices) == 0:
        print('No devices (nenhum dispositivo encontrado!)')
        quit()

    device = devices[0]

    print(f'connected to {device}')

    return device, client

# dando comandos para o celular:
# device, client = connect()
# device.shell("input tap 927 2145")


def rolar_tela(vezes):

    #variaveis que armazenam onde começa a rolagem na tela, termina e a duração.
    start_x = 500
    start_y = 1500
    end_x = 500
    end_y = 700
    duration_ms = 300

    device, client = connect()
    
    #loop para rolar a tela varias vezes
    contador = 0
    while contador < vezes:
        device.shell(f'input swipe {start_x} {start_y} {end_x} {end_y} {duration_ms}')#aqui são passado os valores  das variaveis acima
        print(f'Rolou a tela {contador +1} vezes')
        contador = contador + 1

def abir_navegador(pesquisa):
    device, client = connect()

    time.sleep(2)

    device.shell('input keyevent 64')#abrir o navegador
    barra_pesquisa = '550 100' # x y
    
    device.shell(f'input tap {barra_pesquisa}')#aperta na barar de pesquisa
    time.sleep(2)#respira por 5 segundos
    device.shell(f'input text "{pesquisa}"')# insere o texto à ser pesquisado
    device.shell('input keyevent 66')# aperta enter

abir_navegador("felipe dantas")
