from Personagem import Personagem
from utils import limpar_tela
import time
import sys 

def main():
    limpar_tela()
    
    print('\nBEM VINDO À GERAÇÃO DE ATRIBUTOS (Old Dragon)!')
    print('=============================================')

    print('\n>> Qual é o nome do seu personagem? ')
    nome_personagem = input('>> ').strip()
    personagem = Personagem(nome_personagem)

    limpar_tela()
    
    while True: 
        print(f'>> {personagem.nome}, selecione a forma de distribuição de atributos: ')
        print('=======================\n[1] Estilo Clássico (3d6 em ordem)\n[2] Estilo Aventureiro (3d6, distribui)\n[3] Estilo Heróico (4d6, descarta o menor, distribui) \n[0] Sair\n=======================')

        try:
            op_atributos = int(input('>> '))
        except ValueError:
            print('>> |ERRO| Digite apenas números! (0 a 3)\n')
            time.sleep(2)
            limpar_tela()
            continue

        limpar_tela()

        if op_atributos == 0:
            print('>> Encerrando programa...')
            sys.exit()
        elif op_atributos == 1:
            personagem.estilo_classico()
            break
        elif op_atributos == 2:
            personagem.estilo_aventureiro()
            break
        elif op_atributos == 3:
            personagem.estilo_heroico()
            break
        else:
            print('>> |ERRO| Digite apenas um número entre 0 e 3!\n')
            time.sleep(2)
            limpar_tela()
            continue
            
    while True:
        print('\n>> O que deseja fazer agora?')
        print('=================================\n[1] Exibir Atributos Finais\n[0] Sair\n=================================')

        try:
            op_acao = input('>> ').strip()
        except Exception:
            print('>> |ERRO| Entrada inválida. Tente novamente.')
            time.sleep(1)
            continue
            
        if op_acao == '0':
            print(f'\n>> Obrigado por jogar, {personagem.nome}!')
            break
        elif op_acao == '1':
            personagem.exibir_atributos()
        else:
            print('>> |ERRO| Digite apenas 0 ou 1!\n')
            time.sleep(1)
            continue
        
        
        
if  __name__ == '__main__':
    main()
