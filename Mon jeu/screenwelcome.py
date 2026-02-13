import pygame
import sys
from main import SCREEN
from main import screen_width
from button import Button
from main import NewGame
from main import get_font


def MainMenu():
    launched = True
    while launched:
        
        SCREEN.fill("black")

        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TITLE = get_font(100).render("LE JEU SANS NOM !", True, "yellow") #text du menu 
        MENU_RECT = MENU_TITLE.get_rect(center=(screen_width//2, 100))
        SCREEN.blit(MENU_TITLE, MENU_RECT)

        couleur_button = (213,213,213)

        PLAY_BUTTON = Button(image=None, pos=(screen_width//2,250),text_input="JOUER", font=get_font(75), base_color=couleur_button, hovering_color="White") #(center_basic(screen_width,)
        OPTIONS_BUTTON = Button(image=None, pos=(screen_width//2, 400),text_input="OPTIONS", font=get_font(75), base_color=couleur_button, hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(screen_width//2, 550),text_input="QUITTER", font=get_font(75), base_color=couleur_button, hovering_color="White")

        

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quite avec la croix en haut à droite
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    launched = False
                    NewGame()
                if OPTIONS_BUTTON.checkForInput(MOUSE_POS):
                    print("Je suis dans les options")
                if QUIT_BUTTON.checkForInput(MOUSE_POS): 
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()