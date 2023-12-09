import pygame
from button import Button
from pygame import mixer
import pygame_gui
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 15)
title = pygame.font.Font('freesansbold.ttf', 40)
screen = pygame.display.set_mode([800,600], pygame.RESIZABLE)
timer = pygame.time.Clock()
death_counter = 4

pygame.display.set_caption("THE DEATH GAME")
mixer.music.load('bg_music.wav')
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)



scene_count = -1




def fade(width, height, func, function):
    global scene_count
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        enter(func)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
    if function==game_main:
        scene_count+=1
        function(scene_count)
    elif function==end1:
        scene_count=-2
        function(scene_count)
    elif function==end2:
        scene_count=-2
        function(scene_count)
    else:
        function()





def script(txt, run_function):
    global scene_count
    global death_counter
    print(scene_count)
    if scene_count==-2:
        scene_count=-1
    elif scene_count==100:
        scene_count=100
    elif scene_count==-4:
        death_counter=0
        scene_count=100
    elif scene_count==5:
        scene_count+=3
    elif scene_count==10:
        scene_count+=1
    elif scene_count==11:
        scene_count+=1       
    elif scene_count==0:
        scene_count+=1
    elif scene_count%3==0:
        scene_count+=1
    elif (scene_count+1)%3==0:
        scene_count+=2
    snip = font.render('', True, 'white')
    counter = 0
    speed = 3
    actives = 0
    message = txt[actives]
    done = False


    run = True
    while run:
        screen.fill('black')
        timer.tick(60)

        if counter < speed*len(message):
            counter += 1
        elif counter >= speed*len(message):
            done = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and actives< len(txt)-1:
                    actives += 1
                    done = False
                    message = txt[actives]
                    counter = 0

        snip = font.render(message[0:counter//speed], True, 'white')
        text_rect = snip.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(snip, text_rect)

        pygame.display.flip()
        if actives >= len(txt)-1 and actives<100:
            actives+=1
        elif actives == 100:
            run_function(scene_count)
        
        pygame.display.update()
    pygame.quit()







def options(opt1, opt2, scene_no):
    pygame.init()
    global scene_count
    print(scene_count)
    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()


        opt_btn1 = Button(image=pygame.image.load("black.jfif"), pos=(screen.get_width()/3, screen.get_height()/3), 
                          text_input=opt1, font=font, base_color="white", hovering_color="brown")
        opt_btn2 = Button(image=pygame.image.load("black.jfif"), pos=(screen.get_width()/1.5, screen.get_height()/3), 
                          text_input=opt2, font=font, base_color="white", hovering_color="brown")



        for button in [opt_btn1, opt_btn2]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if opt_btn1.checkForInput(mouse_pos):
                        if scene_no==100:
                            fade(screen.get_width(), screen.get_height(), "YOU REPEAT HISTORY", end1)
                        elif scene_no==10:
                            fade(screen.get_width(), screen.get_height(), "WELCOME TO THE DEATH GAME", character)
                        elif scene_no==1:
                            scene_no+=1
                            scene_count+=1
                            game_main(scene_no)
                        elif (scene_no+1)%2==0:
                            scene_no+=2
                            scene_count+=2
                            game_main(scene_no)
                        elif (scene_no)%2==0:
                            scene_no+=1
                            scene_count+=1
                            game_main(scene_no)
                   
                if opt_btn2.checkForInput(mouse_pos):
                        if scene_no==100:
                             fade(screen.get_width(), screen.get_height(), "YOU REWRITE HISTORY", end2)
                        elif scene_no==10:
                            scene_count=6
                            game_main(scene_count)
                        elif scene_no==1:
                            scene_no+=2
                            scene_count+=2
                            game_main(scene_no)
                        elif (scene_no+1)%2==0:
                            scene_no+=1
                            scene_count+=1
                            game_main(scene_no)
                        elif (scene_no)%2==0:
                            scene_no+=2
                            scene_count+=2
                            game_main(scene_no)
                    
        
        pygame.display.update()
    pygame.quit()







def easter_egg(scene_count):
    pygame.init()
    scene=[]

    if scene_count==-4:
        scene = ["Congratulations!!!",
                 "You figured out the hint and have died the max number of times possible",
                 "You will now be resurrected and all powerful....the DEATH GOD",
                 "*you read a note*",
                 "*You pick up the phone and call someone*",
                 "The note asked you to do something",
                 "Call someone called the game master",
                "Do you want to do it?"]
    
    if scene_count==100:
        options("yes", "no", scene_count)

    script(scene, easter_egg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()






def end1(scene_count):
    pygame.init()
    scene=[]

    if scene_count==-2:
        scene = ["*RRRRRRRRRRRRiiiiiiinnnnnnnnnnnnnnnnnnngggggggggggg*",
                 "Hello gamemaster",
               "*Hello sir*",
               "Is my old body there?",
               "*He is here*",
               "Take him to the dungeon right now and make sure he meets them",
               "*I understand*",
               "Make sure he dies four times",
               "*Yes.....*",
               "*Boys!!*",
               "*Drag him awayyy*"]
    
    if scene_count==-1:
        fade(screen.get_width(), screen.get_height(), "THE END", menu)

    script(scene,end1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



def end2(scene_count):
    pygame.init()
    scene = []

    if scene_count==-2:
        scene = ["Congratulations! You have rewritten history...",
                 "Meaning that you never came to the death game in the first place...",
                 "Meaning that you don't have powers anymore",
                 "*blackout*",
                 "WELCOME TO TRUE DEATH",
                 "THE END"]
    
    if scene_count==-1:
        fade(screen.get_width(), screen.get_height(), "THE END", menu)

    script(scene, end2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()








def death_game(scene_count):
    global death_counter
    pygame.init()
    weapons = ["Axe", "Shield", "Sword", "Bat", "Armor", "Bow", "Arrow", "Pan", "Machin-Gun"]
    stat_name = ["Attack", "Defence", "Speed"]
    weapon_stat = [[4,2,2],[1,5,2],[3,3,3],[2,1,4],[0,5,2],[2,1,4],[2,1,5],[3,2,3],[5,0,0]]
    places = ["Mandrake Fields", "Haunted Forest", "Dracula's Castle", "Moonlit Lake", "Desolate City"]

    global display_text
    print(scene_count)

    name_text = font.render("Inventory", True, 'white')
    name_rect = name_text.get_rect(center=(screen.get_width()-50, screen.get_height()-10))
    screen.blit(name_text, name_rect)

    
    scene=[]

    if scene_count==10:
        scene = [f"Welcome to the DEATH GAME {display_text}. We know you have been eager to come out and we are glad you did",
                 "Otherwise you'd be dead by now!!",
                 "*Crowd roars*",
                 "Anyways we want to give you a set of options on where you can go. Only because we are kind",
                 "Choose wisely...",
                 "Your inventory, health and money are displayed at the bottom of the screen",
                 "TO THE DEATH GAMESSS!!!"]
        
    
    if scene_count==11:
        scene = ["Your options are:",
                 "wait for it......",
                 "wait for it...........",
                 "......",
                 "....",
                 "...",
                 "..",
                 "..........................",
                 "Getting real impatient huh?",
                 "Here you go. Your options are:",]
        
    if scene_count==12:
        scene = ["DEATH",
                 "DEATH",
                 "DEATH",
                 "DEATH",
                 "DEATH",
                 "DEATH",
                 "DEATH",
                 "DEATH",
                 "DEATH",
                 "DEATH",
                 "NAH. THERES NO OTHER CHOICE THIS IS REAL HAHAHAHAH",
                 "WHY DO YOU THINK THIS IS CALLED THE DEATH GAME HUH HAHAHAHHAHAHA",
                 "TRY WHATEVER YOU WANT YOU CAN NEVER LIVE",
                 "SEE YA LOSERRRRRR",
                 "CROWD ROARS",
                 "YOU DIED!!"]

    if scene_count==13:
        death_counter+=1
        fade(screen.get_width(), screen.get_height(), "the more dead you are the more you are alive....", menu)
        
    

    script(scene, death_game)
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()






def textentry(name_to_show):
    while True:
        
        screen.fill('black')

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        
        global display_text
        display_text = name_to_show
        death_game(scene_count)
        pygame.display.update()






def character():
    pygame.init()
    manager = pygame_gui.UIManager((screen.get_width(), screen.get_height()))
    text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((screen.get_width()/2)-(screen.get_width()/8), ((screen.get_height()/2)-25)), (screen.get_width()/4, 50)), manager=manager, object_id="#main_text_entry")

    

    while True:
        
        UI_REFRESH_RATE = timer.tick(60)/1000
        screen.fill('black')

        pname=""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                textentry(event.text)
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(screen)

        


        

    
        name_text = font.render("What is your name challenger", True, 'white')
        name_rect = name_text.get_rect(center=(screen.get_width()/2, 200))
        screen.blit(name_text, name_rect)
    
        
        print(pname)

        
        pygame.display.update()
    











def game_main(scene_count):
    pygame.init()
    global death_counter
    scene=[]

    if scene_count==0:
        scene = ["*cough*",
               "*wheeze*",
               "Young man are you awake? *shakes*",
               "Do you respond?"]
        
    if scene_count==1:
        options("yes", "no", scene_count)
        
    if scene_count==2:
        scene = ["Good you seem to be able to move",
                 "This place is called the DEATH GAMES. People from all over the world take part to earn riches and glory",
                 "However ever so often some people get kidnaped and sold to this place for fun",
                 "Some people are really insane",
                 "Either way, I have some weapons here that I collected....",
                 "I am old now and can't fight anymore feel free to take any that you want.",
                 "Take these and go....",
                 "You have acquired a pan that has attack: 3, defence: 2 and speed: 3",
                 "Do you take this?"]
    
    if scene_count==3:
        scene = ["Young man?",
                 "Young people these days.......",
                 "They have no sense of urgency... and he is about to die",
                 "*rrrrinnnggggg*",
                 "Hello?",
                 "Yes boss. I tried but he is still sound asleep",
                 "I would say it is easier to poison him but whatever gets the crowd going I guess",
                 "Alright I'll leave the note here",
                 "*click*",
                 "Good thing the boss likes you. I would rather kill you right here",
                 "*scribbles*",
                 "*leaves the room*",
                 "Do you want to check the note?"]
    
    if scene_count==4:
        options("yes", "no", scene_count)

    if scene_count==5:
        scene = ["GUYSSS",
                 "I have you now!! Guys he's awake",
                 "*sob*",
                 "He is actually awake. Our savior!!"]
    
    if scene_count==6:
        scene = ["Our Savior is stupid",
                 "I think they messed with him before sending him here to show us despair",
                 "To think we had hope in this guy",
                 "*A huge mob rushes in and kills you in despair*",
                 "YOU GET MANGLED AND BEAT TO DEATH",
                 "SEE YOU IN THE AFTERLIFE",
                 "YOU DIED"]
    
    if scene_count==7:
        scene_count=-1
        death_counter+=1
        fade(screen.get_width(), screen.get_height(), "the more dead you are the more you are alive....", menu)
        menu()

    if scene_count==8:
        fade(screen.get_width(), screen.get_height(), "He is actually awake. Our savior!!", game_main)

    if scene_count==9:
        scene = ["*CROWD CHEERS!!!",
                 "And again welcome back to the.....",
                 "THE DEATHHH GAMESSSSSS!!!!",
                 "Hey folks once again today we have a special surprise for you",
                 "A NEW CONTENDERRRR!!!",
                 "CROWD CHEERS!",
                 "Do you go out to face the crowd?"]
    
    if scene_count==10:
        options("yes", "no", scene_count)

    
    script(scene, game_main)

    





def play():
    


    pygame.init()
    welcome = ["RRRRRRRRRRRRiiiiiiinnnnnnnnnnnnnnnnnnngggggggggggg",
           "Hello sir",
           "He is here",
           "I understand",
           "Yes.....",
           "Boys!!",
           "DRAG HIM AWAY"]

    snip = font.render('', True, 'white')
    counter = 0
    speed = 3
    active = 0
    messages = welcome[active]
    done = False
    global scene_count
    scene_count=-1

    run = True
    while run:
        screen.fill('black')
        timer.tick(60)

        if counter < speed*len(messages):
            counter += 1
        elif counter >= speed*len(messages):
            done = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active< len(welcome)-1:
                    active += 1
                    done = False
                    messages = welcome[active]
                    counter = 0

        snip = font.render(messages[0:counter//speed], True, 'white')
        text_rect = snip.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(snip, text_rect)

        pygame.display.flip()
        
        if active >= 6 and active<100:
            active+=1
        elif active == 100:
            fade(screen.get_width(), screen.get_height(), "DRAG HIM AWAY", game_main)
        
        pygame.display.update()
    pygame.quit()






def menu():
    pygame.init()
    global scene_count
    scene_count=-1
    run = True
    while run:
        screen.fill('black')

        mouse_pos = pygame.mouse.get_pos()

        menu_text = title.render("MAIN MENU", True, 'white')
        menu_rect = menu_text.get_rect(center=(screen.get_width()/2, 200))

        play_btn = Button(image=pygame.image.load("black.jfif"), pos=(screen.get_width()/2, 300), 
                          text_input="PLAY", font=font, base_color="white", hovering_color="brown")
        options_btn = Button(image=pygame.image.load("black.jfif"), pos=(screen.get_width()/2, 400), 
                          text_input="OPTIONS", font=font, base_color="white", hovering_color="brown")
        quit_btn = Button(image=pygame.image.load("black.jfif"), pos=(screen.get_width()/2, 500), 
                          text_input="QUIT", font=font, base_color="red", hovering_color="darkred")

        screen.blit(menu_text, menu_rect)

        for button in [play_btn, options_btn, quit_btn]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_btn.checkForInput(mouse_pos):
                    run=False
                if play_btn.checkForInput(mouse_pos):
                    if death_counter==4:
                        scene_count=-4
                        easter_egg(scene_count)
                    else:
                        play()
        
        pygame.display.update()
    pygame.quit()







def enter(text):
    screen.fill('black')
    enter_text = font.render(text, True, 'white')
    enter_rect = enter_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(enter_text, enter_rect)

#welcome
welcome = ["Hey Adventurer seems like you have decided to risk your life.............",
           "ohhh....",
           "You were.....",
           "ok....",
           "Welcome to the only way to save your life.....",
           "THE DEATH GAMES"]

snip = font.render('', True, 'white')
counter = 0
speed = 3
active = 0
messages = welcome[active]
done = False

run = True
while run:
    screen.fill('black')
    timer.tick(60)
    
    if counter < speed*len(messages):
        counter += 1
    elif counter >= speed*len(messages):
        done = True

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active< len(welcome)-1:
                active += 1
                done = False
                messages = welcome[active]
                counter = 0

    snip = font.render(messages[0:counter//speed], True, 'white')
    text_rect = snip.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(snip, text_rect)

    pygame.display.flip()
    if active >= 5 and active<100:
        active+=1
    elif active == 100:
        fade(screen.get_width(), screen.get_height(), "THE DEATH GAMES", menu)
    
pygame.quit()

