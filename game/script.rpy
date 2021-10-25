# The script of the game goes in this file.

# The game starts here.
label start:
    $ inv = Inventory()
    $ puz = Puzzle_manager()
    scene bg blank
    
    "(wrrrrr) (wrrrr) (wrrrr)"

    "The sounds of rocks break and chip against a large metal drill, dropping somewhere into the pool of darkness below."
    "A crew of three humanoid individuals stare out into a massive darkened cavern; their eyes slowly adjusting to the shadowed chamber."
    "A warm and sweet breeze blows lightly against the figures. The air feels humid and damp."
    "The silhouetted individual in the front leans further out into the dark, searching for any sign of light."
    "They lean even further before saying something to their companions."
    "As they turn, they lose their footing, slipping down onto the rocks and quickly falling, falling, falling, until!"

    "(SPLASH)"

    s_unknown "Captain!"
    s_unknown "Quick, help me pull the captain out! We don’t even know if this is normal water!"

    r_unknown "I agree, this water is too abnormally saturated to be considered normal."
    r_unknown "The captain will need a full scan to determine any injuries or changes in bodily structure."

    "..."
    "..."
    "You slowly regain your senses..."

    scene bg waterfall with dissolve
    "The water shines with a vibrant, almost neon blue against the purple stone walls."
    "The trees give a slight glow and hum like fireflies and illuminate the surrounding cavern and grassy gnoll."

    show scientist shocked with dissolve
    s_unknown "Oh thank goodness!"
    s_unknown "MUS-L you run diagnostics and I’ll make sure the captain didn’t suffer any memory loss."

    "You...remember this person. Her name is Dr. Avery DeWitt and she is a part of you crew. She’s your chief scientist and medical expert."

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

    "MUS-L beeps sadly."
    r "I...apologize. I will categorize this information in my deep storage memory banks to permanently retain this for later."
    r "I told myself to be better than this."

    p "Oh, relax. Nothing bad happened and you were doing as you were directed. You have no reason to feel down."
    p "Okay, so what’s the situation? Give me a rundown of everything we know."

    hide robot happy with dissolve

    show scientist happy at center with dissolve
    s "Yes, Captain, currently not much has changed from our standard mission."
    s "Our job from AstroCorp was to investigate and assist in the terraforming process for planet X-43 in the Hollow Mire system."
    show scientist sad
    s "We arrived approximately 12 hours ago. AstroCorp told us that other drilling operations and machinery have been damaged by plant roots from underground."
    s "Only the three of us were sent to investigate. The rest of the remaining personal wait aboard our ship ready to assist in getting us away, should our lives be in danger."
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

    "{i}In the game, there are certain items you will be able to take a closer look at.{/i}"
    "{i}Click on the note to enlarge it.{/i}"

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
    call screen password_solution

label password_fail:
    show robot happy with dissolve
    p "..."
    p "Hey, MUS-L, you mind showing me one more time?"

    r "Yes, Captain."

    hide robot with dissolve
    call screen password_solution

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
        per.player_name "There we go..."
        per.player_name "Now, let's see here..."

        $ inv.set_uninteractable()
        show screen datapad with dissolve

        "{i}Your datapad displays your currently held item and your team's location and wellbeing.{/i}"
        "{i}Throughout the game, you may need to use held items in order for the story to progress.{/i}"
        "Click on the note you are currently holding."
        $ inv.set_interactable()

        call screen datapad
        jump device_testing
    else:
        "You forgot to enter your name..."
        call screen datapad_tutorial with dissolve

label chap_1_end:
    per.player_name "Now we’re cooking! MUS-L, Doctor, you got anything you can give me about this place?"

    show scientist sad with dissolve
    s "Well, this specific plant type and soil structure are unlike anything I’ve ever seen in previous studies of other planets."
    s "The plant matter appears to..."
    show scientist sad2
    s "ungulate..."
    show scientist sad
    s "when disturbed; the soil is full of rich nutrients that also cause rapid growth of the plant matter I’ve observed."

    per.player_name "Huh, I guess that makes this trip so far somewhat of a success and a failure."
    per.player_name "Great stuff to potentially grow grass and edible plants with, but being so far underground makes it not ideal."
    per.player_name "MUS-L, got anything on the water yet?"
    
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

    per.player_name "Doctor, MUS-L; what did you guys figure out?"
    per.player_name "We haven’t got all day to stand stunned."

    show scientist sad

    r "The only logical connection that can be formed with our understanding of the data is that the entire planet is one central organic life form."

    per.player_name "Are you saying we’re attempting to terraform a plant the size of a planet?!"

    s "I’m afraid so..."
    s "However, this would explain the damage done to the previous drilling machines."
    s "The plant is trying to protect some of its most dense areas that support its life."
    s "The fact that it can do that while being so massive is extremely troubling."

    r "Observing current data, however, this plant is thoroughly tied to everything here."
    r "With the soil and water it produces it could potentially be used as a resource for future operations."
    r "In addition to this, our drill was not blocked off."
    r "This data could be assumed to mean small team operations could be completed, albeit at a slower pace than originally estimated."

    per.player_name "I’m... not sure what will become of this operation, but as captain I am changing the objective of our mission."
    per.player_name "We need to learn more about... whatever this thing is, and fast, so we can figure out our next steps."

    show scientist happy
    s "I suggest, then, that we get moving towards this nearby thicket, Captain."
    s "It would lead more into the woodwork so we could further analyze any data on the vegetation and its rapid growth effects."
    show scientist sad
    s "Also... being out in this open space leaves me feeling rather exposed."

    r "Captain, if I may suggest an alternate route?"
    r "This water’s special properties must lead to some sort of source deeper in the area."
    "MUS-L boops excitedly."
    r "I also am interested in how this water could be potentially used to better our terraforming process on the surface."

    show scientist happy
    s "No matter which way we start; we’ll stick together Captain."
    s "I don’t think going at it alone is a great idea right now…"

    r "Affirmative. The potentiality of injuring one’s self when traversing an alien underground forest could be estimated near a startling percentile."

    per.player_name "Y-you have data on this from the corporation, MUS-L?"

    r "I was attempting to be humorous."
    r "Was it not funny?"

    show scientist sad
    s "It was certainly an... attempt MUS-L."

    show scientist happy

    per.player_name "{i}Hmm, a potential water source, or a stronger and more localized area of the vegetation...{/i}"
    per.player_name "{i}We’ll most likely be able to get to both as long as nothing goes wrong, but which direction would be best to start..?{/i}"

    hide scientist with dissolve

    hide robot with dissolve

    show bg blank with dissolve

    "{i}Would you like to save the game?{/i}"
    menu:
        "Yes":
            call screen save with dissolve
            jump next_chapter
        "No":
            jump next_chapter

label chap_2_end:
    scene bg blank with dissolve
    "{i}This concludes Chapter 2.{/i}"
    "{i}Would you like to save the game?{/i}"
    menu:
        "Yes":
            call screen save with dissolve
            return
        "No":
            return

label next_chapter:
    $ puz = Puzzle_manager()
    $ inv = Inventory()
    $ per.chapter_num += 1
    $ chapter_name = "chapter_" + str(per.chapter_num)
    $ renpy.jump(chapter_name)

label chapter_2:
    per.player_name "{i}Where should we go first..?{/i}"
    $ per.scientist_location = "Waterfall"
    $ per.robot_location = "Waterfall"
    #show screen debug
    #call screen water_source_controls
    $ first_visit = True
    scene bg waterfall with dissolve
    call screen waterfall with dissolve

label thicket_puzzle:
    show scientist happy with dissolve
    s "Captain!"

    "Avery hands you one of the scanners."

    s "Could you attach this one to that vine over there?"

    per.player_name "On it."

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
    
    per.player_name "Now to calibrate it..."
    call screen thicket_activation with dissolve

label thicket_solved:
    per.player_name "Got it!"

    show scientist happy with dissolve
    s "Yes!"
    s "Okay okay okay, the last of the devices are calibrated now, Captain."
    s "It’s going to take a while for them to complete a full deconstruction of the plant matter, but after a couple hours or so we should have a molecular breakdown!"
    s "Now, let’s move on to the large one..."
    hide scientist with dissolve

    show robot happy with dissolve

    if water_source_visited == False:
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

    per.player_name "This is certainly an incredible find...but MUS-L is right."
    show scientist sad2
    per.player_name "This information is gonna have to wait until we have a better understanding of everything in this place itself."

    "Avery stands dumbfounded at your words; her eyes jump between her probes and devices, the large, collapsed, enveloped, structure, and back to you."
    "After a few beats of silence, she says..."

    show scientist angry
    s "If this isn’t still here by the time we get back, then I swear to both of you my research won’t be the only thing that is incomplete! Hmph!"
    hide scientist with dissolve

    "Avery marches off back down the path you came and through the dense jungle. You and MUS-L stand there in stunned silence."

    show robot at center with dissolve
    r "The mind of a scientist; it’s a hard thing for her to hold back her instincts."
    r "I hope she will not terminate me for my previous recommendation."

    if water_source_visited == False:
        r "I am just...drawn to whatever could be at the source."

    per.player_name "It’s alright. If Avery- Dr. DeWitt should be angry at anyone, it's me."
    per.player_name "I’m sure she’ll be okay though; she’s a lot harder to crack than she gives herself credit for."

    r "Affirmative!"

    scene bg blank with dissolve

    "MUS-L nods his head as you start our trek back through the wet jungle."
    "A short walk later, you’re able to meet up with Avery, although she isn’t exactly in the speaking mood."
    "You continue to go back through the entrance you found and start hiking up through more rocky terrain."

    scene bg waterfall with dissolve

    if water_source_visited == False:
        jump water_source

    else:
        jump chap_2_end

label water_source_puzzle:
    "Now to move those rocks..."
    hide robot with dissolve
    call screen water_source_controls with dissolve

label water_source_solved:
    "MUS-L’s large form strains against the rocks as you prepare to quickly move across the newly opened pathway to the tree."
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

    per.player_name "MUS-L, what do you mean a signal? And are you certain that it’s coming from the tree?"

    r "I’m sure Captain; my sensors are reading some sort of frequency and...I feel as if it’s trying to...communica-"
    hide robot with dissolve

    "MUS-L suddenly jerks his arms up and begins emitting loud noises from his vocal outputs."
    "He begins to move erratically, lifting himself out of the water and moving quickly across the now cleared path."

    per.player_name "Ah no no no no, Avery we need to stop whatever’s happening right now!"

    show scientist shocked
    s "Yes Captain!"

    hide robot with dissolve
    hide scientist with dissolve

    "The two of you hastily restrain MUS-L, although the robot nearly overpowers you."
    "MUS-L's face pulses and flashes wildly until he slows to a stop."

    show robot happy with dissolve
    r "I..."

    per.player_name "How are you feeling?"

    r "It seems the worst has passed, although..."

    "MUS-L stares silently into the distance."

    show robot at left with dissolve
    show scientist sad at right with dissolve

    if thicket_visited == False:
        s "I-I think we should head back and investigate the thicket."
        s "There has to be some valuable information in that area."
        s "Plus, this place is starting to make me uneasy..."

    else:
        s "I-I think we should head back..."
        s "This place is starting to make me uneasy..."

    r "But-"

    show scientist angry
    s "We've looked around enough here!"
        
    per.player_name "I think Avery is right."
    per.player_name "It's not safe for any of us to be around that water until we better analyze it."
    per.player_name "We'll leave some scanners around and come back later, okay?"

    r "..."
    r "Alright."

    scene bg blank with dissolve

    "You slowly return the way you had come until you arrive back in the main cavern."

    scene bg waterfall with dissolve

    if thicket_visited == False:
        jump thicket

    else:
        jump chap_2_end