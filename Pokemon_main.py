# Michael Leventeris - Pokemon Typing Simulator

from moviepy.editor import *
import pygame
from Pokemon_class import pokemon_funtions as p
import numpy as np

pygame.init()
WIDTH, HEIGHT = 1920, 1080
win = pygame.display.set_mode((WIDTH,HEIGHT))                # Display Size
pygame.display.set_caption("Pokemon Type Simulator")         # Name in display

# Images
TypeImage = pygame.transform.scale(pygame.image.load("PokemonTypes.png"), (901, 540))

# Fonts
FONT = pygame.font.SysFont('comicsans', 30)
LARGE_FONT = pygame.font.SysFont('comicsans', 70)
POKEMON_FONT = pygame.font.Font("pokemon.ttf", 50)
GAP = 50

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)

# Draw Window Function
def draw(selected_option="None", input_prompt="", input_prompt_2 = "", image_display = True, enter_press = False, type_vector =[]):
    # Background
    win.fill(WHITE)

    # Image Display
    if image_display == True:
         win.blit(TypeImage, (round(WIDTH/2 - 901/2), 400))

    # Title Display
    title = POKEMON_FONT.render("Pokemon Type Simulator", 1, BLACK)
    win.blit(title, (WIDTH/2 - title.get_width()/2 , 5))

    # Controls Display
    controls = FONT.render("R - Reset | Enter - Confirm Types | A - Attack Stats | D - Defend Stats | T - Type Score | F - Fun", 1, BLACK)
    win.blit(controls, (WIDTH/2 - controls.get_width()/2 , 80))

    # Selected Option Display
    status = FONT.render(f"Option: {selected_option}", 1, BLACK)
    win.blit(status, (WIDTH/2 - status.get_width()/2 , 140))

    # Input message display
    if input_prompt != "":
        input_message = FONT.render(f"{input_prompt}", 1, BLACK)
        win.blit(input_message,  (WIDTH/2 - input_message.get_width()/2 , 200))
    if input_prompt_2 != "":
        input_message_2 = FONT.render(f"{input_prompt_2}", 1, BLACK)
        win.blit(input_message_2, (WIDTH/2 - input_message_2.get_width()/2 , 240))

    # Stats Display
    if enter_press == True:
        if selected_option == "Defend Stats":
            defend_display(type_vector)
        if selected_option == "Type Score":
            type_score_message = LARGE_FONT.render("Type Score = " + str(type_vector), 1, BLACK)
            win.blit(type_score_message, (WIDTH/2 - type_score_message.get_width()/2, 280))
        if selected_option == "Attack Stats":
            attack_display(type_vector)

    pygame.display.update()

# Determines the effectiveness of types to defending type/s
def defend_stats(Types):
    defend = np.ones(18)
    for i in range(0,18):
        for type in Types:
            defend[i] = defend[i]*p.AttackDefend(i, type)
    return defend

# Displaying the defensive stats
def defend_display(defend):
    win.blit(FONT.render("Defensive Stats:", 1, BLACK), (20, 330))

    text_height = 400
    def effectiveness_display(number, text_height):
        type_text = ""
        if number not in defend and number > 2**-2 and number < 4:
            type_text = "None  "
        else:
            for i in range(0,18):
                if defend[i] == number:
                    type_text = type_text + p.Number_to_Type(i) + ", "
        if type_text != "":
            win.blit(FONT.render(type_text[:len(type_text) - 2], 1, BLACK), (300, text_height))
            text_height += GAP
        return text_height

    if 0 in defend:
        win.blit(FONT.render("Immune to:", 1, BLACK), (100, text_height))
        text_height = effectiveness_display(0,  text_height)

    for i in range (-7,6):
        if i < 0 and 2**i in defend:
            win.blit(FONT.render(str(-i) + "x Resists:", 1, BLACK) , (100, text_height))
            text_height = effectiveness_display(2**i, text_height)
        elif i == 0 and 2**i in defend:
            win.blit(FONT.render("Neutral to:", 1, BLACK) , (100, text_height))
            text_height = effectiveness_display(1, text_height)
        elif i > 0 and 2**i in defend:
            win.blit(FONT.render(str(i) + "x Weak to:", 1, BLACK) , (100, text_height))
            text_height = effectiveness_display(2**i, text_height)


def attack_stats(type):
    attack = np.ones(18)
    for i in range(0,18):
        attack[i] = p.AttackDefend(type, i)
    return attack



def attack_display(attack_type):
    win.blit(FONT.render("Offensive Stats:", 1, BLACK), (20, 330))

    win.blit(FONT.render("Super Effective:", 1, BLACK), (100, 400))
    win.blit(FONT.render("Neutral Effect:", 1, BLACK), (100, 450))
    win.blit(FONT.render("Not very Effective:", 1, BLACK), (100, 500))
    win.blit(FONT.render("No Effect:", 1, BLACK), (100, 550))

    attack = attack_stats(attack_type)
    text_height = 400

    def attack_text(number, text_height):
        text = ""
        if number not in attack:
            text = "None  "
        else:
            for i in range(0,18):
                if attack[i] == number:
                    text = text + p.Number_to_Type(i) + ", "
        win.blit(FONT.render(text[:len(text) - 2], 1, BLACK), (400, text_height))
        text_height += GAP
        return text_height
    
    text_height = attack_text(2, text_height)
    text_height =  attack_text(1, text_height)
    text_height = attack_text(0.5, text_height)
    text_height = attack_text(0, text_height)


def type_select(m_x, m_y, Types):
    
    # Ensures if mouse click is over one of the types and obtains the type number
    for i in range(0,18):
        if 510 + (i % 6)*150 < m_x < 510 + ((i % 6)+1)*150 and 400 + (i // 6)*180 < m_y < 400 + ((i // 6)+1)*180 and i not in Types:
            Types.append(i)

    # Changing the input message to display type with number to type function from class
    input_types_1 = ""
    input_types_2 = ""
    for i in range(0,len(Types)):
        if len(Types) < 9:
            input_types_1 = input_types_1 + p.Number_to_Type(Types[i]) + "  "
        else:
            input_types_2 = input_types_2 + p.Number_to_Type(Types[i]) + "  "
        input_prompt_1 = "Selected Type/s: " + input_types_1
        input_prompt_2 = input_types_2

    if len(Types) == 0:
        input_prompt_1 = "Selected Type/s: "
        input_prompt_2 = ""
    return input_prompt_1, input_prompt_2, Types

def main():
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    selected_option = "None"
    input_prompt, input_prompt_2 = "", ""
    image_display = True
    type_counter = 0
    enter_press = False
    type_vector = []
    Types = []
    
    # While loop to continuously run program
    while run:
        clock.tick(FPS)
        
        draw(selected_option, input_prompt, input_prompt_2, image_display, enter_press, type_vector)   
        # Checking for events
        for event in pygame.event.get():
            # Quitting game
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_option == "Defend Stats" or selected_option == "Type Score":
                    if type_counter < 18 and enter_press == False:
                        m_x, m_y = pygame.mouse.get_pos()
                        input_prompt, input_prompt_2, Types = type_select(m_x, m_y, Types)
                        type_counter += 1
                elif selected_option == "Attack Stats" and type_counter == 0:
                    m_x, m_y = pygame.mouse.get_pos()
                    input_prompt, input_prompt_2, Types = type_select(m_x, m_y, Types)
                    type_counter = 1


            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                selected_option = "None"
                Types = []
                input_prompt, input_prompt_2 = "", ""
                image_display = True
                type_counter = 0
                enter_press = False
                type_vector = []
                continue
        
            elif event.key == pygame.K_BACKSPACE and len(Types) > 0:
                Types.pop()
                input_prompt, input_prompt_2, Types = type_select(0, 0, Types)

            elif event.key == pygame.K_d and enter_press == False:
                selected_option = "Defend Stats"
                input_prompt = "Please your types: "
                type_counter = 0

            elif event.key == pygame.K_t and enter_press == False:
                selected_option = "Type Score"
                input_prompt = "Please your types: "
                type_counter = 0

            elif event.key == pygame.K_a and enter_press == False:
                selected_option = "Attack Stats"
                input_prompt = "Please select a type: "
                type_counter = 0

            elif event.key == pygame.K_RETURN:
                if selected_option == "None" or type_counter == 0:
                    continue

                if selected_option == "Defend Stats":
                    image_display = False
                    enter_press = True
                    defend = defend_stats(Types)
                    type_vector = defend
                elif selected_option == "Type Score":
                    enter_press = True
                    defend = defend_stats(Types)
                    type_score = sum(defend)
                    type_vector = type_score
                elif selected_option == "Attack Stats":
                    enter_press = True
                    image_display = False
                    type_vector = Types[0]

            elif event.key == pygame.K_f:
                clip = VideoFileClip('pokemon_clip.mp4')
                clip.resize((WIDTH,HEIGHT))
                clip.preview()
                win = pygame.display.set_mode((WIDTH,HEIGHT))


    pygame.quit()

if __name__ == "__main__":
	main()