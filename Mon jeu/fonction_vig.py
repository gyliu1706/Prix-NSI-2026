import pygame

global dimension_screen

def get_dimension(information):
    global dimension_screen
    dimension_screen = information


def pos_center(element_width,element_height):
    return ((dimension_screen[0]//2)-(element_width//2),(dimension_screen[1]//2)-(element_height//2))




def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    return lines

def draw_wrapped_text(surface, text, font, color, position, max_width):
    lines = wrap_text(text, font, max_width)
    x, y = position
    for line in lines:
        rendered_line = font.render(line, True, color)
        surface.blit(rendered_line, (x, y))
        y += font.get_linesize()



