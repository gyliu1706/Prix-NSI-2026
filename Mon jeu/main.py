# 
import pygame
import sys
from sprite import sprites,Sprite
from button import Button
import camera
from entry import Entry
from user import Player
import detection_fonction
import fonction_vig
from map import TileKind
from map import Map
from detection_fonction import keys_down
from screenwelcome import MainMenu

LIST_FONT = ["asset/font/pixel1.ttf"]

def get_font(size):
    return pygame.font.Font("asset/font/pixel1.ttf", size)


cadre_blanc_texte = pygame.image.load("asset/scape/cadre/cadre texte blanc/cadre3.png")
cadre_entry_blanc = pygame.image.load("asset/scape/cadre/cadre texte entry/cadreblanc2.png")
sure_bg1 = pygame.image.load("asset/scape/cadre/cadre verification inscription/cadre1.png")

element_bg = [
    TileKind("grass", "asset/landscape/Herbe2.png", False),
    ]

#--------------------------------------------------------------------------------------------------------------------------------------#

pygame.init()

info_screen = pygame.display.Info()
screen_width = info_screen.current_w
screen_height =  info_screen.current_h
DIMENSION = (screen_width,screen_height)
fonction_vig.get_dimension(DIMENSION)

white = (255,255,255)
black = (0,0,0)
cyan = (0,255,255)

SCREEN=camera.create_screen(screen_width, screen_height, "Mon jeu")





#--------------------------------------------------------------------------------------------------------------------------------------#

player = Player("asset/sprite/MainCharacter.png",32*11, 32*7,100,"","")
#-----Nouveaujeu/lancement du jeu
def NewGame():
    launched = True
    text_box = ""
    passage = 0
    finish = False
    

    while launched:
            SCREEN.fill("black")

            if passage == 0:
                texte_voulu = "Bonjour joueur !"
            elif passage == 1:
                texte_voulu = "Comment vas tu ?"
            elif passage == 2:
                texte_voulu = "J'ai plus trop d'idée"
            elif passage >= 3:
                launched=False
                CreationGame()
                

            if (text_box != texte_voulu):
                text_box = texte_voulu[:len(text_box)+1]
                pygame.time.delay(100)
            else:
                finish = True

            TEXT_BOX = get_font(75).render(text_box, True, "White") #text qui s'affiche
            TEXT_BOX_RECT = TEXT_BOX.get_rect(center=(screen_width//2, 200))
            

            #cadre_blanc = pygame.transform.scale(cadre_blanc_texte, (TEXT_BOX_RECT.width, TEXT_BOX_RECT.height))
            SCREEN.blit(cadre_blanc_texte,((screen_width//2)-(cadre_blanc_texte.get_width()//2), 100)) # (cadre_blanc,((screen_width//2) - (cadre_blanc.get_width()//2), 150))
            
            SCREEN.blit(TEXT_BOX, TEXT_BOX_RECT)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: # quitte avec la croix en haut à droite
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if finish:
                                passage += 1
                                text_box = ""
                                finish=False
                            else :
                                text_box = texte_voulu
        

            pygame.display.flip()

def CreationGame():
    launched = True
    over_entry = False
    text_entry = ""
    time_actuel = pygame.time.get_ticks()
    sure = False
    while launched:
        SCREEN.fill("black")
        delete = False

        MOUSE_POS = pygame.mouse.get_pos()
        
        width_entry = cadre_entry_blanc.get_width()
        height_entry = cadre_entry_blanc.get_height()
        pos_cadre = ((screen_width//2)-(width_entry//2), (screen_height//10)*7)
        
        QUESTION_TEXT = get_font(75).render("Quel est votre nom jeune aventurier ?", True, "White")  
        QUESTION_RECT = QUESTION_TEXT.get_rect(center=(screen_width//2,(screen_height//10)*2))

        ENTRY_USER_NAME = Entry(image=None, pos=(screen_width//2-width_entry//4, (pos_cadre[1]+height_entry//4)), font=get_font(75), color="White",text=text_entry,time=time_actuel)
        ENTRY_USER_NAME.its_over = over_entry

        SCREEN.blit(QUESTION_TEXT, QUESTION_RECT)
        SCREEN.blit(cadre_entry_blanc,(pos_cadre))
        
        
        
        caractere_entry = ""
        for event in pygame.event.get() : 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if detection_fonction.checkForInput(objet_width = width_entry, objet_height = height_entry, position_objet = pos_cadre, position_mouse = MOUSE_POS):
                        ENTRY_USER_NAME.its_over = True
                    else :
                        ENTRY_USER_NAME.its_over = False
                    if sure :
                        if YES_BUTTON.checkForInput(MOUSE_POS):
                            player.name = ENTRY_USER_NAME.value()
                            launched = False
                            ChoiceClass()
                        if NO_BUTTON.checkForInput(MOUSE_POS): 
                            sure=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: 
                        delete = True
                    elif event.key == pygame.K_RETURN:
                        if len(list(ENTRY_USER_NAME.value())) >= 1:
                            sure = True
                    elif event.key == pygame.K_ESCAPE:
                        sure = False

                    else:
                        caractere_entry = event.unicode
                        
        if sure:
            width_verification = sure_bg1.get_width()
            height_verification = sure_bg1.get_height()
            
            pos_cadre = fonction_vig.pos_center(width_verification,height_verification)
    
            MESSAGE_VERIFICATION = get_font(50).render(f"Votre nom est : {ENTRY_USER_NAME.value()}",True, "White")
            QUESTION_VERIFICATION = get_font(50).render(f"Êtes vous sûr de votre choix ?",True,"White")
            VERIFICATION_RECT = MESSAGE_VERIFICATION.get_rect(center=(screen_width//2,(screen_height//2-height_verification//2)+ height_verification//9))
            VERIFICATION_QUESTION_RECT = QUESTION_VERIFICATION.get_rect(center=(screen_width//2,(screen_height//2-height_verification//2)+ height_verification//3))
            YES_BUTTON = Button(image=None, pos=(screen_width//2-width_verification//4, (screen_height//2-height_verification//2)+ height_verification//1.2),text_input="OUI", font=get_font(50), base_color=(117,117,117), hovering_color="White")
            NO_BUTTON = Button(image=None, pos=(screen_width//2+width_verification//4, (screen_height//2-height_verification//2)+ height_verification//1.2),text_input="NON", font=get_font(50), base_color=(117,117,117), hovering_color="White")

        

            for button in [YES_BUTTON, NO_BUTTON]:
                button.changeColor(MOUSE_POS)
                button.update(SCREEN)
                
            
        elif delete:
            ENTRY_USER_NAME.text = ENTRY_USER_NAME.delete()
        else:
            ENTRY_USER_NAME.text = ENTRY_USER_NAME.write(caractere_entry)
        
        ENTRY_USER_NAME.update(SCREEN)
        if sure:
            SCREEN.blit(sure_bg1,pos_cadre)
            SCREEN.blit(MESSAGE_VERIFICATION, VERIFICATION_RECT)
            SCREEN.blit(QUESTION_VERIFICATION, VERIFICATION_QUESTION_RECT)

            for button in [YES_BUTTON, NO_BUTTON]:
                button.changeColor(MOUSE_POS)
                button.update(SCREEN)

        
        time_actuel = ENTRY_USER_NAME.last_update_time
        over_entry = ENTRY_USER_NAME.its_over
        text_entry = ENTRY_USER_NAME.text
        pygame.display.flip()
            
def ChoiceClass():
    launched = True
    image_guerrier = pygame.image.load("asset/bouton/épée.png")
    image_sorcier = pygame.image.load("asset/bouton/sorcier.png")
    image_archer = pygame.image.load("asset/bouton/Arc.png")
    sure = False
    classe_choisi = ""
    while launched:
        SCREEN.fill("black")

        width_verification = sure_bg1.get_width()
        height_verification = sure_bg1.get_height()
        pos_cadre = fonction_vig.pos_center(width_verification,height_verification)
        MOUSE_POS = pygame.mouse.get_pos()

        

        CLASS_TEXT = get_font(75).render("Quel est votre classe jeune aventurier ?", True, "White") #text du menu 
        CLASS_RECT = CLASS_TEXT.get_rect(center=(screen_width//2,(screen_height//10)*2))
        SCREEN.blit(CLASS_TEXT, CLASS_RECT)

        CHEVALIER_BUTTON = Button(image=image_guerrier, pos=(screen_width//8, screen_height//2),text_input="CHEVALIER", font=get_font(50), base_color=(117,117,117), hovering_color="White")
        SORCIER_BUTTON = Button(image=image_sorcier, pos=((screen_width//8)*3, screen_height//2),text_input="SORCIER", font=get_font(50), base_color=(117,117,117), hovering_color="White")
        ARCHER_BUTTON = Button(image=image_archer, pos=((screen_width//8)*5, screen_height//2),text_input="ARCHER", font=get_font(50), base_color=(117,117,117), hovering_color="White")

        for button in [CHEVALIER_BUTTON, SORCIER_BUTTON,ARCHER_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
                    

        

                  
        for event in pygame.event.get() : 
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if sure:
                            if YES_BUTTON.checkForInput(MOUSE_POS):
                                player.classe = classe_choisi
                                launched = False
                                Game()
                            elif NO_BUTTON.checkForInput(MOUSE_POS): 
                                sure = False  
                        else:
                            if CHEVALIER_BUTTON.checkForInput(MOUSE_POS):
                                classe_choisi = "Chevalier"
                                sure = True
                            if SORCIER_BUTTON.checkForInput(MOUSE_POS): 
                                classe_choisi = "Sorcier"
                                sure = True
                            if ARCHER_BUTTON.checkForInput(MOUSE_POS):
                                classe_choisi = "Archer"
                                sure = True
                if event.type == pygame.QUIT: 
                        pygame.quit()
                        sys.exit()

            
        if sure :

                size_font = 50
                MESSAGE_VERIFICATION1 = get_font(size_font).render(f"Vous avez choisi la classe : ",True, "White")
                MESSAGE_VERIFICATION2 = get_font(size_font).render(classe_choisi,True, "White")
                QUESTION_VERIFICATION = get_font(size_font).render("Êtes vous sûr de votre choix ?",True,"White")
                VERIFICATION_RECT1 = MESSAGE_VERIFICATION1.get_rect(center=(screen_width//2,(screen_height//2-height_verification//2)+ height_verification//9))
                VERIFICATION_RECT2 = MESSAGE_VERIFICATION2.get_rect(center=(screen_width//2,(screen_height//2-height_verification//2)+ height_verification//9+size_font))
                VERIFICATION_QUESTION_RECT = QUESTION_VERIFICATION.get_rect(center=(screen_width//2,(screen_height//2-height_verification//2)+ height_verification//3))
                YES_BUTTON = Button(image=None, pos=(screen_width//2-width_verification//4, (screen_height//2-height_verification//2)+ height_verification//1.2),text_input="OUI", font=get_font(50), base_color=(117,117,117), hovering_color="White")
                NO_BUTTON = Button(image=None, pos=(screen_width//2+width_verification//4, (screen_height//2-height_verification//2)+ height_verification//1.2),text_input="NON", font=get_font(50), base_color=(117,117,117), hovering_color="White")
                
                SCREEN.blit(sure_bg1,pos_cadre)
                SCREEN.blit(MESSAGE_VERIFICATION1,VERIFICATION_RECT1)
                SCREEN.blit(MESSAGE_VERIFICATION2,VERIFICATION_RECT2)
                SCREEN.blit(QUESTION_VERIFICATION, VERIFICATION_QUESTION_RECT)
                
                for button in [YES_BUTTON, NO_BUTTON]:
                    button.changeColor(MOUSE_POS)
                    button.update(SCREEN)


        pygame.display.flip()

def Game():


    map_data = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
          ]

    map = Map("data/start.map", element_bg, 32)
    clear_color = (0, 165, 63)

    


    launched = True
    while launched:
    


        for event in pygame.event.get() : 
                    if event.type == pygame.QUIT: 
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        keys_down.add(event.key)
                    elif event.type == pygame.KEYUP:
                        keys_down.remove(event.key)
    
        SCREEN.fill(clear_color)
        map.draw(SCREEN)
        player.update()
        for s in sprites:
            s.draw(SCREEN)

        



        pygame.display.flip()

        pygame.time.delay(17)


MainMenu()



# refaire tout les cadres en petit format