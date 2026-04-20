import random
import time
import os
import json

lista_sorteio = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar(texto,velocidade=0.04):
    for letra in texto:
        print(letra,end='',flush=True)
        time.sleep(velocidade)
    print()

def salvar_dados():
    with open('dados.json','w') as arquivo:
        json.dump(lista_sorteio,arquivo)

def carregar_dados():
    global lista_sorteio

    try:
        with open('dados.json', 'r') as arquivo:
            lista_sorteio = json.load(arquivo)
    except FileNotFoundError:
        lista_sorteio = []

def menu():
    print('\n--- ROLETA DE SORTEIO ---')
    print('Selecione utilizando o número da opção')
    print('1 - Adicionar itens')
    print('2 - Sortear')
    print('3 - Ver itens')
    print('4 - Limpar itens')
    print('5 - Sair')

def voltar_menu():
    input('\nPressione ENTER para voltar... ')

def armazenar_itens():
    while True:
        item = input("Digite um item (Enter vazio para parar): \n")
        
        if item == "":
            break
        lista_sorteio.append(item)
        salvar_dados()
    limpar_tela()
    
def sorteio():
    if not lista_sorteio:
        return "Nenhum item foi adicionado!"
    return random.choice(lista_sorteio)
   
def exibir_resultado():
    limpar_tela()
    if not lista_sorteio:
        print("Nenhum item foi adicionado!")
        voltar_menu()
        return 
    print('--- RESULTADO ---'.center(50))

    #Parte gráfica para efeito de roleta pra o usuário
    for i in range(10):
        print(random.choice(lista_sorteio).center(50), end='\r')
        time.sleep(0.2)
    resultado = sorteio()
      
    #Exbir o resultado final
    time.sleep(0.5)
    limpar_tela()
    print('🎉 RESULTADO FINAL'.center(50))
    print(resultado.center(50))

    voltar_menu()

def ver_itens():
    limpar_tela()
    if not lista_sorteio:
        print('Nenhum item adicionado.')
    else:
        for item in lista_sorteio:
            print(item)
    voltar_menu()

def limpar_lista():
    limpar_tela()
    lista_sorteio.clear()
    salvar_dados()
    print('Lista de itens foi zerada! ')
    voltar_menu()
      
def escolher_opcao():
    try:
        return int(input('\nDigite uma opção: '))
    except ValueError:
        return 0

def sair(texto1,texto2):
    limpar_tela()
    digitar(texto1, 0.1)
    print()
    digitar(texto2, 0.02)
     
def main():
    carregar_dados()

    while True:
        limpar_tela()
        menu()
        opcao = escolher_opcao()

        if opcao == 1:
            armazenar_itens()
        elif opcao == 2:
            exibir_resultado()
        elif opcao == 3:
            ver_itens()
        elif opcao == 4:
            limpar_lista()
        elif opcao == 5:
            sair('Finalizando programa .... ','Até a próxima! 👋\n')
            break
        else:
            print('Opção inválida!')
            input('\nPressione ENTER para tentar novamente...')
   
main()