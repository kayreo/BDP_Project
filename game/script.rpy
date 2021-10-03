# The script of the game goes in this file.

# The game starts here.

label start:
    $ inv = Inventory()

    scene bg waterfall

    show scientist happy with dissolve

    s "Sprite test."

    show scientist sad

    s "1."

    show scientist sad2

    s "2."

    show scientist angry
    
    s "3."
    
    show scientist shocked

    s "4."

    show scientist happy at right

    s "height test."

    show robot happy at left

    r "test."

    r "Reset?"

    menu:
        "Yes":
            jump start

        "No":
            r "Continuing."

    hide scientist with dissolve
    hide robot with dissolve

    show screen debug
    if not inv.handheld_unlocked:
        call screen handheld_tutorial with dissolve

    else:
        call screen handheld with dissolve


label device_unlock:
    "Now that your device is unlocked, you can enter your name."
    call screen handheld_tutorial with dissolve

    return

label name_entered:
    python:
        name = name.strip().capitalize()
    if name != "":
        $ player = Player(name)
        $ side = Side_char()
        player.name "Done"
        jump device_testing
    else:
        "You forgot to enter your name..."
        call screen handheld_tutorial with dissolve

label device_testing:
    $ inv.pickup_item("test_item")
    $ player.current_label = "device_testing"
    "Testing device"
    call screen handheld with dissolve
    $ inv.held_item = "Test_item"
    "Testing inventory"
    call screen handheld with dissolve


label location_control:
    if player.current_label == "device_testing":
        jump device_testing