# Script for submenus in-game
define name = ""

### Input constraints ###
define alphabet = "A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z"
define numbers = "0 1 2 3 4 5 6 7 8 9"

## Classes ###################
init python:
    ### Player ###
    class Player:
        ## Variables ####################
        def __init__(self, name):
            self.name = name
            self.current_label = "Unknown"

    ### Side character manager ###
    class Side_char:
        ## Variables ####################
        def __init__(self):        
            self.scientist_name = "Avery"
            self.robot_name = "Robot"
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
            self.item_list = ["activation code", "old key"]

            # Tutorial puzzle
            self.pin_pos1 = 0
            self.pin_pos2 = 0
            self.pin_pos3 = 0
            self.pin_pos4 = 0
            self.handheld_unlocked = False

        ## Functions ####################
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
            else:
                return "No item description found."

## DEBUG ###################
screen debug:
    text "Debug" xpos 25 ypos 25
    #text "Pin: [pin_pos1] [pin_pos2] [pin_pos3] [pin_pos4]" xpos 25 ypos 75

## Styles ###################
# Used for handheld device's headers
style handheld_text:
    size 50
    font "consola.ttf"
    color "#ffffff"

# Used for handheld device's body text
style handheld_body_text:
    size 35
    font "consola.ttf"
    color "#ffffff"

## Screens ###################
### Handheld tool ###
# This version of the handheld device is used for every instance after the tutorial
screen handheld:
    modal True
    add "menus/handheld_back.png" xalign 0.5 yalign 0.5

    # Setting variables for display
    python:
        scientist_health_color = side.get_health_color("scientist")
        robot_health_color = side.get_health_color("robot")

    # closes screen
    imagebutton:
        focus_mask True
        idle "menus/handheld_back_close.png"
        action Hide("handheld"), Jump("location_control")

    # vbox for main screen
    vbox:
        xalign 0.5 yalign 0.4
        spacing 25
        # hbox for item info
        hbox:
            spacing 5
            if inv.held_item != None:
                imagebutton:
                    idle "menus/item_frame.png" xalign 0.4 yalign 0.3
                    action Hide("handheld"), Show("item_desc")
            else:
                add "menus/item_frame.png" xalign 0.4 yalign 0.3
            vbox:
                text "{=handheld_text}> Current item:"
                text "{=handheld_body_text}[inv.held_item]" xalign 0.5

        # vbox for player location info
        vbox:
            xalign 0.0 yalign 0.45
            text "{=handheld_text}> Current location:" ypos 15
            text "{=handheld_body_text}[player.current_label]" ypos 15
            
        # vbox for side character info
        text "{=handheld_text}> Team status:" ypos 30
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
                text "{=handheld_text}{u}[side.scientist_name]"
                text "{=handheld_body_text}Location: [side.scientist_location]"
                text "{=handheld_body_text}Status:{color=[scientist_health_color]} [side.scientist_health]"
                text "{=handheld_text}{u}[side.robot_name]" ypos 10
                text "{=handheld_body_text}Location: [side.robot_location]" ypos 10
                text "{=handheld_body_text}Status:{color=[robot_health_color]} [side.robot_health]" ypos 10

    # closes handheld
    fixed:
        xpos 1075 ypos 850
        imagebutton:
            idle "close_button"
            hover "close_button_hover"
            action Hide("handheld"), Jump("location_control")
         
        text "{=handheld_text}CLOSE" xalign 0.017 yalign 0.027

# Screen for viewing item and to confirm item use
screen item_desc:
    modal True
    add "menus/handheld_back.png" xalign 0.5 yalign 0.5

    # closes screen
    imagebutton:
        focus_mask True
        idle "menus/handheld_back_close.png"
        action Hide("item_desc"), Jump("location_control")

    # vbox for item info
    vbox:
        xalign 0.5 yalign 0.25
        spacing 35
        vbox:
            spacing 30
            imagebutton:
                idle "menus/item_frame.png" xalign 0.5 yalign 0.3
                action Hide("handheld"), Show("item_desc")
            vbox:
                spacing 15
                text "{=handheld_text}{u}[inv.held_item]" xalign 0.5
                $ held_item_desc = inv.get_item_desc()
                text "{=handheld_body_text}[held_item_desc]" xalign 0.5

    # returns to handheld main screen
    fixed:
        xpos 1075 ypos 850
        imagebutton:
            idle "close_button"
            hover "close_button_hover"
            action Hide("item_desc"), Show("handheld")
         
        text "{=handheld_text}BACK" xalign 0.025 yalign 0.027

# The tutorial version of the handheld device, only used in Chapter 1
screen handheld_tutorial:
    modal True

    imagebutton:
        focus_mask True
        idle "menus/handheld_back_close.png"
        action Hide("handheld_tutorial")
    
    if inv.handheld_unlocked:
        add "menus/handheld_back.png" xalign 0.5 yalign 0.5
        vbox:
            xalign 0.5 yalign 0.29
            spacing 15
            text "{=handheld_text}To complete" xalign 0.5
            text "{=handheld_text}recalibration," xalign 0.5
            text "{=handheld_text}Please enter your" xalign 0.5
            text "{=handheld_text}name below." xalign 0.5

        hbox:
            xalign 0.5 yalign 0.57
            input default "":
                style "handheld_text"
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
                action Hide("handheld_tutorial"), Jump("name_entered")

            text "{=handheld_text}CONFIRM" xalign 0.045 yalign 0.035

    else:
        add "menus/handheld_back_tutorial.png" xalign 0.5 yalign 0.5
        text "{=handheld_text}Welcome!" xalign 0.5 yalign 0.15
        vbox:
            xalign 0.5 yalign 0.29
            spacing 15

            text "{=handheld_body_text}This device is registered to" xalign 0.5
            text "{=handheld_body_text}[company] terraforming captain" xalign 0.5
            text "{=handheld_body_text}ID #1015814117" xalign 0.5
            text "{=handheld_body_text}Due to an unexpected error," xalign 0.5
            text "{=handheld_body_text}this device must be recalibrated." xalign 0.5
            text "{=handheld_body_text}Please enter your pin below:" xalign 0.5

        vbox:
            xalign 0.5 yalign 0.67
            spacing 155
            hbox:
                xalign 0.5 yalign 0.61
                spacing 63
                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action SetVariable("inv.pin_pos1", If(inv.pin_pos1 < 9, inv.pin_pos1 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action SetVariable("inv.pin_pos2", If(inv.pin_pos2 < 9, inv.pin_pos2 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action SetVariable("inv.pin_pos3", If(inv.pin_pos3 < 9, inv.pin_pos3 + 1, 0))

                imagebutton:
                    idle "up_arrow"
                    hover "up_arrow_hover"
                    action SetVariable("inv.pin_pos4", If(inv.pin_pos4 < 9, inv.pin_pos4 + 1, 0))
        
            hbox:    
                xalign 0.5 yalign 0.61
                spacing 63
                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action SetVariable("inv.pin_pos1", If(inv.pin_pos1 > 0, inv.pin_pos1 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action SetVariable("inv.pin_pos2", If(inv.pin_pos2 > 0, inv.pin_pos2 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action SetVariable("inv.pin_pos3", If(inv.pin_pos3 > 0, inv.pin_pos3 - 1, 9))

                imagebutton:
                    idle "down_arrow"
                    hover "down_arrow_hover"
                    action SetVariable("inv.pin_pos4", If(inv.pin_pos4 > 0, inv.pin_pos4 - 1, 9))

        text "{=handheld_text}{size=100}[inv.pin_pos1]  [inv.pin_pos2]  [inv.pin_pos3]  [inv.pin_pos4]" xalign 0.5 yalign 0.64

        fixed:
            xpos 780 ypos 835

            imagebutton:
                idle "menus/confirm_button.png"
                hover "menus/confirm_button_hover.png"
                action Hide("handheld_tutorial"), Jump("code_check")
         
            text "{=handheld_text}CONFIRM" xalign 0.045 yalign 0.035

# Checks to see if the tutorial puzzle's code is correct
label code_check:
    python:
        pin = str(inv.pin_pos1) + str(inv.pin_pos2) + str(inv.pin_pos3) + str(inv.pin_pos4)
    if pin == "5555":
        "Correct!"
        $ inv.handheld_unlocked = True
        jump device_unlock
    else:
        "That doesn't seem to be the right code."