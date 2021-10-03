# Script to store images/names/transformations


#################################
## Characters ###################
#################################

### Avery ###

define s = Character("Avery", color="#baffbe")

image scientist_portrait = im.Scale("characters/scientist/scientist_portrait.png", 100, 100)
image scientist happy = im.Scale("characters/scientist/scientist0.png", 547, 1080)
image scientist sad = im.Scale("characters/scientist/scientist1.png", 547, 1080)
image scientist sad2 = im.Scale("characters/scientist/scientist2.png", 547, 1080)
image scientist angry = im.Scale("characters/scientist/scientist3.png", 547, 1080)
image scientist shocked = im.Scale("characters/scientist/scientist4.png", 547, 1080)

### Robot ###

define r = Character("Robot", color="#db9a6e")

image robot_portrait = im.Scale("characters/robot/robot_portrait.png", 100, 100)
image robot happy = im.Scale("characters/robot/robot0.png", 547, 1080)
image robot sad = im.Scale("characters/robot/robot1.png", 547, 1080)
image robot sad2 = im.Scale("characters/robot/robot2.png", 547, 1080)
image robot angry = im.Scale("characters/robot/robot3.png", 547, 1080)
image robot shocked = im.Scale("characters/robot/robot4.png", 547, 1080)

#################################
## Menus ########################
#################################

### Handheld ###
image up_arrow = im.Flip("menus/arrow.png", vertical ="True")
image down_arrow = "menus/arrow.png"
image up_arrow_hover = im.Flip("menus/arrow_hover.png", vertical ="True")
image down_arrow_hover = "menus/arrow_hover.png"
image close_button = im.Scale("menus/confirm_button.png", 200, 100)
image close_button_hover = im.Scale("menus/confirm_button_hover.png", 200, 100)