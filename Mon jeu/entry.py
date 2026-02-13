import pygame
import copy
    
delai = 250

class Entry(): 
    def __init__(self,image,pos,font,color,text,time):
        self.image = image
        self.posX = pos[0]
        self.posY = pos[1]
        self.font = font
        self.color = color
        self.text = text
        self.rendu = self.font.render(self.text,True,self.color)
        self.its_over = False
        self.last_update_time = time
        if self.image is None:
            self.image = self.rendu
        self.rect = self.image.get_rect()
        self.text_rect = self.rendu.get_rect()

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, (self.posX,self.posY))
        screen.blit(self.rendu, (self.posX,self.posY))

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def write(self,input_text):
        current_time = pygame.time.get_ticks()
        if self.its_over :
            text_entry = str(self.text)
            if len(text_entry) > 0:
                text_entry = list(text_entry)
                if input_text == '|':
                    print("Texte invalide saisi")
                else:
                    reel_text = copy.deepcopy(text_entry)
                    reel_text = clear_barre(reel_text)
                    if reel_text != [] or reel_text is not None:
                        if len(reel_text) == 8:
                            reel_text.append('|')
                            reel_text = "".join(reel_text)
                            return reel_text
                        elif input_text == "" and current_time - self.last_update_time > delai:
                            self.last_update_time = current_time 
                            if text_entry[-1] == '|':
                                reel_text = "".join(reel_text)
                                return reel_text
                            else:
                                text_entry.append('|')
                                text_entry = "".join(text_entry)
                                return text_entry
                        
                        else :
                            if reel_text == text_entry:
                                reel_text.append(input_text)
                                reel_text = "".join(reel_text)
                                return reel_text
                            else:
                                reel_text.append(input_text)
                                reel_text.append('|')
                                reel_text = "".join(reel_text)
                                return reel_text
                    else: 
                        if len(text_entry) == 0 or text_entry is None:
                            if write_empty(input_text,current_time,self.last_update_time) == "|":
                                self.last_update_time = current_time
                                return write_empty(input_text,current_time,self.last_update_time)
                            else:
                                return write_empty(input_text,current_time,self.last_update_time)
                        else:    
                            return ""
            else:
                retour = write_empty(input_text,current_time,self.last_update_time)
                if retour == '|':
                    self.last_update_time = current_time
                    return retour
                else:
                    return retour
        else:
            return "".join(clear_barre(self.text))

    def delete(self):
        texte = self.text
        liste_texte = clear_barre(list(texte))
        if len(liste_texte) == 0:
            return texte
        else:
            del liste_texte[-1]
            if texte[-1] == '|':
                liste_texte.append('|')
            texte = "".join(liste_texte)
            return texte

    def value(self):
        value = "".join(clear_barre(list(self.text)))
        return value.strip()

                    
def clear_barre (text):
    if len(text) >= 1:
        if text[-1] == '|':
            del text[-1]
            return text
        else :
            return text
    else:
        return []
    
def write_empty(input_text,actually_time,last_update):
    if input_text == "" and actually_time - last_update > delai:
        return "|"
    else:
        return input_text 
    



    