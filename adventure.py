inventory = []
box_taken = False

print """
\tHello, and welcome to my adventure game, which is aptly called, ADVENTURE!
\tIn this game you'll explore a series of different environments,
\tinteracting with the environment in order to solve simple puzzles.
\tWhen you see words in all caps, like THIS, it means that it's a word
\tthat can be used to interact with the game. When you see > you can go ahead
\tand type in one of these words and make the game do things.
\tAnd no, you don't have to type in all caps.
\tAnd that's all there is to it. Have fun!
"""

print"""
\n\t\tA D V E N T U R E
\t\tA Game Of Adventure
\n\tYou wake up on a beach. 
\tYou are unsure how you got here. 
\tBut you're here now so you might as well make the most of it.
\n\tTo your left, down the beach twenty feet or so, are some big rocks.
\tTo your right is a set of metal stairs that lead somewhere out of site.
\tIn front of you, laying in the sand, is a small wooden box.
"""

def beach(): 
    print """
    \tSo, what do you want to do?
    \n\tEXAMINE the box
    \tGo left to the ROCKS
    \tGo right up the STAIRS
    """
    next = raw_input("> ")   
    
    if next == "examine" and not box_taken:
        print "\tYou pick up the small box. A latch is positioned on its front."
        print "\tWill you OPEN the box?"
        next = raw_input("> ")
        if next == "open":
            box()
        else:
            print "I don't know what you mean."
            beach()    
    elif next == "examine" and box_taken:
        print "\tThe box is empty"
        beach()           
    elif next == "rocks":
        rocks()
    elif next == "stairs":
        stairs()
    else:
        print "\tI don't know what you mean."        
        
def rocks():        
    print "\tYou walk down the beach towards the big rocks."
    print "\tUpon reaching them, you notice the small opening to a cave."
    print "\tDo you enter?"
    
def box():
    print "\tYou open the box. Inside is a folded letter as well as a strange coin-like object."
    box_contents = "Letter", "Coin"
    next = raw_input("> ")
    if next == "take":
        inventory.append(box_contents)
        global box_taken
        box_taken = True
        beach()
    else:
        print "\tI don't know what you mean."
        box()
    

        
beach()
print inventory