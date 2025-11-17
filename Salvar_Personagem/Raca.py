from abc import ABC, abstractmethod

class Raca(ABC):
    """
    Classe Base Abstrata para todas as Raças.
    Define características comuns (movimento, infravisão, alinhamento)
    e um método para exibir habilidades.
    """
    def __init__(self, movimento, infravisao, alinhamento, peso_base):
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.peso_base = peso_base
        self.habilidades = []
        
    def exibir_habilidades_raca(self):
        """Retorna a lista de habilidades para exibição."""
        return self.habilidades


class Humano(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao=0, alinhamento='Qualquer', peso_base=80)
        self.habilidades = ['Aprendizado', 'Adaptabilidade']

class Elfo(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao=18, alinhamento='Neutro', peso_base=60)
        self.habilidades = ['Percepção Natural', 'Graciosos', 'Arma Racial', 'Imunidades']

class Anao(Raca):
    def __init__(self):
        super().__init__(movimento=6, infravisao=18, alinhamento='Ordem', peso_base=75)
        self.habilidades = ['Mineradores', 'Vigoroso', 'Arma Grande', 'Inimigos']
