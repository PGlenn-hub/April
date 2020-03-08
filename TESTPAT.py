#GAME: "SEARCHING FOR APRIL."

from sys import exit
import time
import random

name = None

invalid = "\nInvalid command. Try something else."
nothing = "\nYou find nothing interesting."
specific = "\nBe more specific."
specific_search = "\nTry being more specific than \"room\" or \"area\" or even just typing \"search\" alone."
windows = "\nThe windows are barred."

command_list = "\nCommands: \"DODGE\", \"ATTACK\", \"GO\", \"OPEN\", \"SEARCH\" and \"LOOK AROUND\".\nThese are the only commands that you need to play the game.\nNOTE: The OPEN and SEARCH commands need an item after it to specifiy what you are opening or searching. Be specific.\nThe GO command is used to move from one //// AREA \\\\\\\\ to another adjacent //// AREA \\\\\\\\, NOT to move your character WITHIN the area.\nType \"LIST\" while playing to have the list of commands.\nType \"CTRL-C\" any#time to quit the game."


curr_prompt = "\n\nWhat do you do?\n\n(Type \"LIST\" for a command recap.)\n"



#Boolean values for Items Found or Triggered Events.


manor_key = False               # Main entrance key described as antique key. Found in cellar() kegs.
manor_unlocked = False          # Allows different elif statement to pass to avoid text redundancy.
Greta_KO = False
prison_key = False              # Prison key described as such. Found on Greta in storage().
prison_unlocked = False         # Allows different elif statement to pass to avoid text redundancy.
flashlight = False              # Needed for killing Greta and finding Silver Dagger, found in kitchen() drawers.
bottle_switch_activated = False # Turns library in dorm_room into alchemy table, allowing to find animal clues to unlock dungeon puzzle where April is. Found in main_room().
silver_dagger = False           # Needed for killing Patronimus and Greta in second fight. Found in prison()



def death(why):
    
    time.sleep(3)
    print "\n", why
    print "\nYou died...\n\nGAME OVER\n"
    print "\n..."
    time.sleep(4)
    print "\nPlay again?"
    choice = raw_input("> ").lower().split()
    if "yes" in choice:
        kitchen()
    else:
        exit(0)

def storage():
    
    global Greta_KO, flashlight 

    print "\n..."
    print "\n//// STORAGE \\\\\\\\"
    while Greta_KO == False:

        if flashlight == False:
            print "\nThe room is pitch black."
            #time().sleep(2)
            print "\nA dark silouette is standing in the middle of the room."
            #time().sleep(2)
        if flashlight:
            print "\nYour flashlight shines on a long haired, barefooted woman dressed in gowns turning your back on you."
        print "\nYou hear an unworldy shreik."
        #time().sleep(3)
        if flashlight == False:
            print "\nFaster than you can react the silouette comes towards you."
            #time().sleep(2)
            print "\nYou feel a cold blade cutting your throat open."
            #time().sleep(2)
            death("You fall to the floor gasping for air while blood gushes out of the wound.")
        if flashlight:
            print "\nShe turns around and starts running towards you with a knife in her hand." 
        print curr_prompt
        choice = raw_input("> ").lower().split()
    

def prison():
    print "You're in the prison."

def balcony():
    print "\nYou're on the balcony."
    print "\nYou can't access it because the game isn't finished."
    print "\nYou're back to the main room."

def kitchen():
    global name, flashlight

    print "\n..."
    #time().sleep(3)
    print "\n//// KITCHEN (FLOOR 0) \\\\\\\\"
    if flashlight == False:
        print "\nThe place is a very dark room with no inside lighting."
    if flashlight:
        print "\nYour flashlight shines on what can only be a kitchen."
    print "\nA barred window lets moonlight shine through."
    if flashlight == False:
        print "\nAt the center of the room is a wooden table."
    if flashlight:
        print "\nAt the center of the room is a wooden table with a hatchet on top."
    print "\nCupboards and drawers in the west corner form an L shaped kitchen area."
    print "\nThe kitchen area has a sink."
    print "\nOn the eastern wall you can distinguish a wooden door."
    if flashlight == False:
        print "\nIt's hard to see anything."
    if flashlight:
        print "\nThere are blood stains on the floor close from the wooden door."
    print curr_prompt
    choice = raw_input("> ").lower().split()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
        elif "go" in choice:
            if "kitchen" in choice:
                print "\nYou're already in the kitchen."
            elif "main" in choice and "room" in choice:
                print "\nYou push the white door open and go back to the main room."
                main_room()
            elif "storage" in choice:
                print "\nYou cautiously open the door."
                storage()
            else:
                print invalid
        elif ["open", "door"] == choice:
            print specific
            print "\nWhich one?"
        elif "open" in choice:
            if "door" in choice:
                if "wooden" in choice:
                    print "\nYou cautiously open the door."
                    storage() 
                elif "white" in choice:
                    print "\nYou push the white door open and go back to the main room."
                    main_room()
                elif "storage" in choice:
                    print "\nYou cautiously open the door."
                    storage()
            else:
                print invalid
        elif ["search"] == choice:
            print specific_search
        elif ["search", "door"] == choice:
            print specific
            print "\nWhich one?"
        elif "search" in choice:
            if "drawers" in choice:
                flashlight = True
                print "\nOne of the drawers has blood stains on it."
                #time().sleep(3)
                print "\nInside are a cell-phone and an LED flashlight. Both are splattered with blood."
                #time().sleep(3)
                print "\nThe cell-phone still has 3% battery and doesn't have a screen-lock."
                #time().sleep(3)
                print "\nThe phone screen is in the text messages menu:"
                #time().sleep(3)
                print "\n"
                print """
                Send to: """, name,"""
                %s help!!! April kidnapped by freak
                can't xplain but u need a silver dagger to kill it.
                Pls this isn't a joke come over I""" % name
                print "\nThe message ends here."
                print "\nYour heart starts pounding: This is Josh's phone."
                print "\nYou turn the flashlight on."
                kitchen()
            elif "table" in choice:
                print "\nOn the table is a blood splattered hatchet."
                print "\nNext to the hatchet is a cut finger."
                print "\nIt was recently cut as the blood hasn't dried yet."
                print "\nHorrific thoughts come to your mind but you notice:\nIt's a male finger."
                print "\nYou fear the worst now."
            elif "door" in choice and "wooden" in choice:
                print "\nYou hear strange undescribable noises in the other room."
            elif "cupboards" in choice:
                print "\nOnly empty cupboards.\n", nothing
            else:
                print nothing
        else:
            print invalid
        print curr_prompt
        choice = raw_input("> ").lower().split()
    kitchen()







#MAIN ROOM: 

def main_room():

    global bottle_switch_activated

    print "\n..."
    #time().sleep(3)
    print "\n//// MAIN ROOM (FLOOR 0) \\\\\\\\"
    print "\nThis is a vast and luxurious room."
    print "\nIt is heavily decorated with paintings, antique weapons and hunting trophies."
    print "\nA fireplace facing the opposite end of the entrance door lights up the\nroom with a warm light."
    print "\nA large balcony on the second floor with six animal statues stands above it. You'd need to\nclimb the stairs to see better."
    print "\nThere is a white door to the left of the fireplace. Further left, still under the balcony,\nis a library with shelves full of books and a few artifacts."
    print "\nTorches on the walls accompany the fireplace creating slow dancing shadows."
    print "\nIn the middle of the room is a large dining table with fine silverwear, plates and glasses."
    print "\nOn the right hand of the fireplace is what you would describe as a living room, with three\nsiting chairs centered around a small table."
    print "\nNext to it again is a medieval metal armor holding a lance."
    print "\nThe stairs leading to the balcony starts right from the west of the entrance of the manor." 
    print "\nOld pictures are hanged in the stairway."
    print "\nA very large stuffed grizzly bear in a threatening pose is up against the east wall."
    print "\nRight in the corner next to the bear, behind the living room, is a full bar with two stools."
    print "\nThe whole place although neatly kept, is covered in dust and cobwebs..."
    print curr_prompt
    choice = raw_input("> ").lower().split()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
        elif "go" in choice:
            if "main" in choice:
                print "\nYou're already in the main room."
            elif "yard" in choice or "outside" in choice:
                print "\nYou exit the manor."
                yard()
            elif "kitchen" in choice:
                print "\nThe door opens with a faint squeak."
                kitchen()
            elif "upstairs" in choice or "up" in choice or "balcony" in choice:
                print "\nYou climb up the stairs."
                balcony()
            else:
                print invalid
        elif ["open", "door"] == choice:
            print "\nWhich one?"
        elif "open" in choice:
            if "kitchen" in choice or ("white" in choice and "door" in choice):
                print "\nThe door opens with a faint squeak."
                kitchen()
            elif "entrance" in choice or ("double" in choice and "door" in choice):
                print "\nYou exit the manor."
                main_room()
            else:
                print invalid
        elif ["search"] == choice:
            print specific_search
        elif ["search", "table"] == choice:
            print specific
            print "\nWhich one?"
        elif ["search", "door"] == choice:
            print specific
            print "\nWhich one?"
        elif "search" in choice:
            if "bar" in choice:
                bottle_switch_activated = True
                print "\nDifferent kinds of liquor compose the bar."
                print "\nYou find a particular bottle with what looks like very thick and dark wine inside."
                print "\nOn the stamp is a wolf sigil decoration, underneath it is written \"Ulfhednar\"."
                print "\nTrying to grab it, it is attached to the shelf but triggers a mechanical sound."
                print "\nThis bottle was some sort of switch."
            elif "library" in choice:
                print "\nOld books and strange objects are on the shelves:\nA bronze world-globe, a human skull and a crow claw, amongst other things."
                print "\nSome of the books have unreadable hieroplyphs."
            elif "table" in choice:
                if "living" in choice and "room" in choice:
                    print "\nA finely decorated table."
                if "dining" in choice or "middle" in choice:
                    print "\nThe table is covered in dust and cobwebs, it looks like it hasn't been touched in a while."
            elif "living" in choice and "room" in choice:
                print "\nFinely decorated furniture. Comfortable chairs and table."
            elif "fireplace" in choice:
                print "\nThe fireplace has no wood in it. You don't understand how there can even be fire..."
            elif "armor" in choice or ("metal" in choice and "armor" in choice):
                print "\nA wolf's sigil is on the breastplate and on the lance. Looks heavy."
            elif "grizzly" in choice or "bear" in choice:
                print "\nIt looks like it's about to slap your head off. Scary."
            elif "pictures" in choice or "pics" in choice or "stairway" in choice or "stairs" in choice:
                print "\nA white haired man appears in most pictures. Other similar haired people appear also.\nThese pictures are very old."
            else:
                print nothing
        else:
            print invalid
        print curr_prompt             
        choice = raw_input("> ").lower().split()
    main_room()


#CELLAR: Items -  Entrance Key.

def cellar():
    global manor_key, prison_key, prison_unlocked

    print "\n..."
    #time().sleep(3)
    print "\n//// CELLAR (FLOOR -1) \\\\\\\\"
    print "\nThe room is a moist and dimly lit stone walled cellar."
    print "\nThe few rays of moonlight coming from the windows"
    print "cast light on what seem to be old wine kegs."
    print "\nA smell of rancid vinegar reaches your nostrils."
    print "\nYou can barely see anything."
    print "\nThere's a bucket next to the wooden door."
    print "\nYou distinguish a heavy steel door at the opposite end"
    print "of the room."
    print curr_prompt
    choice = raw_input("> ").lower().split()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
        elif "go" in choice:
            if "cellar" in choice:
                print "\nYou're already in the cellar."
            elif ("gravel" in choice and "path" in choice) or "path" in choice:
                print "\nYou walk back out."
                gravel_path()
            elif "prison" in choice:
                if prison_unlocked:
                    print "\nYou enter the prison."
                    prison()
                elif prison_key:
                    prison_unlocked = True
                    print "\nThe door unlocks with a mechanical sound."
                    #time().sleep(2)
                    print "\nYou enter the prison."
                    prison()
                elif manor_key:
                    print "\nThis isn't the appropriate key... The door is locked."
                else:
                    print "\nThe door is locked."
            else:
                 print invalid
        elif ["open", "door"] == choice:
                print specific
                print "\nWhich one?" 
        elif "open" in choice:
            if "door" in choice:
                if "wooden" in choice or "cellar" in choice:
                    print "\nYou walk outside."
                    gravel_path()
                elif "steel" in choice or "metal" in choice or "heavy" in choice or "prison" in choice:
                    if prison_unlocked:
                        print "\nYou enter the prison."
                        prison()
                    elif prison_key:
                        prison_unlocked = True
                        print "\nThe door unlocks with a mechanical sound."
                        #time().sleep(2)
                        print "\nYou enter the prison."
                        prison()
                    elif manor_key:
                        print "\nThis isn't the appropriate key... The door is locked."
                    else:
                        print "\nThe door is locked."
            elif "windows" in choice:
                print windows
            elif "prison" in choice:
                if prison_unlocked:
                    print "\nYou enter the prison."
                    prison()
                elif prison_key:
                    prison_unlocked = True
                    print "\nThe door unlocks with a mechanical sound."
                    #time().sleep(2)
                    print "\nYou enter the prison."
                    prison()
                elif manor_key:
                    print "\nThis isn't the appropriate key... The door is locked."
                else:
                    print "\nThe door is locked."
            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice:
                print specific_search
            elif ["search", "door"] == choice:
                print specific
                print "\nWhich one?"
            elif "bucket" in choice:
                print "\nInside you find... Skulls from rodents of some kind. Nothing interesting."
            elif "kegs" in choice:
                if manor_key:
                    print nothing
                else:
                    manor_key = True
                    print "\nYou find an antique key under one of the wine kegs. This might come in handy... You take it with you."
            elif "door" in choice and ("heavy" in choice or "steel" in choice or "metal" in choice):
                print "\nThe steel door has a small barred opening at head's height. The inside of the room is pitch black."
            elif "windows" in choice:
                print windows
            elif "key" in choice:
                print "\nYou have to search something, not the item you're looking for."
            else:
                print nothing
        elif "drink" in choice and ("wine" in choice or "keg" in choice):
            print "\nReally? Now is not the #time()!"
        else:
            print invalid
        print curr_prompt
        choice = raw_input("> ").lower().split()
    cellar()

 
# GRAVEL PATH:

def gravel_path():
    print "\n..."
    #time().sleep(3)
    print "\n//// GRAVEL PATH (FLOOR 0) \\\\\\\\"
    print "\nYou are standing on a gravel path located on a patch of well kept grass."
    print "\nThe property walls surround you on the south and east side."
    print "\nA gigantic pine tree stands in the corner, close to the walls."
    print "\nOn the north side is a wooden door leading underneath the manor."
    print "\nThe gravel marks a left curved way from the gate to the door, ending by lowering steps."
    print "\nThe wind still blows."
    print curr_prompt
    choice = raw_input("> ").lower().split()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
        elif "go" in choice:
            if ("gravel" in choice and "path" in choice) or "path" in choice:
                print "\nYou're already on the gravel path."
            elif "yard" in choice:
                print "\nThe gate is rusty but by pushing hard you manage to open it."
                yard()
            elif "cellar" in choice:
                print "\nYou push and walk through the wooden door."
                cellar()
        elif "open" in choice:
            if "door" in choice or "cellar" in choice:
                print "\nYou push and walk through the wooden door."
                cellar()
            elif "gate" in choice:
                print "\nThe gate is rusty but by pushing hard you manage to open it."
                yard()
            else:
                print invalid
        elif ["search"] == choice:
                print specific_search
        elif "search" in choice:
            print nothing
        else:
            print invalid
        print curr_prompt
        choice = raw_input("> ").lower().split()
    gravel_path()
                
 
#YARD:
# Player starts playing on his own from here on.

def yard():
    global manor_key, manor_unlocked 

    print "\n..."
    #time().sleep(3)
    print "\n///// YARD (FLOOR 0) \\\\\\\\"
    print "\nAs you look around, you find yourself in the yard located in front of the building."
    print "\nFacing north is the main entrance: A large double door made of wood."
    print "\nThe manor is painted white, although #time() has given it a greyish tone."
    print "\nAn alley surrounded by tall trimed bushes on each side leads from the entrance gate to the manor."
    print "\nThe bushes on the east side are cut in the middle by another, yet smaller iron gate."
    print "\nA gloomy light is shined on the manor by the moon."
    print "\nThere are barred windows on the second floor from which warm light can be seen."
    print "\nThe wind blows making the bush leaves sing."
    print curr_prompt
    choice = raw_input("> ").lower().split()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
        elif "go" in choice:
            if "yard" in choice:
                print "\nYou're already in the yard."
            elif ("gravel" in choice and "path" in choice) or "path" in choice:
                print "\nThe gate is rusty but by pushing hard you manage to open it."
                gravel_path()
            elif "manor" in choice or "building" in choice:
                if manor_unlocked:
                    print "\nYou enter the manor."
                    main_room()
                elif manor_key:
                    manor_unlocked = True
                    print "\nThe antique key unlocks the door."
                    #time().sleep(2)
                    print "\nYou enter the manor."
                    main_room()
                else:
                    print "\nThe entrance door is locked."
            elif "gate" in choice:
                print "\n\"Go\" is only used to move from one area to another. There is no need to move WITHIN an area.\nDid you mean \"open\"?"
            else:
                print invalid
        elif "open" in choice:
            if "gate" in choice:
                print "\nThe gate is rusty but by pushing hard you manage to open it."
                gravel_path()
            elif "manor" in choice or "building" in choice or "entrance" in choice or "double door" in choice or "door" in choice:
                if manor_unlocked:
                    print "\nYou enter the manor."
                    main_room()
                elif manor_key:
                    manor_unlocked = True
                    print "\nThe antique key unlocks the door."
                    #time().sleep(2)
                    print "\nYou enter the manor."
                    main_room()
                else:
                    print "\nThe entrance door is locked."
            elif "windows" in choice:
                print windows
            else:
                print invalid
        elif ["search"] == choice:
            print invalid
        elif "search" in choice:
            if "key" in choice:
                print "\nYou have to search something, not the item you're looking for."
            elif "windows" in choice:
                print windows
            else:
                print nothing
        else:
            print invalid
        print curr_prompt
        choice = raw_input("> ").lower().split()
    yard()

        
#WAKE UP TO START GAME:

def wake_up():

    global name

    print "\n..."
    #time().sleep(3)
    print "\n..."
    #time().sleep(3)
    print "\nThis was just a dream..."
    curr_prompt = "\nWould you like to wake up?\n\nType \"yes\" to wake up \"no\" to restart the tutorial.\n"
    print curr_prompt
    choice = raw_input("> ").lower().split()
    while "no" not in choice:
        if "yes" in choice:
            print "\nCommand list:"
            print "\nYou have learned the following commands: \"DODGE\", \"ATTACK\", \"LOOK AROUND\", \"GO\", \"OPEN\" and \"SEARCH\".\nThese are the only commands that you need to play the game."
            print "\nNOTE: The OPEN and SEARCH commands need an item after it to specifiy what you are opening or searching. Be specific."
            print "\nThe GO command is used to move from one //// AREA \\\\\\\\ to another adjacent //// AREA \\\\\\\\, NOT to move your character WITHIN the area."
            print "\nType \"LIST\" while playing to have a command recap.\n"
            scroll = raw_input("\nPress the ENTER KEY to keep scrolling.")
            print "\n..."
            #time().sleep(3)
            print "\n//// CAR \\\\\\\\"
            print "\nYou wake up startled and gasping for air."
            #time().sleep(3)
            print "\nAs your brain turns back on, you start remembering..."
            #time().sleep(4)
            print "\nYou drove 14 hours straight and fell alseep from exhaustion."
            #time().sleep(4)
            print "\nYou check the #time(): 2:53 AM."
            #time().sleep(3)
            print "\nYou remember what you're doing asleep in the driver seat of your car\nin the middle of the night."
            #time().sleep(4)
            print "\n\nYou're searching for your missing daughter April.\n"
            scroll = raw_input("\nPress the ENTER KEY to keep scrolling.")
            print "\nThe last #time() you heard from her was 5 days ago when she went camping\nwith her boyfriend Josh."
            #time().sleep(5)
            print "\nShe should've been back two days ago. You know her damn well, and Josh's a good kid:\nSomething's off." 
            #time().sleep(4)
            print "\nHer phone tracking app's last signal leads here. An isolated and old looking building."
            #time().sleep(4)
            print "\nYou open the car and step outside, the cold hits you."
            #time().sleep(3)
            print "\nYou head for the trunk and grab your baseball bat:\n\n\"Better be safe than sorry...\""
            #time().sleep(4) 
            scroll = raw_input("\nPress the ENTER KEY to keep scrolling.\n\n>") 
            print "\nImposing spiked walls define the property perimeter."
            #time().sleep(3)
            print "\nA double gate with silver ornaments serves as the entrance."
            #time().sleep(3)
            print "\nPeeking through the gate you distinguish what you would describe as a spooky two story manor\nwith two towers located on the north end east and west of the manor."
            #time().sleep(3)
            print "\nChills run down your spine as you push the gate open and enter..."
            #time().sleep(3)
            print "\nThe entrance gate closes behind you with a loud metalic clank.\n"
            scroll = raw_input("Press the ENTER KEY to keep scrolling.\n")
            print "\nThe game starts here, you're on your own now.\n"
            print "\n..."
            time.sleep(5)
            yard()
        print invalid
        print "\nYou should wake up."
        print curr_prompt
        choice = raw_input("> ").lower().split()
    dream()

    
# DREAM TUTORIAL: Here the player learns the following commands:

# -dodge, -attack, Look around, -go LOCATION, -search PLACE and -open PLACE or DOOR. 

def commands():
    fail = "\nCome on, this tutorial is quite simple. Just follow the instructions in the prompt.\n"
    wake = "\n\"YOU GOTTA WAKE UP!\"\n"
    curr_prompt = "\n\nType \"dodge\" to dodge the punch.\n"
    print curr_prompt
    choice = raw_input("> ").lower().split()

# Dodge command

    while "dodge" not in choice:
       print fail
       print curr_prompt
       choice = raw_input("> ").lower().split()
    print "\nYou learned the DODGE command!\n"
    #time().sleep(3)
    curr_prompt = "\n\nType \"attack\" to strike.\n"
    print "\nThe drunk man misses and stumbles.\n"
    #time().sleep(3)
    print "You hear Joe's voice: \"Nice! Now strike him with one of those nasty uppercuts you got!\"" 
    #time().sleep(3)
    print curr_prompt
    choice = raw_input("> ").lower().split() 

# Attack command

    while "attack" not in choice:
        print fail
        curr_prompt = "\nType \"attack\" to strike.\n"
        print curr_prompt 
        choice = raw_input("> ").lower().split() 
    print "\nYou learned the ATTACK command!\n"
    #time().sleep(3)
    print "\nYou hit him so hard he instantly gets knocked out and falls to the ground."
    #time().sleep(3)
    print "\n\nAfter this roughed up \"conversation\", you need a cigarette. But where are they?"
    #time().sleep(3)
    print "\nYou can't find them on you so you tell your co-workers you're going to look for them in your car."
    #time().sleep(3)
    print "\nA quick glance around helps you to locate yourself and know your surroundings." 
    curr_prompt = "\n\nType \"look around\" to have a descripion of where you are.\n"
    print curr_prompt
    choice = raw_input("> ").lower().split() 

# Look around command

    while ["look", "around"] != choice:
        print fail
        print curr_prompt
        choice = raw_input("> ").lower().split()
    print "\nYou learned the LOOK AROUND command!\n"
    #time().sleep(3)
    print "\nThe street is dark and humid."
    #time().sleep(3)
    print "\nVapor is coming out of the sewers and night dwellers are busy doing who knows what."
    #time().sleep(3)
    print "\nYou can faintly here the music coming from within the club."
    #time().sleep(3)
    print "\nYou see your car is at the end of the street."
    #time().sleep(3)
    
# Go to command
 
    curr_prompt = "\n\nType \"go\" and  \"NAME OF LOCATION\" where \"NAME OF LOCATION\" is where you want to go.\nIn this case your CAR.\n"
    print curr_prompt
    choice = raw_input("> ").lower().split()
    while "go" not in choice or "car" not in choice:
        if "go" == choice:
            print "\nOk but WHERE do you want to go?"
            #time().sleep(3)
        elif "go" in choice and "club" in choice:
            print "\nYou're working, this isn't the #time() to party."
            #time().sleep(3)
        print fail
        print curr_prompt
        choice = raw_input("> ").lower().split() 
    print "\nYou learned the GO command!\n\n!!! Note: In game, the GO command is only used to move from one\narea described: \"//// AREA NAME \\\\\\\\\" to another adjacent \"//// AREA \\\\\\\\\".\n"
    #time().sleep(8)
    print "\nYou reach your car."
    #time().sleep(3)
    curr_prompt = "\n\nType \"open\" and \"PLACE\" where \"PLACE\" is what you want to open. For example the car door.\n"
    print curr_prompt
    choice = raw_input("> ").lower().split() 

# Open command
    
    while "open" not in choice or ("car" not in choice and "door" not in choice):
        if "open" in choice and "trunk" in choice:
            print "\nThe trunk is closed and you know for sure the cigarettes are in the car."
            #time().sleep(3)
        elif "open" == choice: 
            print "\nOk but WHAT do you want to open?"
            print specific
            #time().sleep(3)
        print fail
        print curr_prompt
        choice = raw_input("> ").lower().split()          
    print "\nYou learned the OPEN command!\n"
    #time().sleep(3)
    print "\nYou open the car and enter it."
    #time().sleep(3)
    print "\nYou now remember your cigarettes are in the glovebox."
    curr_prompt = "\n\nType \"search PLACE\" where \"PLACE\" is where you're searching. In this case: the glovebox.\n"
    #time().sleep(3)
    print curr_prompt
    choice = raw_input("> ").lower().split()

# Search command

    while "search" not in choice or "glovebox" not in choice:

        if "search" == choice:
            print specific
        elif "search" in choice and "trunk" in choice:
            print "\nThe trunk is closed and you know for sure the cigarettes are in the glovebox.\n"
            #time().sleep(3)
        elif "search" in choice and "car" in choice:
            print specific_search
            print "\nYou know for sure the cigarettes are in the GLOVEBOX.\n"
            #time().sleep(3)
        print fail
        print curr_prompt
        choice = raw_input("> ").lower().split()                   
    print "\nYou learned the SEARCH command!\n"
    #time().sleep(3)
    print "\nYou find the cigarettes and light one up."
    #time().sleep(3)
    print "\nAs you inhale the smoke you ease up a little."
    #time().sleep(3)
    print "\n\"This job sucks.\" you think to yourself as you blow smoke out.\n"
    #time().sleep(3)
    print "You hear a familiar voice: \"So how've you been %s?\"\n" % name
    #time().sleep(3)
    scroll = raw_input("\nPress the ENTER KEY to keep scrolling.\n\n> ")
    print "\nYou turn to your right and on the passenger seat is Joe."
    #time().sleep(4)
    print "\nYour jaw drops."
    #time().sleep(3)
    print "\nYou just can't understand what he's doing in your car. He's eating a slice of pizza as usual.\n"
    #time().sleep(5)
    print "\"Joe?! What on earth are you doing here? How did you get in my car?! You died like 4 years ago!\""
    #time().sleep(5)
    print "\nHe grins at you and says: \"Tell me about it! There's no pizza up there!\""
    #time().sleep(5)
    print "\nHe bites into the slice of pizza and continues: \"I'm here to tell you something...\""
    #time().sleep(4)
    print "\nThis makes no sense to you. You listen, confused and unable to speak.\n"
    #time().sleep(4)
    keep_scrolling = raw_input("\nPress the ENTER KEY to keep scrolling.\n\n> ")
    print "\n\"I'm here to tell you that you gotta wake up!\""
    #time().sleep(4)
    print "\nYou stay silent."
    #time().sleep(3)
    print "\n\"You gotta wake up %s!\"" % name
    #time().sleep(3)
    print "\nHis eyes turn black and his teeth seem to be sharp as razors..."
    #time().sleep(3)
    print "\nA twisted smile appears on his face as he screams louder and louder:"
    #time().sleep(3)
    print wake
    #time().sleep (3)
    print "\nHe starts lascerating you with his arms while repeatidly shouting:"
    #time().sleep(3)
    print wake
    #time().sleep(3)
    print wake
    #time().sleep(3)
    print wake
    #time().sleep(3)
    wake_up()



#DREAM TUTORIAL:

def dream():

    global name
    print "\n\n//// TUTORIAL \\\\\\\\"
    print "\nOn a late thursday night in front of the Shogun club were you work as a bouncer,"
    print "a guy who obviously has had too many drinks starts being aggressive with you."
    #time().sleep(5)
    print "\nHe drunkenly asks you:\n"
    #time().sleep(3)
    print "\"What's your name buddy?\"\n"

    name = raw_input("Name ? > ").strip()
    
    print "\n\"And how much #time() have you been a bouncer here for? I've never seen your face before.\""
    #time().sleep(3)
    print "\nYou answer: \"I moved here a couple of months ago with my...\""
    #time().sleep(3)
    print "\nHe barely listens and starts arguing:"
    #time().sleep(3)
    print "\n\"Why won't you let me in man? My daughter's in there you know.\"\n"
    #time().sleep(3)
    scroll = raw_input("\nPress the ENTER KEY to keep scrolling.\n\n> ")
    print "\nYou calmly respond that he's too drunk to enter,"
    print "and that maybe he souldn't be going out with his daughter on a weekday.\n"
    #time().sleep(5)
    print "\"And who the hell are you to be telling me what to do?\""
    #time().sleep(4)
    print "\nYou patiently answer: \"I'm the guy that has the power to let you in or not.\"\n"
    #time().sleep(3)
    scroll = raw_input("\nPress the ENTER KEY to keep scrolling.\n\n> ")
    print "\nYou've apparently made him mad, and he clumsily tries to punch you.\n"
    #time().sleep(4)
    print "At that moment, you remember Joe, your gym trainer, back in your boxing career days,"
    print "screaming at you while fighting in the ring: \"Dodge the first blow %s!\"\n" % name
    #time().sleep(5)
    commands()




# THE GAME STARTS HERE:

def start():
    print "\n\n\n"
    print "//// SEARCHING FOR APRIL \\\\\\\\"
    print """\n\nWelcome to SEARCHING FOR APRIL !\n
    Instructions : Read the prompt and descriptions carefully.\n
    Enter commands when "> " is displayed.\n
    Type "CTRL-C" at any moment to quit the game.
    Thanks for playing! Good luck and have fun!\n"""
    scroll = raw_input("\nPress the ENTER KEY to keep scrolling.\n\n>")
    dream()
#yard()
#start()   
#cellar()
#wake_up()
#main_room()
kitchen()
