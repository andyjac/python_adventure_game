inventory = []
box_taken = False

def intro():
    print_with_tab("""
                            A D V E N T U R E
                          A Game of Exploration
                 
    Hello, and welcome to my adventure game, which is aptly called, ADVENTURE!
    In this game you'll explore a series of different environments,
    interacting with the environment in order to solve simple puzzles.

    When you see words in all caps, like THIS, it means that it's a word
    that can be used to interact with the game. When you see > you can go ahead
    and type in one of these words and make the game do things.
    And that's all there is to it. Have fun!
    
                                  ----

    You wake up on a beach. 
    You are unsure how you got here. 
    But you're here now so you might as well make the most of it.

    To your left, down the beach twenty feet or so, are some big rocks.
    To your right is a set of metal stairs that lead somewhere out of site.
    In front of you, laying in the sand, is a small wooden box.
    """)
    beach()

def beach(): 
    print_with_tab("""
    So, what do you want to do?
      
    EXAMINE the box
    Go left to the ROCKS
    Go right up the STAIRS
    """)
    next = raw_input("> ")   
    
    if next.lower() == "examine" and not box_taken:
        print_with_tab("You pick up the small box. A latch is positioned on its front.")
        print_with_tab("Will you OPEN the box?")
        next = raw_input("> ")
        if next.lower() == "open":
            box()
        else:
            print_with_tab("I don't know what you mean.")
            beach()    
    elif next.lower() == "examine" and box_taken:
        print_with_tab("The box is empty.")
        beach()           
    elif next.lower() == "rocks":
        rocks()
    elif next.lower() == "stairs":
        stairs()
    else:
        print_with_tab("I don't know what you mean.")        
        
def rocks():        
    print_with_tab("You walk down the beach towards the big rocks.")
    print_with_tab("Upon reaching them, you notice the small opening to a cave.")
    print_with_tab("Do you ENTER?")
    next = raw_input("> ")
    
def box():
    print_with_tab("You open the box. Inside is a folded letter as well as a strange coin-like object.")
    box_contents = "Letter", "Coin"
    print_with_tab("Will you TAKE the items?")
    next = raw_input("> ")
    if next.lower() == "take":
        print_with_tab("You take the items, adding them to your inventory.")
        print_with_tab("+ Letter")
        print_with_tab("+ Coin")
        inventory.append(box_contents)
        global box_taken
        box_taken = True
        beach()
    else:
        print_with_tab("I don't know what you mean.")
        box()

def print_with_tab(line):
    print "\t", line

intro()
print inventory
