# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Paleontologist")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg field1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show paleontologist happy

    # These display lines of dialogue.

    p "Oh, hello! I didn't see you there. I'm your friendly-neighborhood Paleontologist. On behalf of the {a=https://tmdinosaurcenter.org/}Montana Dinosaur Center{/a}, I hope you enjoy this game."

    p "As we progress, we'll be adding more content, characters and conversations to Dinosaur Baddies."
    
    # This ends the game.

    return
