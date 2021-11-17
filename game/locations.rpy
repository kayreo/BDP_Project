# Script for location manager and screens in-game
define first_visit = False
define thicket_visited = False
define water_source_visited = False

define go_with_s = False
define go_with_r = False

## Management ###################
label location_manager:
    if per.player_location == "waterfall":
        $ per.update_location("scientist", "Waterfall")
        $ per.update_location("robot", "Waterfall")
        jump waterfall

    elif per.player_location == "water_source":
        $ per.update_location("scientist", "Water Source")
        $ per.update_location("robot", "Water Source")
        jump water_source

    elif per.player_location == "thicket":
        $ per.update_location("scientist", "Thicket")
        $ per.update_location("Robot", "Thicket")
        jump thicket

    if per.player_location == "device_testing":
        jump device_testing

label waterfall:
    $ per.player_location = "Waterfall"
    $ per.update_location("scientist", "Waterfall")
    $ per.update_location("robot", "Waterfall")
    scene bg waterfall with dissolve

    call screen waterfall

label water_source:
    $ per.player_location = "Water Source"
    $ per.scientist_location = "Water Source"
    $ per.robot_location = "Water Source"
    $ water_source_visited = True
    if per.chapter_num == 2:
        if not thicket_visited:
            show scientist happy at right with dissolve

            show robot happy at left with dissolve

            per.player_name "I think you’re right MUS-L, if this water source has properties like what you’re talking about, then finding out more information on where it all comes from could be valuable to better our understanding...all of this."
            
            show scientist sad

            per.player_name "Dr. DeWitt, I’m sorry but I’m sure we’ll have time to further investigate the data in more detail later."

            show scientist sad2
            s "Oh...yeah, that’s fine I suppose."
            show scientist happy
            s "Maybe we can take some samples and they’ll have some correlation with the plants."

            r "I think this is going to be the start of a way towards the direction of the water flow, Captain. Let’s go through here!"
            
        scene bg blank with dissolve

        per.player_name "Wherever we’re going, it feels like it’s starting to get higher."
        per.player_name "Does anyone feel like it’s getting harder to breathe?"

        r "While I am physically unable to breathe, we have been increasing in elevation levels since we left the bottom of the waterfall area."
        r "I can also confirm that the earth is becoming harder as we have been continuing climbing upward."

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

    if per.chapter_num == 3:
        if not thicket_visited:
            show robot happy at left with dissolve

            show scientist sad2 at right with dissolve

            per.player_name "Let's go back to the water source, first."

            show scientist sad
            s "But, Captain, my devices-"

            per.player_name "We'll go check your devices as soon as we're finished with the water source."

            show scientist sad2
            s "Fine..."

            hide robot with dissolve
            hide scientist with dissolve

            scene bg blank with dissolve

            "You travel in silence back to the water source..."

            scene bg water_source with dissolve

            "You and Avery watch as MUS-L carefully examines the surrounding area."
            "There is something...off about his behavior."
            "It almost looks like he's listening for something."
            "After an uneasy moment of silence, MUS-L turns to the two of you..."

            show robot happy with dissolve
            r "I’m sorry Captain, Dr. DeWitt, but I cannot leave at this moment."
            r "My...directive is enforcing protocol that I stay and further use tools and assessments to better understand the potential of what has transpired."
            r "Captain, as leader of the crew and with company privileges I cannot disobey you except for particular clauses such as this event."
            r "I urge you to stay and continue with the procedure I am following."
            
            per.player_name "MUS-L, you know we can't do that."
            per.player_name "There's too much we'd leave unexplored if we stayed here for too long."
            
            show robot at left with dissolve

            show scientist sad at right with dissolve
            s "[per.player_name] is right, MUS-L, we still have no idea what my devices found in the thicket."
            show scientist sad2
            s "Not to mention that area is much safer than...this place..."

            r "..."
            r "Very well."
            r "I will stay behind and investigate on my own."

            per.player_name "MUS-L..."
            per.player_name "Is there really no changing your mind about leaving?"

            r "Captain...I can’t."
            r "I must attempt to...discover exactly how this has affected me and what it must be in relation to the company’s protocols."
            r "It feels like I’m learning something new that I’ll forget if I leave again."

            show scientist sad
            s "If you feel like that’s what is best for you MUS-L, but...I- we’re both worried about you."
            s "You’ve been acting a lot stranger since we got down here; it’s like you’ve become more..."
            show scientist sad2
            s "alive."
            hide scientist with dissolve

            show robot at center with dissolve
            r "If I am to be alive, then I suppose there must be a reason for what has happened to have happened."
            
            per.player_name "I wish we could spend more time finding out what that is MUS-L, but it's also company protocol that we prioritize the mission above all else."
            per.player_name "If the only reason we're here is for personal reasons, then we've stayed long enough."
            per.player_name "Besides, we can’t just leave you behind. You're coming back with us."

            "As you lean forward, MUS-L’s large metal arms reach out and grab yours; squeezing with a force you’ve never felt lay on your body before."
            "MUS-L has never laid a finger on any of you before."
            "The pain shocks you to your core."

            per.player_name "Agh! MUS-L, you’re hurting me! Let go, please!"

            "MUS-L beeps in distress."
            r "Captain...I’m sorry."

            "MUS-L lets go of you, leaving a large red and purple mark shaped like his hand on your skin."

            r "Captain...Doctor...I urge you to not interfere with what I’m feeling and what I’m doing."
            show robot at left with dissolve

            show scientist shocked at right with dissolve
            s "Captain!"
            show scientist angry
            s "MUS-L, what’s going on? Why are you acting like this!?"
            s "Has this thing made you completely lose it?!"
            show scientist sad

            "MUS-L beeps quietly."
            r "I believe that what...I’m doing...what has been done...is an order that I cannot override."
            r "To better understand this forest and what it’s capable of is my mission. Its importance cannot be changed."

            show scientist angry
            s "Listen to yourself, MUS-L! This thing has clearly done something to you and it’s not going to stop!"

            per.player_name "MUS-L, I don’t want to have to do this, but I’m ordering you to come back with us. Please."

            "MUS-L doesn't move."

            s "Come on Captain, there’s nothing more we can do for him."
            s "If he wants to stay, then I say let him. He’s still just a machine after all."
            hide scientist with dissolve

            show robot at center with dissolve
            "MUS-L beeps solemnly."
            r "Captain....I hope for your safe return back to the crew."
            r "I will return; one way or another."

            "..."
            "You feel like you should say something to MUS-L..."
            menu:
                "Respond resolutely":
                    per.player_name "MUS-L...whatever happens, just know that no matter what happens you can come back."
                    per.player_name "What we want right now is for you to be safe."
                    per.player_name "...Be careful."

                "Respond bitterly":
                    per.player_name "We’ll be fine."
                    per.player_name "Just...do whatever you’ve been ordered to do."

                "Say nothing":
                    "But there is nothing left to say."

            hide robot with dissolve
            scene bg blank with dissolve

            "You stumble down the steppe in silence; unsure of exactly what happened to your crewmate."
            "Only after breaking past the clearing does Avery speak."
            scene bg waterfall with dissolve

            show scientist sad with dissolve
            s "You know...MUS-L doesn’t have any control over what he's doing."
            show scientist sad2
            s "At least...I think he doesn’t."
            s "The corporation never really told us much about how his model is made or designed, but...from when they gave him to us he’s never pulled anything like that before."
            show scientist sad
            s "Do you think he really did see something, somehow?"

            per.player_name "I don’t know...everything about what’s happening is just making me feel like coming out here and taking this mission was a mistake."
            per.player_name "I just can’t put my finger on why yet."

            s "Well...whatever happens moving forward, we’ll figure it out together."
            s "All three of us; even if we may not agree on how to figure it out."

            scene bg blank with dissolve

            "Following the path back through the brush you travel through the dense foliage once more; your feet aching and sore from what could be hours or even days of traveling. Trying to measure distance and time here feels like it’s moving slower and faster at the same time."
            "You finish off the remaining food you carried as you eventually reach the familiar structure once more."

            scene bg thicket with dissolve


            "The devices Dr. DeWitt left on the foliage and vines near the outskirts of the rubble flash a familiar color, signaling they’ve completed their scans."
            "Avery moves towards them excitedly; you can see that even through the immense weight of the unknown around you, her thirst for knowledge knows no bounds."

            show scientist happy with dissolve
            "This is it, Captain! I finally have the molecular structure of the plants as well as more in-depth readings!"
            "It appears that the plant matter’s elemental makeup is similar to that of rubber or aluminum, leading to both very malleable and strong fibrous cells."
            show scientist sad2
            "...Hm."

            "Avery stops for a moment; adjusting her datapad and falling silent before staring intently at the datapad and the other devices."

            per.player_name "Avery, what else are you able to make out?"
            per.player_name "...Avery?"

            show scientist sad
            s "This...forest is alive just like we thought; but it’s connected somehow."
            show scientist sad2
            s "The cells are...moving constantly, like writhing snakes. They're able to disconnect and attach themselves to one another like how a stem cell can form its shape to match and replicate other cells."
            s "This place...it has this appearance for a reason, but with enough focus the vines and trees could bend and shift if they wanted to...But that would mean this place is capable of so much more…"

            per.player_name "Okay...so you’re saying it’s alive {i}and{/i} it has done what exactly? Has it been holding back being able to do something to us...does it even know we’re here?"

            show scientist sad
            s "I...I don’t know, but whatever this place is it certainly could qualify under the corporations clause on finding sentient life."
            s "In order to know for sure though, I feel like whatever’s over there might have some answers."

            "Avery points towards the ruined and tumbled structures ahead."

            per.player_name "...Look, as long as we promise each other to stick together...{i}and{/i} we’re careful...{i}and{/i} we don’t do anything stupid...then let’s try and figure things out."
            
            show scientist happy
            s "Lead the way, Captain!"

            hide scientist with dissolve

            "Stepping over the vines and mounds of roots, you step slowly and carefully towards the ruins."
            "As you begin to approach, a sickening fear begins to fill the pit in your chest and throat."
            "The feeling of fear that an animal in the wilderness feels when being hunted...no other way of describing the immense feeling of being watched could fill your mind."
            "Avery felt it too; her eyes went wide with this sudden pressure as you approached. But you press on…"

            per.player_name "Whatever you do...be as quiet and slow as you can."

            scene bg blank with dissolve

            "Avery nods as you continue; silent step followed by silent step."
            "Getting closer to the ruins, you see now that the building’s previous design and decor has been violently sundered and nearly all of the once-near recognizable art has faded with time."
            "You get closer, the mound of vine and root now closer suddenly seeing it gyrate slowly; like it was breathing."
            "You are so close now that the smell of something...rotten begins to take notice in the air. You try to get even closer and peek further in; your head maybe two or three feet from this wound up mass."
            "Inside...the remains of something once alive but now turned into new life. Fungus-like balls of spores and purple and red flowers rest over the bones and bodies of things once living." 
            "As you lead in further and turn back to warn Avery to move back, you hear the doctor wince in pain."
            "You look down as you see her foot start to bleed on the smallest spine of a vine."
            "You reach out to help, but before you know it…"
            "A clicking...then a hiss."
            "A small flower lined with serrated teeth lunges from the mound and leaps at Avery."
            "You go to shove her out of the way, but before you can reach her it whips around you."
            "After a loud {i}crunch{/i} Avery begins to cry out..."

            s "MY ARM! M-MY ARM!"
            $ per.player_location = "Waterfall"
            $ per.update_location("scientist", "Waterfall")
            $ per.update_health("scientist", "Injured")
            $ per.update_health("robot", "Unknown")

            "Avery falls to the ground and wails. You rush to carry her away as fast as you can run."
            "You turn back...but whatever came for her had disappeared back into the mound."

            scene bg waterfall with dissolve

            "Your journey back was shockingly brief. You would have questioned how you travelled such a vast distance in mere minutes if Avery wasn't unconscious in your arms."
            "You struggle to bandage the wound with what little supplies you have left, but deep down you know she'll quickly succumb to her injuries without proper medical care."
            "Desperately, you look around the cavern. Something had scattered your supplies around the area, throwing most of it into the water..."
            "If there's no medical tech left...maybe some leftover equipment could work? Some of MUS-L's spare parts might still be lying around."
            "You take a deep breath and survey the area..."
            $ puz.puz_tag = "Arms"

            call screen collect_arms with dissolve


label thicket:
    $ per.player_location = "Thicket"
    $ per.scientist_location = "Thicket"
    $ per.robot_location = "Thicket"
    $ thicket_visited = True
    if per.chapter_num == 2:
        if not water_source_visited:
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

    if per.chapter_num == 3:
        "You can't go there just yet..."
        $ thicket_visited = False
        jump waterfall


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