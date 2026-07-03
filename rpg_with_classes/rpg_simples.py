class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_dados(self):
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()}\n{self.get_nivel()}'
    

class Protagonista(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def exibir_dados(self):
        return f'{super().exibir_dados()}\nHabilidade: {self.get_habilidade()}\n'

    def get_habilidade(self):
        return self.__habilidade


class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def exibir_dados(self):
        return f'{super().exibir_dados()}\Tipo: {self.get_tipo()}\n'

    def get_tipo(self):
        return self.__tipo