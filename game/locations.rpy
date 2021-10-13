# Script for location manager and screens in-game

## Management ###################
label location_manager:
    if per.player_location == "waterfall":
        jump waterfall

    elif per.player_location == "forest":
        jump forest

    elif per.player_location == "thicket":
        jump thicket

    if per.player_location == "device_testing":
        jump device_testing

label waterfall:
    scene bg waterfall
    "Waterfall area."
    call screen waterfall

label forest:
    scene bg forest
    "Forest area."
    jump waterfall

label thicket:
    scene bg thicket
    "Thicket area."
    jump waterfall


## Screens ###################
### Waterfall ###
screen waterfall:
    imagemap: 
        idle "backgrounds/waterfall.png"
        hover "backgrounds/waterfall_highlight.png"

        hotspot(0, 101, 585, 573) action SetVariable("per.player_location", "forest"), Jump("location_manager")
        hotspot(1693, 171, 226, 413) action SetVariable("per.player_location", "thicket"), Jump("location_manager")