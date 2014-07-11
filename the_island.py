from sys import exit
inventory = []

lines_and_spaces = "\n   "
line_break = "\n" + (" " * 4) + ("-" * 28) + "\n"
title = """
                  _____ _             _____     _                 _ 
                 /__   \ |__   ___    \_   \___| | __ _ _ __   __| |              
                   / /\/ '_ \ / _ \    / /\/ __| |/ _` | '_ \ / _` |
                  / /  | | | |  __/ /\/ /_ \__ \ | (_| | | | | (_| |            
                  \/   |_| |_|\___| \____/ |___/_|\__,_|_| |_|\__,_|
                                                   
                               A  T E X T - B A S E D                
                           E X P L O R A T I O N  G A M E
                                                                      
    _,-':IWWWW\___           _____                       .    .     . . . .__  .
     .:IIIIWWWWWWW\__   _,--'.;IWW\_                           _,-----_ ,-'  `--.
     .:;IIIIIWWWWWWWW\_/    .;IIWWIW\                 .   .  ,'  ,, _  \     __--
      :;IIIWWWWWWWWWW;:   .:;IIIIWWWW\                      /,,__--'  ,--_ _'  \.
       .:;IIWWWWWWWWWW;.   :;IIIIIWWWW\__             .   ._--' _-   /   )`__  `-.
        ::IIIWWWWWWWWW:.   .;IIIWWWWWWI:M\_       .     _-'  /    /||@   /@@`__
         ::;;;IIIIW;:.        .:;IIMMMWI:WW\           /  /    /||@@@@@ee@@@@@`__
           .:;;III:             ..:::II::WWW\       .,' /   /||@@@@@@@@@@@@@@@@@\_
                                 .........===~~~~~~~/ /  /||~~~~~~~~~~~~~~~~~~~~~\_
                     ....... __  _ .--- '     -    /  /||-  - -_ --__----__-- _- _
      ...     .........._ - '                      |||    -_  -  -- __-- _ -- -_
    ...................'_                              _    -   __ - __  -_  --  -
    ................ ...__   _     _                       _ -   - __- _-_ --   -_
    ............ ..........--- -____-- ____    _            -      -- __- -    _
    .......      ...........................~~ -----_--_--.- __- ___ _.__ _._ ____-
    ..... .............  ..........................................................
    """
intro = """    
    You wake up on a beach. You are unsure how you got here, 
    but you're here now so you might as well make the most of it. 
    """
beach_text = """
    To your left, down the beach twenty feet or so, are some big rocks.
    To your right is a set of metal stairs that lead somewhere out of sight.
    In front of you, laying in the sand, is a small wooden box. """
beach_choice = """
    ----------------------------                                
    1. Examine the box          
    2. Walk left to the rocks   
    3. Walk right up the stairs 
    ---------------------------- 
    """
box_choice1 = """
    You pick up the small box. A latch is positioned on its front, but no lock.
    
    ------------------
    1. Open box        
    2. Leave it alone 
    ------------------ 
    """
box_choice2 = """
    You open the box. Inside is a folded letter as well as a coin-like object.
   
    -------------------------------
    Will you take the items? (y/n) 
    ------------------------------- 
    """
box_items = """
    You take the items, adding them to your inventory.
    + Letter
    + Coin """
letter_choice = """
    --------------------------------
    Will you read the letter? (y/n)
    --------------------------------
    """
letter = """
    You open the letter and begin to read:
    
    -------------------------------------------------------------------------------------
    If you are reading this letter then you are as lost as I am. 
    
    I woke up here on this beach, the same as you, what seems like eons ago, and have 
    been searching for a way off of this island ever since. I have not found one; at 
    least not at the time of this writing.
    
    There are dangerous traps and illusions littering every square-inch of this island,
    and while I surely haven't uncovered them all I can give you the following advice:
    
    * The Caves: Down the beach you will find a series of caves in the rocks. Not only 
      are these dark, damp tunnels a twisted maze; they are also pitch-dark. I wouldn't 
      recommend entering them without a proper light source, for one misstep could be 
      your death.
    
    * The Jungle: Full of poisonous bugs and ferocious beasts, the jungle atop the bluff 
      is a dangerous place indeed. I would recommend trying to find some sort of antidote
      for the bugs as well as a means to protect yourself from the bigger animals.
      
    Finally, You will find a small coin within this box. Take it with you, for it is the
    key to unlocking the secrets of this island and to finding your way home. 
    
    Keep your wits, for if you do not, you may just lose yourself in this place.
    
    Good luck, and watch your back; HE is always watching. 
    
    S.        
    ------------------------------------------------------------------------------------- 
    
    A bit disturbed, you refold the letter and stuff it into your pocket. 
    
    "What did they mean by, 'HE is always watching?' And who is this 'S.,' anyway? Are They
    still on the island?" 
    
    You try to push these frightening questions out of you mind; if this place is truly
    as dangerous as S. claims, then you will need to focus on remaining calm and alert."""                  
rocks_text = """
    You walk down the beach towards the big rocks.
    Upon reaching them, you notice the small opening to a cave. """   
rocks_choice = """    
    ---------------------------
    1. Enter cave             
    2. Head back to the beach 
    --------------------------- 
    """
cave_death = """
    It is pitch black inside the cave. With nothing to light your way, 
    you stumble around in the dark, slipping and falling off a sheer cliff to your death. """
stairs_text = """
    You ascend the stairs. As you reach the top you find yourself on a bluff
    overlooking the beach. Beyond the beach is water as far as the eye can see;
    not even another far away island is visible. 
    
    Turning you attention away from the vast ocean and thoughts of your isolation, 
    you gaze upon what is awaiting you atop the bluff; 
    a small house made of clay, and beyond that, a vast jungle. """
stairs_choice = """  
    --------------------------                         
    1. Enter the house        
    2. Explore the jungle    
    3. Head back to the beach
    -------------------------- 
    """
house_text = """
    Walking towards the house, you notice that its entrance - a dark wooden door with a 
    large brass knob and knocker - is already slightly ajar. You open it the rest 
    of the way, causing it to emit a low-pitched creak.
    
    The inside of the house is small, consisting of a single room just big enough for the
    items that occupy it: A small bed, a cluttered desk, a bookshelf and, directly in 
    front of you, a fireplace.  
    
    The floor is mostly covered by a large rug that, while ornate, looks as though it 
    has seen better days. """
house_choice = """    
    -------------------------
    1. Examine the bed       
    2. Examine the desk      
    3. Examine the bookshelf 
    4. Examine the fireplace
    5. Examine the rug
    6. Leave the house       
    ------------------------- 
    """
jungle_death = """
    You enter the jungle. Thick trees surround you and the sounds of buzzing insects and
    chirping birds fill your ears. Suddenly, out of nowhere, a Jaguar leaps at you from
    behind a patch of vegetation. 
    
    With nothing to protect yourself, the Jaguar pins you 
    to the ground; sinking its razor sharp teeth into your throat. You just lay there,
    helplessly bleeding out, as the cat eats you alive. 
    
    Sorry. """     
dunno = lines_and_spaces + " I don't know what you mean.\n"
game_over = """
     _____                  _____             
    |   __|___ _____ ___   |     |_ _ ___ ___ 
    |  |  | .'|     | -_|  |  |  | | | -_|  _|
    |_____|__,|_|_|_|___|  |_____|\_/|___|_|  
                                          
          T R Y  A G A I N ? ( Y / N )        
   """      

def check_inventory():
    if len(inventory) > 0:
        print lines_and_spaces, "Current inventory:", inventory[0:], "\n"
    else:
       print lines_and_spaces, "It looks like you have nothing in your inventory.\n"

def reset():
    global inventory
    inventory = []

def walk_back(place):
    print lines_and_spaces, "You walk back to the", place + "."

def start():
    next = raw_input("> Press ENTER to begin ").lower()
    
    if next == " ":
        print title
    else:
        print title
    
    next = raw_input("> Press ENTER to continue").lower()
    
    if next == " ":
        print intro, beach_text
        beach()
    else:
        print intro, beach_text
        beach()            

def beach(): 
    print beach_choice
    while True:
        next = raw_input("> ")   
    
        if (next == "1" or "box" in next) and "Letter" not in inventory:
            box()    
        elif (next == "1" or "box" in next) and "Letter" in inventory:
            print lines_and_spaces, "The box is empty.\n"           
        elif next == "2" or "rocks" in next:
            print rocks_text
            rocks()
        elif next == "3" or "stairs" in next:
            print stairs_text
            stairs()
        elif "inventory" in next:
            check_inventory()    
        else:
            print dunno
        
def box():
    print box_choice1 
    while True:
        next = raw_input("> ").lower()
    
        if next == "1" or "open" in next:
            box_open()
        elif next == "2" or "leave" in next:
            print lines_and_spaces, "You set the box back down and step away."
            beach()
        elif "inventory" in next:
            check_inventory()    
        else:
            print dunno 

def box_open():
    print box_choice2
    while True:
        next = raw_input("> ").lower()
        
        if next == "y" or next == "yes":
            inventory.extend(["Letter", "Coin"])
            print box_items
            read_letter()
        elif next == "n" or next == "no":
            print lines_and_spaces, "You leave the items where they are and put the box down."
            beach()
        elif "inventory" in next:
            check_inventory()    
        else:
            print dunno

def read_letter():
    print letter_choice
    while True:
        next = raw_input("> ").lower()
        
        if next == "y" or next == "yes":
            print letter
            beach()
        elif next == "n" or next == "no":
            print lines_and_spaces, "You should probably read it.\n"
            next = raw_input("> ").lower()
           
            if next == " ":
                print letter
                beach()
            else:
                print letter
                beach()
        else:
            print dunno                        
        
def rocks():        
    print rocks_choice
    while True:
        next = raw_input("> ").lower()
        
        if (next == "1" or "cave" in next) and "Torch" not in inventory:
            print cave_death
            dead()
        elif (next == "1" or "cave" in next) and "Torch" in inventory:
            print cave_text
            cave()     
        elif next == "2" or "beach" in next:
            walk_back("beach")
            beach()
        elif "inventory" in next:
            check_inventory()    
        else:
            print dunno
      
def stairs():
    print stairs_choice
    while True:
        next = raw_input("> ").lower()
    
        if next == "1" or "house" in next:
            print house_text
            house()
        elif (next == "2" or "jungle" in next) and "Machete" not in inventory:
            print jungle_death
            dead()    
        elif (next == "2" or "jungle" in next) and "Machete" in inventory:    
            print jungle_text
            jungle()
        elif next == "3" or "beach" in next:
            walk_back("beach")
            beach()
        elif "inventory" in next:
            check_inventory()    
        else:
            print dunno
            
def house():
    print house_choice
    while True:
        next = raw_input("> ").lower()
        
        if next == "1" or "bed" in next:
            bed()
        elif next == "2" or "desk" in next:
            desk()
        elif next == "3" or "bookshelf" in next:
            bookshelf()
        elif next == "4" or "fireplace" in next:
            fireplace()
        elif next == "5" or "rug" in next:
            print lines_and_spaces, "Even though it's a bit worn, this rug still " \
                                    "really ties the room together.\n"
        elif next == "6" or "leave" in next:
            walk_back("bluff")
            stairs() 
        elif "inventory" in next:
            check_inventory()
        else:
            print dunno                 

def dead():
    reset()
    print game_over
    while True:
        next = raw_input("> ").lower()
        
        if next == "y" or next == "yes":
            print lines_and_spaces, "Good choice!\n", line_break, intro, beach_text        
            beach()
        elif next == "n" or next == "no":
            print lines_and_spaces, "Too bad.\n"
            exit(0)
        else:
            print dunno            
        
start()
