# Script for location manager and screens in-game
define first_visit = False
define thicket_visited = False
define water_source_visited = False

## Management ###################
label location_manager:
    if per.player_location == "waterfall":
        $ per.scientist_location = "Waterfall"
        $ per.robot_location = "Waterfall"
        jump waterfall

    elif per.player_location == "water_source":
        $ per.scientist_location = "Water Source"
        $ per.robot_location = "Water Source"
        jump water_source

    elif per.player_location == "thicket":
        $ per.scientist_location = "Thicket"
        $ per.robot_location = "Thicket"
        jump thicket

    if per.player_location == "device_testing":
        jump device_testing

label waterfall:
    $ per.player_location = "Waterfall"
    $ per.scientist_location = "Waterfall"
    $ per.robot_location = "Waterfall"
    scene bg waterfall with dissolve
    "Waterfall area."
    call screen waterfall

label water_source:
    $ per.player_location = "Water Source"
    $ per.scientist_location = "Water Source"
    $ per.robot_location = "Water Source"
    $ water_source_visited = True
    if first_visit == True:
        scene bg blank with dissolve
        "You pass by small clumps of trees that seem to have more large and flayed branches near the tops."
        "The ground becomes harder, more stable, and less wet as large inclines cause you to have to stretch and tug at cliffs and edges of landmasses in order to climb until suddenly..."
        "The solemn sound of running water begins to poke at the edges of your ears."

        "MUS-L beeps excitedly."
        r "I believe that we are arriving close to where the source of the water comes from. This should be an interesting discovery!"

        "You charge further ahead towards the sound; eyes peeled for any creatures and another potential discovery of life and uncertain of what you’ll find with your next couple steps."
        "As you begin to take the lead moving closer to the treeline, something massive lies up ahead. You step out into the open, bracing for something unknown."
        scene bg water_source with dissolve
        "Instead of the unknown, you find the largest tree you've seen in your life."
        "It extends for hundreds and hundreds of feet high; the top branches barely able to be seen as they strangely dig into the ceiling of the cave."
        "The trunk extends down with a purple-green tint to its wood and strangely...holes throughout its lower sides as water gushes from them like a fire hydrant."
        "A moat-like pool of water surrounds the base as it stands supported with massive vines upon a thin tower of rocks just large enough to hold the tree aloft."
        "The water  surround the tree like a wide base; however, the water does lead off of a cliff to your right."
        "You didn’t realize exactly how high you had climbed, but now looking out over the rest of the forest...you have a much better view of the size and scope of this place."
        "As you step out, the others join back with equally fascinated thoughts."

        per.player_name "(whistles)"
        per.player_name "Whew… well this is weird."
        per.player_name "Everything we’ve seen so far has been weird, but this might just take the proverbial weird cake."
        per.player_name "What do you think’s going on here?"

        show scientist shocked with dissolve
        s "I...I don’t know.."
        s "Looking at the structure from the outside, it’s hard to say where the water is coming from and why the tree appears to be so attached to everything."
        show scientist sad
        s "If we could get closer we might be able to get a better idea of what this means...but touching that water without knowing what it does seems a bit risky."
        hide scientist with dissolve

        show robot happy with dissolve
        r "Allow me to go, Captain."
        r "I can proceed towards the tree to complete my scans."
        r "Regardless of any damage, you can gather up my various parts and rebuild me later with my backup drives on the ship."

        per.player_name "I don’t know...it might be better if we’re all able to come with you for this one."
        per.player_name "I don’t like the idea of sending in any crew by themselves even if they can theoretically be assembled again."
        per.player_name "Let’s just see if we can get past these rocks to get an easier path to the tree. MUS-L, think you could give us a hand sorting this out?"

        "MUS-L beeps proudly."
        r "Yes Captain, although I am going to need some things to assist."
        r "Namely, a better set of hands. These drills are not are going to be effective for shoving, pushing, and pulling."

        per.player_name "Sure thing."
        per.player_name "Dr. DeWitt, if you could retrieve MUS-L's other limbs."

        hide robot with dissolve

        show scientist happy with dissolve
        s "Of course, Captain!"
        s "Let me just-"
        show scientist shocked
        s "Oh!"

        "You see a set of robotic hands slip out of Avery's hands."

        show scientist sad
        s "No no no..."
        s "I can't believe I just did that..."

        per.player_name "It's alright, Dr. DeWitt."
        per.player_name "It couldn't have gone far."
        per.player_name "If we just look carefully..."

        hide scientist with dissolve

        call screen water_source with dissolve

label thicket:
    $ per.player_location = "Thicket"
    $ per.scientist_location = "Thicket"
    $ per.robot_location = "Thicket"
    $ thicket_visited = True
    if first_visit:
        #show scientist happy at right with dissolve

        #show robot happy at left with dissolve

        #per.player_name "I think you’re right Doctor, we need to keep moving before anything else out of the ordinary finds us sitting around."
        #per.player_name "MUS-L, if we have time I’m sure we’ll be able to make our way back to the source of the water."

        #r "I will keep my hope modules at a reasonable expectation, Captain."

        #s "I think this is going to be the start of a potential way inside the forest, Captain. Let’s go through here!"
        #hide scientist with dissolve

        #hide robot with dissolve

        scene bg blank with dissolve

        "You make your way through the forest’s opening; the wetness in the air causing an immediate sense of a jungle seeping with moisture."
        "The dark violet earth crunches against the bottoms of your feet. The trees become thicker and denser as you pass over large roots and vines."
        "You walk like this for a while, MUS-L, and Dr. DeWitt occasionally commenting on the strangeness of this bizarre place you've found ourselves in."
        "You pass deeper into the forest."
        "The darkness oozes between the leaves, vines, and trees, turning a once bio-luminescent and warm cave into a dark, dense mass of strange plants."
        "Beeeeep. Beeeeeeep. Beeeeeeeeeeeep!"
        "The datapad rings out loud."

        s "We’re getting close, whatever is nearby has a high amount of the platelets and vegetative tissue like the trees by where we first came from."
        s "This data could be the key to unlocking a form of reliable organic food generation; breakthroughs for natural medicinal supplies!"

        "MUS-L walks past you; his eye beams start scanning the surrounding treeline for any potential life forms."
        r "There are currently no potential hostiles or new life forms being detected by my scans Captain."
        r "However, I do sense that the centralized structure here is different in its visuals than the cavern walls from earlier."

        scene bg thicket with dissolve

        "MUS-L’s flashlight eyes begin to turn on like a spotlight and gaze at a mass of stone and roots up ahead, his eyes revealing something we couldn’t see at first: the stonework was carved and decorated."
        "Purples, grays, blues, and reds faintly dot the stonework like an ancient cave painting. While it’s barely recognizable from the damage; it’s clear that someone...something was depicted on these destroyed ruins."

        per.player_name "I...I can barely believe what I’m seeing."
        per.player_name "Doctor, what do you make of this?"
        per.player_name ".....Doctor?"

        "You turn to Avery, but she just stands there in awe; processing the importance of this discovery."
        "After some quiet couple beats of silence, you begin to snap out of shock. Avery’s voice breaks the tension..."

        show scientist shocked with dissolve
        s "Captain… whatever this forest is, whatever it has done, it’s so much more than what anyone could have expected back home."
        s "We have to study it further; there’s so much we need to understand."
        hide scientist with dissolve

        per.player_name "I agree, although we still need to be careful as much as we can."
        per.player_name "We should gather the data that we came here first before diving into anything further."
        per.player_name "MUS-L, help Dr. DeWitt set up her supplies; I’m going to keep an eye out for anything living in that pile of rubble."

        show robot happy at left with dissolve
        r "Affirmative Captain."
        r "Dr. Dewitt, if you need any of my hands, feel free to take one."
        "MUS-L begins to remove one of his robotic metal arms. It slides off with little effort."
        
        show scientist sad at right with dissolve
        s "Oh, thank you MUS-L but...um...that won’t be necessary."
        s "In fact, could you just stand slightly over...here and begin gathering any of the vines together?"

        r "This is a directive that I can perform. I will begin gathering."
        
        hide robot with dissolve
        hide scientist with dissolve

        "You watch as Avery and MUS-L work together; the droid gathers the large spiny ropes of plant matter in large bundles under his forearms as Avery lifts the various vines up while she examines their undersides with the datapad."
        "After a few minutes, the doctor starts pulling out various small mechanical devices, attaching them to the vines along the earth."
        "The datapad flickers to life once more; this time performing functions to measure the strength, chemical makeup, and flexibility of the plant matter as well as several other facts of interest."

        jump thicket_puzzle


## Screens ###################
### Waterfall ###
screen waterfall:
    imagemap: 
        idle "backgrounds/waterfall.png"
        hover "backgrounds/waterfall_highlight.png"

        if not inv.datapad_opened:
            imagebutton:
                xalign 0.5 yalign 0.97
                idle "menus/expand.png"
                hover "menus/expand_highlight.png"
                action SetVariable("inv.datapad_opened", True), Show("datapad")

        hotspot(0, 101, 585, 573) action SetVariable("per.player_location", "water_source"), Jump("location_manager")
        hotspot(1693, 171, 226, 413) action SetVariable("per.player_location", "thicket"), Jump("location_manager")

screen water_source:
    imagebutton:
        focus_mask True
        idle "puzzles/hand.png"
        hover "puzzles/hand_hover.png"
        action SetVariable("inv.held_item", "MUS-L's hand"), Hide("water_source"), Jump("found_hand")

    if not inv.datapad_opened:
            imagebutton:
                xalign 0.5 yalign 0.97
                idle "menus/expand.png"
                hover "menus/expand_highlight.png"
                action SetVariable("inv.datapad_opened", True), Show("datapad")

screen water_source2:
    if not inv.datapad_opened:
        imagebutton:
            xalign 0.5 yalign 0.97
            idle "menus/expand.png"
            hover "menus/expand_highlight.png"
            action SetVariable("inv.datapad_opened", True), Show("datapad")

label found_hand:
    per.player_name "There it is!"

    "With some effort, you manage to grab the hand out of the water."

    per.player_name "Now to install it onto MUS-L..."
    $ inv.datapad_opened = True
    call screen datapad with dissolve