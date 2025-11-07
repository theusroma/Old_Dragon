from Dado import Dado
from utils import limpar_tela
import time
from Raca import Raca, Humano, Elfo, Anao
from Classe import Classe, Guerreiro, Ladrao, Mago

class Personagem():
    """Classe principal que agrega Raca, Classe e Atributos."""
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0 
        self.raca = None
        self.classe = None
        self.dado_atributo = Dado(6) 
        self.atributos_gerados = [] 

    # ==================== ESTILOS DE GERAÇÃO DE ATRIBUTOS ====================
    
    def estilo_classico(self):
        self.atributos_gerados = []
        atributos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']

        print(f"\n>> Geração de atributos para {self.nome} (Estilo Clássico - 3d6 em ordem):")
        
        for nome_atributo in atributos:
            acumulado = sum(self.dado_atributo.rolar() for _ in range(3)) 
            setattr(self, nome_atributo, acumulado)
            self.atributos_gerados.append(acumulado)
            print(f'   {nome_atributo.capitalize()}: {acumulado}')

    def estilo_aventureiro(self):
        self.atributos_gerados = []
        print("\n>> Gerando 6 valores (Estilo Aventureiro - 3d6):")
        
        for i in range(6):
            acumulado = sum(self.dado_atributo.rolar() for _ in range(3))
            self.atributos_gerados.append(acumulado)
            print(f'   Valor {i+1}: {acumulado}')
        
        self._distribuir_atributos(self.atributos_gerados)

    def estilo_heroico(self):
        self.atributos_gerados = []
        print("\n>> Gerando 6 valores (Estilo Heróico - 4d6, descarta o menor):")

        for i in range(6):
            rolagens = [self.dado_atributo.rolar() for _ in range(4)]
            menor = min(rolagens)
            soma = sum(rolagens) - menor
            
            self.atributos_gerados.append(soma)
            print(f'   Valor {i+1}: {soma} (Rolagens: {rolagens}, Menor descartado: {menor})')
            
        self._distribuir_atributos(self.atributos_gerados)


    def _distribuir_atributos(self, valores_gerados):
        limpar_tela()
        print('=========== DISTRIBUIÇÃO MANUAL DE ATRIBUTOS ===========')
        print(f'>> Valores gerados pelos dados: {sorted(valores_gerados, reverse=True)}')

        atributos_disponiveis = {
            '1': 'forca', '2': 'destreza', '3': 'constituicao',
            '4': 'inteligencia', '5': 'sabedoria', '6': 'carisma',
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
                    valores_restantes.pop(0)
                    escolha_valida = True
                    print(f'\n>> {nome_atributo.capitalize()} recebeu o valor {valor_atual}.')
                else: 
                    print('\n>> Opção inválida ou atributo já escolhido! Tente novamente.')
        
        time.sleep(1)
        limpar_tela()
        print('>> Distribuição finalizada.')
        self.exibir_atributos()
        time.sleep(2)


    # ==================== EXIBIÇÃO DE INFORMAÇÕES ====================

    def exibir_atributos(self):
        print('\n======= SEUS ATRIBUTOS FINAIS =======')
        print(f'>> Força: {self.forca}')
        print(f'>> Destreza: {self.destreza}')
        print(f'>> Constituição: {self.constituicao}')
        print(f'>> Inteligência: {self.inteligencia}')
        print(f'>> Sabedoria: {self.sabedoria}')
        print(f'>> Carisma: {self.carisma}')
        print('=====================================\n')

    def exibir_info_completa(self):
        if not self.raca or not self.classe:
            print('>> Raça e/ou Classe não definidas.')
            return
            
        print('\n========== INFORMAÇÕES DO PERSONAGEM ==========')
        print(f'>> Nome: {self.nome}')
        print(f'>> Raça: {self.raca.__class__.__name__}')
        print(f'>> Classe: {self.classe.__class__.__name__}')
        print('-----------------------------------------------')
        print(f'>> Nível: {self.classe.nivel}')
        print(f'>> Vida Máxima (Inicial): {self.classe.vida}')
        print(f'>> Ataque Base: {self.classe.ataque}')
        print(f'>> Proteção Base (CA): {self.classe.protecao}')
        print(f'>> Dado de Vida: d{self.classe.dado.lados}')
        print('-----------------------------------------------')
        print(f'>> Movimento: {self.raca.movimento}m')
        print(f'>> Infravisão: {self.raca.infravisao}m')
        print(f'>> Alinhamento: {self.raca.alinhamento}')
        print('===============================================\n')

    def exibir_habilidades_classe(self):
        if self.classe:
            habilidades = self.classe.exibir_habilidades_classe()
            print(f'\n========== HABILIDADES DE CLASSE ({self.classe.__class__.__name__}) ==========')
            for h in habilidades:
                print(f'>> {h}')
            print('============================================================\n')
        else:
            print('>> Classe não definida.')

    def exibir_habilidades_raca(self):
        if self.raca:
            habilidades = self.raca.exibir_habilidades_raca()
            print(f'\n========== HABILIDADES DE RAÇA ({self.raca.__class__.__name__}) ==========')
            for h in habilidades:
                print(f'>> {h}')
            print('======================================================\n')
        else:
            print('>> Raça não definida.')