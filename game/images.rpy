# Script to store images/names/transformations

# Also stores information for sound effects, such as looping and start times


#################################
## Characters ###################
#################################

### Temp player name ###
define p = Character("You", color="#ffffff")

### Avery ###

define s = Character("Avery", color="#baffbe")
define s_unknown = Character("???", color = "baffbe")

image scientist_portrait = im.Scale("characters/scientist/scientist_portrait.png", 100, 100)
image scientist happy = im.Scale("characters/scientist/scientist0.png", 547, 1080)
image scientist sad = im.Scale("characters/scientist/scientist1.png", 547, 1080)
image scientist sad2 = im.Scale("characters/scientist/scientist2.png", 547, 1080)
image scientist angry = im.Scale("characters/scientist/scientist3.png", 547, 1080)
image scientist shocked = im.Scale("characters/scientist/scientist4.png", 547, 1080)

image scientist happyB = im.Scale("characters/scientist/scientistB0.png", 547, 1080)
image scientist sadB = im.Scale("characters/scientist/scientistB1.png", 547, 1080)
image scientist sad2B = im.Scale("characters/scientist/scientistB2.png", 547, 1080)
image scientist angryB = im.Scale("characters/scientist/scientistB3.png", 547, 1080)
image scientist shockedB = im.Scale("characters/scientist/scientistB4.png", 547, 1080)

### MUS-L ###

define r = Character("MUS-L", color="#db9a6e")
define r_unknown = Character("???", color = "db9a6e")

image robot_portrait = im.Scale("characters/robot/robot_portrait.png", 100, 100)
image robot happy = im.Scale("characters/robot/robot0.png", 547, 1080)
image robot sad = im.Scale("characters/robot/robot1.png", 547, 1080)
image robot sad2 = im.Scale("characters/robot/robot2.png", 547, 1080)
image robot angry = im.Scale("characters/robot/robot3.png", 547, 1080)
image robot shocked = im.Scale("characters/robot/robot4.png", 547, 1080)

image robot happyB = im.Scale("characters/robot/robotB0.png", 547, 1080)

#################################
## Backgrounds ##################
#################################

image bg blank = im.Scale("backgrounds/blank.png", 1920, 1080)
image bg waterfall = im.Scale("backgrounds/waterfall.png", 1920, 1080)
image bg thicket = im.Scale("backgrounds/thicket.png", 1920, 1080)
image bg water_source = im.Scale("backgrounds/watersource.png", 1920, 1080)
image bg core = im.Scale("backgrounds/core.png", 1920, 1080)

#################################
## Menus ########################
#################################

### Handheld ###
image up_arrow = im.Flip("menus/arrow.png", vertical ="True")
image down_arrow = "menus/arrow.png"
image up_arrow_hover = im.Flip("menus/arrow_hover.png", vertical ="True")
image down_arrow_hover = "menus/arrow_hover.png"
image right_arrow = im.Flip("menus/arrow2.png", horizontal ="True")
image left_arrow = "menus/arrow2.png"
image right_arrow_hover = im.Flip("menus/arrow_hover2.png", horizontal ="True")
image left_arrow_hover = "menus/arrow_hover2.png"
image close_button = im.Scale("menus/confirm_button.png", 200, 100)
image close_button_hover = im.Scale("menus/confirm_button_hover.png", 200, 100)
image reset_button = im.Scale("menus/confirm_button.png", 150, 75)
image reset_button_hover = im.Scale("menus/confirm_button_hover.png", 150, 75)
image help_button = im.Scale("menus/help.png", 150, 150)
image help_button_hover = im.Scale("menus/help_hover.png", 150, 150)


#################################
## Audio ########################
#################################

### Characters ###
# MUS-L's happy beep: play sound "<from 0.7>Audio/Happy_beep2.wav"

# MUS-L's sad beep: "<from 2.7>audio/Sad_beep.wav"

### Items ###
# Paper rustle: play sound "<from 1.9 to 5>audio/Paper_rustle.wav"

# Click button: Play("sound", "<from 0.3>audio/Click_button.wav") OR Play("sound", "<from 0.345>audio/Click_button.wav")

# Open inventory: play sound "<from 0.4>audio/Inventory_click.wav" // Play("sound", "<from 0.4>audio/Inventory_click.wav")

# Correct jingle: play sound "audio/Correct_jingle.wav" // Play("sound", "audio/Correct_jingle.wav")

# Incorrect jingle: play sound "audio/Incorrect_jingle.wav" 

# Datapad beep: play sound "<from 0.5>audio/Datapad_beeping.wav"