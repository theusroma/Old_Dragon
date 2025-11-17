from Personagem import Personagem
from Raca import Humano, Elfo, Anao
from Classe import Guerreiro, Ladrao, Mago
from utils import limpar_tela
import time
import sys

def selecionar_raca():
    """Permite ao usuário selecionar a raça do personagem."""
    racas_map = {
        '1': Humano(),
        '2': Elfo(),
        '3': Anao()
    }
    
    while True:
        print('>> Selecione a Raça do seu personagem: ')
        print('============================')
        print('[1] Humano\n[2] Elfo\n[3] Anão')
        print('============================')

        op_racas = input('>> ').strip()

        if op_racas in racas_map:
            return racas_map[op_racas]
        else:
            print('\n>> |ERRO| Opção inválida! Tente novamente.\n')
            time.sleep(1)

def selecionar_classe():
    """Permite ao usuário selecionar a classe do personagem."""
    classes_map = {
        '1': Guerreiro(),
        '2': Ladrao(),
        '3': Mago()
    }

    while True:
        print('>> Selecione a Classe do seu personagem: ')
        print('========= Classes =========')
        print('[1] Guerreiro\n[2] Ladrão\n[3] Mago')
        print('===========================')

        op_classes = input('>> ').strip()

        if op_classes in classes_map:
            return classes_map[op_classes]
        else:
            print('\n>> |ERRO| Opção inválida! Tente novamente.\n')
            time.sleep(1)

def selecionar_estilo(personagem):
    """Permite ao usuário selecionar o estilo de geração de atributos."""
    while True: 
        print(f'>> {personagem.nome}, selecione o estilo de distribuição de atributos: ')
        print('=======================\n[1] Estilo Clássico (3d6 em ordem)\n[2] Estilo Aventureiro (3d6, distribui)\n[3] Estilo Heróico (4d6, descarta o menor, distribui) \n[0] Sair\n=======================')

        try:
            op_atributos = int(input('>> '))
        except ValueError:
            print('>> |ERRO| Digite apenas números! (0 a 3)\n')
            time.sleep(1)
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
            print('>> |ERRO| Digite apenas um número entre 1 e 3!\n')
            time.sleep(1)
            continue
        
def menu_principal(personagem):
    """Menu de interação final com o personagem criado."""
    while True:
        print('>> O que deseja fazer agora?')
        print('=================================\n[1] Exibir Atributos\n[2] Informações Completas\n[3] Exibir Habilidades de Classe\n[4] Exibir Habilidades da Raça\n[5] Subir de Nível (Teste)\n[0] Sair\n=================================')

        op_acao = input('>> ').strip()
            
        if op_acao == '0':
            print(f'\n>> Obrigado por criar seu personagem, {personagem.nome}!')
            break
        elif op_acao == '1':
            personagem.exibir_atributos()
        elif op_acao == '2':
            personagem.exibir_info_completa()
        elif op_acao == '3':
            personagem.exibir_habilidades_classe()
        elif op_acao == '4':
            personagem.exibir_habilidades_raca()
        elif op_acao == '5':
            personagem.classe.subir_de_nivel()
            print(f'\n>> {personagem.nome} subiu para o Nível {personagem.classe.nivel}! Vida atual: {personagem.classe.vida}.')
            if hasattr(personagem.classe, 'ataque'):
                 print(f'>> Novo Ataque: {personagem.classe.ataque}.')
        else:
            print('>> |ERRO| Opção inválida!\n')
            time.sleep(1)


def main():
    limpar_tela()
    print('\nBEM VINDO À CRIAÇÃO DE PERSONAGEM OLD DRAGON!')
    print('=============================================')

    nome_personagem = input('\n>> Qual é o nome do seu personagem? ').strip()
    personagem = Personagem(nome_personagem)

    limpar_tela()

    personagem.raca = selecionar_raca()
    limpar_tela()
    print(f'>> Raça Selecionada: {personagem.raca.__class__.__name__}')
    time.sleep(1)

    personagem.classe = selecionar_classe()
    limpar_tela()
    print(f'>> Classe Selecionada: {personagem.classe.__class__.__name__}')
    time.sleep(1)

    selecionar_estilo(personagem)
    
    menu_principal(personagem)
        
        
if  __name__ == '__main__':
    main()
