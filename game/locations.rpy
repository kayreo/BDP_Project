# Script for location manager and screens in-game
define first_visit = False

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
    scene bg waterfall with dissolve
    "Waterfall area."
    call screen waterfall

label forest:
    scene bg forest
    "Forest area."
    jump waterfall

label thicket:
    if first_visit:
        show scientist happy at right with dissolve

        show robot happy at left with dissolve

        per.player_name "I think you’re right Doctor, we need to keep moving before anything else out of the ordinary finds us sitting around."
        per.player_name "MUS-L, if we have time I’m sure we’ll be able to make our way back to the source of the water."

        r "I will keep my hope modules at a reasonable expectation, Captain."

        s "I think this is going to be the start of a potential way inside the forest, Captain. Let’s go through here!"
        hide scientist with dissolve

        hide robot with dissolve

        scene bg blank with dissolve

        "You make your way through the forest’s opening; the wetness in the air causing an immediate sense of a jungle seeping with moisture."
        "The dark violet earth crunches against the bottoms of your feet. The trees become thicker and denser as you pass over large roots and vines."
        "You walk like this for a while, MUS-L, and Dr. DeWitt occasionally commenting on the strangeness of this bizarre place you've found ourselves in."
        "You pass deeper into the forest."

        scene bg thicket with dissolve

        "The darkness oozes between the leaves, vines, and trees, turning a once bio-luminescent and warm cave into a dark, dense mass of strange plants."
        jump thicket_puzzle


## Screens ###################
### Waterfall ###
screen waterfall:
    imagemap: 
        idle "backgrounds/waterfall.png"
        hover "backgrounds/waterfall_highlight.png"

        hotspot(0, 101, 585, 573) action SetVariable("per.player_location", "forest"), Jump("location_manager")
        hotspot(1693, 171, 226, 413) action SetVariable("per.player_location", "thicket"), Jump("location_manager")