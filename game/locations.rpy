# Script for location manager and screens in-game
define first_visit = False
define thicket_visited = False
define water_source_visited = False

define go_with_s = False
define go_with_r = False

## Management ###################
label location_manager:
    if per.player_location == "waterfall":
        $ per.player_location = "Waterfall"
        #$ per.update_location("scientist", "Waterfall")
        #$ per.update_location("robot", "Waterfall")
        jump waterfall

    elif per.player_location == "water_source":
        $ per.player_location = "Water Source"
        #$ per.update_location("scientist", "Water Source")
        #$ per.update_location("robot", "Water Source")
        jump water_source

    elif per.player_location == "thicket":
        $ per.player_location = "Thicket"
        #$ per.update_location("scientist", "Thicket")
        #$ per.update_location("robot", "Thicket")
        jump thicket

    if per.player_location == "device_testing":
        jump device_testing

label waterfall:
    stop music fadeout 1.0
    $ snd.play_bg(per.player_location)
    scene bg waterfall with dissolve

    call screen waterfall with dissolve

label water_source:
    $ water_source_visited = True
    if per.chapter_num == 2:
        $ per.player_location = "Water Source"
        $ per.scientist_location = "Water Source"
        $ per.robot_location = "Water Source"
        if not thicket_visited:
            show scientist happy at right with dissolve

            show robot happy at left with dissolve

            y2 "I think you’re right MUS-L, if this water source has properties like what you’re talking about, then finding out more information on where it all comes from could be valuable to better our understanding...all of this."
            
            show scientist sad

            y2 "Dr. DeWitt, I’m sorry but I’m sure we’ll have time to further investigate the data in more detail later."

            show scientist sad2
            s "Oh...yeah, that’s fine I suppose."
            show scientist happy
            s "Maybe we can take some samples and they’ll have some correlation with the plants."

            r "I think this is going to be the start of a way towards the direction of the water flow, Captain. Let’s go through here!"
            
        stop music fadeout 1.0

        scene bg blank with dissolve

        play sound "audio/other/Crumbling_rocks.wav"

        y2 "Wherever we’re going, it feels like it’s starting to get higher."
        y2 "Does anyone feel like it’s getting harder to breathe?"

        r "While I am physically unable to breathe, we have been increasing in elevation levels since we left the bottom of the waterfall area."
        r "I can also confirm that the earth is becoming harder as we have been continuing climbing upward."

        "You pass by small clumps of trees that seem to have more large and flayed branches near the tops."
        stop sound fadeout 1.0
        "The ground becomes harder, more stable, and less wet as large inclines cause you to have to stretch and tug at cliffs and edges of landmasses in order to climb until suddenly..."
        $ snd.play_entering_source()
        "The solemn sound of running water begins to poke at the edges of your ears."

        play sound "<from 0.7>audio/musl/Happy_beep2.wav"
        "MUS-L beeps excitedly."
        r "I believe that we are arriving close to where the source of the water comes from. This should be an interesting discovery!"

        "You charge further ahead towards the sound; eyes peeled for any creatures and another potential discovery of life and uncertain of what you’ll find with your next couple steps."
        "As you begin to take the lead moving closer to the treeline, something massive lies up ahead. You step out into the open, bracing for something unknown."
        
        stop music fadeout 2.0
        scene bg water_source with dissolve
        $ snd.play_bg(per.player_location)

        "Instead of the unknown, you find the largest tree you've seen in your life."
        "It extends for hundreds and hundreds of feet high; the top branches barely able to be seen as they strangely dig into the ceiling of the cave."
        "The trunk extends down with a purple-green tint to its wood and strangely...holes throughout its lower sides as water gushes from them like a fire hydrant."
        "A moat-like pool of water surrounds the base as it stands supported with massive vines upon a thin tower of rocks just large enough to hold the tree aloft."
        "The water  surround the tree like a wide base; however, the water does lead off of a cliff to your right."
        "You didn’t realize exactly how high you had climbed, but now looking out over the rest of the forest...you have a much better view of the size and scope of this place."
        "As you step out, the others join back with equally fascinated thoughts."

        play sound "audio/ch2/Whistle.wav"
        y2 "(whistles)"
        y2 "Whew… well this is weird."
        y2 "Everything we’ve seen so far has been weird, but this might just take the proverbial weird cake."
        y2 "What do you think’s going on here?"

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

        y2 "I don’t know...it might be better if we’re all able to come with you for this one."
        y2 "I don’t like the idea of sending in any crew by themselves even if they can theoretically be assembled again."
        y2 "Let’s just see if we can get past these rocks to get an easier path to the tree. MUS-L, think you could give us a hand sorting this out?"

        play sound "<from 0.7>audio/musl/Happy_beep2.wav"
        "MUS-L beeps proudly."
        r "Yes Captain, although I am going to need some things to assist."
        r "Namely, a better set of hands. These drills are not are going to be effective for shoving, pushing, and pulling."

        y2 "Sure thing."
        y2 "Dr. DeWitt, if you could retrieve MUS-L's other limbs."

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

        y2 "It's alright, Dr. DeWitt."
        y2 "It couldn't have gone far."
        y2 "If we just look carefully..."

        hide scientist with dissolve

        call screen water_source with dissolve

    if per.chapter_num == 3:
        $ per.update_location("robot", "Water Source")
        if not thicket_visited:
            show robot happy at left with dissolve

            show scientist sad2 at right with dissolve

            y2 "Let's go back to the water source, first."

            show scientist sad
            s "But, Captain, my devices-"

            y2 "We'll go check your devices as soon as we're finished with the water source."

            show scientist sad2
            s "Fine..."

            hide robot with dissolve
            hide scientist with dissolve

            stop music fadeout 1.0
            $ snd.play_entering_source()
            scene bg blank with dissolve

            "You travel in silence back to the water source..."

            stop music fadeout 2.0
            scene bg water_source with dissolve
            $ snd.play_bg(per.player_location)

            "You and Avery watch as MUS-L carefully examines the surrounding area."
            "There is something...off about his behavior."
            "It almost looks like he's listening for something."
            "After an uneasy moment of silence, MUS-L turns to the two of you..."

            show robot happy with dissolve
            r "I’m sorry Captain, Dr. DeWitt, but I cannot leave at this moment."
            r "My...directive is enforcing protocol that I stay and further use tools and assessments to better understand the potential of what has transpired."
            r "Captain, as leader of the crew and with company privileges I cannot disobey you except for particular clauses such as this event."
            r "I urge you to stay and continue with the procedure I am following."
            
            y2 "MUS-L, you know we can't do that."
            y2 "There's too much we'd leave unexplored if we stayed here for too long."
            
            show robot at left with dissolve

            show scientist sad at right with dissolve
            s "[per.player_name] is right, MUS-L, we still have no idea what my devices found in the thicket."
            show scientist sad2
            s "Not to mention that area is much safer than...this place..."

            r "..."
            r "Very well."
            r "I will stay behind and investigate on my own."

            y2 "MUS-L..."
            y2 "Is there really no changing your mind about leaving?"

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
            
            y2 "I wish we could spend more time finding out what that is MUS-L, but it's also company protocol that we prioritize the mission above all else."
            y2 "If the only reason we're here is for personal reasons, then we've stayed long enough."
            y2 "Besides, we can’t just leave you behind. You're coming back with us."

            "As you lean forward, MUS-L’s large metal arms reach out and grab yours; squeezing with a force you’ve never felt lay on your body before."
            "MUS-L has never laid a finger on any of you before."
            "The pain shocks you to your core."

            y2 "Agh! MUS-L, you’re hurting me! Let go, please!"

            play sound "<from 2.7>audio/musl/Sad_beep.wav"
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

            play sound "audio/musl/Softlowbeeps.wav"
            "MUS-L beeps quietly."
            r "I believe that what...I’m doing...what has been done...is an order that I cannot override."
            r "To better understand this forest and what it’s capable of is my mission. Its importance cannot be changed."

            show scientist angry
            s "Listen to yourself, MUS-L! This thing has clearly done something to you and it’s not going to stop!"

            y2 "MUS-L, I don’t want to have to do this, but I’m ordering you to come back with us. Please."

            "MUS-L doesn't move."

            s "Come on Captain, there’s nothing more we can do for him."
            s "If he wants to stay, then I say let him. He’s still just a machine after all."
            hide scientist with dissolve

            show robot at center with dissolve
            play sound "<from 2.7>audio/musl/Sad_beep.wav"
            "MUS-L beeps solemnly."
            r "Captain....I hope for your safe return back to the crew."
            r "I will return; one way or another."

            "..."
            "You feel like you should say something to MUS-L..."
            menu:
                "Respond resolutely":
                    y2 "MUS-L...whatever happens, just know that no matter what happens you can come back."
                    y2 "What we want right now is for you to be safe."
                    y2 "...Be careful."

                "Respond bitterly":
                    y2 "We’ll be fine."
                    y2 "Just...do whatever you’ve been ordered to do."

                "Say nothing":
                    "But there is nothing left to say."

            hide robot with dissolve
            scene bg blank with dissolve
            stop music fadeout 2.0

            "You stumble down the steppe in silence; unsure of exactly what happened to your crewmate."
            "Only after breaking past the clearing does Avery speak."
            $ per.player_location = "Waterfall"
            $ snd.play_bg(per.player_location)
            scene bg waterfall with dissolve

            show scientist sad with dissolve
            s "You know...MUS-L doesn’t have any control over what he's doing."
            show scientist sad2
            s "At least...I think he doesn’t."
            s "The corporation never really told us much about how his model is made or designed, but...from when they gave him to us he’s never pulled anything like that before."
            show scientist sad
            s "Do you think he really did see something, somehow?"

            y2 "I don’t know...everything about what’s happening is just making me feel like coming out here and taking this mission was a mistake."
            y2 "I just can’t put my finger on why yet."

            s "Well...whatever happens moving forward, we’ll figure it out together."
            s "All three of us; even if we may not agree on how to figure it out."

            scene bg blank with dissolve
            $ per.player_location = "thicket"
            jump location_manager

        stop music fadeout 2.0
        scene bg water_source with dissolve
        $ snd.play_bg(per.player_location)

        y2 "MUS-L?"

        show robot happy with dissolve
        r "I am here, Captain."

        y2 "There you are!"
        y2 "Are you alright?"
        y2 "Get closer so I can inspect your frame and check if any signals hijacked your mainframe control matrix."

        "MUS-L stands up and walks over before lowering himself so you can closely inspect his features."
        "While the body and outside frame are the same color and shape as before, there is some visible damage near the lower half where something from the tree wrapped itself around him."
        "Strangely, he’s mostly intact other than the small marks left behind. When he turns around, you begin to examine the faceplate; reading out a series of error codes and messages showcasing that something happened to his internal software."

        y2 "Well, whatever happened to you, thankfully didn’t do too much physical damage at least from what I can see."
        y2 "Do an internal report scan and tell me what you think the problem could be."
            
        r "Affirmative Captain, standing by for scan."
        
        "A couple of minutes pass as MUS-L’s eyes flash in and out, blinking as various metallic limbs shift up and down individually then all together."
        "After a while, the light turns back on and quickly MUS-L responds…"
        
        r "Captain, it appears that physical integrity is stable while software protocol shows a previous dip in stability from around the time I was suddenly overcome by...the unknown signal."
        r "The signal, while faint, is also still located at its original focal point by the tree."

        y2 "Okay, hold on."
        y2 "So, we need to stop that signal in order for you to get back to normal right? Do you think ending the signal could shed some light into what’s targeting and affecting you?"

        r "There is a high probability, but that would mean to return to the strongest point of the signal which currently is still…"

        "MUS-L motions towards the tree stuck in place and spewing water still."
        "You sigh knowing that to further the mission and best understand the newness of this place you'd be trekking back to the top."

        y2 "Alright...alright I get what we’re going to need to do. Just give me a hand with everything and it should be alright."

        hide robot with dissolve

        scene bg blank with dissolve

        "You begin preparing for the climb over the unsteady rock bridge MUS-L helped put into place; carefully making sure that with each step you move light enough to not disturb this unsteady walkway."
        play sound "audio/ch3/Crossingrockbridge.wav"
        "As you cross, the rocks move and shift slightly with each step causing some small bits and debris to fall and become caught in the water as it makes its way across and over the large cliffside."
        "Suddenly...a boulder under your feet shifts slightly more than usual…"

        y2 "MUS-L, do...not...move."

        r "Captain...structurally any slight movements would most likely cause this section to loosen the remaining structural integrity in the walkway."
        r "You must hurriedly cross and climb while I attempt to shift my weight to your position."
        r "Are you ready, Captain?"

        y2 "Absolutely not! Don’t do a thing yet MUS-L!"

        stop sound fadeout 1.0

        r "Yes Captain."

        play sound "audio/ch3/Breathing.wav"

        "You feel the beat of a drum ring through your chest as you breathe in and out; in and out."
        "You’re halfway out and there’s only a few more steps needed to reach the tree. You pause and lift your back foot…"

        y2 "Now! Go, go go!"

        stop sound fadeout 1.0

        "You narrowly push off the weight of your body onto your forward foot and leap and bound across the rickety stone."
        "You don’t look back as you fully commit to the sprint before finally reaching the center mass of dirt and start climbing."
        play sound "audio/ch3/Rockfall.wav"
        "Once your feet touch the wall you climb and climb and climb when suddenly..."
        "CRASH"
        "You hear the rocks slide, shift, and collapse into the “sploosh”."
        "You scramble up the climb holding onto dead roots and vines as you try to scamper up the side."
        "Just as one hand feels a solid and level surface you pull with the little bit of strength left and tumble onto the side."
        "Before you have time to relax, though, instincts kick in as you turn over to the side of where you climbed…"
        "You see MUS-L gripping his metal arms into the dirt wall. His eye turns towards you as you see his arms begin to dig and pull their way up with little to no issue."
        "As he arrives at the top, you feel the familiar sense of some sort of presence or force. The plant life seems to thrum with some sort of energy and the water shines as blue and brilliantly as always."

        scene bg water_source with dissolve

        y2 "I really hope that this is going to be worth it otherwise trying to get back is going to be...a little challenging now."
        y2 "MUS-L, what are you reading from the tree? Is it the source like you thought?"

        show robot happy with dissolve
        r "Yes it’s still the source...but it’s a lot stronger than last time. Scans are indicating that it’s coming from the tree!"

        y2 "Don’t move yet then, let me go check this out this time and when it seems safe then follow me."

        r "Executing guard mode. Standing by Captain."

        hide robot with dissolve
        "Upon moving towards the tree, it remains unchanged since last seeing it this close."
        "The knotted vines and roots surround its base while the holes in the tree pour and pour water still like a never ending storm."
        "However...whether these original flowers were here or not, it appears that two colored blooming plants sit next to the tree."
        "To the left, a red blooming pod of coral-like flowers bloom out and around the tree with a vibrant red glow. To the right sits small sprouting purple flowers that also shine a different colored light."

        y2 "MUS-L, you can stand down and approach slowly. I’m not entirely sure what to make of this still so just remain on high alert."

        show robot happy with dissolve
        r "Yes Captain. I also must inform you that the signal’s strength is at its highest point and that...I feel something beginning-"

        "From behind you, you turn and see MUS-L begin to move uncontrollably, flailing his arms while attempting to grasp the floor to remain stable before suddenly...an almost metallic chiming sound booms and resonates out from MUS-L."
        $ puz.sound_replay()
        "You cover your ears in pain as the loud ringing fills your senses as it plays and plays...until the moment it stops."

        y2 "MUS-L, what the hell was that? Did the signal take control again?"

        "There’s a moment of quiet as the light returns across MUS-L’s facial display loadout. You stare, anxious at the thought of what he could say next, thinking about how what he has done or said up to this point could have been influenced by the unknown signal."
        "A few moments later, MUS-L responds…"

        r "No Captain...now I understand a bit more about what has been happening to me."
        r "The signal...it’s not from a machine or from someone else. It’s a cry for help."

        y2 "From who?"

        r "From the forest. We need to help it, and it’s able to communicate through me to you using electromagnetic signals."
        r "The only problem is that communication is limited; we’ll need to use those somehow."
        
        "MUS-L gestures towards the rocks pressed into the cliffside."

        y2 "MUS-L that’s insane! How the hell are you acting so calm about this?"

        r "Because it follows along a path chartered by AstroCorp, if intelligent life needs help then we must first ascertain if it deserves it. That’s what the next mission has been ordered to be."
        r "Here, please use my display readings as a control panel. I will gather what we may need."
        hide robot with dissolve

        "MUS-L starts moving closer towards the tree before you have a chance to panic."
        "He quickly snatches some of the nearby flowers in his hands and then rests at the base of the tree; his back towards the wet bark."

        show robot happy with dissolve
        r "Now Captain, we must figure out the right way to speak to the forest."
        r "I can only use what’s around us so take that into consideration for what I should try to communicate."

        y2 "Whoa whoa whoa, we’re not communicating with anything until I first understand why?"

        "MUS-L sits there still as ever, his display and lit eye looking at you for a moment before beeping affirmatively."

        r "The forest is dying Captain, it needs our help to survive."
        r "If we can save it, we can learn more about it and how it could help humanity’s push forward."
        r "It’s at least worth investigating more thoroughly."

        y2 "..."
        y2 "Let’s try and figure this out then."

        hide robot with dissolve

        $ puz.sound_replay()
        "You listen carefully..."

        $ per.update_health("robot", "Fine")
        #$ per.update_location("scientist", "Thicket")
        #$ per.update_location("robot", "Water Source")
        #$ per.update_health("scientist", "Unknown")
        call screen sound_pattern with dissolve


label thicket:
    $ thicket_visited = True
    if per.chapter_num == 2:
        $ per.player_location = "Thicket"
        $ per.scientist_location = "Thicket"
        $ per.robot_location = "Thicket"
        if not water_source_visited:
            show scientist happy at right with dissolve

            show robot happy at left with dissolve

            y2 "I think you’re right Doctor, we need to keep moving before anything else out of the ordinary finds us sitting around."
            y2 "MUS-L, if we have time I’m sure we’ll be able to make our way back to the source of the water."

            r "I will keep my hope modules at a reasonable expectation, Captain."

            s "I think this is going to be the start of a potential way inside the forest, Captain. Let’s go through here!"
            hide scientist with dissolve

        hide robot with dissolve

        stop music fadeout 1.0
        $ snd.play_entering_thicket()
        scene bg blank with dissolve

        "You make your way through the forest’s opening; the wetness in the air causing an immediate sense of a jungle seeping with moisture."
        "The dark violet earth crunches against the bottoms of your feet. The trees become thicker and denser as you pass over large roots and vines."
        "You walk like this for a while, MUS-L, and Dr. DeWitt occasionally commenting on the strangeness of this bizarre place you've found ourselves in."
        "You pass deeper into the forest."
        "The darkness oozes between the leaves, vines, and trees, turning a once bio-luminescent and warm cave into a dark, dense mass of strange plants."
        play sound "<from 0.5>audio/ch2/Datapad_beeping.wav"
        "Beeeeep. Beeeeeeep. Beeeeeeeeeeeep!"
        "The datapad rings out loud."

        s "We’re getting close, whatever is nearby has a high amount of the platelets and vegetative tissue like the trees by where we first came from."
        s "This data could be the key to unlocking a form of reliable organic food generation; breakthroughs for natural medicinal supplies!"

        "MUS-L walks past you; his eye beams start scanning the surrounding treeline for any potential life forms."
        r "There are currently no potential hostiles or new life forms being detected by my scans Captain."
        r "However, I do sense that the centralized structure here is different in its visuals than the cavern walls from earlier."

        stop music fadeout 2.0
        scene bg thicket with dissolve
        $ snd.play_bg(per.player_location)

        "MUS-L’s flashlight eyes begin to turn on like a spotlight and gaze at a mass of stone and roots up ahead, his eyes revealing something we couldn’t see at first: the stonework was carved and decorated."
        "Purples, grays, blues, and reds faintly dot the stonework like an ancient cave painting. While it’s barely recognizable from the damage; it’s clear that someone...something was depicted on these destroyed ruins."

        y2 "I...I can barely believe what I’m seeing."
        y2 "Doctor, what do you make of this?"
        y2 ".....Doctor?"

        "You turn to Avery, but she just stands there in awe; processing the importance of this discovery."
        "After some quiet couple beats of silence, you begin to snap out of shock. Avery’s voice breaks the tension..."

        show scientist shocked with dissolve
        s "Captain… whatever this forest is, whatever it has done, it’s so much more than what anyone could have expected back home."
        s "We have to study it further; there’s so much we need to understand."
        hide scientist with dissolve

        y2 "I agree, although we still need to be careful as much as we can."
        y2 "We should gather the data that we came here first before diving into anything further."
        y2 "MUS-L, help Dr. DeWitt set up her supplies; I’m going to keep an eye out for anything living in that pile of rubble."

        show robot happy at left with dissolve
        r "Affirmative Captain."
        r "Dr. Dewitt, if you need any of my hands, feel free to take one."
        play sound "audio/musl/MUSL_arm.wav"
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
        if not water_source_visited:
            $ per.update_location("scientist", "Thicket")
            $ per.update_location("robot", "Water Source")
            show robot happy at left with dissolve

            show scientist sad2 at right with dissolve

            y2 "We'll go check on Avery's devices first."

            show scientist sad
            r "Captain, I believe we should-"

            y2 "We'll head over to the water source as soon as we gather our data, alright?"

            r "..."
            r "Very well."

            hide robot with dissolve
            hide scientist with dissolve

            stop music fadeout 1.0
            scene bg blank with dissolve
            $ snd.play_entering_thicket()

            "You travel in silence back to the thicket..."

            stop music fadeout 2.0
            scene bg thicket with dissolve
            $ snd.play_bg(per.player_location)

            "Avery coldly looks over the data collected from the devices, her back purposefully turned away from you and MUS-L."

            y2 "Avery...we should start heading back to the water source soon."

            "Avery makes no reply."

            y2 "We need to look into what's happening to MUS-L."
            y2 "..."
            y2 "Avery...please, think about what this all means? What AstroCorp is trying to do here when we don’t even know what this thing is and how it works?"
            y2 "I know you wanna find all of this out too and that’s why trying to figure out what happened with MUS-L could be so important!"

            show scientist angry with dissolve
            s "Captain, what you are saying would mean that MUS-L has had a vision akin to something based not off of science or reason."
            s "He’s mechanical; whatever this thing is understands how MUS-L functions and is using him to doubt us and the mission!"
            show scientist at right with dissolve
            
            show robot happy at left with dissolve
            r "Do you not believe what happened to me Doctor?"

            show scientist sad2
            s "MUS-L...it’s just impossible to believe."
            s "What you’re saying makes absolutely no sense and it’s clear to me that something is starting to happen to you and that’s dangerous…"
            
            y2 "This whole place is dangerous Avery, that’s exactly why it’s important we all stick together and try to find whatever deeper meaning could be understood by something supposedly this sentient and alive."

            "A moment of silence falls over the three of you with Avery looking clearly disturbed and distraught."
            "She’s a scientist, she knows that whatever this thing is could be bigger than what you can comprehend. But..."

            hide robot with dissolve
            
            show scientist at center with dissolve
            show scientist sad
            s "We still need something though, we need to know why living beings were here and what happened to them."
            s "If we don't try to figure it out now we might end up like whatever made those crumbled structures."
            show scientist sad2
            s "Please...we need to know the history before moving towards the future."

            y2 "...I’m sorry Avery, but there’s something that happened right here right now to MUS-L that changes a lot about what we think we know."
            y2 "Now please, just stay with us and help us figure this out together."

            "Avery begins to move towards you before stopping still, her head falling to the floor. You feel the shame and hurt in her steps as she begins to turn around and walk towards the structure."

            s "I...I can’t do that. I’m sorry, but if you’re not willing to see how lost we are then I can’t call you my captain anymore."

            "..."
            "You feel like you should say something to Avery..."
            menu:
                "Respond resolutely":
                    y2 "Avery...we’re not lost. We just need a little bit more time to figure things out."

                "Respond bitterly":
                    y2 "Fine...if you’re not going to be able to understand my decision then leave."

                "Say nothing":
                    "But you can't find the right words."

            hide scientist with dissolve
            play sound "audio/other/Avery_stomping.wav"
            "You watch as Avery steps into the dense foliage until the swaying of brush and branches stops still, knowing that she’s gone."

            show robot happy with dissolve
            r "Captain, I know this decision was difficult but Avery only chose to believe in something just as we did. I’m sure we may yet find her again soon."

            y2 "...Let’s just focus on figuring out exactly what happened to you."

            hide robot with dissolve

            stop music fadeout 1.0
            scene bg blank with dissolve
            $ snd.play_entering_thicket()

            "The two of you leave the thicket and head back to the water source."

            $ per.update_location("scientist", "Thicket")
            $ per.update_health("scientist", "Unknown")
            $ per.player_location = "water_source"
            jump location_manager

        $ snd.play_entering_thicket()
        $ per.player_location = "Thicket"
        "Following the path back through the brush you travel through the dense foliage once more; your feet aching and sore from what could be hours or even days of traveling. Trying to measure distance and time here feels like it’s moving slower and faster at the same time."
        "You finish off the remaining food you carried as you eventually reach the familiar structure once more."

        stop music fadeout 2.0
        scene bg thicket with dissolve
        $ snd.play_bg(per.player_location)

        "The devices Dr. DeWitt left on the foliage and vines near the outskirts of the rubble flash a familiar color, signaling they’ve completed their scans."

        if water_source_visited:
            show scientist shocked with dissolve
            s "Captain!"
            show scientist sad2
            s "...I..."
            show scientist happy
            s "I'm glad you're here."
            s "You're just in time, too, look at this!"
            hide scientist with dissolve

        play sound "audio/other/Avery_stomping.wav"
        "Avery moves towards them excitedly; you can see that even through the immense weight of the unknown around you, her thirst for knowledge knows no bounds."

        show scientist happy with dissolve
        "This is it, Captain! I finally have the molecular structure of the plants as well as more in-depth readings!"
        "It appears that the plant matter’s elemental makeup is similar to that of rubber or aluminum, leading to both very malleable and strong fibrous cells."
        show scientist sad2
        "...Hm."

        "Avery stops for a moment; adjusting her datapad and falling silent before staring intently at the datapad and the other devices."

        y2 "Avery, what else are you able to make out?"
        y2 "...Avery?"

        show scientist sad
        s "This...forest is alive just like we thought; but it’s connected somehow."
        show scientist sad2
        s "The cells are...moving constantly, like writhing snakes. They're able to disconnect and attach themselves to one another like how a stem cell can form its shape to match and replicate other cells."
        s "This place...it has this appearance for a reason, but with enough focus the vines and trees could bend and shift if they wanted to...But that would mean this place is capable of so much more…"

        y2 "Okay...so you’re saying it’s alive {i}and{/i} it has done what exactly? Has it been holding back being able to do something to us...does it even know we’re here?"

        show scientist sad
        s "I...I don’t know, but whatever this place is it certainly could qualify under the corporations clause on finding sentient life."
        s "In order to know for sure though, I feel like whatever’s over there might have some answers."

        "Avery points towards the ruined and tumbled structures ahead."

        y2 "...Look, as long as we promise each other to stick together...{i}and{/i} we’re careful...{i}and{/i} we don’t do anything stupid...then let’s try and figure things out."
            
        show scientist happy
        stop music fadeout 2.0
        s "Lead the way, Captain!"

        hide scientist with dissolve
        $ snd.play_entering_thicket()

        "Stepping over the vines and mounds of roots, you step slowly and carefully towards the ruins."
        stop music fadeout 2.0
        "As you begin to approach, a sickening fear begins to fill the pit in your chest and throat."
        $ snd.play_bg(per.player_location)
        play sound "audio/ch3/Heartbeats.wav"
        "The feeling of fear that an animal in the wilderness feels when being hunted...no other way of describing the immense feeling of being watched could fill your mind."
        "Avery felt it too; her eyes went wide with this sudden pressure as you approached. But you press on…"

        y2 "Whatever you do...be as quiet and slow as you can."

        scene bg blank with dissolve

        "Avery nods as you continue; silent step followed by silent step."
        "Getting closer to the ruins, you see now that the building’s previous design and decor has been violently sundered and nearly all of the once-near recognizable art has faded with time."
        "You get closer, the mound of vine and root now closer suddenly seeing it gyrate slowly; like it was breathing."
        "You are so close now that the smell of something...rotten begins to take notice in the air. You try to get even closer and peek further in; your head maybe two or three feet from this wound up mass."
        "Inside...the remains of something once alive but now turned into new life. Fungus-like balls of spores and purple and red flowers rest over the bones and bodies of things once living." 
        "As you lead in further and turn back to warn Avery to move back, you hear the doctor wince in pain."
        "You look down as you see her foot start to bleed on the smallest spine of a vine."
        "You reach out to help, but before you know it…"
        play sound "audio/other/flowerattack.wav"
        "A clicking...then a hiss."
        "A small flower lined with serrated teeth lunges from the mound and leaps at Avery."
        "You go to shove her out of the way, but before you can reach her it whips around you."
        play sound "audio/ch3/bone_crack.wav"
        "After a loud {i}crunch{/i} Avery begins to cry out..."

        play sound "audio/other/Avery_scream.wav"
        s "MY ARM! M-MY ARM!"
        $ per.player_location = "Waterfall"
        $ per.update_location("scientist", "Waterfall")
        $ per.update_health("scientist", "Injured")
        $ per.update_health("robot", "Unknown")

        "Avery falls to the ground and wails. You rush to carry her away as fast as you can run."
        "You turn back...but whatever came for her had disappeared back into the mound."

        s "CAPTAIN...PLEASE HELP ME!!"

        y2 "Avery! You gotta stay with me, please! I’m gonna do everything I can!"

        play sound "audio/ch3/Avery_wailing.wav"
        "The blood drips down her torso and falls soaking into the violet earth. Her screams and wailing fill your ears and terror starts to creep in at the thought of how you’ve never seen anything like that until now."
        "This place’s predators could be hiding anywhere or have been following this whole time."

        $ snd.play_bg(per.player_location)

        scene bg waterfall with dissolve

        "Your journey back was shockingly brief. You would have questioned how you travelled such a vast distance in mere minutes if Avery wasn't rapidly losing consciousness in your arms."
            
        s "My medical kit...pull out my medical kit quickly..."

        stop sound fadeout 2.0

        "You lay her down as gently as you can onto an open patch of dirt by various small shrubbery and jungle trees."
        "Her temperature is starting to burn up and her wound is bleeding profusely through the gauze."
            
        s "Now...take the bottle and...attach the-"

        "Before she can finish she stops and falls limp in your hands."

        y2 "Avery... no, Avery, you gotta tell me what I need to do!!"

        "You look at her old pack, several bottles of liquids and strange small electronic robots are jumbled between gauze tape and small surgical tools."
        "A thin metal pipet loosely reads “cauterizing laser” on the side, along with scalpels and prepping drugs."
        "You struggle to stop the bleeding with what little supplies you have left, but deep down you know she'll quickly succumb to her injuries without proper medical care."
        "Desperately, you look around the cavern. Something had scattered your supplies around the area, throwing most of it into the water..."
        "If you could just somehow make her a replacement arm, the items in Avery's medical kit could take care of the rest."
        "You take a deep breath and survey the area..."
        $ puz.puz_tag = "Arms"

        call screen collect_arms with dissolve

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
                action Function(snd.open_inv), SetVariable("inv.datapad_opened", True), Show("datapad")

        hotspot(0, 101, 585, 573) action SetVariable("per.player_location", "water_source"), Jump("location_manager")
        hotspot(1693, 171, 226, 413) action SetVariable("per.player_location", "thicket"), Jump("location_manager")

screen water_source:
    imagebutton:
        focus_mask True
        idle "puzzles/hand.png"
        hover "puzzles/hand_hover.png"
        action Function(snd.play_click), SetVariable("inv.held_item", "MUS-L's hand"), Hide("water_source"), Jump("found_hand")

    if not inv.datapad_opened:
            imagebutton:
                xalign 0.5 yalign 0.97
                idle "menus/expand.png"
                hover "menus/expand_highlight.png"
                action Function(snd.open_inv), SetVariable("inv.datapad_opened", True), Show("datapad")

screen water_source2:
    if not inv.datapad_opened:
        imagebutton:
            xalign 0.5 yalign 0.97
            idle "menus/expand.png"
            hover "menus/expand_highlight.png"
            action Function(snd.open_inv), SetVariable("inv.datapad_opened", True), Show("datapad")

label found_hand:
    y2 "There it is!"

    "With some effort, you manage to grab the hand out of the water."

    y2 "Now to install it onto MUS-L..."
    $ inv.datapad_opened = True
    $ snd.open_inv()
    call screen datapad with dissolve