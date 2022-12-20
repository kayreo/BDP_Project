# The script of the game goes in this file.
define persistent.game_completed = False

# The game starts here.
label start:
    stop music fadeout 3.0
    $ snd = Sound_mng()
    $ inv = Inventory()
    $ puz = Puzzle_manager()
    $ per = Personnel("no name")
    $ per.player_location = "Waterfall"
    if persistent.game_completed:
        "Welcome!"
        "Please select which chapter you would like to start on."
        menu:
            "Chapter 1":
                jump chapter_1

            "Chapter 2":
                "Before you begin chapter 2, please enter your name."
                python:
                    name = renpy.input("Please enter your name", length=10)
                    name = name.strip()
                    name = name.capitalize()     
                    if not name:
                        name = "No name"
                $ per = Personnel(name)
                define y2 = Character("[per.player_name]", color="#ffffff")
                $ per.chapter_num = 2
                "Is [name] correct?"
                menu:
                    "Yes":
                        $ per.player_location = "Waterfall"
                        $ per.scientist_location = "Waterfall"
                        $ per.robot_location = "Waterfall"
                        jump chapter_2
                    "No":
                        jump start

            "Chapter 3":
                "Before you begin chapter 3, please enter your name."
                python:
                    name = renpy.input("Please enter your name", length=10)
                    name = name.strip()
                    name = name.capitalize()      
                    if not name:
                        name = "No name"
                $ per = Personnel(name)
                define y2 = Character("[per.player_nam]", color="#ffffff")
                $ per.chapter_num = 3
                "Is [name] correct?"
                menu:
                    "Yes":
                        $ per.player_location = "Waterfall"
                        $ per.scientist_location = "Waterfall"
                        $ per.robot_location = "Waterfall"
                        jump chapter_3
                    "No":
                        jump start

            "Chapter 4":
                "Before you begin chapter 4, please enter your name."
                python:
                    name = renpy.input("Please enter your name", length=10)
                    name = name.strip()
                    name = name.capitalize()      
                    if not name:
                        name = "No name"
                $ per = Personnel(name)
                define y2 = Character("[per.player_nam]", color="#ffffff")
                $ per.chapter_num = 3
                "Is [name] correct?"
                menu:
                    "Yes":
                        "Who would you like to start with?"
                        menu:
                            "Avery":
                                $ per.player_location = "waterfall"
                                jump chapter_4
                            "MUS-L":
                                $ per.player_location = "water_source"
                                jump chapter_4
                    "No":
                        jump start
    else:
        jump chapter_1

       # "Test room":
        #    "Enter name"
         #   python:
          #      name = renpy.input("Please enter your name", length=10)
           #     name = name.strip()
            #    name = name.capitalize()      
             #   if not name:
              #      name = "No name"
            #$ per = Personnel(name)
            #$ per.chapter_num = 3
            #"Is [name] correct?"
            #menu:
             #   "Yes":
              #      jump test_room
               # "No":
                #    jump start

label chapter_1:
    $ inv = Inventory()
    $ puz = Puzzle_manager()
    scene bg blank

    "(wrrrrr) (wrrrr) (wrrrr)"

    play sound "audio/other/Construction.wav"

    "The sounds of rocks break and chip against a large metal drill, dropping somewhere into the pool of darkness below."
    "A crew of three humanoid individuals stare out into a massive darkened cavern; their eyes slowly adjusting to the shadowed chamber."
    "A warm and sweet breeze blows lightly against the figures. The air feels humid and damp."
    "The silhouetted individual in the front leans further out into the dark, searching for any sign of light."
    "They lean even further before saying something to their companions."
    
    stop sound fadeout 2.0

    play sound "audio/other/Splash.wav"
    "As they turn, they lose their footing, slipping down onto the rocks and quickly falling, falling, falling, until!"

    "(SPLASH)"

    s_unknown "Captain!"
    s_unknown "Quick, help me pull the captain out! We don’t even know if this is normal water!"

    r_unknown "I agree, this water is too abnormally saturated to be considered normal."
    r_unknown "The captain will need a full scan to determine any injuries or changes in bodily structure."

    stop sound fadeout 2.0

    "..."
    "..."
    "You slowly regain your senses..."

    scene bg waterfall with dissolve
    $ snd.play_bg(per.player_location)
    "The water shines with a vibrant, almost neon blue against the purple stone walls."
    "The trees give a slight glow and hum like fireflies and illuminate the surrounding cavern and grassy gnoll."

    show scientist shocked with dissolve
    s_unknown "Oh thank goodness!"
    s_unknown "MUS-L you run diagnostics and I’ll make sure the captain didn’t suffer any memory loss."

    "You...remember this person. Her name is Dr. Avery DeWitt and she is a part of your crew. She’s your chief scientist and medical expert."

    show scientist sad at right with dissolve
    show robot happy with dissolve
    r "Running diagnostics now...this may take a while, Dr.DeWitt." 
    r "I will deploy temporary guard mode until the diagnostics check is complete."

    "MUS-L begins to emit a blue wave of light that starts scanning you while he turns to face the strange forest."

    "You remember him too thankfully. It’s MUS-L, your personal Manual Unconditional Service Loader."
    "He’s the bot sent by AstroCorp to assist in the mining and protection of the crew."

    show robot at left with dissolve

    p "Dr. DeWitt, MUS-L, I feel fine."
    p "Probably just gave me a bad bruise is all."

    r "Diagnostics complete. The captain is correct. Only minor injuries were sustained."
    r "Life support systems are fully functioning. Glad to see you’re not terminated."
    
    s "Oh MUS-L, we talked about this!" 
    s "Avoid using that word whenever something bad like this happens. It can be insensitive."

    play sound "<from 2.7>audio/musl/Sad_beep.wav"
    "MUS-L beeps sadly."
    r "I...apologize. I will categorize this information in my deep storage memory banks to permanently retain this for later."
    r "I told myself to be better than this."

    p "Oh, relax. Nothing bad happened and you were doing as you were directed. You have no reason to feel down."
    p "Okay, so what’s the situation? Give me a rundown of everything we know."

    hide robot happy with dissolve

    show scientist happy at center with dissolve
    s "Yes, Captain, currently not much has changed from our standard mission."
    s "Our job from AstroCorp was to investigate and assist in the terraforming process for planet X.B-2513 in the Hollow Mire system."
    show scientist sad
    s "We arrived approximately 12 hours ago. AstroCorp told us that other drilling operations and machinery have been damaged by plant roots from underground."
    s "Only the three of us were sent to investigate. The rest of the remaining personnel wait aboard our ship ready to assist in getting us away, should our lives be in danger."
    s "We have gone down through the previous holes left by the machines to continue digging with small equipment and now..."
    show scientist sad2
    s "We’ve brought you back from falling through the hole {i}we{/i} just fell through."

    p "I see."
    p "Are you two alright? We can’t continue investigating...whatever this weird forest is unless you two are ready to get moving."

    show scientist at right

    show robot happy at left with dissolve
    r "I have sustained no serious injuries, Captain."

    show scientist sad
    s "I'm fine as well, just a little nervous about all of this." 
    s "It’s beautiful, but at the same time I can’t help but feel like we’re in a bit of a bind."

    p "Well, for now, let’s just focus on what we can control."
    p "MUS-L, the water that you mentioned before. Scan it, I wanna know if that glow is just for show." 
    p "Dr. DeWitt, plan on getting soil and samples of nearby trees for analysis. We can use my-"
    p "Wait. Where’s my datapad?"

    hide robot with dissolve

    show scientist shocked at center
    s "Oh,  I almost forgot!"
    show scientist happy
    s "Captain, here you are; it fell off your belt on the way down."
    s "I’ll get started on the samples. We can use the pad to contact the ship."
    hide scientist with dissolve

    show robot happy with dissolve
    r "Roger Roger, Captain. I will report back with any updates regarding the contents of the water."
    hide robot with dissolve

    "The doctor quickly takes out various tools and scoops small piles of dirt, being careful to scrape off any of the plant matter from the roots."
    "MUS-L walks over to the waterfall and begins studying the glowing water."

    p "Alright, now I just need to pull up our holographic test kit and see what we can learn..."

    "The datapad screen pulls up asking for its passcode." 
    "You look fondly at the chips and dents in its casing. A great deal of use has gone into using this pad ever since it was given to you."

    $ puz.puz_tag = "Tutorial"
    call screen datapad_tutorial

label first_password_fail:
    p "..."
    p "Oh no..."
    p "No, no, no. Why the hell can’t I remember!?"
    p "We’re screwed if I can’t get this thing on."

    show scientist happy with dissolve
    s "Captain, I'm almost finished with-"
    show scientist sad
    s "Is something wrong?"

    p "Uh...well..."

    show scientist angry
    s "Wait, did you forget your password again!?"
    show scientist sad2
    s "I knew this was going to happen..."

    p "Look, as captain, I have a lot to keep track of!"
    p "Transfer files, mission reports, updating MUS-L's operating system..."
    p "Hold on."
    p "Doesn't MUS-L have a copy of the code somewhere?"

    show scientist angry
    s "I don't know, but you better figure out how to get that thing working!"
    show scientist sad2
    s "I didn't come all this way just to die in some hole..."
    hide scientist with dissolve

    p "MUS-L!"

    show robot happy with dissolve
    show screen password with dissolve
    r "Yes?"

    p "I think you might have something I need."

    r "If you are referring to the results of my scan, I am unfortunately not finished yet."

    p "No, something else actually."

    r "I do not understand your request. Please directly state what you require from me."

    p "...Well..."
    p "I...forgot the passcode to my datapad."
    
    r "I see."
    r "I believe that you once absentmindedly scrawled your passcode somewhere on my body."

    "MUS-L turns to show you countless scratches and crudely scribbled messages on his side."
    
    p "One of these has to be it..."

    "You desperately read whatever legible writing you can find."

    "After a moment you find a note stuck on MUS-L's torso."

    p "Maybe it's this...?"

    "{i}In the game, there are certain items you will be able to interact with.{/i}"
    "{i}If you ever get stuck during a puzzle, you can click on a help button that will appear in the upper left corner.{/i}"
    "{i}To continue, click on the note to enlarge it.{/i}"

    call screen click_password

label found_solution:
    hide screen password with dissolve

    p "That's it!"
    hide screen password_solution_1 with dissolve

    p "If I just enter this into the datapad..."

    hide robot with dissolve
    call screen datapad_tutorial

label second_password_fail:
    show robot happy with dissolve
    p "..."
    
    r "..."
    r "Perhaps your injuries are more severe than we first estimated."
    r "Are you experiencing a headache or any dizziness? Perhaps it would be best to not lose consciousness before we return to base."

    p "I-I'm fine!"
    p "Could I just see that code again?"

    r "Certainly."

    hide robot with dissolve
    play sound "<from 1.9 to 5>audio/ch1/Paper_rustle.wav"
    call screen password_solution with dissolve

label password_fail:
    show robot happy with dissolve
    p "..."
    p "Hey, MUS-L, you mind showing me one more time?"

    r "Yes, Captain."

    hide robot with dissolve
    play sound "<from 1.9 to 5>audio/ch1/Paper_rustle.wav"
    call screen password_solution with dissolve

label device_unlock:
    p "Got it!"
    "The datapad flickers to life."
    "{i}Now that your device is unlocked, you can enter your name.{/i}"
    call screen datapad_tutorial with dissolve

label name_entered:
    python:
        name = name.strip().capitalize()
    if name != "":
        $ inv.pickup_item("activation code")
        $ per = Personnel(name)
        define y2 = Character("[per.player_name]", color="#ffffff")
        y2 "There we go..."
        y2 "Now, let's see here..."

        $ inv.set_uninteractable()
        $ snd.open_inv()
        show screen datapad with dissolve

        "{i}Your datapad displays your currently held item and your team's location and wellbeing.{/i}"
        "{i}Throughout the game, you may need to use held items in order for the story to progress.{/i}"
        "{i}Click on the note you are currently holding.{/i}"
        $ inv.set_interactable()

        call screen datapad
        jump device_testing
    else:
        "You forgot to enter your name..."
        call screen datapad_tutorial with dissolve

label chap_1_end:
    y2 "Now we’re cooking! MUS-L, Doctor, you got anything you can give me about this place?"

    show scientist sad with dissolve
    s "Well, this specific plant type and soil structure are unlike anything I’ve ever seen in previous studies of other planets."
    s "The plant matter appears to..."
    show scientist sad2
    s "undulate..."
    show scientist sad
    s "when disturbed; the soil is full of rich nutrients that also cause rapid growth of the plant matter I’ve observed."

    y2 "Huh, I guess that makes this trip so far somewhat of a success and a failure."
    y2 "Great stuff to potentially grow grass and edible plants with, but being so far underground makes it not ideal."
    y2 "MUS-L, got anything on the water yet?"
    
    hide scientist with dissolve

    show robot happy with dissolve
    r "Affirmative Captain."
    r "My scans indicate that the water in this section is nearly entirely saturated with carbon dioxide as well as nitrogen, phosphorus, and potassium."
    r "The chemical makeup of the liquid could theoretically be produced by other plant life on current organic plant data at a .0001\% odds of success with enough roots and chloroplasts."

    show robot at left with dissolve
    
    show scientist sad at right with dissolve
    s "MUS-L, you can’t be serious."
    s "Even if it were possible that would mean that..."

    show scientist sad2

    "..."

    y2 "Doctor, MUS-L; what did you guys figure out?"
    y2 "We haven’t got all day to stand stunned."

    show scientist sad

    r "The only logical connection that can be formed with our understanding of the data is that the entire planet is one central organic life form."

    y2 "Are you saying we’re attempting to terraform a plant the size of a planet?!"

    s "I’m afraid so..."
    s "However, this would explain the damage done to the previous drilling machines."
    s "The plant is trying to protect some of its most dense areas that support its life."
    s "The fact that it can do that while being so massive is extremely troubling."

    r "Observing current data, however, this plant is thoroughly tied to everything here."
    r "With the soil and water it produces it could potentially be used as a resource for future operations."
    r "In addition to this, our drill was not blocked off."
    r "This data could be assumed to mean small team operations could be completed, albeit at a slower pace than originally estimated."

    y2 "I’m... not sure what will become of this operation, but as captain I am changing the objective of our mission."
    y2 "We need to learn more about... whatever this thing is, and fast, so we can figure out our next steps."

    show scientist happy
    s "I suggest, then, that we get moving towards this nearby thicket, Captain."
    s "It would lead more into the woodwork so we could further analyze any data on the vegetation and its rapid growth effects."
    show scientist sad
    s "Also... being out in this open space leaves me feeling rather exposed."

    r "Captain, if I may suggest an alternate route?"
    r "This water’s special properties must lead to some sort of source deeper in the area."
    play sound "<from 0.7>audio/musl/Happy_beep2.wav"
    "MUS-L boops excitedly."
    r "I also am interested in how this water could be potentially used to better our terraforming process on the surface."

    show scientist happy
    s "No matter which way we start; we’ll stick together Captain."
    s "I don’t think going at it alone is a great idea right now…"

    r "Affirmative. The potentiality of injuring one’s self when traversing an alien underground forest could be estimated near a startling percentile."

    y2 "Y-you have data on this from the corporation, MUS-L?"

    r "I was attempting to be humorous."
    r "Was it not funny?"

    show scientist sad
    s "It was certainly an... attempt MUS-L."
    hide scientist with dissolve

    hide robot with dissolve

    stop music fadeout 1.0

    show bg blank with dissolve

    "{i}This concludes Chapter 1.{/i}"
    "{i}Would you like to save the game?{/i}"
    menu:
        "Yes":
            call screen save with dissolve
            jump next_chapter
        "No":
            jump next_chapter

label chap_2_end:
    stop music fadeout 1.0
    scene bg blank with dissolve
    "{i}This concludes Chapter 2.{/i}"
    "{i}Would you like to save the game?{/i}"
    menu:
        "Yes":
            call screen save with dissolve
            jump next_chapter
        "No":
            jump next_chapter

label next_chapter:
    python:
        per.chapter_num += 1
        first_visit = True
        thicket_visited = False
        water_source_visited = False
        go_with_s = False
        go_with_r = False
        chapter_name = "chapter_" + str(per.chapter_num)
        puz.reset_tag()
        #inv.remove_item():
        if per.chapter_num != 4:
            per.player_location = "Waterfall"
            per.scientist_location = "Waterfall"
            per.robot_location = "Waterfall"
        renpy.jump(chapter_name)

label chapter_2:
    y2 "{i}Hmm, a potential water source, or a stronger and more localized area of the vegetation...{/i}"
    y2 "{i}Or, in simpler terms, left or right.{/i}"
    y2 "{i}We’ll most likely be able to get to both as long as nothing goes wrong, but which direction would be best to start..?{/i}"
    $ per.player_location == "waterfall"
    $ first_visit = True
    jump location_manager

label thicket_puzzle:
    $ puz.puz_tag = "Thicket1"
    show scientist happy with dissolve
    s "Captain!"

    "Avery hands you one of the scanners."

    s "Could you attach this one to that vine over there?"

    y2 "On it."

    s "Thank you, I-"
    show scientist shocked
    s "Oh, I almost forgot!"
    show scientist happy
    s "You'll need to calibrate the device."
    s "The air down here is exhibiting some strange abnormalities, so you may need to make some adjustments."

    "Dr. DeWitt gives you a quick, reassuring smile before disappearing behind a clump of vines."
    hide scientist with dissolve
    "You bring the scanner to a friendly-looking vine on the right and awkwardly attach it to one of its thicker portions."
    "With a slight hum, the small device clamps on; tiny beams of grid-patterned light moving up and down the spines of the vines."
    
    y2 "Now to calibrate it..."
    call screen thicket_activation with dissolve

label thicket_solved:
    y2 "Got it!"

    show scientist happy with dissolve
    s "Yes!"
    s "Okay okay okay, the last of the devices are calibrated now, Captain."
    s "It’s going to take a while for them to complete a full deconstruction of the plant matter, but after a couple hours or so we should have a molecular breakdown!"
    s "Now, let’s move on to the large one..."
    hide scientist with dissolve

    show robot happy with dissolve

    if not water_source_visited:
        r "Excuse me, Captain?"
        r "I believe that now could be a more optimal time to further investigate the unnatural water from earlier."
        r "If we must wait, it would be a better function of our time to understand more of this location."

    else:
        r "Captain, I believe we should return to the main cavern."
        r "These scanners will take some time to fully gather sufficient data."
        r "If we must wait, it would be a better function of our time to understand more of this location."

    show robot at left with dissolve

    show scientist sad at right with dissolve
    s "But...we’re so close to uncovering something so incredible!"

    y2 "This is certainly an incredible find...but MUS-L is right."
    show scientist sad2
    y2 "This information is gonna have to wait until we have a better understanding of everything in this place itself."

    "Avery stands dumbfounded at your words; her eyes jump between her probes and devices, the large, collapsed, enveloped, structure, and back to you."
    "After a few beats of silence, she says..."

    show scientist angry
    s "If this isn’t still here by the time we get back, then I swear to both of you my research won’t be the only thing that is incomplete! Hmph!"
    hide scientist with dissolve

    play sound "audio/other/Avery_stomping.wav"
    "Avery marches off back down the path you came and through the dense jungle. You and MUS-L stand there in stunned silence."

    show robot at center with dissolve
    r "The mind of a scientist; it’s a hard thing for her to hold back her instincts."
    r "I hope she will not terminate me for my previous recommendation."

    if not water_source_visited:
        r "I am just...drawn to whatever could be at the source."

    y2 "It’s alright. If Avery- Dr. DeWitt should be angry at anyone, it's me."
    y2 "I’m sure she’ll be okay though; she’s a lot harder to crack than she gives herself credit for."

    r "Affirmative!"

    stop music fadeout 1.0
    scene bg blank with dissolve
    $ snd.play_entering_thicket()

    "MUS-L nods his head as you start our trek back through the wet jungle."
    "A short walk later, you’re able to meet up with Avery, although she isn’t exactly in the speaking mood."
    "You continue to go back through the entrance you found and start hiking up through more rocky terrain."

    $ per.player_location = "Waterfall"
    $ snd.play_bg(per.player_location)
    scene bg waterfall with dissolve

    if not water_source_visited:
        y2 "Now that that's out of the way, we should go check out the source of that water..."
        $ per.player_location = "water_source"
        jump location_manager

    else:
        jump chap_2_end

label water_source_puzzle:
    $ puz = Puzzle_manager()
    $ puz.puz_tag = "Water1"
    "Now to move those rocks..."
    $ puz.populate_map()
    hide robot with dissolve
    call screen water_source_controls with dissolve

label water_source_solved:
    "MUS-L’s large form strains against the rocks as you prepare to quickly move across the newly opened pathway to the tree."
    play sound "audio/other/Splash.wav"
    "He lunges upon the rocks with a sharp sound of squeaking metal; the rocks begin to break apart, loosening until they eventually find the flow of water that leads off the cliff face."
    "The rocks tumble and bob up and down in the water as they eventually slide off the edge of the cliff, crashing into the earth below."

    show scientist happy with dissolve
    s "Great job MUS-L!"
    show scientist sad
    s "Are you okay? No circuits and parts not damaged from the water or anything?"
    show scientist at right with dissolve

    show robot happy at left with dissolve
    r "Running diagnostic scan...my systems to appear to be undamaged but something...strange is occurring with a nearby signal that’s close by."
    r "It’s strong and coming from...there."

    "MUS-L points his large metal hands and turns to face the tree."

    y2 "MUS-L, what do you mean a signal? And are you certain that it’s coming from the tree?"

    r "I’m sure Captain; my sensors are reading some sort of frequency and...I feel as if it’s trying to...communica-"

    play sound "audio/musl/Weird_beeps.wav"
    "MUS-L suddenly jerks his arms up and begins emitting loud noises from his vocal outputs."
    "He begins to move erratically, lifting himself out of the water and moving quickly across the now cleared path."
    hide robot with dissolve

    y2 "Ah no no no no, Avery we need to stop whatever’s happening right now!"

    show scientist shocked
    s "Yes Captain!"

    hide robot with dissolve
    hide scientist with dissolve

    "You race past the rocky waters; understanding that whatever has happened to MUS-L could endanger not only himself but also risk your chances of all of you getting out of here alive and safe."
    "Climbing on the rocky path, you follow after MUS-L as he rolls ahead of you."
    "Before you’re able to catch up, MUS-L’s arms dig into the mound of dirt and roots and start climbing up, digging his claws into the earth as he starts moving upward."

    show robot happy with dissolve
    r "Captain, this signal...I do not understand it’s capability to direct me."
    r "All I...feel is that I must go further towards this tree."
    hide robot with dissolve

    "He climbs higher and higher before reaching the top just as you reach the base of the mound of roots and dirt."

    show scientist shocked with dissolve
    s "Captain, I’ll give you a boost. Just catch up with him and hurry!"
    hide scientist with dissolve

    "With the help of Dr.DeWitt, you grip the earth and with a running leap heave your body onto the massive structure the tree sits on."
    "Standing there, the tree is even more massive and imposing up close; the massive holes where water pours out on all sides pumping the shining fluorescent liquid down the rocks and off the cliff's edge."
    "Looking straight ahead, MUS-L stands still in front of the largest hole. By his feet the roots are slowly swirling and rising around him."

    y2 "MUS-L, look out!"

    "You run towards your metal companion."
    play sound "audio/ch2/Root_slither.wav"
    "As you wrap your arms around him and pull away, the roots start to snake towards your feet before stopping just on the edge of the mound of rocks, dirt, and roots you stand on."

    y2 "MUS-L!"
    
    "You shake him; his central light flashing over his head."
    "Screens read out error codes as you attempt to understand what happened to him."
    "The error codes all flash off and the still metal husk of MUS-L for a moment locks in place..."
    "Suddenly, central eye flashes once more with a familiar yellow-blue light."

    show robot happy with dissolve
    r "Captain...I do not understand what has just transpired."
    stop sound fadeout 2.0
    r "Is everything functioning normally?"

    play sound "<from 0.3>audio/ch2/Phew.wav"
    "A sigh of relief passes from your lips."

    y2 "MUS-L, we need to talk right now."
    y2 "Come on down; Avery is probably worried sick about us."

    hide robot with dissolve

    show scientist angry with dissolve
    s "You’re damn right I am! What the hell happened to you MUS-L?"
    hide scientist with dissolve

    "As you climb down, MUS-L explains how his vision went dark after pushing the rocks, how he saw the colossal tree reach out to him through its roots, and the images that he saw while frozen."

    show robot happy at left with dissolve
    r "The only logical summary I can surmise from this encounter is that the forest was attempting to communicate somehow."
    r "I do not understand it’s reasoning; but in line with company policy in possible engagement of alien life forms with intelligence we must first ascertain its level of danger through further contact."

    show scientist angry at right with dissolve
    s "Woah, woah, woah. Forget the company for a second MUS-L; you almost lost yourself trying to investigate this tree and now you wanna go {i}back{/i}?"
    show scientist sad
    if not thicket_visited:
        s "We still need to find out about the ruins back in the denser areas of the tree."
    s "Captain, what MUS-L is saying is important, but the fact that more lifeforms could have been here {i}and{/i} now knowing what this forest is capable of is more than enough reason to go back and focus on what we’ve found."
    if thicket_visited:
        s "My devices in the thicket finished up a little while ago so we’re clear to go back now."
    show scientist sad2
    s "Please..."

    r "But-"

    show scientist angry
    s "We've looked around enough here!"
        
    y2 "I think Avery is right."
    y2 "It's not safe for any of us to be around that water until we better analyze it."
    y2 "We'll leave some scanners around and come back later, okay?"

    r "..."
    r "Alright."

    stop music fadeout 1.0
    scene bg blank with dissolve

    "You slowly return the way you had come until you arrive back in the main cavern."

    $ per.player_location = "Waterfall"
    $ snd.play_bg(per.player_location)
    scene bg waterfall with dissolve

    if not thicket_visited:
        y2 "And now to investigate the thicket..."
        $ per.player_location = "thicket"
        jump location_manager

    else:
        jump chap_2_end

label chapter_3:
    "As you return to the main cavern, the air is thick with tension."
    "Both Avery and MUS-L seem lost in their own worlds. You catch the two of them restlessly glancing at each other."

    y2 "{i}Avery's devices in the thicket should be nearly done calibrating by now, but MUS-L still needs to go back to the water source for more analysis..."
    y2 "{i}Which should I direct us to first..?{/i}"

    jump location_manager

label arm_success:    
    $ inv.held_item = None
    $ go_with_s = True
    "As you prepare and give Avery the pills, you unwrap the bandages and pour the nanobots over her stumped arm. They begin to swarm and take shape."
    "Avery lies there; blood covering her body as a mass of black moving mite-like mass begins to radiate heat. The arm throbbing with blood begins to calm and cool as the bots stitch metal and wiring into place."
    "Sitting there watching the body, darkness begins to fall over you as you look down and feel exhaustion overtake you."

    stop music fadeout 1.0

    scene bg blank with dissolve

    "..."
    "..."

    $ snd.play_bg(per.player_location)

    scene bg waterfall with dissolve

    show scientist sadB with dissolve
    s "What...what happened?"

    "Avery's voice jolts you awake."

    y2 "Oh, thank goodness!"
    y2 "There was an accident; you got injured..."

    show scientist sad2B
    s "..."

    y2 "..."

    if not go_with_r:
        y2 "Just try to get some rest for now."

        s "I wonder... MUS-L..."

        y2 "I'll go look for him."
        y2 "You stay put, alright?"

        stop music fadeout 1.0
        hide scientist with dissolve

        scene bg blank with dissolve
        $ per.player_location = "Water Source"
        jump water_source

    else:
        y2 "Let's... let's just rest for now."

        jump chap_3_end

label sound_success:
    $ go_with_r = True
    play sound "audio/ch3/Earthshake.wav"
    "With a pleasant sounding call, the earth trembles and shakes. The roots and vines around you glow even brighter than before, the reds and purples shining brilliantly while water begins to steadily slow down."
    stop sound fadeout 4.0
    "As the torrent slows, the mouths of the tree begin to drastically extend and snap open; the darkness inside revealing some sort of chute leading underground with...something small and bright at the bottom."

    show robot happy with dissolve
    play sound "<from 0.7>audio/musl/Happy_beep2.wav"
    r "Captain, you’re the first human to communicate with alien life. Congratulations!"

    y2 "That currently doesn’t feel like that great of an achievement MUS-L."
    y2 "What exactly did they hear and is that...thing down there where the source of the signals have been coming from?"

    r "I’m not entirely sure...all I know is that they are happy with what you said to them. Should we continue forward?"

    y2 "Yeah...just bust out that light for me will you?"

    r "Certainly Captain."

    hide robot with dissolve

    scene bg blank with dissolve

    $ renpy.music.set_volume(0.4, 0.2, 'music')

    "You carefully lower yourself down until reaching the wet and damp interior of this cavernous tree."
    "The walls and floors are the same hard and dense, dark, wood as the bark but are covered with moss and vines. The only light that helps us navigate is MUS-L’s headlamp and the dim glows from the outside."
    "You step forward and forward, closer and closer, until you see what awaits at the end…a plant nearly the same size as a datapad or MUS-L’s head."
    "It’s covered in various small bussing flowers; but, it appears that some sides of it show it dying and covered in dark black dead leaves and dry dirt."
    "A warmth emanates from it out through you as you stand in awe."

    y2 "This is definitely unlike anything we’ve seen so far...MUS-L, can you scan it?"

    r "Yes Captain...I can confirm that this is the signal’s source; whatever was reaching out and heard the sounds."
    r "It...it’s what I remember seeing in the vision."

    "MUS-L’s hand goes to reach for the plant and before you can tell him…"

    y2 "No, MUS-L wait!"

    play sound "audio/ch3/Wrapping.wav"

    "The plant’s vines and roots wrap around his arm and begin to glow so intense it nearly blinds you."
    "You step back momentarily stunned by the light as you look over to MUS-L. The plant begins to climb and twist; wrapping itself over and around him before stopping near him head."

    y2 "MUS-L, help me get it off of you!"

    r "No Captain wait, please! Stay away, whatever it is just let it happen before accidentally hurting yourself!"

    "The light begins to slightly dim as bright reds and purples fill the room."
    "The vines further snake along their metal form as the tops of the plant dig roots into MUS-L's head with a loud sizzle." 
    "His lights go out as whatever attached itself to MUS-L, for now, has disabled him."

    y2 "MUS-L! NO!"

    "You reach out and swat the plant away and as you grab with both your hands around its vines your eyes go white!"
    "You see images and pictures of a small plant; growing, and growing, and growing, under a moonlit sky."
    "A massive red and purple jungle with strange-looking figures covered in plant-made robes wielding massive wooden tools and weapons."
    "Trees and bushes provide large foods while several of the figures take people and throw them into a massive flower."
    "Its red and purple budding leaves are hundreds of feet long and as someone gets thrown into the center the rest of the figures leave and continue grazing and hunting the spoils of the jungle."
    "Next, a massive bright light crashes as my body shakes and burns."
    stop sound fadeout 2.0
    stop music fadeout 2.0
    "The jungle gone and wiped out, the surface of the planet dead and gone."
    "Darkness, then...you wake up to the sound of a familiar voice…"

    r "Captain...wake up. Open your eyes…"
    $ renpy.music.set_volume(1.0, 0, 'music')
    scene bg blank with dissolve

    "..."
    "..."

    if not go_with_s:
        scene bg water_source with dissolve
    
        $ snd.play_bg(per.player_location)

        show robot happyB with dissolve
    
        y2 "...MUS-L?"

        "The sight of MUS-L startles you awake."

        r "It's alright, Captain."
        r "I am unharmed."

        y2 "..."
        y2 "I-I see..."

        r "This discovery is something remarkable."
        r "Dr. DeWitt should be informed of this immediately."
        r "However...I must remain here for now."

        y2 "I'll go look for her."
        y2 "You be careful now, okay?"

        r "Yes, Captain."

        hide robot with dissolve

        scene bg blank with dissolve

        jump thicket

    else:
        #y2 "..."
        #y2 "We should head back now."
        #y2 "Avery... she's been injured."

        #r "..."
        #r "I cannot leave, Captain."
        #r "Not yet."
        #r "But..."
        #r "Please ensure Dr. DeWitt's safety."

        #y2 "I will."
        #y2 "You be careful now, okay?"

        #r "Yes, Captain."

        $ per.player_location = "water_source"
        jump chap_3_end

label chap_3_end:
    $ per.update_location("scientist", "Waterfall")
    $ per.update_location("robot", "Water Source")
    stop music fadeout 1.0
    scene bg blank with dissolve
    "{i}This concludes Chapter 3.{/i}"
    "{i}Would you like to save the game?{/i}"
    menu:
        "Yes":
            call screen save with dissolve
            jump next_chapter
        "No":
            jump next_chapter


label chapter_4:
    if per.player_location.lower() == "waterfall":
        $ go_with_s = True
        $ snd.play_bg(per.player_location)
        scene bg waterfall with dissolve

        "You jump out of rest when an intense cold feeling coats your face."
        
        play sound "audio/ch4/Waterdump.wav"

        "Your eyes fly open to the feeling of water pouring over you; immediately causing your body to become hype-aware and alert as you come to."
        
        y2 "AHHHH THAT’S COLD! What the hell-"

        "But before you can finish...you realize that it’s Avery."
        "Her clothes are tattered and torn with various ripped leaves and vines acting as bandages to cuts and bruises. Her face looks slightly thinner than last time you can remember and her arm...it’s turned into a complete metal replica."
        "It has a dull black sheen to it with tiny wiring inlaid deep inside. The metal and plastic plates shape the arm to fit attached to her shoulder like it was carefully molded with the design of the wound in mind."
        "Her hand is even more intricate...petitely shaped fingers made out of black and great metal alloys are finely connected and wired to her hand."
        "She clenches her fist and you can see how fluently the arm and hand move; like she’s always had this new appendage."
        "You realize slightly too late that you could have been staring and immediately wonder what she’s had to do since you’ve been out…"

        show scientist sadB with dissolve

        y2 "Avery...I’m really glad to see you up and about...what happened?"

        "She stands silent for a moment and you wonder then if she’s had more trouble taking care of you or taking care of herself."

        s "It’s…"
        
        show scientist sad2B

        play sound "<from 0.2>audio/ch4/Avery_sigh.wav"

        "Avery sighs."

        show scientist sadB
        
        s "...there’s a lot that’s happened...Captain. You’ve been out for a while and I’m honestly not sure when."
        s "Keeping track of the time we’ve spent here was MUS-L’s deal and I just...haven’t been able to focus on that too much; most likely a couple days though."

        y2 "Well...I still feel like crap but better than I was when I passed out..."
        y2 "Thank you for doing what you did to take care of us."

        show scientist sad2B

        "Avery doesn’t respond for a while...it’s hard to believe that the person you're staring at is even still there. Her whole demeanor is different; like she’s been lost in a maze and is waiting for something unexpected to jump out at any moment."

        show scientist sadB

        s "Just glad that you’re fine Captain." 
        s "…"
        show scientist happyB
        s "You know...I guess I should thank you for this. If you hadn’t listened and acted as quick as you did I’d probably be dead by now."
        show scientist sad2B
        s "I’m...I’m not over it but I’m more than glad things aren’t as worse as they could have been."

        y2 "Avery..."

        show scientist sadB
        s "Hey listen...I appreciate whatever you were going to say but right now there’s something else we need to talk about and I really need to show you first anyway."
        s "We’re going to go back to the ruins."

        y2 "Um...are you sure we should be doing that?"

        show scientist happyB 
        s "Relax Captain…"
        
        "Avery points to the various vines and wrappings around her skin and clothing."
        
        s "I already got a taste of revenge from the damn thing...now we’re going straight for the heart."
        show scientist sadB
        s "First things first though, follow me."

        y2 "Woah woah wait for a second, you killed that...thing?"

        s "Yes...yes I did, now come along. I already got most of the information from the place but you need to see it for yourself."
        s "Let me help you up and out."

        $ per.player_location = "Thicket"
        $ per.scientist_location = "Thicket"

        hide scientist with dissolve

        stop music fadeout 2.0
        scene bg blank with dissolve

        "And so, against your better judgment, Avery helps escort you back towards the ruins."

        $ snd.play_entering_thicket()

        "As you move through the trees and past the various plants and vines she barely speaks a word. Instead, she is constantly looking for something hidden in the brushes, stopping occasionally to listen out for any sounds or scan behind us for...something."
        
        stop music fadeout 2.0
        scene bg thicket with dissolve
        $ snd.play_bg(per.player_location)
        
        "Eventually, you make it to the familiar cleared circle of dirt with the mass of ruins centered not but less than a hundred feet ahead. Avery starts a careful approach now; her metal arm at the ready in front of her."
        "She carefully moves one foot in front of the other before standing still once more as you follow up from behind."

        "For one moment, you get a knot in your stomach flashing back to the last moments of what this looked like."
        "This time, however, Avery doesn’t wait back. With a sudden dash of movement she sprints towards the ruins; diving into them and lunging with her arms into the pile of plant matter before quickly standing up!"

        show scientist shockedB with dissolve
        s "It’s okay; it’s okay!" 
        show scientist happyB
        s "I’m sorry if you got a little freaked out, but I had to be sure that nothing was waiting inside again."

        y2 "I’m just...amazed that you can so readily do that right now. Especially considering…"

        s "Well, just be glad that another one hasn’t grown back yet."
        s "Anywho, I wanted to show you the reason why we’re here, Captain."

        hide scientist with dissolve

        "Stepping inside the ruins; it’s clearer to see the designs and drawings of those who were somehow here before."
        "Strange human-esque figures with heads and bodies much larger than that of any normal human being."
        "Their skin colored green; the pictures of them depicted in a broken down circle all around you with chunks of purple carved stone shattered next to incomplete sketches."

        show scientist happyB with dissolve
        s "From what I can best gather, this place was some sort of library or place where they chronicled information."
        s "The drawings were a bit hard to make out at first but I started assembling the bits and pieces together and I think I put together some of what was drawn."

        y2 "So...when you woke up, you took care of me AND did this?"

        show scientist sad2B
        s "I didn’t think I had a lot of time left considering the circumstances so I tried to do everything I could in case another one of those things came out of the woodwork and hunted us down."
        s "I think that...maybe the forest thinks that we’re afraid of it now and that hurting me would make me stop trying to figure out what this all means."

        y2 "But now it’s making you wanna push even harder."

        show scientist happyB
        "Avery shrugs."
        s "What can I say, I’m a pretty stubborn gal."
        s "The important thing Captain, is that these drawings; they show some...things working with this forest."
        s "The figures-" 
        "She points towards the hulking green folk on the stone."
        show scientist sadB
        s "they tell a story of something going wrong."
        hide scientist with dissolve

        "She guides her hands over the various painted stones; the figures building their structures in the trees and large groves of the forest. They cover themselves in leaves and vines and gather things to eat from the bushes and treetops."
        "The next image shows many of them together around a large flower; a bussing and bright massive flower that showers them with golden dust."

        show scientist happyB with dissolve
        s "They were celebrating something; they found peace and joy here."
        show scientist sadB
        s "But whatever they were happy with didn’t last."
        hide scientist with dissolve

        "Avery runs her hands over a picture of a table divided with figures grabbing each other. One side depicted in the greenery with the other side of the table covered in purple stonework."
        "A figure near the end of the table standing with hands up defiantly. They are shown moving towards the side of the stone-clad people."
        "Another depiction, this time the figures with wooden and stone weapons; a small group defending the center large plant while many figures surround them. A lone figure stands defiantly at the top of the flower in the middle of throwing someone off into the plant’s surface."
        "The final and last image near the end of the circle shows the masses leaving the forest heading towards a bright and shining sun; the forest itself dying and graying away against the dark."

        show scientist sadB with dissolve
        s "I think that a war happened in this place Captain...and I think that it was over their relationship with this place."

        y2 "So this place...it was being worshipped and then it got angry that it stopped."

        s "I think it got angry that it stopped being fed."
        show scientist shockedB
        s "I mean look at this!"
        hide scientist with dissolve

        "Avery points towards the figure above the flower and the small body of someone falling in."

        show scientist sadB with dissolve
        s "A forest that behaves intelligently and dominantly, one that can transform itself to attack people, and was at one time providing a whole society with resources."
        s "People doubt what they know; they question what they are living under and why things can’t change for the better. Why do they have to give up someone for this thing?"
        s "It follows along so many of our own stories Captain, they looked to the past and saw that they wanted a better future and the people who believed in their old ways fought to keep them going."
        show scientist sad2B
        s "So those who disagreed left...or at least they tried to."

        y2 "Then this thing...it would try to be after one of us. Or anyone who comes down here."

        show scientist sadB
        s "And that’s exactly why we need to stop it from doing anything else."
        s "If people found out that this forest could provide a safe-haven at the cost of someone’s life, there are people out there at places like Astrocorp who would find a way to make this information go away and allow it to happen."
        s "All under the idea that this would be better for humanity’s future"

        y2 "..."

        "You weren’t sure what else could be said. In that moment, the heat and humidity of the jungle began to feel suffocating as if the air was the inhalation of a massive beast."
        "How could you have been so careless all this time in thinking this thing could be reasoned with?"
        "Your worries drift back to your companions when you realize..."
        "...MUS-L."

        y2 "Avery...MUS-L could be in danger; we should go back and find him and fast!"

        show scientist sad2B
        s "I...I’m not sure about that Captain; he’s a machine getting orders from something beyond our authority and I don’t know if there's a way that can change."
        show scientist sadB
        s "Plus he’s Astrocorp made; you don’t think that he’ll be dead set on getting all of this back to them?"

        y2 "I guess I just wonder if there’s a way to at least keep him safe at all…"

        s "Well...if you wanna do that then, the only plan I see going forward as the astrobiologist is to eliminate the specimen."
        s "All of it."

        y2 "And how in the hell are you supposing we do that?"

        show scientist happyB

        "Avery smiles for a moment as she pulls out a familiar scanning device."

        play sound "audio/ch4/Deviceconfig.wav"

        "Its readout display is still functioning, she configures the devices and sets it on her waist pouch as she looks up at you."

        s "Well...like a lot of living things; this thing seems to have some sort of nervous system."
        s "The roots and tree we found earlier feed the plant by harnessing the natural hydrogen and oxygen found in the atmosphere...but it’s starting to run out."
        s "This thing’s alive; the cell’s are able to rapidly mutate and change to fit its need so that must mean there’s a central nervous system somewhere."
        show scientist sadB
        s "Killing the roots would only hurt it; not destroy it."
        s "That’s why my guess is here: the place where they were feeding this thing."

        y2 "Consuming something there...and the desire for these creatures to protect it…"

        show scientist happyB
        s "Exactly!"
        s "If these people fought the thing right where that giant bud is it means that it has to be vulnerable somewhat."
        s "And if they were worried about some people with rocks and stones to put up enough of a fight-"

        y2 "Then there’s gotta be something we can do to it."
        y2 "Okay...I hear you; we need to hurry then before something worse happens."

        play sound "audio/ch4/Tearingplants.wav"

        "As the words left your lips, a great rumbling of earth started to shake the ground below cracking and splitting your ears with the sounds of tearing plants."
        "The dirt began to sift and move like sand as your could feel vibrations from underneath your pulse."

        y2 "We need to move now! Tell me you have something in mind or we might not make it anyways!"

        show scientist shockedB
        s "I do I do! Come on, we’ll set up the devices on the way there!"
        
        scene bg blank with dissolve
        stop music fadeout 2.0
        jump final_choice


    else:
        $ go_with_r = True
        $ snd.play_bg(per.player_location)
        scene bg water_source with dissolve

        "The sense of blindness begins to fade away as your eyes flutter open to the sound of a familiar voice."

        show robot happyB with dissolve

        r "Hello Captain, I’m glad to see that no ocular impairment occurred when you attempted to help prevent communion with my new...companion."

        "MUS-L proudly rotates his arms to gesture to the alien bouquet resting on his head."
        play sound "audio/ch4/VinesonMUSL.wav"
        "Vines and roots spiral around his head, neck, and shoulders. Faint thinning vines also wrap around his torso but are not digging into him like earlier, instead only resting comfortably along with his metal frame."

        r "Are you okay to walk Captain? I hope your sensory stimuli were not too damaged in your experience of the past."

        y2 "Yeah yeah MUS-L I’m fi-"
        stop sound fadeout 2.0
        y2 "I’m sorry what did you just say? I think I’m still disoriented a bit."

        r "The images that flashed in your mind, I saw them as well."
        r "The forest was trying to show me...well...us its history on this planet and what its purpose is."

        y2 "Woah woah woah...you’re gonna need to slow down for this one MUS-L."
        y2 "What exactly was there to see?"

        r "In essence Captain...the destruction of this lifeform and the planet itself."
        r "Please, come follow me and I can explain further as we leave this cramped space."

        y2 "I’m definitely ready to get out of here but I really need to know what happened MUS-L."
        y2 "What even is this thing that’s attached to you and are you okay at all? What did it do to me?"

        hide robot with dissolve
        "As you begin to climb out of the tunnel, MUS-L’s frame begins to walk and climb out of the wooden and dirt-walled chamber at the mouth of the tree."

        show robot happyB with dissolve
        r "This entity wanted to talk to {i}you{/i} Captain, and to show that it tried to tell you what it’s been going through all these many years."
        r "The vision...that was its history; it was a lone creature that was tired from traveling the stars so it settled down and took root. Soon, it evolved around space itself until it took shape to what was surviving: a planet."
        r "Its surface was its shielded roots but deep inside it still kept what it was; a creature desperate to survive."

        y2 "But I saw other...people, MUS-L. Other creatures here; in this place where you and I are at right now. And now you’re saying these people are just gone?"

        "As you climb and begin to look out over the stretch of the large root tree; the forest is alive and glowing as bright as ever. The waterfall lurches over the cliffside and floods the rapids below as they spiral down into the darkened purple wood."
        "The massive and familiar budding pink and red flower resting squarely many, many, many miles ahead. No sunlight, no sky; just the ever-present shimmering glow of water and flower light reflected across the surfaces of the earth."
        "MUS-L stares out silent for a moment taking in the sights of this place almost like he’s suddenly remembered a bad memory..."

        play sound "<from 2.7>audio/musl/Sad_beep.wav"
        r "Yes...they are; other creatures found this place and grew within and alongside this place."
        r "They borrowed and were given resources to grow, learn, and adapt and as they did the forest grew more and more complex. But in order for this growth to happen; they had to give up one of their own."
        r "The chemicals and resources in their bodies allowed the entity to further expand and help assist the lives of its inhabitants as long as it could continually consume from time to time-"

        y2 "Consume? Consume?!"
        y2 "MUS-L have you completely lost it?! If this place is eating people to survive that means us! And everyone else that’s planning on coming to live here!"

        r "Please Captain, let me explain. The story isn’t as simple as you think."
        r "The entity would consume others to survive only due to its need for the chemical resources in their bodies..."
        r "When the peoples of this place grew tired of continuing on with this cycle they decided that they would try to live elsewhere; taking the advanced knowledge and growth they’ve had for so long with them and tried to live on the surface above."
        r "Some tried to destroy the entity’s heart...some tried to protect it but most left to start somewhere new. Those that fought fell and thus fed the entity over time."
        r "But now...things are changing Captain."

        "MUS-L turns to you facing away from the natural landscapes of the forest below."
        "For a second there’s a worrying pause before MUS-L continues…"

        r "The entity needs something to keep living, it needs someone to die so that its offspring can take its place."
        r "It’s old and starting to wilt with the lack of minerals found in other organic beings and has left this child in its place."
        r "But before it can take over…it needs one last bit of life to sustain itself for its child."
        r "We can go to the very heart of the forest, save this place, and find ways through the help of the rest of the crew and humanity to better this place so that life can flourish here!"

        "You stand in stunned silence; thoughts of the forest race through your mind as visions and memories that aren’t your own are felt through you."
        "Creatures lay fallen in the dirt as blood and soil mix together until bodies sink into the ground. Vines and roots dig into their flesh and life spread throughout the forest once more."
        "Silence and isolation creep in for years and years and years…until eventually, sleep takes hold to preserve the little life left."
        "Then…a sound as something finds purchase close by. Voices, names, and creatures like the ones from long ago surprise a suddenly awoken mass."

        y2 "Agh! MUS-L, why am I seeing this?!"

        r "Captain, because this entity is alive and can feel."
        r "This is what Astrocorp sent us to do: we’ve found sentient alien life and if properly understood could save and help so many lives."
        r "Food and water, natural resources, scientific advancement through analysis of. We now should take the time to better understand and help it; it does not kill for enjoyment and takes life only because it doesn’t know other ways to adapt."
        r "With help, we can turn this-"
        "MUS-L gestures to the flower."
        r "-into something much better; something that can work with and support the goals of humankind for generations to come."

        play sound "audio/ch4/Collapse.wav"
        "The images suddenly stop as you crumble to the ground. You step away as fast as you can from the edge, afraid at the thought of how close you could have fallen off the edge and could be swept away by the rapids."

        y2 "I…I need a minute to think."
        y2 "And just…stay away for a moment, please."

        r "As you wish Captain."

        "There’s a bit of an awkward pause as you and MUS-L quietly observe each other over the crashing waterfall. It’s hard to imagine that throughout this discovery there would be so much turmoil; so much of a disconnect between everyone even after working together for so long."
        "You move by the tree afraid at the thought that this place has been aware of your presence this whole time. Your thoughts couldn’t help but drift to Dr. DeWitt resting in the main cavern."
        "Avery..."

        y2 "Avery's been injured."

        "MUS-L begins to approach slowly; uncertain if now’s the right time to attempt at reaching out. Saying nothing, he sits down."

        y2 "S-she lost her arm in an accident, I had to assemble a new one..."
        
        "Realization begins to dawn on you. How long had you been away?"

        y2 "We need to go back and make sure she's alright."
        y2 "She left because we stayed behind; alone it’s still dangerous here and even though you may have some connection with the planet we need to stick together."
        y2 "Please…help me find her. Talk to the…entity and find out if she's alright."

        r "I…understand Captain, I certainly can attempt something like this. Let’s begin travelling then as it will take a while to return."

        hide robot with dissolve
        stop music fadeout 2.0
        scene bg blank with dissolve

        $ snd.play_entering_thicket()

        "You begin to set out through the path down again racing against the thought of Avery’s wellbeing."
        play sound "audio/ch4/MUSL_communications.wav"
        "With each step as you pass through the forest, MUS-L’s new attached plant glows and hums as the forest, seemingly affected by its presence, glows and moves slightly with a hum."
        "For hours you make your trek back and MUS-L continues making the strange and warbled sounds that occurred when the plant reached out and attached itself to him."

        r "Captain, I know your mind is set on finding Dr. DeWitt but if we get there and she isn’t there…what will we do then?"

        y2 "I don’t know yet MUS-L but let’s just wait and see what we find eh?"
        y2 "I’m sure everything is gonna be fine…it's gotta be."

        r "Well…if I may suggest something. The entity is wanting to grow and learn to be better, maybe we could teach it that starting with helping it find Dr. DeWitt."

        "You stop for a moment, thinking about exactly what such a plan would look like."

        y2 "The forest is wanting to help now? Why? What has it been saying to you?"

        r "The entity is…split is the best way I can put it."
        r "This version with me is one that is wanting to assist in Dr. DeWitt’s discovery but the older version is less than willing."
        r "The issue is…we’d have to go right now to the heart of it all. We’d need to make sure that this new version overwrites the older entity and takes over this place completely."
        r "Otherwise, the forest will keep acting out in self-preservation until it can feed on what it knows is here."

        y2 "And you’re sure that this is the end-goal, that it will help us in the end?"

        r "Captain…I would like to give you such reassurance but I can’t. I’m only attempting to interpret what is being said."
        r "But…if I did have a choice, it’s better to get help from something than to go at it alone"

        y2 "..."
        y2 "Where’s the center that we need to get to MUS-L? Where’s the heart of this place?"

        r "I believe that it resides that way; it’s significantly a much longer hike there instead of to the ruins."

        y2 "Then we’d better hurry, come on MUS-L. I’m trusting that you and this thing understand what’s at stake otherwise…"

        r "Captain…I’ll do my best, as your MUS-L bot and crew member."

        stop sound fadeout 2.0
        stop music fadeout 2.0
        "You begin to track and trek through the foliage; unaware of the knowledge and decisions that would come about in your last and final encounter with the unknown."
        jump final_choice


label final_choice:
    $ per.player_location = "Core"
    play sound "audio/ch4/Running_forest.wav"
    "Through the echoed shakes, you ran and as best you could towards the center of the massive petaled bud; the center of this place."
    "You eventually escaped the sound and the rumbling and as you caught your breath it dawned on you the realization of what you’d be doing, what was at stake, and how only the three of you entered into this planet without knowing what you’d find."
    if go_with_s:
        "Avery suggested that you rest as much as you can and prepare for what you’d need to do."
    if go_with_r:
        "MUS-L suggested that you rest as much as you can and prepare for what you’d need to do."

    stop sound fadeout 2.0

    "As you approached you quickly began to see the forest’s massive center."

    play music "<loop 0.0 to 18.15>audio/locations/Core_background.wav" fadeout 1.0
    scene bg core with dissolve

    "The bulb was hundreds of feet wide with massive thorny roots that spread out all over the ground like spider webs."
    "It wrapped itself in thick and knotted vines that made up a strong stem at its base while massive pinkish-red leaves jutted out."
    "All you could begin to focus on once you made visual contact with the plant was the question of how you’d ascend something so massive."

    if go_with_s:
        y2 "So...the plan is to get through the thorns on the ground, climb up to the top, and then let the devices do their thing, right?"
        
        show scientist happyB with dissolve

        s "Exactly, I’ll prepare setting up the devices now."
        s "They hopefully shouldn’t take too long but it’s going to cost most of my arm to do it."
        s "We should wait until we’re absolutely sure they’ll go in and then we can cause them to start consuming the forest bit by bit."

    if go_with_r:
        y2 "So...the plan is to get through the thorns on the ground, climb up to the top, and then  let the little guy do his thing, right?"

        show robot happyB with dissolve
        r "Exactly, the entity is somewhat expecting us."
        r "It shouldn’t take too long to transfer over its control to its child."
        r "We should wait until we’re absolutely sure they’ll go in and then we tell the creature to start taking over the forest bit by bit."

    y2 "So how do you think we’ll get up there? Getting through the vines on the ground could be a problem plus I don’t see a way we can easily climb up to the top."

    if go_with_s:
        show scientist sad2B
        s "Well being honest…I’m not exactly sure yet."
        show scientist sadB
        s "We can’t do anything so far away from it at the moment so let’s just approach carefully for now."
        show scientist happyB
        s "You have anything, Captain?"
        hide scientist with dissolve

    if go_with_r:
        r "I’m not exactly sure yet."
        r "We can’t do anything so far away from it at the moment so let’s just approach carefully for now."
        r "Do you have anything, Captain?"
        hide robot with dissolve

    play sound "audio/ch4/Howlingwind.wav"
    "As you begin to cross the thorns, the sound of wind begins to rush and condense somewhere above you."
    stop sound fadeout 2.0
    "The leaves begin to bend inward almost reflexively tugging like muscle contractions towards the thick knotted stem."
    queue sound "audio/ch4/Phoosh.wav"
    "With a loud {i}PHOOOSH{/i}, you see a sort of pinkish residue fill the air high in the sky as the leaves begin to relax back into their original positions."
    "The residue covers the air and begins to coat nearby trees and earth before quickly disappearing; almost like it was absorbed into the plants and dirt."

    y2 "Maybe if we could somehow keep our grip on the leaves we could somehow allow the plant to take us up the rest of the way?"

    if go_with_s:
        show scientist sadB with dissolve
        s "That…honestly might be the only way up."
        s "As long as they stay relatively in place near the base we could climb up and then use the momentum there to pull us up."
        s "There is some climbing gear still remaining from when we initially fell in but it might not get us up all the way."

    if go_with_r:
        show robot happyB with dissolve
        r "That might be the only way up."
        r "As long as they stay relatively in place near the base we could climb up and then use the momentum there to pull us up."
        r "There is some climbing gear still remaining from when we initially fell in but it might not get us up all the way."

    y2 "Then we use what we can; attach yourself to me and go on up ahead first. I’ll be right behind you."
    y2 "Just make sure to not get us both killed on the way up, alright?"

    if go_with_s:
        show scientist happyB
        s "Will do, Captain."
        hide scientist with dissolve

    if go_with_r:
        r "Will do, Captain."
        hide robot with dissolve

    "The climb began after making your way across the thorns; no one was damaged thankfully but with each step, you made sure to remember how painful and large the spines were."
    
    if go_with_s:
        "Eventually, you reached the base of the stem, and using Avery’s supplies you ascended up to a point where you could take a minute to rest before looking above at the petaled exterior above us."

    if go_with_r:
        "Eventually, you reached the base of the stem, and using MUS-L's claws you ascended up to a point where you could take a minute to rest before looking above at the petaled exterior above us."

    y2 "Just…a bit…more to go. Are you good to keep going?"
    
    if go_with_s:
        s "Yeah…just trying to…get used to climbing with this new arm. A little tight on the joints, hehe!"

    if go_with_r:
        r "I’m alright Captain, just be careful not to overexert yourself. The hardest part will be approaching soon."

    y2 "Yeah…I can definitely understand that. Okay, one more push!"

    "You begin to hold on with all of our might as the bulb contracts."
    play sound "audio/ch4/Phoosh.wav" fadein 2.0
    "You look over at your crew member as you brace for the force that you’ll feel and after just a moment the {i}PHOOOOSH{/i} happens once more."
    stop sound fadeout 1.0
    "Leaves lurch and lift from the sides of the rooted stem."
    play sound "audio/ch4/Movingleaves.wav" fadein 1.0
    "Wind flies past your face and as you look down the floor lies hundreds of feet below almost in an instant."
    "Your palms begin to sweat as a sudden jolt of fear runs down your spine at the thought of your potential downfall."
    stop sound fadeout 2.0

    if go_with_s:
        s "Move towards me, Captain! I’ll pull you the rest of the way up! Just keep climbing! We’re almost at the top!"
        "Even while attached to Avery the climb across and up the petals is rendered difficult."

    if go_with_r:
        r "Move towards me, Captain! I’ll pull you the rest of the way up! Just keep climbing! We’re almost at the top!"
        "Even while attached to MUS-L the climb across and up the petals is rendered difficult."
     
    "The outside of the petals are delicate and slippery; covered with moisture leaving out any strong handholds."
    "The only way you can dig in and lift yourself up is to dig your hands into the petal itself where some sort of red wet flesh sticks to your palms and hands."
    
    if go_with_s:
        "Avery’s ropes and hooks keep you from blowing away as the bulb contracts against the pulse of wind coming in and out of the top…"
        "After a while, however, you see Avery reach the top and feel a tug as she begins to pull you up."

    if go_with_r:
        "MUS-L's limb keep you from blowing away as the bulb contracts against the pulse of wind coming in and out of the top…"
        "After a while, however, you see MUS-L reach the top and feel a tug as he begins to pull you up."
    
    "With your load becoming lightened somewhat; you move up the side as steadily and slowly as you can and eventually tumble to what appears to be the top of one of the leaves that lies more inward towards the hole."

    if go_with_s:
        s "Captain, we’ve done it! Come on, let’s hurry and see this through!"

    if go_with_r:
        r "Captain, we’ve done it! Come on, let’s hurry and see this through!"

    "As you turn to face them and stand up exhausted, your eyes hone in on the massive and jagged hole in the center of the plant."
    "Large swaths of thorns lie down a dark and wet hole; massive pink and red mounds of some sort of pollen-like substance rest all around the hole while you struggle to see a…figure standing on the opposite side of the center."

    "And then you realize..."
    
    if go_with_s:
        "It's MUS-L."
        "MUS-L stands there covered in the pink and red mounds of the pollen-like substance."
        "Multiple vines and roots cover and run up and down his legs, arms, and chest and his face lies completely unchanged since you last saw him."

    if go_with_r:
        "It's Avery."
        "She stands there bloodied and covered in the pink and red mounds of the pollen-like substance."
        "Multiple scars runs up and down her legs, chest, and arms, and her face is set with shock and contempt lies in her eyes."

    y2 "What the hell…are you doing here? What happened to you?"

    if go_with_s:
        show robot happyB with dissolve
        r "The forest is dying; it needs new life to grow."
        r "I’m here to make sure it doesn’t make the same mistakes it has before."
        r "Dr. Avery appears unwell and you do too Captain, what happened?"

        "You explain what the ruins from the old civilization that left here left behind, how Avery lost her arm and how you helped heal her, and that you came here to find a way to stop the forest from growing."

        r "..."
        r "Well then…she's not exactly going to be happy with what I came here to do."
        r "Dr. DeWitt, please move aside. I need to make sure that the entity will be able to learn and grow with compassion and find a better way to feed itself with help."

        "MUS-L steps forward quickly and lifts his arms to remove the plant from his head."
        "You try to move towards them but Avery stands beside you and starts moving quickly to meet him before he can get any further."

        r "Dr. DeWitt, I would ask you calmly consider how much we’d lose and what’s at stake."
        r "Think about it with proper regulations and rules put in place behind Astrocorp and other agencies we could make this planet a paradise for humanity!"
        r "All we’d need is one last person to give themselves up and humanity could prosper on this planet in a way we’ve never seen before!"
        show robot at left with dissolve

        show scientist angryB at right with dissolve
        s "I’ve already considered it and {i}this{/i} was the price I paid for trying to understand something unknown MUS-L!"
        s "I’m not going to be swayed by a plight to help humanity when we’ve been doing fine so far."
        show scientist sadB
        s "Besides…this thing hurts people, MUS-L, and I’m not too rosy-eyed so think that it can be changed so easily."

    if go_with_r:
        show scientist sadB with dissolve
        s "After you left I went back to the ruins."
        show scientist angryB
        s "And now, I’m here to take this whole place down."
        show scientist shockedB
        s "What the hell happened to you!? What the hell happened to MUS-L?"
        show scientist sadB

        "You explain what the forest showed to you and MUS-L, how its new version could take over the forest and help it grow and learn, and that you came here to find her."

        show scientist sad2B
        s "..."
        show scientist angryB
        s "Well then…he's not exactly going to be happy with what I came here to do."
        s "MUS-L, please move aside. I need to make sure that this thing will never have the chance to do anything as it did before ever again."

        "Avery steps forward quickly unlatches several small data devices covered in shards of metal."
        "You try to move towards them but MUS-L stands beside you and starts moving quickly to meet her before she can get any further."

        show scientist shockedB
        s "MUS-L you’re insane!"
        show scientist angryB
        s "This place has corrupted you, it’s literally taking itself and constricting you into believing something that you don’t know is true!"
        s "We can’t confirm this thing isn’t going to be able to change and there’s no way that you or anyone else could prove to me that right now!"
        show scientist at right with dissolve

        show robot happyB at left with dissolve
        r "But I do know Dr. DeWitt, I’ve been shown the reasoning for its peace and the need for its adaptability."
        r "It wants to work together with a new species, not consume it."
        r "We just need to give nature a chance and nurture it with the knowledge we have to make something that can benefit both humans and this entity."

    "They start to argue and fight amongst standing opposite the void of the open hole in the flower."
    "You get up off of your knees to catch your balance and begin to stand and stumble forward."
    "They go back and forth; the question of the survival or termination of the creature you stand upon."
    "They both stand resolute and begin to move closer towards each other bent on forcing the other to comply."

    y2 "Please, both of you stop!"
    #stop music fadeout 1.0
    y2 "Nothing good can come from this bickering right now and as Captain, I’m making the call right now to…to…"

    menu:
        "Save the entity":
            jump save_ending

        "Destroy the entity":
            jump destroy_ending

label save_ending:
    #$ snd.play_bg(per.player_location)
    y2 "Avery…"
    y2 "MUS-L’s right. What if we’re throwing away an opportunity to change and better help the next advancement for humanity?"
    y2 "If we kill this thing that is alive and aware of itself we’re killing off everything because we’re scared and afraid."
    y2 "We can’t let emotions and the fact that…that you’re angry and hellbent on doing whatever it is you’re going to do end a possible betterment of everyone else."
    y2 "Now, please…I’m ordering you to stand down and come with us!"

    "Avery stares for a moment at us, looking to MUS-L then to me with eyes wide. Her mouth twisted into a disgusted yet stoic expression."
    "She pulls a device from her waist belt and holds it in her hand, ready to throw it into the flower when suddenly MUS-L yells!"

    play sound "audio/musl/Alarmed.wav"
    r "Stop her, quickly!"

    hide scientist with dissolve
    hide robot with dissolve

    play sound "audio/other/Flowerattack.wav" fadein 2.0
    "As fast as lightning, the plant on MUS-L’s head whips to life, and the vines and roots that were wrapped around MUS-L fly towards Avery and wrap around her arms and waist."
    stop sound fadeout 2.0
    "They quickly grab the belt of devices and with a loud beeping sound from MUS-L the roots fling the belt towards the sides of the leaf and it slides down…down…and down until it falls off the plant."
    play sound "audio/other/Avery_scream.wav"
    "The roots then pull Dr.DeWitt towards the hole as she begins to kick and scream."

    y2 "MUS-L, STOP THIS NOW! PLEASE!"

    "Yet before you have any chance to help her she is pulled down into the hole and MUS-L’s attached plant begins to unwind itself; the roots and vines uncoiling as it slides off and into the hole dropping with her."
    "You scramble towards the side of the hole."

    y2 "AVERY NO!"

    show robot happy with dissolve
    play sound "audio/musl/Softlowbeeps.wav"
    r "Cap-Cap-Captain, I’m not so-so-so sure that I’m functioning properly anymore."
    r "I have sustained much more dam-dam-damage than previously determined."
    r "Please, we mus-must escape and allow the entity to be properly transferred before we become at risk of hurting ourselves." 
    r "Captain?"

    "She’s gone…after all of the time you spent as both each other’s crew and company she’s gone."
    "You're stunned; your eyes are glued to the pit of darkness below where somewhere Avery’s body is down there with the plant you hope will help humanity’s future."
    "It’s a twisted joke, that in order to save the lives of everyone you had to lose her to do it and you didn’t even get a chance to say goodbye."

    stop music fadeout 2.0
    scene bg blank with dissolve
    
    "MUS-L eventually helps you come back to reality; letting you know that all you can do now is watch and wait. And so you did, and he was right…somewhat."
    "The forest that you once had some understanding of faded away and over time something…new took its place."
    $ snd.play_entering_thicket()
    "By the time you had finished climbing down and returned to your collapsed tunnel, the remaining crew on the ship and those whose jobs were still to survey and help terraform the planet found you."
    play sound "audio/other/Construction.wav"
    "You got evac’d and out and you believe that MUS-L said to “Make a full report and propose it to the company.”"
    "You think that was his exact wording, but in the back of your head, the least that you could do was let maybe more than just one corporation decide something this monumental."
    "You think Avery maybe would have at least preferred that over the alternative. So, after reviewing the events that have transpired, everything’s been finished."
    "Everything about that time’s been laid out and recorded. You're not exactly sure what or who Astrocorp, humanity, or the world will do."
    stop music fadeout 2.0
    "But there’s a chance."
    play music "<from 0.0 to 30.0>Audio/Menu_8bit.wav" fadein 2.0
    "Somehow, somewhere, you might be able to do something and crack this puzzle."
    "For now though, all you can do is remember the past and hope that the future can look brighter through the cracks you make and leave behind to heal."
    jump credits

label destroy_ending:
    #$ snd.play_bg(per.player_location)
    y2 "MUS-L..."
    y2 "Avery’s right. What if by letting this thing survive and grow it ends up being more cause for harm to others?"
    y2 "What if by trying to understand and probe deeper we end up digging too much and realize this thing just can’t be on our side?"
    y2 "We can’t let such a big risk like this be decided by just us and in order to keep everyone safe then this thing has to go."
    y2 "I’m sorry MUS-L…but I can’t allow your directives and pursuit of saving intelligent and dangerous life continue so I’m ordering you as Captain to stand down and come back with us…please!"

    "MUS-L stares for a moment at you, looking to Avery then to you with his eye blank and distant."
    play sound "<from 2.7>audio/musl/Sad_beep.wav"
    "His expression remains robotic but for a small moment, a faint and sad beep drones quietly from him."
    "He begins to start slowly unleashing strange and warbled sound as the vines wrapped around MUS-L begin to detach themselves!"

    show scientist shockedB
    s "MUS-L, stop this now!"

    hide scientist with dissolve
    hide robot with dissolve
    "Avery hurls one of the devices towards MUS-L while scrambling to take off the rest of the devices."
    play sound "audio/ch4/Swarming_nanobots.wav"
    "The small metal plate and shards fly and smack across MUS-L’s form as the installed reprogramed bots begin to swarm and cover MUS-L like ants."
    stop sound fadeout 2.0
    "He begins to step back attempting to scrape them off but they just keep crawling over him until they reach the top of his head!"

    play sound "audio/musl/Alarmed.wav"
    r "CAPTAIN, PLEASE STOP HER QUICKLY!"

    "You turn to Avery, face set determined with the remaining devices in hand."
    stop sound fadeout 2.0
    "Your eyes meet before you give her a solemn nod as she hurls the devices, belt and all, into the hole of the center of the bulb."
    queue sound "audio/ch4/Swarming_nanobots.wav"
    "Metal shards and bots begin to rain into the whole as one by one they being to sprinkle along the sides of the plant already beginning the process of destroying its center."

    s "Captain come on! There’s nothing left for us to do other than run!"

    "As Avery begins trying to pull you away, you can’t help but stare back at MUS-L."

    stop sound fadeout 2.0

    "He keeps attempting to keep the bots off of him and eventually falls over unable to stop their assault over his body."
    queue sound "audio/musl/MUSL_Death.wav"
    "Two different warbled screeches, robotic and guttural, start emanating out from his body as you stand frozen knowing that MUS-L’s frame will be destroyed by the bots as they eliminate any foreign entity."
    "His warbled cries for help mixed with a pained cry like jagged stones being scraped against each other."
    "Avery brings you back to reality after MUS-L’s form slowly vanishes through the crowd of darkened microbots covering his frame as the plant on his head fades."
    stop sound fadeout 2.0
    "She reminds you that the entire forest; maybe even the planet could eventually fade away and break apart so you needed to leave quickly."
    scene bg blank with dissolve
    stop music fadeout 2.0
    play sound "audio/ch4/running_forest.wav"
    "You run and run…past the decaying trees and roots as the bioluminescent light fade away from the familiar ruins, the cliffs, and the water."
    stop sound fadeout 2.0
    "You keep running..."
    play sound "audio/other/construction.wav" fadein 2.0
    "By the time you reach the collapsed entrance you once entered; several other crew members and terraforming engineers are curious as to how you haven’t been in contact and to what exactly is this strange underground world you’ve discovered."
    "They wouldn’t exactly be happy to hear how quickly you’d need to evacuate everyone off the planet immediately without remaining personal crew wondering what happened to MUS-L and to the mission."
    stop sound fadeout 2.0
    "“The mission changed; MUS-L and the company’s protocols almost got us killed,” Avery said sternly."
    play music "<from 0.0 to 30.0>Audio/Menu_8bit.wav" fadein 2.0
    "Now, as you ride back answering the crew’s questions and planning out meeting Astrocorp executives to brief them on the situation you think back on MUS-L’s potential that he’d talk about with the plants."
    "Maybe one-day humanity could be ready for that potential; but, until the system can change you’re left in the dark; searching for a potential future that you’ll be able to use to heal the scars and cracks you leave behind."
    jump credits

label credits:
    $ _skipping = False
    show screen credits with dissolve
    "Thank you for playing!"
    "If you want to see the other ending, or just want to play through the game again, you can access the game's chapters after going back to the menu and clicking New Game."
    $ persistent.game_completed = True
    return

screen credits:
    hbox:
        xalign 0.5 yalign 0.5
        spacing 50
        vbox:
            spacing 25
            text "{=datapad_text}| Kayla Han |"
            text "{=datapad_body_text}| Programming |" xalign 0.5
            text "{=datapad_body_text}| Character art |" xalign 0.5
        vbox:
            spacing 25
            text "{=datapad_text}| Natalie Tobita |"
            text "{=datapad_body_text}| Sound design |" xalign 0.5
            text "{=datapad_body_text}| Background art |" xalign 0.5
        vbox:
            spacing 25
            text "{=datapad_text}| Zane Stewart |"
            text "{=datapad_body_text}| Writing |" xalign 0.5
            text "{=datapad_body_text}| Concept design |" xalign 0.5

label test_room:
    "Testing."
    scene bg water_source
    call screen sound_pattern