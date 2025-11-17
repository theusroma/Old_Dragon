from abc import ABC, abstractmethod
from Dado import Dado

class Classe(ABC):
    """
    Classe Base Abstrata para todas as Classes de Personagem.
    Define características iniciais e um método obrigatório para subir de nível.
    """
    def __init__(self, vida_inicial, ataque_inicial, protecao_inicial, dado_vida_lados):
        self.vida = vida_inicial
        self.ataque = ataque_inicial
        self.protecao = protecao_inicial
        self.habilidades_classe = []
        self.nivel = 1
        self.dado = Dado(dado_vida_lados) 
    
    @abstractmethod
    def subir_de_nivel(self):
        """Obrigatório: Implementa o ganho de vida e outros bônus de nível."""
        pass
    
    def exibir_habilidades_classe(self):
        """Retorna a lista de habilidades para exibição."""
        return self.habilidades_classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__(vida_inicial=10, ataque_inicial=1, protecao_inicial=5, dado_vida_lados=10)
        self.habilidades_classe = ['Aparar', 'Maestria em Arma', 'Ataque Extra']

    def subir_de_nivel(self):
        self.vida += self.dado.rolar()
        self.ataque += 1
        self.nivel += 1

class Ladrao(Classe):
    def __init__(self):
        super().__init__(vida_inicial=6, ataque_inicial=1, protecao_inicial=5, dado_vida_lados=6)
        self.habilidades_classe = ['Ataque Furtivo', 'Ouvir Ruídos', 'Talentos de Ladrão']

    def subir_de_nivel(self):
        self.vida += self.dado.rolar()
        self.nivel += 1

class Mago(Classe):
    def __init__(self):
        super().__init__(vida_inicial=4, ataque_inicial=0, protecao_inicial=5, dado_vida_lados=4)
        self.habilidades_classe = ['Magias Arcanas', 'Ler Magias', 'Detectar Magias']
        self.magias_arcanas = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0} # Exemplo de recurso de classe

    def subir_de_nivel(self):
        self.vida += self.dado.rolar()
        self.nivel += 1
