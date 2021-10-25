# Script for submenus in-game
define name = ""

### Input constraints ###
define alphabet = "A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z"
define numbers = "0 1 2 3 4 5 6 7 8 9"

## Classes ###################
init python:
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
            if self.held_item == remove_item:
                self.held_item = None
            else:
                return

        # Returns item description
        def get_item_desc(self):
            if self.held_item == "test_item":
                return "This item is for testing."
            if self.held_item == "activation code":
                return "This is the passcode to your datapad. Probably best to keep it somewhere safe..."

            if self.held_item == "MUS-L's hand":
                return "One of MUS-L's many hand attachments. Its installation is thankfully simple."
            else:
                return "No item description found."

    ### Puzzles ###
    class Puzzle_manager:
        def __init__(self):
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
            self.robo_x = self.left
            self.robo_y = self.bottom

            self.rock1_x = self.left
            self.rock1_y = self.middle_y

            self.rock2_x = self.right
            self.rock2_y = self.bottom

            self.rock3_x = self.middle_x
            self.rock3_y = self.middle_y

            self.arrow_dir = "None"

            self.nearest_rock = "None"


            # General puzzles
            self.num_fails = 0

        # Increases number of failures after failing to solve a puzzle
        def increase_fails(self):
            self.num_fails += 1

        # Reset number of failures after solving puzzle
        def reset_fails(self):
            self.num_fails = 0

        # Gets rock x position
        def get_rock_x(self, rock_id):
            if rock_id == "rock1":
                return self.rock1_x
            elif rock_id == "rock2":
                return self.rock2_x          
            elif rock_id == "rock3":
                return self.rock3_x
            else:
                return "None"

        # Gets rock y position
        def get_rock_y(self, rock_id):
            if rock_id == "rock1":
                return self.rock1_y
            elif rock_id == "rock2":
                return self.rock2_y
            elif rock_id == "rock3":
                return self.rock3_y
            else:
                return "None"

        def get_rock_x_dist(self, rock_id):
            if rock_id == "rock1":
                return str(abs(self.robo_x - self.rock1_x))
                
            elif rock_id == "rock2":
                return str(abs(self.robo_x - self.rock2_x))
                       
            elif rock_id == "rock3":
                return str(abs(self.robo_x - self.rock3_x))
                
        def get_rock_y_dist(self, rock_id):
            if rock_id == "rock1":
                return str(abs(self.robo_y - self.rock1_y))   
                
            elif rock_id == "rock2":
                return str(abs(self.robo_y - self.rock2_y))
                
            elif rock_id == "rock3":
                return str(abs(self.robo_y - self.rock3_y))

        # Gets nearest rock to robot
        def get_nearest(self):
            for i in range(3):
                rock = "rock" + str(i)
                check_pos1 = self.get_rock_x_dist(rock)
                check_pos2 = self.get_rock_y_dist(rock)
                if check_pos1 == str(self.x_increment) and str(self.robo_y) == str(self.rock1_y) or check_pos2 == str(self.y_increment) and str(self.robo_x) == str(self.rock1_x):
                    self.nearest_rock = "rock1"
                    return

                elif check_pos1 == str(self.x_increment) and str(self.robo_y) == str(self.rock2_y) or check_pos2 == str(self.y_increment) and str(self.robo_x) == str(self.rock2_x):
                    self.nearest_rock = "rock2"
                    return

                elif check_pos1 == str(self.x_increment) and str(self.robo_y) == str(self.rock3_y) or check_pos2 == str(self.y_increment) and str(self.robo_x) == str(self.rock3_x):
                    self.nearest_rock = "rock3"
                    return

            else:
                self.nearest_rock = "None"

        # Moves robot left
        def move_robo_left(self):
            if self.nearest_rock != "None":
                rock_x = str(self.get_rock_x(self.nearest_rock))
                if self.robo_x > self.left and self.can_move_rock(rock_x, str(self.left)):
                    self.robo_x -= self.x_increment
                else:
                    return         
            else:
                if self.robo_x > self.left:
                    self.robo_x -= self.x_increment
                else:
                    return

        # Moves robot right
        def move_robo_right(self):
            if self.nearest_rock != "None":
                rock_x = str(self.get_rock_x(self.nearest_rock))
                if self.robo_x < self.right and self.can_move_rock(rock_x, str(self.right)):
                    self.robo_x += self.x_increment
                else:
                    return       
            else:    
                if self.robo_x < self.right:
                    self.robo_x += self.x_increment
                else:
                    return

        # Moves robot up
        def move_robo_up(self):
            if self.nearest_rock != "None":
                rock_y = str(self.get_rock_y(self.nearest_rock))
                if self.robo_y > self.top and self.can_move_rock(rock_y, str(self.top)):
                    self.robo_y -= self.y_increment
                else:    
                    return
            else:
                if self.robo_y > self.top:
                    self.robo_y -= self.y_increment
                else:
                    return

        # Moves robot down
        def move_robo_down(self):
            if self.nearest_rock != "None":
                rock_y = str(self.get_rock_y(self.nearest_rock))
                if self.robo_y < self.bottom and self.can_move_rock(rock_y, str(self.bottom)):
                    self.robo_y += self.y_increment
                else:
                    return
            else:
                if self.robo_y < self.bottom:
                    self.robo_y += self.y_increment
                else:
                    return

        # Checks if rock can be moved
        def can_move_rock(self, rock_id, rock_pos):
            if rock_id != rock_pos:
                return True
            else:
                return False

        # Checks if robot had collided with rock
        def check_robo_pos(self):
            robo_x = str(self.robo_x)
            robo_y = str(self.robo_y)

            rock1_x = str(self.rock1_x)
            rock1_y = str(self.rock1_y)
            rock2_x = str(self.rock2_x)
            rock2_y = str(self.rock2_y)
            rock3_x = str(self.rock3_x)
            rock3_y = str(self.rock3_y)

            if robo_x == rock1_x and robo_y == rock1_y:
                if self.arrow_dir == "right" and self.can_move_rock(rock1_x, str(self.right)):
                    self.rock1_x += self.x_increment

                elif self.arrow_dir == "left" and self.can_move_rock(rock1_x, str(self.left)):
                    self.rock1_x -= self.x_increment

                elif self.arrow_dir == "up" and self.can_move_rock(rock1_y, str(self.top)):
                    self.rock1_y -= self.y_increment

                elif self.arrow_dir == "down" and self.can_move_rock(rock1_y, str(self.bottom)):
                    self.rock1_y += self.y_increment

            elif robo_x == rock2_x and robo_y == rock2_y:
                if self.arrow_dir == "right" and self.can_move_rock(rock2_x, str(self.right)):
                    self.rock2_x += self.x_increment

                elif self.arrow_dir == "left" and self.can_move_rock(rock2_x, str(self.left)):
                    self.rock2_x -= self.x_increment

                elif self.arrow_dir == "up" and self.can_move_rock(rock2_y, str(self.top)):
                    self.rock2_y -= self.y_increment

                elif self.arrow_dir == "down" and self.can_move_rock(rock2_y, str(self.bottom)):
                    self.rock2_y += self.y_increment

            elif robo_x == rock3_x and robo_y == rock3_y:
                if self.arrow_dir == "right" and self.can_move_rock(rock3_x, str(self.right)):
                    self.rock3_x += self.x_increment

                elif self.arrow_dir == "left" and self.can_move_rock(rock3_x, str(self.left)):
                    self.rock3_x -= self.x_increment

                elif self.arrow_dir == "up" and self.can_move_rock(rock3_y, str(self.top)):
                    self.rock3_y -= self.y_increment

                elif self.arrow_dir == "down" and self.can_move_rock(rock3_y, str(self.bottom)):
                    self.rock3_y += self.y_increment
            

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
                action SetVariable("inv.datapad_opened", False), Show("water_source2"), Hide("datapad")
            else:
                action SetVariable("inv.datapad_opened", False), Hide("datapad")

    # displays item, if one is equipped
    if inv.held_item != None:
        $ held_item = inv.held_item.capitalize()
        add "items/[inv.held_item].png" xalign 0.377 yalign 0.155

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
                    action Hide("datapad"), Show("item_desc")
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
                    action SetVariable("inv.datapad_opened", False), Show("water_source2"), Hide("datapad")
                else:
                    action SetVariable("inv.datapad_opened", False), Hide("datapad")
         
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
            action SetVariable("inv.datapad_opened", False), Hide("datapad")

    # vbox for item info
    add "items/[inv.held_item].png" xalign 0.5 yalign 0.165
    vbox:
        xalign 0.5 yalign 0.35
        spacing 35
        vbox:
            spacing 30
            imagebutton:
                idle "menus/item_frame.png" xalign 0.5 yalign 0.3
                action Hide("datapad"), Show("item_desc")
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
                        action Jump("use_item")

                    imagebutton:
                        if per.chapter_num != 1:
                            idle "close_button" xalign 0.25
                            hover "close_button_hover" 
                            action Hide("item_desc"), Show("datapad")
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
                action Hide("item_desc"), Show("datapad")
         
            text "{=datapad_text}BACK" xalign 0.025 yalign 0.027

# Uses equipped item
label use_item:
    hide screen item_desc with dissolve
    if inv.held_item == "activation code":
        name "It's probably not a good idea to just have this lying around somewhere..."
        "You stuff the crumpled up note into your pocket."
        jump chap_1_end

    elif inv.held_item == "MUS-L's hand":
        show robot happy with dissolve
        
        "You remove MUS-L's drill attachments and slip his hands into the sockets."

        r "Thank you, Captain."
        
        jump water_source_puzzle

screen open_datapad:
    imagebutton:
        idle "menus/expand.png"
        hover "menus/expand_highlight.png"
        action Hide("open_datapad"), Show("datapad")


# The tutorial version of the datapad device, only used in Chapter 1
screen datapad_tutorial:
    modal True

    imagebutton:
        focus_mask True
        idle "menus/datapad_back_close.png"
        action Hide("datapad_tutorial")
    
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
                action Hide("datapad_tutorial"), Jump("name_entered")

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
                    action SetVariable("puz.pin_pos1", If(puz.pin_pos1 < 9, puz.pin_pos1 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action SetVariable("puz.pin_pos2", If(puz.pin_pos2 < 9, puz.pin_pos2 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action SetVariable("puz.pin_pos3", If(puz.pin_pos3 < 9, puz.pin_pos3 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action SetVariable("puz.pin_pos4", If(puz.pin_pos4 < 9, puz.pin_pos4 + 1, 0))
        
            hbox:    
                xalign 0.5 yalign 0.61
                spacing 63
                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action SetVariable("puz.pin_pos1", If(puz.pin_pos1 > 0, puz.pin_pos1 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action SetVariable("puz.pin_pos2", If(puz.pin_pos2 > 0, puz.pin_pos2 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action SetVariable("puz.pin_pos3", If(puz.pin_pos3 > 0, puz.pin_pos3 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action SetVariable("puz.pin_pos4", If(puz.pin_pos4 > 0, puz.pin_pos4 - 1, 9))

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
        xalign 0.49 yalign 0.55
        focus_mask True
        idle "puzzles/note.png"
        hover "puzzles/note_highlight.png"
        action Show("password_solution_1"), Hide("click_password"), Jump("found_solution")

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
        action Hide("thicket_activation", transition=dissolve), Show("thicket_controls")

    if not inv.datapad_opened:
        imagebutton:
            xalign 0.5 yalign 0.97
            idle "menus/expand.png"
            hover "menus/expand_highlight.png"
            action SetVariable("inv.datapad_opened", True), Show("datapad")

### Solution: 444
screen thicket_controls:
    add "menus/datapad_back_hori.png" xalign 0.5 yalign 0.5
    add "menus/thicket_puz_frame.png" xalign 0.5 yalign 0.5

    if puz.thick_bar1 != 4 or puz.thick_bar2 != 4 or puz.thick_bar3 != 4:
        hbox:
            xalign 0.5 yalign 0.73
            spacing 200
            imagebutton:
                idle "up_arrow"
                hover "up_arrow_hover"
                action SetVariable("puz.thick_bar2", 2), SetVariable("puz.thick_bar3", 4)

            imagebutton:
                idle "up_arrow"
                hover "up_arrow_hover"
                action SetVariable("puz.thick_bar2", 4)

            imagebutton:
                idle "up_arrow"
                hover "up_arrow_hover"
                action SetVariable("puz.thick_bar1", 4), SetVariable("puz.thick_bar3", 3)

    else:
        vbox:
            xalign 0.5 yalign 0.22
            text "{=datapad_body_text}Calibration complete." xalign 0.5
            text "{=datapad_body_text}Please exit the device." xalign 0.5

        imagebutton:
            xalign 0.5 yalign 0.755
            idle "menus/confirm_button.png"
            hover "menus/confirm_button_hover.png"
            action Hide("thicket_controls"), Jump("thicket_solved")

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
    add "menus/datapad_back.png" xalign 0.5 yalign 0.5
    add "menus/source_puz_frame.png" xalign 0.5 yalign 0.5
    
    add "puzzles/rock.png" xalign puz.rock1_x yalign puz.rock1_y
    add "puzzles/rock.png" xalign puz.rock2_x yalign puz.rock2_y
    add "puzzles/rock.png" xalign puz.rock3_x yalign puz.rock3_y
    add "puzzles/robo.png" xalign puz.robo_x yalign puz.robo_y

    if str(puz.robo_y) != str(puz.top) or str(puz.robo_x) != str(puz.middle_x):
        hbox:
            spacing 200
            xalign 0.501 yalign 0.8
            imagebutton:
                idle "left_arrow"
                hover "left_arrow_hover"
                action Function(puz.move_robo_left), SetVariable("puz.arrow_dir", "left"), Function(puz.get_nearest), Function(puz.check_robo_pos), Function(puz.get_nearest),
        
            imagebutton:
                idle "right_arrow"
                hover "right_arrow_hover"
                action Function(puz.move_robo_right), SetVariable("puz.arrow_dir", "right"), Function(puz.get_nearest), Function(puz.check_robo_pos), Function(puz.get_nearest),

        vbox:
            spacing 100
            xalign 0.5 yalign 0.85
            imagebutton:
                idle "up_arrow"
                hover "up_arrow_hover"
                action Function(puz.move_robo_up), SetVariable("puz.arrow_dir", "up"), Function(puz.get_nearest), Function(puz.check_robo_pos), Function(puz.get_nearest),


            imagebutton:
                idle "down_arrow"
                hover "down_arrow_hover"
                action Function(puz.move_robo_down), SetVariable("puz.arrow_dir", "down"), Function(puz.get_nearest), Function(puz.check_robo_pos), Function(puz.get_nearest),

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
                action Jump("water_source_solved"), Hide("water_source_controls")

        text "{=datapad_text}EXIT" xalign 0.5 yalign 0.83
