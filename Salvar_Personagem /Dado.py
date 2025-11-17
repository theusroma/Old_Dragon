import random

class Dado():
    """Classe para simular a rolagem de um dado de N lados."""
    def __init__(self, lados):
        self.lados = lados

    def rolar(self):
        """Retorna um número aleatório entre 1 e o número de lados."""
        return random.randint(1, self.lados)
