import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size = prend une police de caractère dans le fichier "assets" et rajoute la taille
    return pygame.font.Font("assets/font.ttf", size)# charge une police de caractère et sa taille qui est rentrée

def play(): #tourne en boucle
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White") # crée le texte avec la police et taille de la fonction get_font
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260)) #prend toutes les informations du "rectangle" PLAY_TEXT
        SCREEN.blit(PLAY_TEXT, PLAY_RECT) #pose la surface PLAY_TEXT dans les coordonnées PLAY_RECT (prise juste avant)

        PLAY_BACK = Button(image=None, pos=(640, 460), #crée un boutton de la classe Button (fichier "button.py") sans image avec ces coordonnées
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green") #autre argument du bouton

        PLAY_BACK.changeColor(PLAY_MOUSE_POS) #charge constamment cette fonction
        PLAY_BACK.update(SCREEN) #charge constamment cette fonction

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quite avec la croix en haut à droite
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # si la touche MOUSEBUTTONDOWN est pressée
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS): # fait la fonction checkForInput de la classe button
                    main_menu() # passe à la fonction main_menu
                    return

        pygame.display.flip()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white") #met l'écran en blanc

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.flip()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0)) #affiche sur la zone "SCREEN" l'iùmage contenu dans "BG" mis en coordonnées x=0 y=0)

        MENU_MOUSE_POS = pygame.mouse.get_pos() # prend constamment la position de la souris

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40") #text du menu 
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100)) # prend les coordonnées de la zone de textes "MENU_TEXT"

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), #bouton 1
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), #bouton 2
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), #bouton 3
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT) #affiche sur le texte "SCREEN" l'image contenu dans "MENU_TEXT" mis en coordonnées de MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]: # on fait chacune des fonctions pour chaque boutons
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quite avec la croix en haut à droite
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                    return
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                    return
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): 
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

main_menu()


