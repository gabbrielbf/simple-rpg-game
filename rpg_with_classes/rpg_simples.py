class Personagem:
    """ Classe responsável por 
    instânciar e definir os personagens """
    def __init__(self, nome, vida, nivel, mana):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        self.__mana = mana

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def get_mana(self):
        return self.__mana
    
    def exibir_dados(self):
        return f'- Nome: {self.get_nome()}\n- Vida: {self.get_vida()}\n- Nivel: {self.get_nivel()}\n- Mana: {self.get_mana()}'
    

class Protagonista(Personagem):
    def __init__(self, nome, vida, nivel, mana, habilidade):
        super().__init__(nome, vida, nivel, mana)
        self.__habilidade = habilidade

    def exibir_dados(self):
        return f'{super().exibir_dados()}\n- Habilidade: {self.get_habilidade()}\n'

    def get_habilidade(self):
        return self.__habilidade


class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, mana, tipo):
        super().__init__(nome, vida, nivel, mana)
        self.__tipo = tipo

    def exibir_dados(self):
        return f'{super().exibir_dados()}\n- Tipo: {self.get_tipo()}\n'

    def get_tipo(self):
        return self.__tipo
    

class Play:
    """ Classe responsável por 
    inciar e orquestrar o jogo """
    def __init__(self):
        self.protagonista = Protagonista(nome='Goku', vida=100, nivel=5, mana=60 ,habilidade='Kamehameha')
        self.vilao = Vilao(nome='Coringa', vida=160, nivel=3, mana=30, tipo='Assassino')

    def inciar_batalha(self):
        """ Gestiona as batalhas 
        em turno estilo Pokémon """
        print('='*19)
        print('|Iniciando batalha|')
        print('='*19)

        while self.protagonista.get_vida() > 0 and self.vilao.get_vida() > 0:
            print('Personagens:')
            print(self.protagonista.exibir_dados())
            print(self.vilao.exibir_dados())

            input('Press ENTER...')
            print('1 - Ataque normal')
            print('2 - Ataque especial')
            opcao = input('Digite aqui -> ')
            