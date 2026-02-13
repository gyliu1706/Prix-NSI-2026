import pygame

def checkForInput(objet_width,objet_height,position_objet ,position_mouse):
        if position_mouse[0] in range(position_objet[0], position_objet[0]+objet_width) and position_mouse[1] in range(position_objet[1], position_objet[1]+objet_height):
            return True
        return False


keys_down = set()

def is_key_pressed(key):
    return key in keys_down
