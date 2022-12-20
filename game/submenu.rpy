# Script for submenus in-game
define name = ""

### Input constraints ###
define alphabet = "A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z"
define numbers = "0 1 2 3 4 5 6 7 8 9"

## Classes ###################
init python:
    ### Sound manager ###
    class Sound_mng:
        def __init__(self):
            self.click = "<from 0.345>audio/menus/Click_button.wav"
            self.inv_click = "<from 0.4>audio/menus/Inventory_click.wav"
            self.correct_jingle = "audio/menus/Correct_jingle.wav"
            self.incorrect_jingle = "audio/menus/Incorrect_jingle.wav"
            self.waterfall_bg = "<loop 0.3 to 30.3>audio/locations/Waterfall.wav"
            self.thicket_bg = "<loop 1.0 to 16.9>audio/locations/Thicket_Background.wav"
            self.source_bg = "<loop 0.35 to 16.2>audio/locations/Watersource_Background.wav"
            self.core_bg = "<loop 0.0 to 18.2>audio/locations/Core_background.wav"
            self.enter_thicket = "<loop 1.0 to 18.0>audio/locations/Entering_Thicket.wav"
            self.enter_source = "<loop 7.0 to 9.4>audio/locations/Entering_Watersource.wav"

        def open_inv(self):
            renpy.sound.play(self.inv_click)

        def play_click(self):
            renpy.sound.play(self.click)

        def play_jingle(self, type):
            if type == "c":
                renpy.sound.play(self.correct_jingle)
            else:
                renpy.sound.play(self.incorrect_jingle)

        def play_bg(self, location):
            if location.capitalize() == "Waterfall":
                renpy.music.play(self.waterfall_bg)
            elif location.capitalize() == "Thicket":
                renpy.music.play(self.thicket_bg, fadein=1.0)
            elif location.capitalize() == "Core":
                renpy.music.play(self.core_bg, fadein=3.0)
            else:
                renpy.music.play(self.source_bg, fadein=2.0)

        def play_entering_thicket(self):
            renpy.music.play(self.enter_thicket, fadein=1.0)

        def play_entering_source(self):
            renpy.music.play(self.enter_source, fadein=2.0)

    ### Character manager ###
    class Personnel:
        ## Variables ####################
        def __init__(self, name):
            self.player_name = name
            self.player_location = "Unknown"
            self.chapter_num = 1

            self.scientist_name = "Avery"
            self.robot_name = "MUS-L"
            self.scientist_location = "Unknown"
            self.robot_location = "Unknown"
            self.scientist_health = "Fine"
            self.robot_health = "Fine"

        # Updates location for side character
        def update_location(self, who, location):
            if who == "scientist":
                self.scientist_location = location
            elif who == "robot":
                self.robot_location = location

        # Updates health variable for side character
        def update_health(self, who, status):
            if who == "scientist":
                self.scientist_health = status
            elif who == "robot":
                self.robot_health = status

        # Gets color code for side character health
        def get_health_color(self, who):
            if who == "scientist":
                if self.scientist_health == "Fine":
                    return "#89e89a"
                elif self.scientist_health == "Injured":
                    return "#e67765"
                else:
                    return "#b5b5b5"

            if who == "robot":
                if self.robot_health == "Fine":
                    return "#89e89a"
                elif self.robot_health == "Injured":
                    return "#e67765"
                else:
                    return "#b5b5b5"

    ### Inventory ###
    class Inventory:
        ## Variables ####################
        def __init__(self):
            # Inventory management
            self.held_item = None
            self.item_list = ["activation code", "old key", "MUS-L's hand"]

            self.datapad_interactable = True
            self.datapad_unlocked = False
            self.datapad_opened = False

        ## Functions ####################
        # Allows the player to use the datapad
        def set_interactable(self):
            self.datapad_interactable = True

        # Prevents the player from using the datapad, 
        # such as during scripted scenes
        def set_uninteractable(self):
            self.datapad_interactable = False

        # Equips item
        def pickup_item(self, new_item):
            if self.held_item == None:
                self.held_item = new_item
            else:
                return

        # Unequips item
        def remove_item(self, remove_item):
            self.held_item = None

        # Returns item description
        def get_item_desc(self):
            if self.held_item == "test_item":
                return "This item is for testing."
            if self.held_item == "activation code":
                return "This is the passcode to your datapad. Probably best to keep it somewhere safe..."

            if self.held_item == "Avery's arm":
                return "Avery's robotic replacement arm, now fully assembled. Better get this to her quick!"

            if self.held_item == "MUS-L's hand":
                return "One of MUS-L's many hand attachments. Its installation is thankfully simple."

            else:
                return "No item description found."

    ### Puzzles ###
    class Puzzle_manager:
        def __init__(self):
            self.puz_tag = None

            # Tutorial puzzle
            self.pin_pos1 = 0
            self.pin_pos2 = 0
            self.pin_pos3 = 0
            self.pin_pos4 = 0

            #Thicket puzzle
            self.thick_bar1 = 0
            self.thick_bar2 = 0
            self.thick_bar3 = 0

            #Water source puzzle
            # GRID POSITIONS

            # X POSITIONS
            self.x_increment = 0.098
            self.left = 0.406
            self.middle_x = 0.504
            self.right = 0.602

            # Y POSITONS
            self.y_increment = 0.187
            self.top = 0.213
            self.middle_y = 0.4
            self.bottom = 0.587
     
            # OBJECTS
            # _x and _y variables are for visuals
            # _pos_x and _pos_x are for positions within rock_map
            self.robo_x = self.left
            self.robo_y = self.bottom
            self.robo_pos_x = 0
            self.robo_pos_y = 2

            self.rock1_x = self.left
            self.rock1_y = self.middle_y
            self.rock1_pos_x = 0
            self.rock1_pos_y = 1

            self.rock2_x = self.right
            self.rock2_y = self.bottom
            self.rock2_pos_x = 2
            self.rock2_pos_y = 2

            self.rock3_x = self.middle_x
            self.rock3_y = self.middle_y
            self.rock3_pos_x = 1
            self.rock3_pos_y = 1

            self.rock_map = [[0, 0, 0], 
                        [0, 0, 0], 
                        [0, 0, 0]]

            # Arm puzzle
            self.got_arm_1 = False
            self.got_arm_2 = False
            self.got_arm_3 = False
            self.built_arm = False

            # Sound puzzle
            self.correct_code = "53421"
            self.code_entry = ""
            self.button_id = "0"

            # General puzzles
            self.num_fails = 0

        # Increases number of failures after failing to solve a puzzle
        def increase_fails(self):
            self.num_fails += 1

        # Reset number of failures after solving puzzle
        def reset_fails(self):
            self.num_fails = 0

        # Resets the puzzle tag once puzzle is complete
        def reset_tag(self):
            self.puz_tag = None

        # Adds progress to code_entry
        def sound_code_progress(self):
            if len(self.code_entry) < 5:
                self.code_entry += self.button_id
            else:
                self.code_entry = self.button_id

        # Resets sound code
        def sound_reset_code(self):
            self.code_entry = ""

        # Replays correct answer
        def sound_replay(self):
            renpy.sound.play("audio/ch3/sound_puzzle/Answer.wav")

        # Checks if arm is completed
        def check_arm_progress(self):
            if self.got_arm_1 == True and self.got_arm_2 == True and self.got_arm_3 == True:
                self.built_arm = True
                inv.held_item = "Avery's arm"

        # Reset rock and robot positions
        def reset_rock(self):
            self.robo_x = self.left
            self.robo_y = self.bottom
            self.robo_pos_x = 0
            self.robo_pos_y = 2

            self.rock1_x = self.left
            self.rock1_y = self.middle_y
            self.rock1_pos_x = 0
            self.rock1_pos_y = 1

            self.rock2_x = self.right
            self.rock2_y = self.bottom
            self.rock2_pos_x = 2
            self.rock2_pos_y = 2

            self.rock3_x = self.middle_x
            self.rock3_y = self.middle_y
            self.rock3_pos_x = 1
            self.rock3_pos_y = 1

            self.populate_map()

        # Gets rock x position
        def get_rock_x(self, rock_id):
            if rock_id == "rock1":
                return self.rock1_pos_x  
            if rock_id == "rock2":
                return self.rock2_pos_x
            if rock_id == "rock3":
                return self.rock3_pos_x

        # Gets rock y position
        def get_rock_y(self, rock_id):
            if rock_id == "rock1":
                return self.rock1_pos_y  
            if rock_id == "rock2":
                return self.rock2_pos_y
            if rock_id == "rock3":
                return self.rock3_pos_y

        # Places rocks and robot in rock_map
        def populate_map(self):
            for i in range(0, len(self.rock_map)):
                for j in range(0, len(self.rock_map)):
                    if i == self.robo_pos_y and j == self.robo_pos_x:
                        self.rock_map[i][j] = 2
                    elif i == self.rock1_pos_y and j == self.rock1_pos_x:
                        self.rock_map[i][j] = 1
                    elif i == self.rock2_pos_y and j == self.rock2_pos_x:
                        self.rock_map[i][j] = 1                    
                    elif i == self.rock3_pos_y and j == self.rock3_pos_x:
                        self.rock_map[i][j] = 1
                    else:
                        self.rock_map[i][j] = 0

        # Moves robot left
        def move_robo_left(self):
            check_pos_x = self.robo_pos_x - 1
            check_pos_y = self.robo_pos_y
            if check_pos_x >= 0:
                if self.rock_map[check_pos_y][check_pos_x] == 0:
                    self.robo_x -= self.x_increment
                    self.robo_pos_x -= 1
                    self.populate_map()
                else:
                    if(self.can_move_rock(self.get_rock_id(check_pos_x, check_pos_y), "left")):
                        self.robo_x -= self.x_increment
                        self.robo_pos_x -= 1
                        self.populate_map()
                    else:
                        return
            else:
                return
                
        # Moves robot right
        def move_robo_right(self):
            check_pos_x = self.robo_pos_x + 1
            check_pos_y = self.robo_pos_y
            if check_pos_x <= 2:
                if self.rock_map[check_pos_y][check_pos_x] == 0:
                    self.robo_x += self.x_increment
                    self.robo_pos_x += 1
                    self.populate_map()
                else:
                    if(self.can_move_rock(self.get_rock_id(check_pos_x, check_pos_y), "right")):
                        self.robo_x += self.x_increment
                        self.robo_pos_x += 1
                        self.populate_map()
                    else:
                        return
            else:
                return

        # Moves robot up
        def move_robo_up(self):
            check_pos_x = self.robo_pos_x
            check_pos_y = self.robo_pos_y - 1
            if check_pos_y >= 0:
                if self.rock_map[check_pos_y][check_pos_x] == 0:
                    self.robo_y -= self.y_increment
                    self.robo_pos_y -= 1
                    self.populate_map()
                else:
                    if(self.can_move_rock(self.get_rock_id(check_pos_x, check_pos_y),"up")):
                        self.robo_y -= self.y_increment
                        self.robo_pos_y -= 1
                        self.populate_map()
                    else:
                        return
            else:
                return

        # Moves robot down
        def move_robo_down(self):
            check_pos_x = self.robo_pos_x
            check_pos_y = self.robo_pos_y + 1
            if check_pos_y <= 2:
                if self.rock_map[check_pos_y][check_pos_x] == 0:
                    self.robo_y += self.y_increment
                    self.robo_pos_y += 1
                    self.populate_map()
                else:
                    if(self.can_move_rock(self.get_rock_id(check_pos_x, check_pos_y), "down")):
                        self.robo_y += self.y_increment
                        self.robo_pos_y += 1
                        self.populate_map()
                    else:
                        return
            else:
                return

        # Get rock at certain position
        def get_rock_id(self, check_pos_x, check_pos_y):
                if check_pos_y == self.rock1_pos_y and check_pos_x == self.rock1_pos_x:
                    return "rock1"
                elif check_pos_y == self.rock2_pos_y and check_pos_x == self.rock2_pos_x:
                    return "rock2"                   
                elif check_pos_y == self.rock3_pos_y and check_pos_x == self.rock3_pos_x:
                    return "rock3"

        # Move rock if movable
        def update_rock_pos(self, rock_id, x_y, increment):
            if x_y == "x":
                if rock_id == "rock1":
                    self.rock1_x += increment * self.x_increment
                    self.rock1_pos_x += increment
                if rock_id == "rock2":
                    self.rock2_x += increment * self.x_increment
                    self.rock2_pos_x += increment
                if rock_id == "rock3":
                    self.rock3_x += increment * self.x_increment
                    self.rock3_pos_x += increment

            if x_y == "y":
                if rock_id == "rock1":
                    self.rock1_y += increment * self.y_increment
                    self.rock1_pos_y += increment
                if rock_id == "rock2":
                    self.rock2_y += increment * self.y_increment
                    self.rock2_pos_y += increment
                if rock_id == "rock3":
                    self.rock3_y += increment * self.y_increment
                    self.rock3_pos_y += increment

        # Checks if rock can be moved
        def can_move_rock(self, rock_id, check_dir):
            check_pos_x = self.get_rock_x(rock_id)
            check_pos_y = self.get_rock_y(rock_id)
            if check_dir == "left":
                check_pos_x -= 1
                if check_pos_x >= 0:
                    if self.rock_map[check_pos_y][check_pos_x] == 0:
                        self.update_rock_pos(rock_id, "x", -1)
                        return True
                else:
                    return False
            elif check_dir == "right":
                check_pos_x += 1
                if check_pos_x <= 2:
                    if self.rock_map[check_pos_y][check_pos_x] == 0:
                        self.update_rock_pos(rock_id, "x", 1)
                        return True
                else:
                    return False
            elif check_dir == "up":
                check_pos_y -= 1
                if check_pos_y >= 0:
                    if self.rock_map[check_pos_y][check_pos_x] == 0:
                        self.update_rock_pos(rock_id, "y", -1)
                        return True
                else:
                    return False
            elif check_dir == "down":
                check_pos_y += 1
                if check_pos_y <= 2:
                    if self.rock_map[check_pos_y][check_pos_x] == 0:
                        self.update_rock_pos(rock_id, "y", 1)
                        return True
                else:
                    return False
            else:
                return False
            

## DEBUG ###################
screen debug:
    text "Debug" xpos 25 ypos 25
    #text "Pin: [pin_pos1] [pin_pos2] [pin_pos3] [pin_pos4]" xpos 25 ypos 75
    text "Thicket: [puz.thick_bar1] [puz.thick_bar2] [puz.thick_bar3]" xpos 25 ypos 100
    python: 
        booltest = False
        if puz.nearest_rock == "rock1" or puz.nearest_rock == "rock2" or puz.nearest_rock == "rock3":
            booltest = True

        rock = "rock" + "1"
        check_pos1 = puz.get_rock_x_dist(rock)
        check_pos2 = puz.get_rock_y_dist(rock)
    text "Water Source: [puz.arrow_dir], [puz.nearest_rock] [booltest]" xpos 25 ypos 150
    text "ROBOT: [puz.robo_x] , [puz.robo_y]" xpos 25 ypos 200
    text "ROCK1: [puz.rock1_x] , [puz.rock1_y]" xpos 25 ypos 250
    text "[rock] [check_pos1] [check_pos2]" xpos 25 ypos 300

## Styles ###################
# Used for datapad device's headers
style datapad_text:
    size 50
    font "consola.ttf"
    color "#ffffff"

# Used for datapad device's body text
style datapad_body_text:
    size 35
    font "consola.ttf"
    color "#ffffff"

## Screens ###################
### Datapad tool ###
# This version of the datapad device is used for every instance after the tutorial
screen datapad:
    add "menus/datapad_back.png" xalign 0.5 yalign 0.5

    # Setting variables for display
    python:
        scientist_health_color = per.get_health_color("scientist")
        robot_health_color = per.get_health_color("robot")

    if inv.datapad_interactable:
        modal True

    # closes screen
    if per.chapter_num != 1:
        imagebutton:
            focus_mask True
            idle "menus/datapad_back_close.png"
            if per.chapter_num == 2 and per.player_location == "Water Source":
                action Function(snd.open_inv), SetVariable("inv.datapad_opened", False), Show("water_source2"), Hide("datapad")
            else:
                action Function(snd.open_inv), SetVariable("inv.datapad_opened", False), Hide("datapad")

    # displays item, if one is equipped
    if inv.held_item != None:
        $ held_item = inv.held_item.capitalize()
        add "items/[inv.held_item].png" xalign 0.377 yalign 0.155

    if puz.built_arm == False and puz.got_arm_3 == True:
        add "puzzles/arm_3.png" xalign 0.377 yalign 0.155
        $ puz.check_arm_progress()

    if puz.built_arm == False and puz.got_arm_2 == True:
        add "puzzles/arm_2.png" xalign 0.377 yalign 0.155
        $ puz.check_arm_progress()

    if puz.built_arm == False and puz.got_arm_1 == True:
        add "puzzles/arm_1.png" xalign 0.377 yalign 0.155
        $ puz.check_arm_progress()

    # vbox for main screen
    vbox:
        xalign 0.5 yalign 0.4
        spacing 25
        # hbox for item info
        hbox:
            spacing 5
            if inv.datapad_interactable and inv.held_item != None:
                imagebutton:
                    idle "menus/item_frame.png" xalign 0.4 yalign 0.3
                    hover "menus/item_frame_highlight.png"
                    action Function(snd.play_click), Hide("datapad"), Show("item_desc")
            else:
                add "menus/item_frame.png" xalign 0.4 yalign 0.3
            vbox:
                text "{=datapad_text}> Current item:"
                text "{=datapad_body_text}[inv.held_item]" xalign 0.5

        # vbox for player location info
        vbox:
            xalign 0.0 yalign 0.45
            text "{=datapad_text}> Current location:" ypos 15
            text "{=datapad_body_text}[per.player_location]" ypos 15
            
        # vbox for side character info
        text "{=datapad_text}> Team status:" ypos 30
        hbox:
            ypos 10
            spacing 10
            vbox:
                spacing 65
                add "scientist_portrait" yalign 0.0
                add "robot_portrait" yalign 0.0
            vbox:
                spacing 10
                xalign 0.0 yalign 0.45
                text "{=datapad_text}{u}[per.scientist_name]"
                text "{=datapad_body_text}Location: [per.scientist_location]"
                text "{=datapad_body_text}Status:{color=[scientist_health_color]} [per.scientist_health]"
                text "{=datapad_text}{u}[per.robot_name]" ypos 10
                text "{=datapad_body_text}Location: [per.robot_location]" ypos 10
                text "{=datapad_body_text}Status:{color=[robot_health_color]} [per.robot_health]" ypos 10

    # closes datapad
    if per.chapter_num != 1:
        fixed:
            xpos 1075 ypos 850
            imagebutton:
                idle "close_button"
                hover "close_button_hover"
                if per.chapter_num == 2 and per.player_location == "Water Source":
                    action Function(snd.open_inv), SetVariable("inv.datapad_opened", False), Show("water_source2"), Hide("datapad")
                else:
                    action Function(snd.open_inv), SetVariable("inv.datapad_opened", False), Hide("datapad")
         
            text "{=datapad_text}CLOSE" xalign 0.017 yalign 0.027

# Screen for viewing item and to confirm item use
screen item_desc:
    modal True
    add "menus/datapad_back.png" xalign 0.5 yalign 0.5
    $ held_item = inv.held_item.capitalize()

    # closes screen
    if per.chapter_num != 1:
        imagebutton:
            focus_mask True
            idle "menus/datapad_back_close.png"
            action SetVariable("inv.datapad_opened", False), Hide("item_desc")

    # vbox for item info
    add "items/[inv.held_item].png" xalign 0.5 yalign 0.165
    vbox:
        xalign 0.5 yalign 0.35
        spacing 35
        vbox:
            spacing 30
            imagebutton:
                idle "menus/item_frame.png" xalign 0.5 yalign 0.3
                action Function(snd.play_click), Hide("datapad"), Show("item_desc")
            vbox:
                xmaximum 650
                spacing 30
                text "{=datapad_text}{u}[held_item]" xalign 0.5
                $ held_item_desc = inv.get_item_desc()
                text "{=datapad_body_text}[held_item_desc]" xalign 0.5

                text "{=datapad_text}Use this item?" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 50
                    imagebutton:
                        idle "close_button" xalign 0.25
                        hover "close_button_hover" 
                        action Function(snd.open_inv), Jump("use_item")

                    imagebutton:
                        if per.chapter_num != 1:
                            idle "close_button" xalign 0.25
                            hover "close_button_hover" 
                            action Function(snd.play_click), Hide("item_desc"), Show("datapad")
                        else:
                            idle "close_button_hover" xalign 0.25
                            hover "close_button_hover"

    fixed:                      
        xpos 790 ypos 725
        text "{=datapad_text}YES" xalign 0.0
        text "{=datapad_text}NO" xalign 0.145

    # returns to datapad main screen
    if per.chapter_num != 1:
        fixed:
            xpos 1075 ypos 850
            imagebutton:
                idle "close_button"
                hover "close_button_hover"
                action Function(snd.open_inv), Hide("item_desc"), Show("datapad")
         
            text "{=datapad_text}BACK" xalign 0.025 yalign 0.027

# Uses equipped item
label use_item:
    $ inv.datapad_opened = False
    hide screen item_desc with dissolve

    if inv.held_item == "activation code":
        y2 "It's probably not a good idea to just have this lying around somewhere..."
        "You stuff the crumpled up note into your pocket."
        $ inv.held_item = None
        jump chap_1_end

    elif inv.held_item == "MUS-L's hand":
        hide screen water_source2 with dissolve
        show robot happy with dissolve
        
        play sound "audio/musl/MUSL_arm.wav"
        "You remove MUS-L's drill attachments and slip his hands into the sockets."

        r "Thank you, Captain."
        $ inv.held_item = None
        jump water_source_puzzle

    elif inv.held_item == "Avery's arm":
        python:
            inv.held_item = None
            puz.got_arm_1 = False
            puz.got_arm_2 = False
            puz.got_arm_3 == False
        jump arm_success


screen open_datapad:
    imagebutton:
        idle "menus/expand.png"
        hover "menus/expand_highlight.png"
        action Hide("open_datapad"), Show("datapad")


# The tutorial version of the datapad device, only used in Chapter 1
screen datapad_tutorial:
    modal True
    
    if inv.datapad_unlocked:
        add "menus/datapad_back.png" xalign 0.5 yalign 0.5
        vbox:
            xalign 0.5 yalign 0.29
            spacing 15
            text "{=datapad_text}To complete" xalign 0.5
            text "{=datapad_text}recalibration," xalign 0.5
            text "{=datapad_text}Please enter your" xalign 0.5
            text "{=datapad_text}name below." xalign 0.5

        hbox:
            xalign 0.5 yalign 0.57
            input default "":
                style "datapad_text"
                allow alphabet
                length 10 
                xalign 0.5 
                yalign 0.6
                value VariableInputValue("name")

            text " "

        fixed:
            xpos 780 ypos 750

            imagebutton:
                idle "menus/confirm_button.png"
                hover "menus/confirm_button_hover.png"
                action Function(snd.play_click), Hide("datapad_tutorial"), Jump("name_entered")

            text "{=datapad_text}CONFIRM" xalign 0.045 yalign 0.035

    else:
        add "menus/datapad_back_tutorial.png" xalign 0.5 yalign 0.5
        text "{=datapad_text}Welcome!" xalign 0.5 yalign 0.15
        vbox:
            xalign 0.5 yalign 0.29
            spacing 15

            text "{=datapad_body_text}This device is registered to" xalign 0.5
            text "{=datapad_body_text}AstroCorp terraforming captain" xalign 0.5
            text "{=datapad_body_text}ID #1015814117" xalign 0.5
            text "{=datapad_body_text}Due to an unexpected error," xalign 0.5
            text "{=datapad_body_text}this device must be recalibrated." xalign 0.5
            text "{=datapad_body_text}Please enter your pin below:" xalign 0.5

        vbox:
            xalign 0.5 yalign 0.67
            spacing 155
            hbox:
                xalign 0.5 yalign 0.61
                spacing 63
                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action Function(snd.play_click), SetVariable("puz.pin_pos1", If(puz.pin_pos1 < 9, puz.pin_pos1 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action Function(snd.play_click), SetVariable("puz.pin_pos2", If(puz.pin_pos2 < 9, puz.pin_pos2 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action Function(snd.play_click), SetVariable("puz.pin_pos3", If(puz.pin_pos3 < 9, puz.pin_pos3 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action Function(snd.play_click), SetVariable("puz.pin_pos4", If(puz.pin_pos4 < 9, puz.pin_pos4 + 1, 0))
        
            hbox:    
                xalign 0.5 yalign 0.61
                spacing 63
                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action Function(snd.play_click), SetVariable("puz.pin_pos1", If(puz.pin_pos1 > 0, puz.pin_pos1 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action Function(snd.play_click), SetVariable("puz.pin_pos2", If(puz.pin_pos2 > 0, puz.pin_pos2 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action Function(snd.play_click), SetVariable("puz.pin_pos3", If(puz.pin_pos3 > 0, puz.pin_pos3 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action Function(snd.play_click), SetVariable("puz.pin_pos4", If(puz.pin_pos4 > 0, puz.pin_pos4 - 1, 9))

        text "{=datapad_text}{size=100}[puz.pin_pos1]  [puz.pin_pos2]  [puz.pin_pos3]  [puz.pin_pos4]" xalign 0.5 yalign 0.64

        fixed:
            xpos 780 ypos 835

            imagebutton:
                idle "menus/confirm_button.png"
                hover "menus/confirm_button_hover.png"
                action Hide("datapad_tutorial"), Jump("code_check")
         
            text "{=datapad_text}CONFIRM" xalign 0.045 yalign 0.035

### Puzzles ###

### Chapter 1 Puzzle ###
### Tutorial Puzzle ###
# Checks to see if the tutorial puzzle's code is correct
label code_check:
    python:
        pin = str(puz.pin_pos1) + str(puz.pin_pos2) + str(puz.pin_pos3) + str(puz.pin_pos4)
    if pin == "3415":
        hide robot with dissolve
        $ snd.play_jingle("c")
        "Correct!"
        $ puz.reset_fails()
        $ inv.datapad_unlocked = True
        jump device_unlock
    else:
        python:
            puz.pin_pos1 = 0
            puz.pin_pos2 = 0
            puz.pin_pos3 = 0
            puz.pin_pos4 = 0
        $ snd.play_jingle("n")
        "That doesn't seem to be the right code."
        if puz.num_fails == 0:
            $ puz.increase_fails()
            jump first_password_fail
        elif puz.num_fails == 1:
            $ puz.increase_fails()
            jump second_password_fail
        else:
            $ puz.increase_fails()
            jump password_fail

# Unclickable variant of solution password
screen password:
    add "puzzles/note.png" xalign 0.49 yalign 0.55

# Click to reveal solution password
screen click_password:
    modal True

    imagebutton:
        focus_mask True
        xalign 0.01 yalign 0.01
        idle "help_button"
        hover "help_button_hover"
        action Play("sound", "<from 0.345>audio/menus/Click_button.wav"), Show("help_window")

    imagebutton:
        xalign 0.49 yalign 0.55
        focus_mask True
        idle "puzzles/note.png"
        hover "puzzles/note_highlight.png"
        action Play("sound", "<from 1.9 to 5>audio/ch1/Paper_rustle.wav"), Show("password_solution_1", transition=dissolve), Hide("click_password"), Jump("found_solution")

# Solution to tutorial puzzle
screen password_solution_1:
    modal False
    add "puzzles/note_zoom.png" xalign 0.5 yalign 0.5

screen password_solution:
    modal True
    add "puzzles/note_zoom.png" xalign 0.5 yalign 0.5
    
    imagebutton:
        focus_mask True
        idle "menus/back_close.png"
        action Show("datapad_tutorial"), Hide("password_solution", dissolve)

### Chapter 2 Puzzles ###

### Thicket Puzzle ###
### Activation ###
screen thicket_activation:
    imagebutton:
        xalign 0.94 yalign 0.69
        focus_mask True
        idle "puzzles/thicket_scanner.png"
        hover "puzzles/thicket_scanner_hover.png"
        action Function(snd.play_click), Hide("thicket_activation", transition=dissolve), Show("thicket_controls")

    if not inv.datapad_opened:
        imagebutton:
            xalign 0.5 yalign 0.97
            idle "menus/expand.png"
            hover "menus/expand_highlight.png"
            action Function(snd.open_inv), SetVariable("inv.datapad_opened", True), Show("datapad")

### Solution: 444
screen thicket_controls:
    imagebutton:
        focus_mask True
        xalign 0.01 yalign 0.01
        idle "help_button"
        hover "help_button_hover"
        action Play("sound", "<from 0.345>audio/menus/Click_button.wav"), Show("help_window")

    add "menus/datapad_back_hori.png" xalign 0.5 yalign 0.5
    add "menus/thicket_puz_frame.png" xalign 0.5 yalign 0.5

    if puz.thick_bar1 != 4 or puz.thick_bar2 != 4 or puz.thick_bar3 != 4:
        hbox:
            xalign 0.5 yalign 0.73
            spacing 200
            imagebutton:
                idle "up_arrow"
                hover "up_arrow_hover"
                action Function(snd.play_click), SetVariable("puz.thick_bar2", 2), SetVariable("puz.thick_bar3", 4)

            imagebutton:
                idle "up_arrow"
                hover "up_arrow_hover"
                action Function(snd.play_click), SetVariable("puz.thick_bar2", 4)

            imagebutton:
                idle "up_arrow"
                hover "up_arrow_hover"
                action Function(snd.play_click), SetVariable("puz.thick_bar1", 4), SetVariable("puz.thick_bar3", 3)

    else:
        vbox:
            xalign 0.5 yalign 0.22
            text "{=datapad_body_text}Calibration complete." xalign 0.5
            text "{=datapad_body_text}Please exit the device." xalign 0.5

        imagebutton:
            xalign 0.5 yalign 0.755
            idle "menus/confirm_button.png"
            hover "menus/confirm_button_hover.png"
            action Play("sound", "audio/menus/Correct_jingle.wav"), Hide("thicket_controls"), Jump("thicket_solved")

        text "{=datapad_text}EXIT" xalign 0.5 yalign 0.74

    python:
        if puz.thick_bar1 == 4 and puz.thick_bar2 == 4 and puz.thick_bar3 == 4:
            thicket_icon = "thicket_bar_solved"
        else:
            thicket_icon = "thicket_bar"
        yplace1 = 600
        yplace2 = 600
        yplace3 = 600
    for i in range(puz.thick_bar1):
        add "puzzles/[thicket_icon].png" xalign 0.35 ypos yplace1
        $ yplace1 -= 100
        
    for i in range(puz.thick_bar2):
        add "puzzles/[thicket_icon].png" xalign 0.5 ypos yplace2
        $ yplace2 -= 100
        
    for i in range(puz.thick_bar3):
        add "puzzles/[thicket_icon].png" xalign 0.65 ypos yplace3
        $ yplace3 -= 100

### Water Source Puzzle ###
### Solution: 
screen water_source_controls:
    #DEBUG
    #vbox:
     #   xalign 0.10
      #  yalign 0.2
       # text "[puz.rock_map[0]]"
        #text "[puz.rock_map[1]]"
        #text "[puz.rock_map[2]]"

    imagebutton:
        focus_mask True
        xalign 0.01 yalign 0.01
        idle "help_button"
        hover "help_button_hover"
        action Play("sound", "<from 0.345>audio/menus/Click_button.wav"), Show("help_window")

    add "menus/datapad_back.png" xalign 0.5 yalign 0.5
    add "menus/source_puz_frame.png" xalign 0.5 yalign 0.5
    
    add "puzzles/rock.png" xalign puz.rock1_x yalign puz.rock1_y
    add "puzzles/rock.png" xalign puz.rock2_x yalign puz.rock2_y
    add "puzzles/rock.png" xalign puz.rock3_x yalign puz.rock3_y
    add "puzzles/robo.png" xalign puz.robo_x yalign puz.robo_y

    $ puz.populate_map()

    if str(puz.robo_y) != str(puz.top) or str(puz.robo_x) != str(puz.middle_x):
        hbox:
            spacing 200
            xalign 0.501 yalign 0.8
            imagebutton:
                idle "left_arrow"
                hover "left_arrow_hover"
                action Play("sound", "<from 0.3>audio/menus/Move_rocks.wav"), Function(puz.move_robo_left)

            imagebutton:
                idle "right_arrow"
                hover "right_arrow_hover"
                action Play("sound", "<from 0.3>audio/menus/Move_rocks.wav"), Function(puz.move_robo_right)

        vbox:
            spacing 100
            xalign 0.5 yalign 0.85
            imagebutton:
                idle "up_arrow"
                hover "up_arrow_hover"
                action Play("sound", "<from 0.3>audio/menus/Move_rocks.wav"), Function(puz.move_robo_up)


            imagebutton:
                idle "down_arrow"
                hover "down_arrow_hover"
                action Play("sound", "<from 0.3>audio/menus/Move_rocks.wav"), Function(puz.move_robo_down)

        imagebutton:
            xalign 0.64 yalign 0.88
            idle "reset_button"
            hover "reset_button_hover"
            action Function(snd.play_click), Function(puz.reset_rock)

        text "{=datapad_body_text}RESET" xalign 0.635 yalign 0.87

    else:
        vbox:
            xalign 0.5 yalign 0.83
            spacing 20
            vbox:
                xalign 0.5
                text "{=datapad_body_text}Path cleared." xalign 0.5
                text "{=datapad_body_text}Please exit the device." xalign 0.5
            imagebutton:
                xalign 0.5 yalign 0.9
                idle "menus/confirm_button.png"
                hover "menus/confirm_button_hover.png"
                action Play("sound", "audio/menus/Correct_jingle.wav"), Jump("water_source_solved"), Hide("water_source_controls")

        text "{=datapad_text}EXIT" xalign 0.5 yalign 0.83


### Chapter 3 Puzzles ###
### Arm Puzzle ###
screen collect_arms:
    imagebutton:
        focus_mask True
        xalign 0.01 yalign 0.01
        idle "help_button"
        hover "help_button_hover"
        action Play("sound", "<from 0.345>audio/menus/Click_button.wav"), Show("help_window")

    if not inv.datapad_opened:
        imagebutton:
            xalign 0.5 yalign 0.97
            idle "menus/expand.png"
            hover "menus/expand_highlight.png"
            action Function(snd.open_inv), SetVariable("inv.datapad_opened", True), Show("datapad")

    if puz.got_arm_1 == False:
        imagebutton:
            xalign 1.0 yalign 0.4
            focus_mask True
            idle "puzzles/arm_1.png"
            hover "puzzles/arm_1_hover.png"
            action Function(snd.play_click), SetVariable("puz.got_arm_1", True)
        
    if puz.got_arm_2 == False:
        imagebutton:
            xalign 0.8 yalign 0.75
            focus_mask True
            idle "puzzles/arm_2.png"
            hover "puzzles/arm_2_hover.png"
            action Function(snd.play_click), SetVariable("puz.got_arm_2", True)

    if puz.got_arm_3 == False:        
        imagebutton:
            xalign 0.0 yalign 0.72
            focus_mask True
            idle "puzzles/arm_3.png"
            hover "puzzles/arm_3_hover.png"
            action Function(snd.play_click), SetVariable("puz.got_arm_3", True)

### Sound Puzzle ###
### Solution: 5 3 2 4 1
screen sound_pattern:
    python:
        length = len(puz.code_entry)
        puz.puz_tag = "Sound"

    if not inv.datapad_opened:
        imagebutton:
            xalign 0.5 yalign 0.97
            idle "menus/expand.png"
            hover "menus/expand_highlight.png"
            action Function(snd.open_inv), SetVariable("inv.datapad_opened", True), Show("datapad")

    imagebutton:
        focus_mask True
        xalign 0.01 yalign 0.01
        idle "help_button"
        hover "help_button_hover"
        action Play("sound", "<from 0.345>audio/menus/Click_button.wav"), Show("help_window")

    #text "PROGRESS: [puz.code_entry], [length] CORRECT: [puz.correct_code]"
    imagemap:
        xalign 0.5 yalign 0.5
        idle "images/puzzles/rocks.png"
        hover "images/puzzles/rocks_hover.png"

        hotspot(446, 402, 83, 97) action Play("sound", "audio/ch3/sound_puzzle/Choice5.wav"), SetVariable("puz.button_id", "1"), Function(puz.sound_code_progress)
        hotspot(522, 593, 97, 87) action Play("sound", "audio/ch3/sound_puzzle/Choice4.wav"), SetVariable("puz.button_id", "2"), Function(puz.sound_code_progress)
        hotspot(594, 691, 110, 94) action Play("sound", "audio/ch3/sound_puzzle/Choice2.wav"), SetVariable("puz.button_id", "3"), Function(puz.sound_code_progress)
        hotspot(787, 721, 130, 101) action Play("sound", "audio/ch3/sound_puzzle/Choice3.wav"), SetVariable("puz.button_id", "4"), Function(puz.sound_code_progress)
        hotspot(981, 574, 86, 135) action Play("sound", "audio/ch3/sound_puzzle/Choice1.wav"), SetVariable("puz.button_id", "5"), Function(puz.sound_code_progress)

    imagemap:
        xalign 0.9 yalign 0.5
        idle "images/menus/audio_puz_mini.png"
        hover "images/menus/audio_puz_mini_hover.png"

        hotspot(42, 259, 120, 114) action Function(puz.sound_replay)
        hotspot(185, 261, 120, 113) action Hide("sound_pattern", transition=dissolve), Jump("sound_check_code")
        hotspot(45, 403, 259, 88) action Function(puz.sound_reset_code)
        text "{=datapad_text}RESET" xalign 0.485 yalign 0.881

        text "{=datapad_text}{size=75}[puz.code_entry]" xalign 0.48 yalign 0.31

label sound_check_code:
    if puz.code_entry == puz.correct_code:
        $ snd.play_jingle("c")
        "Correct!"
        $ puz.puz_tag = None
        $ puz.reset_fails()
        jump sound_success
    else:
        $ puz.sound_reset_code()
        play sound "audio/menus/Incorrect_jingle.wav"
        "That doesn't seem to be the right sequence."
        if puz.num_fails == 0:
            $ puz.increase_fails()
            jump first_sound_fail
        elif puz.num_fails == 1:
            $ puz.increase_fails()
            jump second_sound_fail
        else:
            $ puz.increase_fails()
            jump sound_fail

label first_sound_fail:
    show robot happy with dissolve

    y2 "That's not right..."

    r "That's alright, Captain, we can try again."

    hide robot with dissolve
    call screen sound_pattern with dissolve

label second_sound_fail:
    show robot happy with dissolve

    y2 "That's not right..."

    r "That's alright, Captain, we can try again."

    hide robot with dissolve
    call screen sound_pattern with dissolve

label sound_fail:
    show robot happy with dissolve

    y2 "That's not right..."

    r "That's alright, Captain, we can try again."

    hide robot with dissolve
    call screen sound_pattern with dissolve

### Help Window ###
screen help_window:
    modal True

    # closes screen
    imagebutton:
        focus_mask True
        idle "menus/help_window_close.png"
        action Hide("help_window") 

    add "menus/help_window.png" xalign 0.5 yalign 0.5

    if puz.puz_tag == "Tutorial":
        vbox:
            xalign 0.5 yalign 0.5
            spacing 50
            text "You need to unlock your datapad! But you can't remember your password..." xmaximum 750
            text "Maybe MUS-L can help?" xmaximum 750

    elif puz.puz_tag == "Thicket1":
        vbox:
            xalign 0.5 yalign 0.5
            spacing 50
            text "Click on the arrows at the bottom of the screen. Each arrow will either decrease or increase the value of one or more of the green bars." xmaximum 750
            text "To complete the puzzle, click the arrows until every green bar reaches the top of the screen at the same time." xmaximum 750

    elif puz.puz_tag == "Water1":
        vbox:
            xalign 0.5 yalign 0.5

            spacing 50
            text "Click on the arrows to control MUS-L, the orange square. If there is enough space, MUS-L can push a rock out of the way when he is next to one." xmaximum 750
            text "To complete the puzzle, help MUS-L move the rocks until he reaches the goal at the top of the screen. If you get stuck, you can reset the puzzle." xmaximum 750

    elif puz.puz_tag == "Arms":
        vbox:
            xalign 0.5 yalign 0.5
            spacing 50
            text "Collect the pieces of Avery's replacement arm scattered around the area. You can check your progress by looking at your datapad." xmaximum 750
            text "Once you've found all the pieces, you can use your datapad to give the arm to Avery." xmaximum 750

    elif puz.puz_tag == "Sound":
        vbox:
            xalign 0.5 yalign 0.5
            spacing 50
            text "Click the rocks in the area to replicate the sequence of sounds you hear. You can check your sequence by clicking on the checkmark in the progress window." xmaximum 750
            text "If you want to hear the sequence of sounds again, click the replay button." xmaximum 750