from Dado import Dado
from utils import limpar_tela
import time
import sys

class Personagem():
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0 
        self.dado = Dado(6)
        self.atributos_gerados = []

    def exibir_atributos(self):
        print('\n======= SEUS ATRIBUTOS FINAIS =======')
        print(f'>> Força: {self.forca}')
        print(f'>> Destreza: {self.destreza}')
        print(f'>> Constituição: {self.constituicao}')
        print(f'>> Inteligência: {self.inteligencia}')
        print(f'>> Sabedoria: {self.sabedoria}')
        print(f'>> Carisma: {self.carisma}')
        print('=====================================\n')


    def estilo_classico(self):
        self.atributos_gerados = []
        atributos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']

        print(f"\n>> Geração de atributos para {self.nome} (Estilo Clássico - 3d6 em ordem):")
        time.sleep(1)

        for nome_atributo in atributos:
            acumulado = sum(self.dado.rolar() for _ in range(3)) 
            setattr(self, nome_atributo, acumulado)
            self.atributos_gerados.append(acumulado)
            print(f'   {nome_atributo.capitalize()}: {acumulado}')
            time.sleep(0.5)

        print('\n>> Atributos definidos automaticamente.')
        self.exibir_atributos()

    def estilo_aventureiro(self):
        self.atributos_gerados = []
        print("\n>> Gerando 6 valores (Estilo Aventureiro - 3d6):")
        time.sleep(1)

        for i in range(6):
            acumulado = sum(self.dado.rolar() for _ in range(3))
            self.atributos_gerados.append(acumulado)
            print(f'   Valor {i+1}: {acumulado}')
            time.sleep(0.5)
        
        self.distribuir_atributos(self.atributos_gerados)

    def estilo_heroico(self):
        self.atributos_gerados = []
        print("\n>> Gerando 6 valores (Estilo Heróico - 4d6, descarta o menor):")
        time.sleep(1)

        for i in range(6):
            rolagens = [self.dado.rolar() for _ in range(4)]
            menor = min(rolagens)
            soma = sum(rolagens) - menor
            
            self.atributos_gerados.append(soma)
            print(f'   Valor {i+1}: {soma} (Rolagens: {rolagens}, Menor descartado: {menor})')
            time.sleep(0.5)
            
        self.distribuir_atributos(self.atributos_gerados)


    def distribuir_atributos(self, valores_gerados):
        limpar_tela()
        print('=========== ESCOLHA DE ATRIBUTOS ===========')
        print(f'>> Valores gerados pelos dados: {sorted(valores_gerados, reverse=True)}')

        atributos_disponiveis = {
            '1': 'forca',
            '2': 'destreza',
            '3': 'constituicao',
            '4': 'inteligencia',
            '5': 'sabedoria',
            '6': 'carisma',
        }
        
        valores_restantes = sorted(list(valores_gerados), reverse=True)
        atributos_alocados = []
        
        while valores_restantes:
            valor_atual = valores_restantes[0]
            print(f'\n>> Qual atributo você escolhe para receber o valor: {valor_atual}?')
            
            opcoes_validas = {}
            for chave, nome in atributos_disponiveis.items():
                if nome not in atributos_alocados:
                    print(f'[{chave}] {nome.capitalize()}')
                    opcoes_validas[chave] = nome

            escolha_valida = False
            while not escolha_valida:
                try:
                    escolha = input('>> ').strip()
                except Exception:
                    print('>> |ERRO| Entrada inválida. Tente novamente.')
                    continue

                if escolha in opcoes_validas:
                    nome_atributo = atributos_disponiveis[escolha]
                    setattr(self, nome_atributo, valor_atual)
                    atributos_alocados.append(nome_atributo)
                    escolha_valida = True
                    print(f'\n>> {nome_atributo.capitalize()} recebeu o valor {valor_atual}.')
                else: 
                    print('\n>> Opção inválida ou atributo já escolhido! Tente novamente.')
        
        time.sleep(2)
        limpar_tela()
        print('>> Distribuição finalizada.')
        self.exibir_atributos()