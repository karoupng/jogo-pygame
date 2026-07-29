import pygame
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        # 1. CORREÇÃO: Adicionamos o 'self.' para a janela ser global na classe
        self.window = pygame.display.set_mode(size=(600, 480))

        # 2. CORREÇÃO: Declaramos o menu na "certidão de nascimento"
        self.menu = None

    def run(self):
        while True:

            self.menu = Menu(self.window)
            self.menu.run()
            pass

       