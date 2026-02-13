import pygame
import sys 
import fonction_vig
from button import Button

def YouAreSure(texte,screen,font,dimension,position_souris,background):
    width_verification = background.get_width()
    height_verification = background.get_height()
            
    pos_cadre = fonction_vig.pos_center(width_verification,height_verification)
    
    MESSAGE_VERIFICATION = font.render(texte,True, "White")
    QUESTION_VERIFICATION = font(50).render("Êtes vous sûr de votre choix ?",True,"White")
    VERIFICATION_RECT = MESSAGE_VERIFICATION.get_rect(center=(dimension[0]//2,(dimension[1]//2-height_verification//2)+ height_verification//9))
    VERIFICATION_QUESTION_RECT = QUESTION_VERIFICATION.get_rect(center=(dimension[0]//2,(dimension[1]//2-height_verification//2)+ height_verification//4))
    YES_BUTTON = Button(image=None, pos=(dimension[0]//2-width_verification//4, (dimension[1]//2-height_verification//2)+ height_verification//1.2),text_input="OUI", font=get_font(50), base_color=(117,117,117), hovering_color="White")
    NO_BUTTON = Button(image=None, pos=(dimension[0]//2+width_verification//4, (dimension[1]//2-height_verification//2)+ height_verification//1.2),text_input="NON", font=get_font(50), base_color=(117,117,117), hovering_color="White")
    for button in [YES_BUTTON, NO_BUTTON]:
                button.changeColor(position_souris)
                button.update(screen)
    screen.blit(background,pos_cadre)
    screen.blit(MESSAGE_VERIFICATION, VERIFICATION_RECT)
    screen.blit(QUESTION_VERIFICATION, VERIFICATION_QUESTION_RECT)

    for event in pygame.event.get() : 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if YES_BUTTON.checkForInput(position_souris):
                            return True
                        elif NO_BUTTON.checkForInput(position_souris): 
                            return False
                        
    return None
                            
                        
    













    screen.blit(background,pos_cadre)
    background.blit(MESSAGE_VERIFICATION, VERIFICATION_RECT)



