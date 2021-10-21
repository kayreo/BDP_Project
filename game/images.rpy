# Script to store images/names/transformations


#################################
## Characters ###################
#################################

### Temp player name ###
define p = Character("You")

### Avery ###

define s = Character("Avery", color="#baffbe")
define s_unknown = Character("???", color = "baffbe")

image scientist_portrait = im.Scale("characters/scientist/scientist_portrait.png", 100, 100)
image scientist happy = im.Scale("characters/scientist/scientist0.png", 547, 1080)
image scientist sad = im.Scale("characters/scientist/scientist1.png", 547, 1080)
image scientist sad2 = im.Scale("characters/scientist/scientist2.png", 547, 1080)
image scientist angry = im.Scale("characters/scientist/scientist3.png", 547, 1080)
image scientist shocked = im.Scale("characters/scientist/scientist4.png", 547, 1080)

### Robot ###

define r = Character("MUS-L", color="#db9a6e")
define r_unknown = Character("???", color = "db9a6e")

image robot_portrait = im.Scale("characters/robot/robot_portrait.png", 100, 100)
image robot happy = im.Scale("characters/robot/robot0.png", 547, 1080)
image robot sad = im.Scale("characters/robot/robot1.png", 547, 1080)
image robot sad2 = im.Scale("characters/robot/robot2.png", 547, 1080)
image robot angry = im.Scale("characters/robot/robot3.png", 547, 1080)
image robot shocked = im.Scale("characters/robot/robot4.png", 547, 1080)

#################################
## Backgrounds ##################
#################################

image bg blank = im.Scale("backgrounds/blank.png", 1920, 1080)
image bg waterfall = im.Scale("backgrounds/waterfall.png", 1920, 1080)
image bg thicket = im.Scale("backgrounds/thicket.png", 1920, 1080)

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