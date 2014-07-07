from sys import exit
inventory = []

lines_and_spaces = "\n   "
line_break = "\n" + "    " + ("-" * 30) + "\n"
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
    You wake up on a beach. You are unsure how you got here. 
    But you're here now so you might as well make the most of it.
    """
beach_setup = """
    To your left, down the beach twenty feet or so, are some big rocks.
    To your right is a set of metal stairs that lead somewhere out of sight.
    In front of you, laying in the sand, is a small wooden box.
    """
beach_choice = """
    ----------------------------                                
    1. look at the box          
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
    + Coin"""                  
cave_choice1 = """
    You walk down the beach towards the big rocks.
    Upon reaching them, you notice the small opening to a cave.
   
    ---------------------------
    1. Enter cave             
    2. Head back to the beach 
    ---------------------------
    """
cave_choice2 = """
    It is pitch black inside the cave. With nothing to light your way, 
    you stumble around in the dark, slipping and falling off a sheer cliff to your death.
    """
stairs_choice1 = """
    You ascend the stairs. As you reach the top you find yourself on a bluff
    overlooking the beach. Beyond the beach is water as far as the eye can see;
    not even another far away island is visible. 
    
    Turning you attention away from the vast ocean and thoughts of your isolation, 
    you gaze upon what is awaiting you atop the bluff; 
    a small house made of clay, and beyond that, a vast jungle.
    
    --------------------------                         
    1. Enter the house        
    2. Explore the jungle    
    3. Head back to the beach
    --------------------------
    """  
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
        print lines_and_spaces, inventory[0:], "\n"
    else:
       print lines_and_spaces, "It looks like you have nothing in your inventory.\n"

def reset():
    global inventory
    inventory = []

def walk_back(place):
    print lines_and_spaces, "You walk back to the", place

def start():
    next = raw_input("> Press ENTER to begin ").lower()
    if next == " ":
        print title
    else:
        print title
    next = raw_input("> Press ENTER to continue").lower()
    if next == " ":
        print intro, beach_setup
        beach()
    else:
        print intro, beach_setup
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
            rocks()
        elif next == "3" or "stairs" in next:
            stairs()
        elif "inventory" in next:
            check_inventory()    
        else:
            print dunno
        
def box():
    print box_choice1 
    while True:
        next = raw_input("> ").lower()
    
        if next == "1" or next == "open":
            box_open()
        elif next == "2" or next == "leave it alone":
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
            beach()
        elif next == "n" or next == "no":
            print lines_and_spaces, "You leave the items where they are and put the box down."
            beach()
        elif "inventory" in next:
            check_inventory()    
        else:
            print dunno
                            
        
def rocks():        
    print cave_choice1
    while True:
        next = raw_input("> ").lower()
        
        if (next == "1" or "cave" in next) and "Torch" not in inventory:
            print cave_choice2
            dead()
        elif next == "2" or "beach" in next:
            walk_back("beach")
            beach()
        elif "inventory" in next:
            check_inventory()    
        else:
            print dunno
      
def stairs():
    print stairs_choice1
    while True:
        next = raw_input("> ").lower()
    
        if next == "1" or "house" in next:
            house()
        elif next == "2" or "jungle" in next:
            jungle()
        elif next == "3" or "beach" in next:
            walk_back("beach")
            beach()
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
            print lines_and_spaces, "Good choice!\n", line_break, intro, beach_setup        
            beach()
        elif next == "n" or next == "no":
            print lines_and_spaces, "Too bad.\n"
            exit(0)
        else:
            print dunno            
        
start()
