#GAME: "SEARCHING FOR APRIL."

from termios import tcflush, TCIFLUSH
import sys
import time
import random

## TEXT COLOR:
default = "\033[0;37;40m"
bold = "\033[1;37;40m"
gray = "\033[1;30;40m"

red = "\033[1;31;40m"
blue = "\033[1;34;40m"
yellow = "\033[1;33;40m"
cyan = "\033[1;36;40m"
magenta = "\033[1;35;40m"

name = None
player_HP = 6
p_player_HP = "\n%s(Player HP: %s/6.)%s" % (gray, player_HP, default)
invalid = "\n%sInvalid command.%s\n" % (red, default)
nothing = "\nYou find nothing interesting."
specific = "\nBe more specific."
specific_search = "\nTry being more specific than typing \"key\", \"room\" or \"area\" or even just typing \"search\" alone."
windows = "\nThe windows are barred."

go = "%sgo%s" % (blue, default)
search = "%ssearch%s" % (blue, default)
look = "%slook around%s" % (blue, default)
block = "%sblock%s" % (blue, default)
dodge = "%sdodge%s" % (blue, default)
attack = "%sattack%s" % (blue, default)
list0 = "%slist%s" % (blue, default)
paper = "%spaper%s" % (blue, default)

command_list = """
            Command list: 
            
            \"%s\", \"%s\" and \"%s\" are only used in combat sequences.

            \"%s\", \"%s\" and \"%s\" are the only commands that you can use in the game.

            The %s command needs an item after it to specifiy %swhere%s you are searching. Be specific.
            The %s command is used to move from one %s//// AREA \\\\\\\\\%s to another adjacent %s//// AREA \\\\\\\\\%s not to move your character within the area.
            The %s command is useful to refresh the area description.

            Type \"%s\" while playing to have a command recap.""" % (block, dodge, attack, search, go, look, search, yellow, default, go, cyan, default, cyan, default, look, list0)

paper1 = """%s
         \"The walking stag,\"
         \"Leads to the sun setting tower.\"
         \"Therein lies,\"
         \"The path to silver power.\"
         %s""" % (bold, default)

paper2 = """%s
         \"You must shake the walking stag's paw,\"
         \"Before you drink from the silver bottle.\"
         \"Like two sides of the same coin,\"
         \"The mahogany letters are of taste.\"
         \"Like two sides of the same coin,\"
         \"The %sring%s and the %sdagger%s at the %saltar%s meet their fate.\"
         %s""" % (bold, magenta, bold, magenta, bold, magenta, bold, default)

curr_prompt = "\n\nWhat do you do?\n\n%s(Type \"%s%s\" for a command recap.)%s\n" % (gray, list0, gray, default)
battle_prompt = "\n\nWhat do you do?\n\n%s(Type \"%s%s\", \"%s%s\" or \"%s%s\".)%s\n" % (gray, block, gray, dodge, gray, attack, gray, default)
scroll = "\n\n%s(Press any key to keep scrolling.)%s" % (gray, default)


#Boolean values for Items Found or Triggered Events.



manor_key = False               # Main entrance key described as iron key. Found in cellar() kegs.
manor_unlocked = False          # Allows different elif statement to pass to avoid text redundancy.
greta_ko = False
greta_body = False
greta_dead = True
josh_found = False
prison_key = False              # Prison key described as such. Found on Greta in storage().
prison_unlocked = False         # Allows different elif statement to pass to avoid text redundancy.
flashlight = False              # Needed for killing Greta and finding Silver Dagger, found in kitchen() drawers.
pictures = False
bottle_switch_found = False     # Turns desk in dorm_room into altar, allowing to find animal clues to unlock dungeon puzzle where April is. Found in main_room().
bottle_switch_on = False
paw_switch_found = False
paw_switch_on = False
bedroom_trap = False
bedroom_visited = False
balcony_visited = False
barred_door_seen = False
april_found = False
april_freed = False
altar_dispell = False
altar = False
altar_seen = False
rings_taken = False
defense_activated = False
grizzly_killed = False
silver_dagger = False           # Needed for killing Abhartach and Greta in second fight. Found in prison()
abhartach_killed = False
bucket1 = False
bucket2 = False

first = "enemy"
saved_player_HP = None
tin_cans = "three tin cans"

def rand(item):
    rand = random.choice(item)
    return rand

def p_choice():
    global choice
    print curr_prompt
    tcflush(sys.stdin, TCIFLUSH)
    choice = raw_input("> ").lower().split()
    return choice

def p_scroll():
    tcflush(sys.stdin, TCIFLUSH)
    print scroll
    raw_input()

def p_player_HP(hp):
    global player_HP
    print "\n%s(Player HP: %s/6.)%s" % (gray, hp, default)
    return hp
    


# ENNEMY CLASS LIST:

class Enemy:


    def __init__(self, pronouns, possessive_pronoun, personal_pronoun, reflexive_pronoun, enemy_weapons, max_HP, death_str, environment, hint):


        self.pronouns = pronouns
        self.possessive_pronoun = possessive_pronoun
        self.personal_pronoun = personal_pronoun
        self.reflexive_pronoun = reflexive_pronoun    
        self.enemy_weapons = enemy_weapons
        self.enemy_HP = max_HP
        self.max_HP = max_HP
        self.death_str = death_str
        self.environment = environment
        self.hint = hint

battle_hint = "You have a much higher chance of success on your next attack when your ennemies are confused."

#Greta called
Greta_pronouns = ["the woman", "she", "she", "she", "she", "the enemy", "the freak"]

Greta_weapons = ["knife", "knife", "hatchet", "hatchet", "blade", "weapon"]

Greta_environment = ["cupboard", "wall", "door", "furniture"]


Greta = Enemy(Greta_pronouns, "her", "her", "herself", Greta_weapons, 3, "\nShe throws a hard punch to your face and you lose balance.\n\nYou feel a knife ripping through your heart as blood gushes out of your mouth.", Greta_environment, battle_hint)
###

#Greta_ghould called
Greta_ghoul_pronouns = ["the woman", "she", "she", "she", "she", "the ghoul", "the monster"]

Greta_ghoul_weapons = ["knife", "knife", "knife", "blade", "weapon"]

Greta_ghoul_environment = ["tree", "gate", "wall"]

Greta_ghoul = Enemy(Greta_ghoul_pronouns, "her", "her", "herself", Greta_ghoul_weapons, 3, "\nWith a swift kick she makes you trip and fall.\n\nShe immediately jumps on your chest and stabs you repeatidly in the face.", Greta_ghoul_environment, battle_hint)
###

#Abhartach called
Abhartach_pronouns = ["the man", "he", "he", "he", "he", "he", "Abhartach", "the vampire"]

Abhartach_weapons = ["claw-like hand", "razor-sharp finger", "claw", "claw", "claw"]

Abhartach_environment = ["door", "painting", "wall", "wall", "bookshelf", "map", "bed"]

Abhartach = Enemy(Abhartach_pronouns, "his", "him", "himself", Abhartach_weapons, 6, "\nHe kicks your chest and you fall backwards.\n\nHis iron claws slice your throat open.\n\nThe last thing you see before your vision blurs is Abhartach, grining and staring down at you.", Abhartach_environment, battle_hint)
###

#Grizzly called
Grizzly_pronouns = ["the bear", "it", "it", "it", "it", "the grizzly", "the animal"]

Grizzly_weapons = ["fang", "claw", "paw",]

Grizzly_environment = ["table", "bar stool", "hunting trophy", "wall", "door", "shelf"]

Grizzly = Enemy(Grizzly_pronouns, "its", "it", "itself", Grizzly_weapons, 4, "\nYou slide underneath him and hit him hard in the stomach.\n\nThe grizzly grabs you by the arm, lifts you in the air and rips your jaw off.", Grizzly_environment, battle_hint)
###

# GENERIC BATTLE FUNCTION:


def battle(enemy, last_checkpoint, p_weapons):
    global player_HP, enemy_dead, first, saved_player_HP, p_player_HP
    enemy_dead = False
    saved_player_HP = player_HP
    enemy.enemy_HP = enemy.max_HP

    p_scroll()

    actions = ["attacks you", "comes for you", "tries to strike you", "dashes towards you", "runs at you"]
    
    adverbs = ["fearcefully", "aggresively", "mercilessly", "dangerously", "swiftly", "powerfully", "vigorously", "mightily", "decisively"]

    verbs = ["slashing", "swaying", "swinging", "hacking", "lashing", "cutting"]
    
    targets = ["aiming for", "headed for", "going for", "trying to hit", "targetting", "focusing on"]
    
    body_parts = ["chest", "neck", "head", "stomach", "rib-cage", "throat"]
    
    rand_e_weapon = rand(enemy.enemy_weapons)
    rand_target = rand(targets)
    p_rand_body_part = rand(body_parts)
    e_rand_body_part = rand(body_parts)

    
    
    ### ENNEMY STANDING STILL:
    
    enemy_still1 = "\n%s remains still and far from you." % rand(enemy.pronouns).capitalize()
    
    enemy_still2 = "\n%s is standing away from you, facing you with intent." % rand(enemy.pronouns).capitalize()
    
    enemy_still3 = "\nYou gaze at one another, waiting for the first one to move."

    enemy_still4 = "\nYou tensely pace a few feet away from each other."
    
    enemy_still = [enemy_still1, enemy_still2, enemy_still3, enemy_still4]
    
    ### ENNEMY FIRST ATTACK:
    
    enemy_attack1 = "\n%s %s %s your %s." % (rand(enemy.pronouns).capitalize(), rand(actions), rand_target, p_rand_body_part)
    
    enemy_attack2 = "\n%s %s %s with %s %s %s you." % (rand(enemy.pronouns).capitalize(), rand(adverbs), rand(actions), enemy.possessive_pronoun, rand_e_weapon, rand(targets))

    enemy_attack3 = "\n%s %s %s %s away." % (rand(enemy.pronouns).capitalize(), rand(adverbs), rand(actions), rand(verbs))

    enemy_attack4 = "\n%s %s %s." % (rand(enemy.pronouns).capitalize(), rand(actions), rand(adverbs))

    enemy_attack5 = "\nYou see %s %s %s you." % (enemy.personal_pronoun, rand(adverbs), rand(targets))

    
    enemy_attack = [enemy_attack1, enemy_attack2, enemy_attack3, enemy_attack4, enemy_attack5]
    
    ### ENNEMY SECOND ATTACK:
    
    enemy_second_attack1 = "\n%s repeatidly tries to stab you with %s %s." % (rand(enemy.pronouns).capitalize(), enemy.possessive_pronoun, rand(enemy.enemy_weapons))
    
    enemy_second_attack2 = "\n%s immediately strikes again." % rand(enemy.pronouns).capitalize()
    
    enemy_second_attack3 = "\n%s is very close and swings once more." % rand(enemy.pronouns).capitalize()
    
    enemy_second_attack = [enemy_second_attack1, enemy_second_attack2, enemy_second_attack3]
    
    
    ### ENNEMY COUNTER:
    
    enemy_counter1 = "\nThis has given %s the opportunity to hit you back." % enemy.personal_pronoun
    
    enemy_counter2 = "\n%s takes advantage of the momentum to strike back." % (rand(enemy.pronouns).capitalize())
    
    enemy_counter3 = "\n%s pushes you back with force and hits you with a violent slash." % rand(enemy.pronouns).capitalize()
    
    enemy_counter = [enemy_counter1, enemy_counter2, enemy_counter3]
    
    ### ENNEMY STAGGERED:
    
    enemy_staggered1 = "\n%s is staggered for a moment." % rand(enemy.pronouns).capitalize()
    
    enemy_staggered2 = "\n%s seems confused." % rand(enemy.pronouns).capitalize()
    
    enemy_staggered3 = "\nThis has taken %s aback for a short instant." % enemy.possessive_pronoun

    enemy_staggered4 = "\nThis slows %s down enough for you to take a shot." % enemy.personal_pronoun

    enemy_staggered5 = "\n%s is momentarily disorientated." % rand(enemy.pronouns).capitalize()
    
    enemy_staggered = [enemy_staggered1, enemy_staggered2, enemy_staggered3, enemy_staggered4, enemy_staggered5]
    
    
    ### PLAYER ATTACK:
    
    player_attack1 = "\nYou wait for the right moment to jab your %s at your foe." % rand(p_weapons)
    
    player_attack2 = "\nYou aim for %s %s with all your strength." % (enemy.possessive_pronoun, e_rand_body_part)
    
    player_attack3 = "\nYou dash ahead and attack %s." % enemy.personal_pronoun

    player_attack4 = "\nYou sway away %s." % rand(adverbs)

    player_attack5 = "\nYou time your move and swing at %s." % enemy.personal_pronoun
    
    player_attack = [player_attack1, player_attack2, player_attack3, player_attack4, player_attack5]
    
    
    ### PLAYER COUNTER:
    
    player_counter1 = "\nYou opportunistically sway your %s." % rand(p_weapons) 
    
    player_counter2 = "\nFast thinking, you seize the moment strike"
   
    player_counter3 = "\nTaking advantage, you %s sway your %s again." % (rand(adverbs), rand(p_weapons))


    player_counter = [player_counter1, player_counter2, player_counter3]
    
    
    ### PLAYER DODGE:
    
    player_dodge1 = "\nYou quickly lean backwards."
    
    player_dodge2 = "\nYou duck and roll forward with agility."
    
    player_dodge3 = "\nYou roll over to the side attempting to avoid the attack."

    player_dodge4 = "\nYou try to move away fast."
    
    player_dodge = [player_dodge1, player_dodge2, player_dodge3, player_dodge4]
    
    ### PLAYER DODGE SUCCESS:
    
    dodge_hit1 = "\nIt pays off and you evade the %s." % rand_e_weapon
    
    dodge_hit2 = "\nYou hastily dodge the attack."
    
    dodge_hit3 = "\nYou manage to escape at the last moment."

    dodge_hit4 = "\n%s %s misses you by a few inches." % (enemy.possessive_pronoun.capitalize(), rand_e_weapon)
    
    dodge_hit = [dodge_hit1, dodge_hit2, dodge_hit3, dodge_hit4]
    
    ### PLAYER BLOCK:
    
    player_block1 = "\nYou guard with your %s." % rand(p_weapons)
    
    player_block2 = "\nYou aim to fend off the coming attack with your %s." % rand(p_weapons)
    
    player_block3 = "\nYou firmly block, anticipating the next strike."

    player_block4 = "\nYou stand strong, awaiting to deflect the %s." % rand_e_weapon
   
    player_block = [player_block1, player_block2, player_block3, player_block4]
    
    ### PLAYER BLOCK SUCCESS:
    
    block_hit1 = "\nThe %s hits your weapon, you hold strong and push back." % rand_e_weapon
    
    block_hit2 = "\nYou successfully deflect %s attack." % enemy.possessive_pronoun
    
    block_hit3 = "\nThe weapon clanks with yours, protecting your %s." % p_rand_body_part

    block_hit4 = "\nYou accurately prevent the %s from reaching you." % rand_e_weapon
    
    block_hit = [block_hit1, block_hit2, block_hit3, block_hit4]
    
    
    ### PLAYER BLOCK/DODGE FAIL:
    
    db_fail1 = "\nYou miss your step and stumble for a split second."
    
    db_fail2 = "\nThe attack comes much quicker than you thought."
    
    db_fail3 = "\n%s hits so fast you can't react in time." % rand(enemy.pronouns).capitalize()
    
    db_fail4 = "\n%s attacks you in such an angle you can't avoid it." % rand(enemy.pronouns).capitalize()

    db_fail5 = "\nYou slightly slip and fail to properly do so."

    db_fail6 = "\n%s reacts extremely fast and you fail your attempt." % rand(enemy.pronouns).capitalize()

    
    db_fail = [db_fail1, db_fail2, db_fail3, db_fail4, db_fail5, db_fail6]
    
    ### PLAYER MISSED OPPORTUNITY:
    
    opp_miss1 = "\nYou miss a perfect opportunity to strike."
    
    opp_miss2 = "\nYour opponent was staggered, there probably was enough time for attacking."
    
    opp_miss3 = "\n%s was startled, you probably should've taken a shot at %s." % (rand(enemy.pronouns).capitalize(), enemy.personal_pronoun)
    
    opp_miss = [opp_miss1, opp_miss2, opp_miss3]
    
    ### ROOM AFFECTED:
    
    room_aff1 = "\nThe %s behind you is scraped by the %s." % (rand(enemy.environment), rand_e_weapon)
    
    room_aff2 = "\n%s inertia sinks %s %s in the wall." % (enemy.possessive_pronoun.capitalize(), enemy.possessive_pronoun, rand(enemy.enemy_weapons))
    
    room_aff3 = "\nThe %s lands in the %s behind you." % (rand(enemy.enemy_weapons), rand(enemy.environment))

    room_aff4 = "\nA hole is made right where you were standing."

    room_aff = [room_aff1, room_aff2, room_aff3, room_aff4]
    
    
    ### PLAYER ATTACK FAIL:
    
    attack_fail1 = "\nHowever, you get carried away and miss."
    
    attack_fail2 = "\nUnfortunately, you sway too early and hit nothing but air."
    
    attack_fail3 = "\n%s dodges with impressive agility." % rand(enemy.pronouns).capitalize()
    
    attack_fail4 = "\nBut your attempted attack fails."
    
    attack_fail5 = "\n%s deflects your attack with %s %s." % (rand(enemy.pronouns).capitalize(), enemy.possessive_pronoun, rand(enemy.enemy_weapons))
    
    attack_fail6 = "\nPoor judgement makes you miss and hit the %s instead." % rand(enemy.environment)
    
    attack_fail = [attack_fail1, attack_fail2, attack_fail3, attack_fail4, attack_fail5, attack_fail6]
    
    
    ### PLAYER ATTACK SUCCESS:
    
    attack_hit1 = "\nThe %s reaches %s %s." % (rand(p_weapons), enemy.possessive_pronoun, e_rand_body_part)
    
    attack_hit2 = "\nYou feel the %s hitting your opponent's body." % rand(p_weapons)
    
    attack_hit3 = "\nYou hit exactly where you were aiming."

    attack_hit4 = "\n%s is struck by your %s." % (rand(enemy.pronouns).capitalize(), rand(p_weapons))

    attack_hit5 = "\nYou hit %s right in the %s." % (enemy.personal_pronoun, e_rand_body_part)

    attack_hit6 = "\nYour %s meets %s %s." % (rand(p_weapons), enemy.possessive_pronoun, e_rand_body_part)

    attack_hit7 = "\n%s %s gets hit by your %s" % (enemy.possessive_pronoun.capitalize(), e_rand_body_part, rand(p_weapons))


    
    attack_hit = [attack_hit1, attack_hit2, attack_hit3, attack_hit4, attack_hit5, attack_hit6, attack_hit7]
    
    
    ### PLAYER LOW HP:
    
    player_lowHP1 = "\nYou're severely wounded... One more hit and you probably won't make it alive."
    
    player_lowHP2 = "\nYou're feeling dizzy. Better not get hit again..."
    
    player_lowHP = [player_lowHP1, player_lowHP2]
    
   ### PLAYER HURT: 
    
    player_hurt1 = "\n%s %s scrapes your %s." % (enemy.possessive_pronoun.capitalize(), rand_e_weapon, p_rand_body_part)
    
    player_hurt2 = "\nYou feel %s cold %s cutting you open." % (enemy.possessive_pronoun, rand(enemy.enemy_weapons))
    
    player_hurt3 = "\nBlood starts dripping from where you got hit."
    
    player_hurt4 = "\nYou take a hit to the %s. The pain is vivid." % p_rand_body_part

    player_hurt5 = "\n%s %s stings your %s." % (enemy.possessive_pronoun, rand_e_weapon, p_rand_body_part)
    
    player_hurt = [player_hurt1, player_hurt2, player_hurt3, player_hurt4, player_hurt5]
    
    ### ENNEMY LOW HP:
    
    enemy_lowHP1 = "\n%s is panting. Looks like %s's about to collapse." % (rand(enemy.pronouns).capitalize(), rand(enemy.pronouns))
    
    enemy_lowHP2 = "\n%s wounds are pretty bad. %s seems critically hurt." % (enemy.possessive_pronoun.capitalize(), rand(enemy.pronouns).capitalize())
    
    enemy_lowHP = [enemy_lowHP1, enemy_lowHP2]
    
    ### ENEMY HURT:
    
    enemy_hurt1 = "\n%s lets out a hurt gasp." % rand(enemy.pronouns).capitalize()
    
    enemy_hurt2 = "\nThat hurt %s for sure." % enemy.personal_pronoun

    enemy_hurt3 = "\nAn open wound is made where you just hit."
    
    enemy_hurt4 = "\n%s jolts with pain." % rand(enemy.pronouns).capitalize()

    enemy_hurt5 = "\nYou hear %s scream and spasm." % enemy.personal_pronoun

    enemy_hurt6 = "\nA painful growl comes from %s." % enemy.personal_pronoun

    enemy_hurt7 = "\n%s must've felt that one." % rand(enemy.pronouns).capitalize()

    
    enemy_hurt = [enemy_hurt1, enemy_hurt2, enemy_hurt3, enemy_hurt4, enemy_hurt5, enemy_hurt6, enemy_hurt7]
    
    ### CLOSE:

    close1 = "\nYou are both very close to one another."

    close2 = "\n%s is right at arms reach from you." % rand(enemy.pronouns).capitalize()

    close = [close1, close2]

    ### RETURN TO INITIAL STANCE:
    
    init1 = "\nYou both step away, staring carefully at each other."
    
    init2 = "\n%s jumps a few steps back." % rand(enemy.pronouns).capitalize()
    
    init3 = "\n%s gathers %s away from you in a heartbeat." % (rand(enemy.pronouns).capitalize(), enemy.reflexive_pronoun)

    init4 = "\nYou distance yourself from %s." % enemy.personal_pronoun
    
    init = [init1, init2, init3, init4]

    def attack_sequence(p_attack, attack_prob, stagger_prob, counter_prob):
    
        global player_HP, saved_player_HP, enemy_dead, p_player_HP
        invalid_cmd = False
        result = random.randint(0, 100)
        e_stagger = random.randint(0, 100)
        e_counter = random.randint(0, 100)
        print p_attack
    
        if result <= attack_prob:
            enemy.enemy_HP -= 1
            print rand(attack_hit)
    
            if enemy.enemy_HP == 0:
                enemy_dead = True
                return 
    
            print rand(enemy_hurt)
            if enemy.enemy_HP < 2:
                print rand(enemy_lowHP)
    
            if e_stagger < stagger_prob:
                print rand(enemy_staggered)
                print  battle_prompt
                tcflush(sys.stdin, TCIFLUSH)
                choice = raw_input("> ").lower().split()
                if "attack" not in choice and "block" not in choice and "dodge" not in choice:
                    invalid_cmd = True
                while invalid_cmd:
                    print invalid
                    print  battle_prompt
                    tcflush(sys.stdin, TCIFLUSH)
                    choice = raw_input("> ").lower().split()

                    if "attack" in choice or "block" in choice or "dodge" in choice:
                        invalid_cmd = False

    
                if "attack" in choice:
                    attack_sequence(rand(player_counter), 95, 0, 0)
                elif "block" in choice or "dodge" in choice:
                    print rand(opp_miss)
                    print rand(enemy_counter)
                    player_HP -= 1
                    if player_HP == 0:
                        death(enemy.death_str, last_checkpoint, saved_player_HP, enemy.hint)
                    print rand(player_hurt)
                    p_player_HP(player_HP)
    
                    if player_HP < 2:
                        print rand(player_lowHP)

        else:
            print rand(attack_fail)
    
            if e_counter <= counter_prob:
                player_HP -= 1
                print rand(enemy_counter)
    
                if player_HP == 0:
                    death(enemy.death_str, last_checkpoint, saved_player_HP, enemy.hint)
                print rand(player_hurt)
                p_player_HP(player_HP)

                if player_HP < 2:
                    print rand(player_lowHP)
    
    
    def block_sequence(p_block, block_prob, stagger_prob, counter_prob):
        global player_HP, enemy_dead, saved_player_HP, p_player_HP
        invalid_cmd = False 
        result = random.randint(0, 100)
        e_stagger = random.randint(0, 100)
        e_counter = random.randint(0, 100)
        print p_block
    
        if result <= block_prob:
            print rand(block_hit)
    
            if e_stagger <= stagger_prob:
                print rand(enemy_staggered)
                print  battle_prompt
                tcflush(sys.stdin, TCIFLUSH)
                choice = raw_input("> ").lower().split()


                if "attack" not in choice and "block" not in choice and "dodge" not in choice:
                    invalid_cmd = True
                while invalid_cmd:
                    print invalid
                    print  battle_prompt
                    tcflush(sys.stdin, TCIFLUSH)
                    choice = raw_input("> ").lower().split()

                    if "attack" in choice or "block" in choice or "dodge" in choice:
                        invalid_cmd = False
    
                if "attack" in choice:
                    attack_sequence(rand(player_counter), 80, 0, 0)
                elif "block" in choice or "dodge" in choice:
                    print rand(opp_miss)
                    print rand(enemy_counter)
                    player_HP -= 1
                    if player_HP == 0:
                        death(enemy.death_str, last_checkpoint, saved_player_HP, enemy.hint)
                    print rand(player_hurt)
                    p_player_HP(player_HP)
    
                    if player_HP < 2:
                        print rand(player_lowHP)
   
            elif ((e_stagger <= stagger_prob) == False) and (e_counter <= counter_prob):
                print rand(enemy_second_attack)
                print  battle_prompt
                tcflush(sys.stdin, TCIFLUSH)
                choice = raw_input("> ").lower().split()


                if "attack" not in choice and "block" not in choice and "dodge" not in choice:
                    invalid_cmd = True
                while invalid_cmd:
                    print invalid
                    print  battle_prompt
                    tcflush(sys.stdin, TCIFLUSH)
                    choice = raw_input("> ").lower().split()

                    if "attack" in choice or "block" in choice or "dodge" in choice:
                        invalid_cmd = False
                if "attack" in choice:
                    attack_sequence(rand(player_attack), 45, 5, 75) 
    
                elif "block" in choice:
                    block_sequence(rand(player_block), 65, 10, 33)
    
                elif "dodge" in choice:
                    dodge_sequence(rand(player_dodge), 55, 66, 33)
    
            else:
                print rand(close)
                print  battle_prompt
                tcflush(sys.stdin, TCIFLUSH)
                choice = raw_input("> ").lower().split()

                if "attack" not in choice and "block" not in choice and "dodge" not in choice:
                    invalid_cmd = True
                while invalid_cmd:
                    print invalid
                    print  battle_prompt
                    tcflush(sys.stdin, TCIFLUSH)
                    choice = raw_input("> ").lower().split()

                    if "attack" in choice or "block" in choice or "dodge" in choice:
                        invalid_cmd = False

                if "attack" in choice:
                    attack_sequence(rand(player_attack), 85, 10, 80)
                if "block" in choice:
                   block_sequence(rand(player_block), 66, 75, 33) 
                if "dodge" in choice:
                    dodge_sequence(rand(player_dodge), 33, 10, 50)
                    
        else:
            player_HP -= 1
            print rand(db_fail)
            #print rand(enemy_counter)
    
            if player_HP == 0:
                death(enemy.death_str, last_checkpoint, saved_player_HP, enemy.hint)
            print rand(player_hurt)
            p_player_HP(player_HP)
    
            if player_HP < 2:
                print rand(player_lowHP)
    
    
    def dodge_sequence(p_dodge, dodge_prob, stagger_prob, counter_prob):
    
        global player_HP, saved_player_HP, enemy_dead, p_player_HP
        invalid_cmd = False 
        result = random.randint(0, 100)
        e_stagger = random.randint(0, 100)
        e_counter = random.randint(0, 100)
        print p_dodge
    
        if result <= dodge_prob:
            print rand(dodge_hit)
            print rand(room_aff)
    
            if e_stagger <= stagger_prob:
                print rand(enemy_staggered)
                print  battle_prompt
                tcflush(sys.stdin, TCIFLUSH)
                choice = raw_input("> ").lower().split()

                if "attack" not in choice and "block" not in choice and "dodge" not in choice:
                    invalid_cmd = True
                while invalid_cmd:
                    print invalid
                    print  battle_prompt
                    tcflush(sys.stdin, TCIFLUSH)
                    choice = raw_input("> ").lower().split()

                    if "attack" in choice or "block" in choice or "dodge" in choice:
                        invalid_cmd = False
                if "attack" in choice:
                    attack_sequence(rand(player_counter), 100, 0, 0)
                elif "block" in choice or "dodge" in choice:
                    print rand(opp_miss)
                    print rand(enemy_counter)
                    player_HP -= 1
                    if player_HP == 0:
                        death(enemy.death_str, last_checkpoint, saved_player_HP, enemy.hint)
                    print rand(player_hurt)
                    p_player_HP(player_HP)
    
                    if player_HP < 2:
                        print rand(player_lowHP)
                    
            elif ((e_stagger <= stagger_prob) == False) and (e_counter <= counter_prob):
                print rand(enemy_second_attack)
                print  battle_prompt
                tcflush(sys.stdin, TCIFLUSH)
                choice = raw_input("> ").lower().split()

                if "attack" not in choice and "block" not in choice and "dodge" not in choice:
                    invalid_cmd = True
                while invalid_cmd:
                    print invalid
                    print  battle_prompt
                    tcflush(sys.stdin, TCIFLUSH)
                    choice = raw_input("> ").lower().split()

                    if "attack" in choice or "block" in choice or "dodge" in choice:
                        invalid_cmd = False


                if "attack" in choice:
                    attack_sequence(rand(player_attack), 10, 0, 66)

                elif "block" in choice:
                    block_sequence(rand(player_block), 66, 33, 50)

                elif "dodge" in choice:
                    dodge_sequence(rand(player_dodge), 67, 66, 66)
        else:
            player_HP -= 1
            print rand(db_fail)
            #print rand(enemy_counter)
            if player_HP == 0:
                death(enemy.death_str, last_checkpoint, saved_player_HP, enemy.hint)
            print rand(player_hurt)
            p_player_HP(player_HP)
    
            if player_HP < 2:
                print rand(player_lowHP)


###### BATTLE LOOP:

    invalid_cmd = False
    while enemy_dead == False: 
        rand_e_weapon = rand(enemy.enemy_weapons)
        rand_target = rand(targets)
        p_rand_body_part = rand(body_parts)
        e_rand_body_part = rand(body_parts)

        actions = ["attacks you", "comes at you", "tries to strike you", "swings at you", "dashes towards you", "lashes out at you", "moves towards you"]
        
        adverbs = ["fearcefully", "aggresively", "mercilessly", "dangerously", "swiftly", "powerfully", "vigorously", "mightily", "decisively"]

        verbs = ["slashing", "swaying", "swinging", "hacking", "lashing"]
        
        targets = ["aiming for", "headed for", "going for", "trying to hit", "targetting"]
        
        body_parts = ["chest", "neck", "head", "stomach", "rib-cage", "throat"]
        
        rand_e_weapon = rand(enemy.enemy_weapons)
        rand_target = rand(targets)
        p_rand_body_part = rand(body_parts)
        e_rand_body_part = rand(body_parts)

        
        
        ### ENNEMY STANDING STILL:
        
        enemy_still1 = "\n%s remains still and far from you." % rand(enemy.pronouns).capitalize()
        
        enemy_still2 = "\n%s is standing in front of you, facing you with intent." % rand(enemy.pronouns).capitalize()
        
        enemy_still3 = "\nYou gaze at one another, waiting for the first one to move."

        enemy_still4 = "\nYou tensely pace a few feet away from each other."
        
        enemy_still = [enemy_still1, enemy_still2, enemy_still3, enemy_still4]
        
        ### ENNEMY FIRST ATTACK:
        
        enemy_attack1 = "\n%s %s %s your %s." % (rand(enemy.pronouns).capitalize(), rand(actions), rand_target, p_rand_body_part)
        
        enemy_attack2 = "\n%s %s %s with %s %s." % (rand(enemy.pronouns).capitalize(), rand(adverbs), rand(actions), enemy.possessive_pronoun, rand_e_weapon)

        enemy_attack3 = "\n%s %s %s %s away." % (rand(enemy.pronouns).capitalize(), rand(adverbs), rand(actions), rand(verbs))

        enemy_attack4 = "\nYou see %s %s %s you." % (enemy.personal_pronoun, rand(adverbs), rand(targets))

        
        enemy_attack = [enemy_attack1, enemy_attack2, enemy_attack3, enemy_attack4]
        
        ### ENNEMY SECOND ATTACK:
        
        enemy_second_attack1 = "\n%s repeatidly tries to stab you with %s %s." % (rand(enemy.pronouns).capitalize(), enemy.possessive_pronoun, rand(enemy.enemy_weapons))
        
        enemy_second_attack2 = "\n%s immediately strikes again." % rand(enemy.pronouns).capitalize()
        
        enemy_second_attack3 = "\n%s is very close and swings once more." % rand(enemy.pronouns).capitalize()
        
        enemy_second_attack = [enemy_second_attack1, enemy_second_attack2, enemy_second_attack3]
        
        
        ### ENNEMY COUNTER:
        
        enemy_counter1 = "\nThis has given %s the opportunity to hit you back." % enemy.personal_pronoun
        
        enemy_counter2 = "\n%s takes advantage of the momentum to strike back." % (rand(enemy.pronouns).capitalize())
        
        enemy_counter3 = "\n%s pushes you back with force and hits you with a violent slash." % rand(enemy.pronouns).capitalize()
        
        enemy_counter = [enemy_counter1, enemy_counter2, enemy_counter3]
        
        ### ENNEMY STAGGERED:
        
        enemy_staggered1 = "\n%s is staggered for a moment." % rand(enemy.pronouns).capitalize()
        
        enemy_staggered2 = "\n%s seems confused." % rand(enemy.pronouns).capitalize()
        
        enemy_staggered3 = "\nThis has taken your target aback for a short instant."

        enemy_staggered4 = "\nThis slows %s down enough for you to take a shot." % enemy.personal_pronoun

        enemy_staggered5 = "\n%s is momentarily disorientated." % rand(enemy.pronouns).capitalize()
        
        enemy_staggered = [enemy_staggered1, enemy_staggered2, enemy_staggered3, enemy_staggered4, enemy_staggered5]
        
        
        ### PLAYER ATTACK:
        
        player_attack1 = "\nYou wait for the right moment to jab your %s at your foe." % rand(p_weapons)
        
        player_attack2 = "\nYou aim for %s %s with all your strength." % (enemy.possessive_pronoun, e_rand_body_part)
        
        player_attack3 = "\nYou dash ahead and attack %s." % enemy.personal_pronoun

        player_attack4 = "\nYou sway away %s." % rand(adverbs)

        player_attack5 = "\nYou time your move and swing at %s." % enemy.personal_pronoun
        
        player_attack = [player_attack1, player_attack2, player_attack3, player_attack4, player_attack5]
        
        
        ### PLAYER COUNTER:
        
        player_counter1 = "\nYou opportunistically sway your %s." % rand(p_weapons) 
        
        player_counter2 = "\nFast thinking, you seize the moment strike"
   
        player_counter3 = "\nTaking advantage, you %s sway your %s again." % (rand(adverbs), rand(p_weapons))


        player_counter = [player_counter1, player_counter2, player_counter3]
        
        
        ### PLAYER DODGE:
        
        player_dodge1 = "\nYou quickly lean backwards."
        
        player_dodge2 = "\nYou duck and roll forward with agility."
        
        player_dodge3 = "\nYou roll over to the side attempting to avoid the attack."

        player_dodge4 = "\nYou try to move away fast."
        
        player_dodge = [player_dodge1, player_dodge2, player_dodge3, player_dodge4]
        
        ### PLAYER DODGE SUCCESS:
        
        dodge_hit1 = "\nIt pays off and you evade the %s." % rand_e_weapon
        
        dodge_hit2 = "\nYou hastily dodge the attack."
        
        dodge_hit3 = "\nYou manage to escape at the last moment."

        dodge_hit4 = "\n%s %s misses you by a few inches." % (enemy.possessive_pronoun.capitalize(), rand_e_weapon)
        
        dodge_hit = [dodge_hit1, dodge_hit2, dodge_hit3, dodge_hit4]
        
        ### PLAYER BLOCK:
        
        player_block1 = "\nYou guard with your %s." % rand(p_weapons)
        
        player_block2 = "\nYou aim to fend off the coming attack with your %s." % rand(p_weapons)
        
        player_block3 = "\nYou firmly block, anticipating the next strike."

        player_block4 = "\nYou stand strong, awaiting to deflect the %s." % rand_e_weapon
   
        player_block = [player_block1, player_block2, player_block3, player_block4]
        
        ### PLAYER BLOCK SUCCESS:
        
        block_hit1 = "\nThe %s hits your weapon, you hold strong and push back." % rand_e_weapon
        
        block_hit2 = "\nYou successfully deflect %s attack." % enemy.possessive_pronoun
        
        block_hit3 = "\nThe weapon clanks with yours, protecting your %s." % p_rand_body_part

        block_hit4 = "\nYou accurately prevent the %s from reaching you." % rand_e_weapon
        
        block_hit = [block_hit1, block_hit2, block_hit3, block_hit4]
        
        
        ### PLAYER BLOCK/DODGE FAIL:
        
        db_fail1 = "\nYou miss your step and stumble for a split second."
        
        db_fail2 = "\nThe attack comes much quicker than you thought."
        
        db_fail3 = "\n%s hits so fast you can't react in time." % rand(enemy.pronouns).capitalize()
        
        db_fail4 = "\n%s attacks you in such an angle you can't avoid it." % rand(enemy.pronouns).capitalize()

        db_fail5 = "\nYou slightly slip and fail to properly do so."

        db_fail6 = "\n%s reacts extremely fast and you fail your attempt." % rand(enemy.pronouns).capitalize()

        
        db_fail = [db_fail1, db_fail2, db_fail3, db_fail4, db_fail5, db_fail6]
        
        ### PLAYER MISSED OPPORTUNITY:
        
        opp_miss1 = "\nYou miss a perfect opportunity to strike."
        
        opp_miss2 = "\nYour opponent was staggered, there probably was enough time for attacking."
        
        opp_miss3 = "\n%s was startled, you probably should've taken a shot at %s." % (rand(enemy.pronouns).capitalize(), enemy.personal_pronoun)
        
        opp_miss = [opp_miss1, opp_miss2, opp_miss3]
        
        ### ROOM AFFECTED:
        
        room_aff1 = "\nThe %s behind you is scraped by the %s." % (rand(enemy.environment), rand_e_weapon)
        
        room_aff2 = "\n%s inertia sinks %s %s in the wall." % (enemy.possessive_pronoun.capitalize(), enemy.possessive_pronoun, rand(enemy.enemy_weapons))
        
        room_aff3 = "\nThe %s lands in the %s behind you." % (rand(enemy.enemy_weapons), rand(enemy.environment))

        room_aff4 = "\nA hole is made right where you were standing."
        
        room_aff = [room_aff1, room_aff2, room_aff3, room_aff4]
        
        
        ### PLAYER ATTACK FAIL:
        
        attack_fail1 = "\nHowever, you get carried away and miss."
        
        attack_fail2 = "\nUnfortunately, you sway too early and hit nothing but air."
        
        attack_fail3 = "\n%s dodges with impressive agility." % rand(enemy.pronouns).capitalize()
        
        attack_fail4 = "\nBut your attempted attack fails."
        
        attack_fail5 = "\n%s deflects your attack with %s %s." % (rand(enemy.pronouns).capitalize(), enemy.possessive_pronoun, rand(enemy.enemy_weapons))
        
        attack_fail6 = "\nPoor judgement makes you miss and hit the %s instead." % rand(enemy.environment)
        
        attack_fail = [attack_fail1, attack_fail2, attack_fail3, attack_fail4, attack_fail5, attack_fail6]
        
        
        ### PLAYER ATTACK SUCCESS:
        
        attack_hit1 = "\nThe %s scratches %s %s." % (rand(p_weapons), enemy.possessive_pronoun, e_rand_body_part)
        
        attack_hit2 = "\nYou feel the %s hitting your opponent's body." % rand(p_weapons)
        
        attack_hit3 = "\nYou hit exactly where you were aiming."

        attack_hit4 = "\n%s is struck by your %s." % (rand(enemy.pronouns).capitalize(), rand(p_weapons))

        attack_hit5 = "\nYou hit %s right in the %s." % (enemy.personal_pronoun, e_rand_body_part)

        attack_hit6 = "\nYour %s meets %s %s." % (rand(p_weapons), enemy.possessive_pronoun, e_rand_body_part)

        attack_hit7 = "\n%s %s gets hit by your %s" % (enemy.possessive_pronoun.capitalize(), e_rand_body_part, rand(p_weapons))


        
        attack_hit = [attack_hit1, attack_hit2, attack_hit3, attack_hit4, attack_hit5, attack_hit6, attack_hit7]
        
        
        ### PLAYER LOW HP:
        
        player_lowHP1 = "\nYou're severely wounded... One more hit and you probably won't make it alive."
        
        player_lowHP2 = "\nYou're feeling dizzy. Better not get hit again..."
        
        player_lowHP = [player_lowHP1, player_lowHP2]
        
        ### PLAYER HURT: 
        
        player_hurt1 = "\n%s %s scrapes your %s." % (enemy.possessive_pronoun.capitalize(), rand_e_weapon, p_rand_body_part)
        
        player_hurt2 = "\nYou feel %s cold %s cutting you open." % (enemy.possessive_pronoun, rand(enemy.enemy_weapons))
        
        player_hurt3 = "\nBlood starts dripping from where you got hit."
        
        player_hurt4 = "\nYou take a hit to the %s. The pain is vivid." % p_rand_body_part

        player_hurt5 = "\nThe %s stings your %s." % (rand_e_weapon, p_rand_body_part)
        
        player_hurt = [player_hurt1, player_hurt2, player_hurt3, player_hurt4, player_hurt5]
        
        ### ENNEMY LOW HP:
        
        enemy_lowHP1 = "\n%s is panting. Looks like %s's about to collapse." % (rand(enemy.pronouns).capitalize(), rand(enemy.pronouns))
        
        enemy_lowHP2 = "\n%s wounds are pretty bad. %s seems critically hurt." % (enemy.possessive_pronoun.capitalize(), rand(enemy.pronouns).capitalize())
        
        enemy_lowHP = [enemy_lowHP1, enemy_lowHP2]
        
        ### ENEMY HURT:
        
        enemy_hurt1 = "\n%s lets out a hurt gasp." % rand(enemy.pronouns).capitalize()
        
        enemy_hurt2 = "\nThat hurt %s for sure." % enemy.personal_pronoun

        enemy_hurt3 = "\nAn open wound is made where you just hit."
        
        enemy_hurt4 = "\n%s jolts with pain." % rand(enemy.pronouns).capitalize()

        enemy_hurt5 = "\nYou hear %s scream and spasm." % enemy.personal_pronoun

        enemy_hurt6 = "\nA painful growl comes from %s." % enemy.personal_pronoun

        enemy_hurt7 = "\n%s must've felt that one." % rand(enemy.pronouns).capitalize()

        
        enemy_hurt = [enemy_hurt1, enemy_hurt2, enemy_hurt3, enemy_hurt4, enemy_hurt5, enemy_hurt6, enemy_hurt7]
        
        ### CLOSE:

        close1 = "\nYou are both very close to one another."

        close2 = "\n%s is right at arms reach from you." % rand(enemy.pronouns).capitalize()

        close = [close1, close2]

        ### RETURN TO INITIAL STANCE:
        
        init1 = "\nYou both step away, staring carefully at each other."
        
        init2 = "\n%s jumps a few steps back." % rand(enemy.pronouns).capitalize()
        
        init3 = "\n%s gathers %s away from you in a heartbeat. You're ready to react." % (rand(enemy.pronouns).capitalize(), enemy.reflexive_pronoun)

        init4 = "\nYou distance yourself from %s." % enemy.personal_pronoun
        
        init = [init1, init2, init3, init4]



        if "enemy" in first:
            if invalid_cmd == False:
                print rand(enemy_attack)
            print  battle_prompt
            tcflush(sys.stdin, TCIFLUSH)
            choice = raw_input("> ").lower().split()
            
            if "attack" in choice: 
                attack_sequence(rand(player_attack), 10, 10, 80)
            elif "block" in choice:
                block_sequence(rand(player_block), 66, 15, 66)
            elif "dodge" in choice:
                dodge_sequence(rand(player_dodge), 66, 50, 66)
            else:
                print invalid
                invalid_cmd = True
                continue
            if enemy_dead == False:
                print rand(init)

        elif "player" in first:
            rand(enemy_attack)

            if invalid_cmd == False:
                print rand(enemy_still)
            print  battle_prompt
            tcflush(sys.stdin, TCIFLUSH)
            choice = raw_input("> ").lower().split()

            if "attack" in choice:
                attack_sequence(rand(player_attack), 75, 5, 66)
            elif "block" in choice:
                print rand(enemy_attack)
                block_sequence(rand(player_block), 50, 10, 50)
            elif "dodge" in choice:
                print rand(enemy_attack)
                dodge_sequence(rand(player_dodge), 50, 33, 66)
            else:
                print invalid
                invalid_cmd = True
                continue
            if enemy_dead == False:
                print rand(init)

        invalid_cmd = False
        first = rand(["player", "enemy", "enemy", "enemy"])
    p_scroll()


def death(why, last_checkpoint, HP, hint):
    global bottle_switch_on, paw_switch_on, altar, altar_seen, bedroom_trap, april_found, altar_dispell, player_HP, defense_activated, april_freed
    print why
    p_scroll()
    print "\n%sYou died...\n\nGAME OVER%s\n" % (red, default)
    print "\nHint:", hint
    print "\n..."
    print "\nPlay again?\n"
    choice = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()
    while True:
        if "yes" in choice and "no" not in choice:
            april_found = False
            defense_activated = False
            bottle_switch_on = False
            paw_switch_on = False
            bedroom_trap = False
            altar = False
            altar_seen = False
            altar_dispell = False
            april_freed = False
            if player_HP == 0:
                player_HP = saved_player_HP
            print "\nYou will restart at the last checkpoint."
            print "\n%sPlayer HP: %s/6%s" % (bold, player_HP, default)
            p_scroll()
            last_checkpoint()

        elif "no" in choice and "yes" not in choice:
                exit(0) 
        else:
            print invalid
        print "\n\nPlay again?\n"
        choice = raw_input("\n(Type \"yes\" or \"no\".)\n\n> ").lower().split()


def ending():
    print "\n..."
    time.sleep(3)
    print "\n%s//// CAR \\\\\\\\%s" % (cyan, default)
    print "\nAs soon as you close the gate and finally step outside of the manor you find yourself in front of a wolf."
    print "\nA very powerful aura emanates from it, his eyes are as blue as a frozen river."
    print "\nThe wolf is way bigger than an average one, probably your height."
    print "\nHe barks once at you and gazes into your eyes. He then steadily walks up to you."
    p_scroll()
    print "\nA few seconds after he starts lickings some of your wounds."
    print "\nHe howls very loudly into the night and finally jumps over the gate and disappears into the yard." 
    print "\nYou're shaking from what just happened while you calmly fasten April in the passenger seat."
    print "\nShe's still fast asleep, you gently caress her hair and finally rest from this incredible journey."
    print "\nA pat on your pocket reminds you of the rings you found, at least these will help you for a few\nmonths until you find a new job."
    print "\nThe sun is starting to rise in the east, you turn the engine on."
    p_scroll()
    print "\nAs you drive away, you notice in the rear mirror a blue light coming from the manor." 
    print "\nYou distinguish the light growing bigger and bigger until you see it bursting in a loud and huge\nblue spherical explosion where the manor was."
    print "\nYou feel the shockwave passing you and you hear a wolf howling one last time in the distance..."
    p_scroll()
    print "\n\n\n\t\t%sTHE END" % red
    print "\n\t\tCongratulations!"
    print "\n\n\n\n\n"
    exit(0)


def east_tower():
    global april_found, altar_dispell, april_freed, bucket1, bucket2
    print "\n..."
    time.sleep(3)
    print "\n%s//// EAST TOWER (FLOOR 3) \\\\\\\\\%s" % (cyan, default)
    if april_found:
        if altar_dispell == False and april_freed == False:
            print "\nApril is lying there, asleep."
        elif altar_dispell and april_freed == False:
            april_freed = True
            print "\nYou reach the top and this time %sApril is awake%s, sitting on the bunk bed, crying." % (red, default)
            print "\nThe only thing left of the vine are the cuts on April's skin."
            print "\nYou rush to her and hold her tight in your arms."
            print "\nYou hold back tears of relief as you whisper to her ears:"
            print "\n\"It's over sweety, daddy's here. You're safe now.\""
            print "\nShe sobs even harder after she realizes you're there."
            p_scroll()
            print "\nAfter a few moments she starts explaining:"
            print "\n\"I don't know what happened, something happened to Josh, and... my head's dizzy...\""
            print "\n\"It's all blurry, I've been having nightmares...\" she keeps on crying."
            print "\n\"Dad, this lady... she.. she kidnapped us while we were camping,\""
            print "\nYou say: \"Don't worry about it, you're safe now, let's go. Can you walk?\""
            print "\n\"Where are we?.. Where's Josh?..\" She asks." 
            p_scroll()
            print "\nYou start answering the question but she immediatley passes out in your arms."
            print "\nProbably the shock or the spell..."
            print "\nYou pick her limp body up on your shoulder and decide it's time to head out of this hell-hole."
            p_scroll()

    elif april_found == False:
        april_found = True
        print "\nReaching the end of the stairs you are baffled by what you find."
        print "\nRight in front of you lies %sApril%s, unconscious." % (red, default)
        print "\nShe is tied to the iron bunk bed she is sleeping on by some strange dark-brown thorned vine."
        p_scroll()
        print "\nYou immediately rush to her, trying to wake her up."
        print "\nYou check for a pulse and breathing and you sigh in relief: she's alive."
        print "\n\"April!\" you shout as you shake her nervously."
        print "\nThere is nothing to do, she looks heavily sedated."
        p_scroll()
        print "\nYou try to see if you can remove the thorned vine but it's impossible."
        print "\nAs soon as you touch it the vine squeezes around April even tighter."
        print "\nBlood drips from the thorns pressing against April's skin."
        print "\nThe metal bed can't be moved around either."
        print "\nYou need to find a way to wake her up."
        p_scroll()
    print "\nA glance around shows you a stone walled circular room."
    print "\nAside from April's bunk bed and a wooden bucket there isn't anything in the room."
    print "\nA small oval shaped opening in the wall serves as a window."
    print "\nA single lit oil lamp lights the place."
    if april_freed:
        print "\n%sApril is on your back.%s" % (bold, default)
    choice = p_choice()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2
        elif "go" in choice:
            if ["go"] == choice:
                print specific
            elif "bedroom" in choice or "down" in choice or "downstairs" in choice or "stairs" in choice or "second" in choice:
                print "\nYou climb down the stairs."
                april_found = True
                bedroom()
            elif "east" in choice and "tower" in choice:
                print "\nYou're already in the east tower."
            elif "window" in choice:
                print "\nThe window is too small for you to go through."
            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "room"] == choice or ["search", "tower"] == choice:
                print specific_search
            elif "april" in choice:
                print "\nHer body is limp and she's freezing."
            elif "bucket" in choice:
                print "\nThere is vomit in the bucket. She's probably sick."
            elif "vine" in choice or "thorns" in choice and altar_dispell == False:
                print "\nThe thorns hold her hands together and then run around her to both her ankles and to the bed."
                print "\nIts like the vine is alive."
                print "\nThere is nothing you can do to remove it."
            elif "vine" in choice or "vines" in choice or "thorns" in choice and altar_dispell:
                print "\nThe vine has somehow vanished."
            else:
                print nothing
        else:
            print invalid
        choice = p_choice()
    east_tower()

def west_tower():
    global flashlight, rings_taken, defense_activated, grizzly_killed, bucket1, bucket2, paw_switch_found, paw_switch_on, bedroom_visited, barred_door_seen 
    paw_switch_on = True
    print "\n..."
    time.sleep(3)
    print "\n%s//// WEST TOWER (FLOOR 3) \\\\\\\\\%s" % (cyan, default)
    print "\nThe top of the tower is a circular room made of stones."
    print "\nYou can see the moon through the oval window opening in the wall but this place has no inside lighting."
    if flashlight == False:
        print "\nThe moon light isn't enough for you to clearly see inside."
        print "\nYou distinguish a medium sized box on the floor."
        print "\nThere also is a metallic stand with something on it."
        print "\nThe object on the stand has two green light reflections coming from the moon."
        print "\nYour feet bump into a wooden object."
        print "\nIf only you had something to light the room."
    elif flashlight:
        print "\n%sWith your flashlight you discover a silver chest on the floor." % bold
        print "\nClose to it is a metallic perch with a stuffed owl standing on it."
        print "\nThe owl has two emeralds replacing its eyes."
        print "\nOn the floor is an empty wooden bucket.%s" % default
    choice = p_choice()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2

        elif "go" in choice:
            if ["go"] == choice:
                print invalid
            elif "tower" in choice and ("left" in choice or "west" in choice):
                    print "\nYou're already in the west tower."
            elif "bedroom" in choice or "down" in choice or "downstairs" in choice or "stairs" in choice or "second" in choice:
                print "\nYou climb back down."
                bedroom()
            elif "window" in choice:
                print "\nThe oval window is very small, you can't go through it."
            else:
                print invalid
        elif ["search"] == choice:
            print specific_search
        elif "search" in choice:
            if flashlight:
                if "chest" in choice or "rings" in choice: 
                    print "\nThe chest's outter lining is carved with floral ornaments like trees, leaves and flowers."
                    print "\nForest animals are also represented on the surface."
                    print "\nYou push the chest lid open and inside you find %ssilver rings%s." % (magenta, default)
                    print "\nThere are, roughly estimating, three hundred of these."
                    print "\nThey are all identical: pretty wide with two wolf ornaments holding a ruby."
                    print "\nThe sight of this makes your head spin: this is probably worth a lot of money."
                    if rings_taken == False:
                        while True:
                            print "\n\nShould you take some?"
                            choice = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()
                            if "yes" in choice:
                                if grizzly_killed == False:
                                    defense_activated = True
                                rings_taken = True
                                print "\nYou grab a handful and stuff them in your pocket."
                                if grizzly_killed == False:
                                    print "\nAs soon as you touch them you notice a brief spark in the stuffed owl's emerald eyes."
                                print "\nYou close the chest again."
                                break
                            elif "no" in choice:
                                print "\nYou leave them alone and close the chest again."
                                break
                            else:
                                print invalid
                    else:
                        print "\n%sYou can't stuff any more of these in your pockets." % bold
                        print "\nYou close the chest.%s" % default
                elif "perch" in choice:
                    print "\nA standard perch made for birds."
                elif "owl" in choice:
                    print "\nA grey owl who's emerald eyes make you uneasy, like it was staring at you."
                    print "\nYou can't say why and although you know it is stuffed it feels alive."
                elif "bucket" in choice:
                    print "\nThe bucket is empty."
                    if bucket2 == False:
                        bucket2 = True
                        print "\nYou notice one of its wood slits has a piece of %sfolded paper%s stuck in it." % (magenta, default)
                        print "\nAfter a few moments you manage to remove it and unfold it."
                        print "\nThe paper has a handwritten message on it:"
                        print paper2
                        print "\nYou grab it with you."
                        print "\n%s(Type \"%s%s\" any time to read the paper again.)%s" % (gray, paper, gray, default)
                    elif bucket2:
                        print "\nThere is nothing else to find."
                else:
                    print nothing
            elif flashlight == False:
                print "\nYou can't see anything."
        else:
            print invalid
        choice = p_choice()
    west_tower()

def bedroom():
    global bedroom_visited, barred_door_seen, bedroom_trap, altar, altar_seen, pictures, first, april_found, saved_player_HP, abhartach_killed, altar_dispell, silver_dagger, rings_taken, april_freed, defense_activated

    print "\n..."
    time.sleep(3)
    print "\n%s//// BEDROOM (FLOOR 2) \\\\\\\\\%s" % (cyan, default)
    if bedroom_trap:
        death("\nAs soon as you walk through the door, metal spikes come out of the ceiling and pierce your body from skull to toe.", main_room, player_HP, "Beware of switches.")
    elif april_found == False or abhartach_killed:
        print "\nAs the door closes behind you, your eyes lay on an impressive bedroom."
        print "\nJust like the main room it is refinely decorated and quite vast."
        print "\nA king size bed faces you at the end of the room."
        print "\nIt looks very well kept also but is covered in dust and cobwebs."
        print "\nIn the middle of the left wall is a fireplace with three armchairs facing it."
        print "\nThe right wall has a large library shelf with books on it."
        print "\nThe walls are decorated with a map and painted portraits of white haired people."
        print "\nRight to the left of the bed is some sort of chemistry bench with bottles and bunsen burners."
        print "\nOn the right side of the bed is a real size christian cross turned upside down."
        print "\nThe cross has a body hanging on it, upside down as well. Disturbing..."
        print "\nAn oil lantern hanging in the middle of the ceiling accompanies the fireplace's orange lights."
        print "\nA tube goes from the body, above the bed, to the chemistry table."
        if altar_seen and altar == False:
            print "\n%sThe %saltar%s has disappeared and has been replaced by the mahogany desk again.%s" % (bold, magenta, bold, default)
        elif altar == False:
            print "\nTo the immediate left of the double door is a nice looking mahogany desk with no chair."
        elif altar and bedroom_visited == False:
            print "\nTo the immediate left of the double door is a massive stone %saltar%s." % (magenta, default)
            altar_seen = True
        elif altar and bedroom_visited:
            print "\n%sYou notice that where the desk was there is now a massive stone %saltar%s." % (bold, magenta, default)
            altar_seen = True
        print "\nIn both left and right corners of the wall facing the entrance are wooden doors."
        if barred_door_seen == False and paw_switch_on == False:
            if bedroom_visited:
                print "\n%sThe left corner door is barred with three thick metal spikes horizontally blocking the door.%s" % (bold, default)
            elif bedroom_visited == False:
                print "\nThe left corner door is barred with three thick metal spikes horizontally blocking the door."
            barred_door_seen = True
        elif barred_door_seen and paw_switch_on:
            print "\n%sThe left corner door isn't barred anymore.%s" % (bold, default)
        elif bedroom_visited and barred_door_seen and paw_switch_on == False:
            print "\n%sThe left corner door is barred with three thick metal spikes again.%s" % (bold, default)
        if april_freed:
            print "\n%sYou can feel April's weight.%s" % (bold, default)
    elif april_found and abhartach_killed == False:
        print "\n%sAs you come down the stairs and push the wooden door open back into the bedroom\nyou notice something different.%s" % (bold, default)
        p_scroll()
        print "\nA man is sitting in one of the armchairs by the fireplace."
        print "\nYou can't see him well due to the angle you're coming from."
        print "\nBefore you can say anything the man speaks:"
        print "\n\"So you found her? She's been here for a couple of days.\" he says with a brittish accent."
        print "\n\"Her friend has been resting with us as well, Greta took good care of him.\""
        print "\n\"However, the plan was for her to stay here.\""
        p_scroll()
        print "\nThe man stands up and turns around, now facing you from across the room."
        print "\n\"The name is Abhartach.\" he calmly says with a smile."
        print "\nHe's extremely tall and slender, above 6 feet."
        print "\nHis hair is dark and well groomed with a thin mustache."
        print "\nHe's wearing an old fashioned tuxedo."
        print "\nIn his hand is a glass on which he sips."
        print "\nWithout saying a word he lifts his free hand towards you and motions it in a fist opening."
        p_scroll()
        if silver_dagger == False or (silver_dagger and altar_dispell):
            print "\nSuddenly you feel a tingling in your chest followed by unbearable pain."
            print "\nIt's like your brain and heart were being turned to mud."
            print "\nYou fall to your knees in agony while losing your sanity at the same time."
            death("\nYou start crying blood while the pain grows stronger. Your vision blurs red and your brain finally implodes.", main_room, player_HP, "A magical item would protect you from this man's powers.")
        elif silver_dagger:
            print "\nThe man looks surprised."
            print "\n\"Are you related to the Ulfedhnars? Your hair isn't white though.\""
            print "\nHe stands still, thoughtful."
            print "\n\"Oh, I see, you found the dagger. Ulfric was quite clever on that one I must admit.\""
            print "\n\"The spell he cast stucking me here was well thought.\""
            print "\n\"I miss him in some way, things can get pretty dull with only Greta around.\""
            print "\nYou intervene: \"Greta's dead.\""
            print "\nHe pauses, then continues as if you had said nothing."
            p_scroll()
            print "\n\"I do enjoy the manor though, he had great taste and a fascinating collection of books.\""
            print "\n\"You see, Anna over here is almost empty. Greta found April with perfect timing.\""
            print "\n\"Her skin is so soft, he says with a grin, it will be a pleasure to make her mine.\""
            print "\n\"Anna will replace Greta rest assured.\""
            print "\n\"You must be her father of course. How foolish of me to consider you an Ulfedhnar.\""
            print "\nHe continues, \"Anyhow it matters little wether you are protected by the dagger's magic or not.\""
            print "\n\"Humans have little to say in our quarels.\""
            p_scroll()
            print "\nHe puts the glass down and you notice his appearance slowly changing."
            print "\nHis eyes seem to slant and turn wider in an almond shape, they're as dark as the night."
            print "\nHis fingers elongate before your eyes, turning into sharp iron blades."
            print "\nHis grin shows a row of sharp teeth."
            p_scroll()
            print "\n\"I never quite understood how love and bonding could make you do such insensible things.\""
            print "\n\"En guarde sir.\" he finally adds."
            first = "player"
                battle(Abhartach, main_room, ["silver dagger", "dagger", "dagger", "weapon", "blade"])
            abhartach_killed = True
            print "\nHe reaches for you with the tip of one of his scizor fingers."
            print "\nYou quickly hack your dagger towards it and slice the finger off."
            print "\nThe vampire hurls with pain and disbelief."
            print "\nImmediatley after, you headbutt him in the nose and Abhartach is pushed a few steps back."
            print "\nFor a faint moment you can see a look of despair on his face."
            p_scroll()
            print "\nIn a moment of clarity you run up close to him and jam the dagger in his abdomen."
            print "\nHe falls to the floor, you jump on his chest and plunge the silver weapon in his heart."
            print "\nDark blood splatters as the blade rips his thorax open."
            if altar == False:
                print "\nA powerful electrical ark goes from the dagger to the desk."
            if altar:
                print "\nA powerful electrical ark goes from the dagger to the altar."
            print "\nSmoke starts coming out from him and the blood turns to goo."
            print "\nJust like Greta did, all of his body starts melting and smoking."
            print "\nYou stand victoriously while he convulses and screams."
            print "\nEventually there is nothing left for him aside from the sulfur smell of the smoke."
                
    choice = p_choice()
    while choice != ["look", "around"]:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2

        elif ["go", "door"] == choice or (["go", "wooden", "door"] in choice and paw_switch_on == False):
            print "\nWhich one?"
        elif "go" in choice:
            if "bedroom" in choice:
                print "\nYou're already in the bedroom."
            elif "balcony" in choice or "entrance" in choice or "double" in choice or "outside" in choice:
                print "\nYou step back on the balcony."
                bedroom_visited = True
                balcony()
            elif "door" in choice or "tower" in choice:
                if "wooden" in choice and paw_switch_on == False:
                    print "\nYou push the wooden door open and walk up the circular stoned stairway."
                    bedroom_visited = True
                    east_tower()
                if "east" in choice or "right" in choice:
                    print "\nYou push the wooden door open and walk up the circular stoned stairway."
                    bedroom_visited = True
                    east_tower()
                elif "west" in choice or "left" in choice:
                    if paw_switch_on:
                        print "\nYou push the wooden door open and walk up the circular stoned stairway."
                        bedroom_visited = True
                        west_tower()
                    if paw_switch_on == False:
                        print "\nThe access is blocked by three horizontal spikes."
                else:
                    print invalid
            elif "windows" in choice:
                print windows
            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "room"] == choice or ["search", "bedroom"] == choice:
                print specific_search
            elif ["search", "door"] == choice or ["search", "wooden", "door"] == choice:
                print "\nWhich one?"
            elif "left" in choice and paw_switch_on:
                print "\nThe left door is barred with heavy metal spikes."
            elif "bed" in choice:
                print "\nThe bed sheets and cover are folded with immaculate precision."
                print "\nThe fabric is of excellent quality."
                print "\nIt looks like it's never been used."
                print "\nIt is covered in a layer of dust."
            elif "cross" in choice or "body" in choice:
                print "\nThe wood cross is the closest you've seen to a real one."
                print "\nThe dried body is one of a woman, dark hair."
                print "\nIts like all the water and blood from her body was sucked out."
                print "\nShe looks like a mix of young and old all in one. Quite unsettling."
                print "\nHer eyes and eye sockets are dry but injected with blood due to being upside down."
                print "\nAn intraveinous hose is stuck in her left forearm, it leads to the chemistry table."
                print "\nHer neck has two swollen bruises and her wrists and ankles are nailed to the wood..."
                print "\nYou can't really tell if the woman is dead or not. Probably dead."
                print "\nA lump on her stomach makes you realize the woman was pregnant."
                print "\nThere is nothing you can do about it."
            elif "bench" in choice:
                print "\nThe chemistry bench is a complex set of bottles, burners, vials and test tubes all interconnected."
                print "\nSome vials are bubbling, smoke is coming from others. This was being used not long ago."
                print "\nThe hose coming from the corpse extracts blood into a glass spring shaped tube."
                print "\nIt looks like it is then processed by all sorts of chemical reactions."
                print "\nYou have no knowledge of how any of this works nor what the expected result should be."
            elif "map" in choice:
                print "\nYou recognize the geography: its a map of the North and Baltic Sea."
                print "\nThe island of Ireland isn't on it but most of the continental coast is."
                print "\nThe description and location names are in latin."
            elif "desk" in choice and altar == False:
                print "\nThe mahogany is carved elegantly."
                print "\nAlthough a nice piece of furniture, the desk appears unused recently."
                print "\nOn it are still left a few sheets of parchment paper, a feather pen and a dry ink well."
                print "\nProbably antique."
            elif "desk" in choice and altar:
                print "\nThere is a stone altar instead of the mahogany desk."
            elif "altar" in choice and altar == False:
                print "\nThere is no altar, only a mahogany desk."
            elif "altar" in choice and altar:
                print "\nThe altar is made of stone, a kind you've never seen before."
                print "\nIt is filled with hundreds of coins with animals on them."
                print "\nThe whole altar has slots running through it linking the coins to each other in geometrical shapes."
                print "\nNone of the coins can be removed from their slots."
                print "\nIt feels somewhat electric."
                print "\nIn the center of it is a triangle with a larger wolf symbol in the middle."
                print "\nThe triangle has three animal coins going from top and clockwise: a %swhale%s, a %sstag%s and an %seagle%s." % (magenta, default, magenta, default, magenta, default)
                print "\nThe center wolf symbol has a %sslit%s in its mouth and a %sring slot%s underneath it." % (magenta, default, magenta, default)
                if silver_dagger == False:
                    print "\nYou don't know what to do with this."
                elif silver_dagger:
                    print "\nIt looks like the %sdagger%s fits in the %sslit%s." % (magenta, default, magenta, default)
                    while altar_dispell == False:
                        print "\n\nShould you slide your %sdagger%s in it?" % (magenta, default)
                        choice = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)) 
                        if "yes" in choice:
                            print "\nOnce inserted you rotate the dagger clockwise in the slit."
                            print "\n..."
                            time.sleep(3)
                            if rings_taken == False:
                                print "\nBut nothing happens. You probably need to use the ring slot for it to work."
                                print "\nThere is nothing else you can do. You withdraw the dagger."
                            if rings_taken:
                                print "\nYou then press one of the rings you took earlier in the ring slot."
                                print "\n..."
                                time.sleep(3)
                                if abhartach_killed == False:
                                    print "\nYou hear a voice in your head:"
                                    print "\n%s\"The dagger must have met the caster's blood for the curse to be lifted.\"%s" % (bold, default)
                                    print "\nYou withdraw the ring and the dagger."
                                elif abhartach_killed:
                                    print "\nThe dagger suddenly starts vibrating and turning light blue."
                                    print "\nAs it vibrates more and more, it levitates above the slit, emiting electric arks between it and the altar."
                                    print "\nThe intensity rises, you take a few steps back."
                                    p_scroll()
                                    print "\nA blue spherical halo grows around the dagger, growing steadily bigger."
                                    print "\nElectric arks run through you and the room."
                                    print "\nWith an impressive thunder sound the dagger is absorbed into oblivion as the halo bursts."
                                    print "\nSoon, nothing is left from the dagger or the ring."
                                    print "\nYou feel ok, although confused by what just happened."
                                    altar_dispell = True
                                    defense_activated = False
                            break
                        elif "no" in choice:
                            print "\nYou leave it alone."
                            break
                        else:
                            print invalid
            elif "library" in choice or "shelf" in choice or "books" in choice or "bookshelf" in choice or "bookshelves" in choice:
                print "\nDozens of books are layed on the shelves."
                print "\nNone of which you recognize the alphabets."
                print "\nSome are collections, you can guess by their size and cover."
                print "\nThe content is incomprehensible with sometimes strange drawings and schematics."
                print "\nVery esoteric stuff overall."
            elif "fireplace" in choice:
                print "\nThe flames are coming from nowhere because the fire has no wood to burn from."
            elif "armchairs" in choice or "armchair" in choice:
                print "\nOne of the armchairs has a small glass flask on the armrest."
                print "\nThe content looks like a thick and dark paste."
            elif "windows" in choice:
                print windows
            else:
                print nothing
        else:
            print invalid
        choice = p_choice()
    bedroom()

def prison():
    global silver_dagger, greta_dead, saved_player_HP, pictures, bucket1, bucket2
    print "\n..."
    time.sleep(3)
    coin_list = ["stag", "boar", "whale", "bear", "eagle", "snake"]
    print "\n%s//// PRISON (FLOOR -1) \\\\\\\\\%s" % (cyan, default)
    print "\nThis is a very dark place with no windows."
    print "\nYour flashlight shows shackles and chains hanging from the wall."
    print "\nOne of them has a dried skeleton attached to it."
    print "\nRight next to it is another wooden bucket."
    print "\nImmediately to your right is a peculiar, heavily decorated casket made of silver."
    if silver_dagger:
        print "\n%sThe casket is open with the dead man in armor inside." % bold
        print "\nSmoke is coming out of his eyes and mouth.%s" % default
    print "\nIt is mounted vertically on a stone pedestal."
    print "\nAn unsettling aura emanates from it."
    print "\nYou hear rats somewhere in the room."
    choice = p_choice()
    while choice != ["look", "around"]:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2
        elif "go" in choice:
            if "cellar" in choice or "door" in choice or "outside" in choice:
                print "\nYou step out of the prison."
                cellar()
            elif "prison" in choice:
                print "\nYou're already in the prison."
            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "prison"] == choice or ["search", "room"] == choice:
                print specific_search
            elif "casket" in choice and silver_dagger == False:
                print "\nIt is decorated with precious stones, fine ornaments and hieroglyphs."
                print "\nA wolf sigil is at the center of it and on the sides."
                print "\nYou notice the left side has some kind of mechanism."
                print "\nUnderneath the sigil there is a display with six silver coins with animals on them."
                print "\n%s.Stag .Boar .Whale" % bold
                print "\n.Bear .Eagle .Snake%s" % default
                print "\nThe mechanism has three empty coin slots forming a triangle around the sigil."
                while True:
                    print "\n\nFrom top and clockwise, how should you place the coins?\n\n%s(Type \"exit\" to leave.)%s\n\n" % (gray, default)
                    choice = raw_input("> ").lower().replace(",","").replace(".","").split()
                    if choice == ["whale", "stag", "eagle"]:
                        silver_dagger = True
                        greta_dead = False
                        print "\nYou hear a click and the mechanics start rotating."
                        print "\n..."
                        time.sleep(3)
                        print "\nHydraulic noises come from within the casket while the door activates."
                        print "\nBlack smoke comes out of it as it opens."
                        print "\nThe inside of the casket is decorated just like the outside."
                        print "\nHowever a strange glowing metal lights the interior."
                        print "\nInside is a dead man's body wearing an armor with a silver dagger stuck through its chest."
                        if pictures:
                            print "\nYou recognize the man: he is the one on the pictures in the staircase of the manor."
                        print "\nThe armored corpse is holding the dagger in a self stabbing motion."
                        print "\nThis is certainly the %sdagger%s Josh tried to text you about." % (magenta, default)
                        p_scroll()
                        print "\nYou decide to take it with you."
                        if pictures == False:
                            print "\nThe body hasn't decayed and although very old, you've seen it somewhere already."
                        if pictures:
                            print "\nThe body hasn't decayed and although very old, you recognize the man from the pictures."
                        print "\nAs soon as you touch the body the hand releases its grasp around the dagger."
                        print "\nWith a little strength, you manage to remove the weapon from the body."
                        print "\nHis mouth and eyes open, releasing more black smoke."
                        print "\nIt is very long, almost like a small sword."
                        print "\nThe knob has the same wolf sigil you've seen around the manor."
                        print "\nSimilar hieroglyphs cover the blade. They look like runes."
                        print "\nHolding it in your hand is a sensation like you've never felt before."
                        print "\nYou are now holding the dagger in one hand and your baseball bat in the other."
                        break
                    elif "exit" in choice:
                        print "\nYou leave the coins alone."
                        break
                    else:
                        invalid_cmd = False
                        for coin in choice:
                            if coin not in coin_list:
                                invalid_cmd = True
                                print invalid
                                break
                        if invalid_cmd == True:
                            continue
                        death("\nA lightning bolt strikes you out of nowhere and turns you into a pile of dust.", main_room, player_HP, "You should search for the correct combination of coins somewhere.")
            elif "casket" in choice and silver_dagger:
                print "\nThe inside of the casket is decorated just like the outside."
                print "\nHowever a strange glowing metal lights the interior."
                print "\nThe armored body lies there, stiff as wood."
                if pictures:
                    print "\nYou recognize the man: he is the one on the pictures in the manor."
            elif "body" in choice or "corpse" in choice and silver_dagger:
                print "\nBlack smoke is still coming from the open eyes and mouth."
                print "\nThe man has long white hair tied in a knot."
                if pictures:
                    print "\nHe's the one on the pictures in the manor."
                print "\nMany scars mark his face and hands."
                print "\nThe hand which was holding the dagger has runes tattooed on it."
                print "\nAmongst them, you can read \"Ulfhednar\"."
            elif "bucket" in choice:
                print "\nOnly cobwebs and an old rusty spoon."
            elif "skeleton" in choice:
                print "\nThis one must've been here for a while."
                print "\nBoth hands are tied to the shackles. The hands only have four fingers."
                print "\nThe skull has a very strange elongated shape."
            elif "rats" in choice:
                print "\nYou can't find them."
            elif "windows" in choice:
                print "\nThere are no windows here."
            else:
                print nothing
        else:
            print invalid
        choice = p_choice()
    prison()


def storage():
    
    global greta_ko, greta_body, josh_found, flashlight, prison_key, first, saved_player_HP, april_freed, bucket1, bucket2
    print "\n..."
    time.sleep(3)
    print "\n%s//// STORAGE (FLOOR 1)\\\\\\\\\%s" % (cyan, default)
    if greta_ko == False:
        if flashlight == False:
            print "\nThe room is pitch black."
            print "\nA dark silhouette is standing in the middle of the room."
        if flashlight:
            print "\n%sYour flashlight shines on a long haired, barefooted woman dressed in old gowns turning your back on you.%s" % (bold, default)
            print "\nHer skin is a very pale blue-gray and her hair is extremely dirty."
        print "\nYou hear a loud shreik."
        if flashlight == False:
            print "\nThe silouette turns around and swiftly comes running towards you."
            print "\nFaster than you can react you feel a cold blade cutting your throat open."
            death("\nYou fall to the floor gasping for air while blood gushes out of the wound.", kitchen, player_HP, "If you had something to light the room you could see what's inside and react in time.")
        if flashlight:
            print "\nShe turns around and starts running towards you with a knife in one hand and a hatchet\nin the other." 
            first = "enemy"
        battle(Greta, kitchen, ["baseball bat", "bat", "weapon"])
        greta_ko = True
        greta_body = True
        print "\nShe crumbles to the floor screaming in pain."
        print "\nYou stand above her and carefully swing your bat to her head like a golf club."
        print "\nYou hear a crunch sound when your weapon hits her."
        print "\nShe stops moving as one last gasp of air leaves her lungs."
        print "\nYou look around the room you're in:"
        p_scroll()
        storage()
    if greta_ko == True:
        print "\nYou are in the kitchen storage."
        print "\nA disgusting smell permeates the room."
        print "\nThere is no natural light here as the only window is boarded with wood planks."
        print "\nThe center of the room has a kitchen island with a bowl on it."
        print "\nThe wall in front of it is mounted with cupboards and drawers."
        print "\nA big metal closet stands to the right of the cupboards."
        print "\nOn your left in the corner of the room is a big pile of potato bags. On the floor close to the bags is a broken stool."
        print "\nThe right side has a corpse on the floor lying against the wall."
        print "\nAll limbs but the right arm have been torn off..."
        print "\nA puddle of blood surrounds it."
        if greta_body == True:
            print "\nThe body of the woman is lying on the floor to your feet."
        elif greta_body == False:
            print "\n%sThe woman's body has disappeared.%s" % (bold, default)
        print "\nThe scene and the horrible smell make you gag."
        if april_freed:
            print "\n%sApril wakes up and starts sobbing hard: \"Oh my god... Josh!...\"" % bold
            print "\nShe keeps on weeping until she falls unconscious.%s" % default
        choice = p_choice()
        while ["look", "around"] != choice:
            if "list" in choice:
                print command_list
                if bucket1 and bucket2:
                    print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
                elif bucket1 or bucket2:
                    print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
            elif "paper" in choice and (bucket1 or bucket2):
                if bucket1:
                    print paper1
                if bucket2:
                    print paper2
            elif "go" in choice:
                if "kitchen" in choice or "door" in choice:
                    print "\nYou go back to the kitchen."
                    kitchen()
                elif "storage" in choice:
                    print "\nYou're already in the kitchen storage."
                elif "windows" in choice or "window" in choice:
                    print "\nThe window is boarded with planks."
                else:
                    print invalid
            elif "search" in choice:
                if ["search"] == choice:
                    print specific_search
                elif "bowl" in choice or "island" in choice:
                    print "\nThe bowl contains what remains of a chewed hand..."
                    print "\nIt's missing a finger."
                elif "bags" in choice:
                    print "\nMostly rotten vegetables and flies."
                    print "\nSome have human bones inside."
                elif "cupboards" in choice:
                    print "\nInside you find wooden bowls piled up."
                elif "drawers" in choice:
                    print "\nOne of them has a dead crow creeping with maggots."
                    print "\nIts wings were ripped apart from it."
                elif ["search", "body"] == choice and greta_body == True:
                    print "\nWhich one?"
                elif ("body" in choice and greta_body == False) or ("corpse" in choice or "josh" in choice or "crippled" in choice or "dismembered" in choice):
                    print "\nHis face is distorted with pain."
                    print "\nYou have no doubt now: This is Joshua's body."
                    print "\nYou clench your fist with anger and fear."
                    print "\nThe limbs were brutally chopped off. Poor kid."
                    print "\nYou pray that April is ok..."
                    josh_found = True
                elif "woman" in choice or "greta" in choice and greta_body == True:
                    print "\nThe neck is broken forming a square angle with her head. That last hit got her for sure."
                    print "\nPaying closer attention to her you notice her skin is covered in scabs and zits."
                    print "\nHer mouth is covered with blood, she smells terrible and her overall appearance is repulsive."
                    print "\nThe scariest part is her dark black eyes. There is no white in them, they look like marbles."
                    if prison_key == False:
                        print "\nYou notice a chain tied to her neck. Attached to it is a %ssteel key%s, could be useful." % (magenta, default)
                        print "\nYou stuff it in your pocket."
                    prison_key = True
                elif "closet" in choice:
                    print "\nOpening the closet, you are disgusted by what you find inside."
                    print "\nHuman limbs are hanging upside down."
                    print "\nThey still have clothing on and are peirced by the hooks they are hanging from."
                    if josh_found:
                        print "\nBlood is dripping from them, they are Joshua's..."
                    if josh_found == False:
                        print "\nBlood is dripping from them, they are from the crippled body."
                    print "\nThere are also older limbs hanging there."
                elif "window" in choice or "windows" in choice:
                    print "\nThe window is boarded with planks."
                else:
                    print nothing
            else:
                print invalid
            choice = p_choice()
        storage()



def balcony():
    global paw_switch_found, paw_switch_on, bottle_switch_on, bedroom_trap, altar, april_freed, flashlight, rings_taken, defense_activated, balcony_visited, bucket1, bucket2
    balcony_visited = True
    print "\n..."
    time.sleep(3)
    print "\n%s//// BALCONY (FLOOR 2) \\\\\\\\\%s" % (cyan, default)
    print "\nFacing the stairs in the immediate left corner of the balcony is a bookshelf."
    print "\nThe balcony rail is an excellent piece of wood craft with golden paint decoration."
    print "\nContinuing to the right of the bookshelf are three marble statues representing\nin order: a boar, a bear and a whale."
    print "\nFollowing the whale statue is a large double door painted brown."
    print "\nAbove the double door is a smaller marble statue of a wolf's head coming out of the wall."
    print "\nOn the opposite side of the whale statue, after the door, are the three other\nstatues: a stag, a snake and an eagle."
    print "\nEach statue is made of white marble and is above 6 feet tall."
    print "\nThey are remarkably well carved."
    print "\nAt the corner end of the balcony, is a glass display decorated with strange objects."
    print "\nThe view from the balcony makes you realize how big the main room is."
    if april_freed:
        print "\n%sApril is asleep breathing on your shoulder.%s" % (bold, default)
    choice = p_choice()
    while choice != ["look", "around"]:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2
        elif "go" in choice:
            if "balcony" in choice:
                print "\nYou're already on the balcony."
            elif "main" in choice or "down" in choice or "downstairs" in choice or "stairs" in choice or "first" in choice or "ground" in choice:
                print "\nYou climb down the stairs."
                main_room()
            elif "bedroom" in choice or "entrance" in choice or "door" in choice or "inside" in choice:
                print "\nYou push the double door open and enter the next room."
                bedroom()
            elif "windows" in choice or "window" in choice:
                print windows
            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "balcony"] == choice:
                print specific_search
            elif "wolf" in choice or "wolf's" in choice:
                print "\nThe statue is too high for your reach."
                print "\nThe wolf's head is carved like it was howling."
            elif "shelf" in choice or "books" in choice or "shelves" in choice or "bookshelf" in choice or "bookshelves" in choice or "library" in choice:
                print "\nThis bookshelf only has books on it."
                print "\nYou can't read a single word of them since their alphabet is unknown to you."
                print "\nSome are very ancient for sure."
            elif "display" in choice or "objects" in choice:
                    print "\nThe display is a five angle glass tower with three bronze shelfs."
                    print "\nGlass windows prevent you from touching the inside."
                    print "\nThese objects look like nothing you've ever seen before."
                    print "\nThere is a small golden sphynx, a compass holding a scalpel, an hourglass using pearls for sand and\na very bright red crystal."
                    print "\nYou can't figure out if these are decorative or have some use."
                    print "\nAnyhow you would not be able to use them."
            elif ["search", "statue"] == choice:
                    print "\nWhich one?"
            elif "statues" in choice:
                print "\nAll statues have different postures."
            elif "boar" in choice:
                print "\nThe boar is standing still."
            elif "whale" in choice:
                print "\nThe whale is mounted on waves, like it was coming out of the ocean."
            elif "bear" in choice:
                print "\nThe bear is on his four legs in a running motion."
            elif "eagle" in choice:
                print "\nThe eagle had both its wings deployed in a combat posture."
            elif "snake" in choice:
                print "\nThe snake is standing up with its mouth open and its fangs out."
            elif "stag" in choice or "paw" in choice:
                print "\nThe stag has a walking stance with one paw held up."
                if paw_switch_found == False:
                    paw_switch_found = True
                    print "\nLooking carefully, you notice its lifted paw has a slot line."
                    print "\nIt can rotate clockwise."
                    print "\nIt looks like the paw is actually a %sswitch%s." % (magenta, default)
                if paw_switch_found:
                    while True:
                        if paw_switch_on == False:
                            print "\n\nDo you wish to pull the paw %sswitch%s on%s?" % (magenta, bold, default)
                            choice = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()
                            if "yes" in choice:
                                paw_switch_on = True
                                print "\nYou turn the paw clockwise and hear a mechanical sound in the other room."
                                break
                            elif "no" in choice:
                                print "\nYou leave it alone."
                                break
                            else:
                                print invalid
                        elif paw_switch_on:
                            print "\n\nDo you wish to pull the paw %sswitch%s off%s?" % (magenta, bold, default)
                            choice = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()
                            if "yes" in choice:
                                print "\nYou turn the paw counter-clockwise and hear a mechanical sound in the other room."
                                if altar:
                                    print "\n%sIt sounds like something big moved next door%s." % (bold, default)
                                if bottle_switch_on:
                                    bedroom_trap = True
                                paw_switch_on = False
                                altar = False
                                break
                            elif "no" in choice:
                                print "\nYou leave it alone."
                                break
                            else:
                                print invalid
            elif "windows" in choice or "window" in choice:
                print windows
            else:
                print nothing
        else:
            print invalid
        choice = p_choice()
    balcony()
        


def kitchen():
    global name, flashlight, player_HP, saved_player_HP, tin_cans, prison_key, greta_body, josh_found, april_freed, bucket1, bucket2
    if prison_key:
        greta_body = False
    print "\n..."
    time.sleep(3)
    print "\n%s//// KITCHEN (FLOOR 1) \\\\\\\\\%s" % (cyan, default)
    if flashlight == False:
        print "\nThe place is a very dark room with no inside lighting."
    if flashlight:
        print "\n%sYour flashlight shines on what can only be a kitchen.%s" % (bold, default)
    print "\nA barred window lets moonlight shine through."
    if flashlight == False:
        print "\nAt the center of the room is a wooden table."
    if flashlight:
        print "\nAt the center of the room is a wooden table %swith a blood stain on its surface.%s"  % (bold, default)
    print "\nCupboards and drawers in the west corner form an L shaped kitchen area."
    print "\nThe kitchen area has a rusty sink."
    print "\nOn the floor is a camping bag."
    print "\nOn the eastern wall you can distinguish a wooden door."
    if flashlight == False:
        print "\nIt's hard to see anything."
    elif flashlight:
        print "\n%sThere is blood on the floor close to it.%s" % (bold, default)
    if april_freed:
        print "\n%sApril is getting heavy.%s" % (bold, default)
        
    choice = p_choice()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2
        elif ["go", "door"] == choice:
            print "\nWhich one?"
        elif "go" in choice:
            if "kitchen" in choice:
                print "\nYou're already in the kitchen."
            elif "door" in choice or "storage" in choice:
                if "wooden" in choice or "storage" in choice:
                    print "\nYou cautiously open the door."
                    storage() 
                elif "white" in choice or "main" in choice:
                    print "\nYou push the white door open and go back to the main room."
                    main_room()
            elif "main" in choice:
                print "\nYou push the white door open and go back to the main room."
                main_room()
            elif "windows" in choice or "window" in choice:
                print windows
            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "kitchen"] == choice or ["search", "room"] == choice:
                print specific_search
            elif ["search", "door"] == choice:
                print "\nWhich one?"
            elif "drawers" in choice or "drawer" in choice and flashlight == False:
                flashlight = True
                print "\nOne of the drawers has blood stains on it."
                print "\nInside are a cell-phone and a headband %sLED flashlight%s. Both are splattered with blood." % (magenta, default)
                print "\nThe cell-phone still has 3% battery and doesn't have a screen-lock."
                print "\nThe phone screen is in the text messages menu:"
                p_scroll()
                print "\n"
                print """
                %sSend to: %s

                %s help!!! April kidnapped by freak
                can't explain but u need a %ssilver 
                dagger%s to kill it. Pls this isn't a
                joke come over I%s""" % (bold, name, name, magenta, bold, default) 
                p_scroll()
                print "\nThe message ends here and the phone dies soon after."
                print "\nYour heart starts pounding: This is Josh's phone."
                print "\nYou turn the flashlight on."
            elif "drawers" in choice or "drawer" in choice and flashlight:
                print "\nAll the other drawers are empty."
                print nothing
            elif "table" in choice or "stain" in choice:
                print "\nOn the table is a cut finger lying in blood."
                print "\nApparently it's been chewed... The blood hasn't coagulated yet."
                if josh_found == False:
                    print "\nYou start fearing for April but you notice:"
                    print "\nIt looks like a male finger."
                    print "\nYou fear the worst now."
                if josh_found:
                    print "\nThis is Joshua's finger."
            elif "floor" in choice:
                print "\nThe blood on the floor isn't quite dry yet."
            elif "door" in choice and "wooden" in choice:
                if greta_ko == False:
                    print "\nYou hear strange undescribable noises in the other room."
                print "\nThe door knob has blood on it."
            elif "cupboards" in choice:
                print "\nOnly empty cupboards."
            elif "sink" in choice:
                print "\nThe sink has pasty brown water in it."
                print "\nThe tap is broken."
            elif "bag" in choice:
                print "\nInside you find camping gear and male clothing."
                if "two" in tin_cans or "one" in tin_cans:
                    print "\nYou also find %s." % tin_cans
                    print "\nThis could come in handy if you ever feel too tired..."
                    p_player_HP(player_HP)
                    while "yes" not in choice and "no" not in choice:
                        print "\n\nDo you wish to eat and heal?\n"
                        choice = raw_input("%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()
                        if "yes" not in choice and "no" not in choice:
                            print invalid
                    if "no" in choice:
                        print "\nYou leave the cans untouched."
                    elif "yes" in choice:
                        if player_HP == 6:
                            print "\nYou're not hungry right now.\n\n%s(Player health is at maximum.)%s" % (gray, default)
                        elif player_HP < 6:
                            if "one" in tin_cans:
                                tin_cans = "zero"
                            elif "two" in tin_cans:
                                tin_cans = "one tin can"
                            elif "three" in tin_cans:
                                tin_cans = "two tin cans."
                            print "\nCold beans... Whatever, you feel much better."
                            player_HP = 6
                            saved_player_HP = player_HP
                            p_player_HP(player_HP)
                elif "zero" in tin_cans:
                    print "\nThere are no tin cans left."
            elif "windows" in choice or "window" in choice:
                print windows
            else:
                print nothing
        else:
            print invalid
        choice = p_choice()
    kitchen()

#MAIN ROOM: 

def main_room():

    global silver_dagger, bottle_switch_found, bottle_switch_on, pictures, bedroom_trap, altar, altar_dispell, defense_activated, grizzly_killed, saved_player_HP, first, april_freed, balcony_visited, rings_taken, bucket1, bucket2
    print "\n..."
    time.sleep(3)
    print "\n%s//// MAIN ROOM (FLOOR 1) \\\\\\\\\%s" % (cyan, default)
    if defense_activated:
        print "\n%sAs you climb down the last stair and touch the floor, you hear an extremely loud voice.%s" % (bold, default)
        p_scroll()
        print "\nThe voice is very deep and sounds like its coming from everywhere."
        print "\n%s\"You, who have foresaken the Ulfedhnar rings of trust.\"" % bold
        print "\n\"You, who have entered this home unwelcomed.\""
        print "\n\"Fight your best and let your lungs pump their last breath.\"%s" % default
        p_scroll()
        print "\nOut of nowhere the stuffed grizzly bear stands on its two legs."
        print "\nIt emits a deep growl and threateningly shows its teeth."
        print "\nIt now starts running towards you, pushing the furniture on its way."
        first = "enemy"
        rings_taken = False
        if silver_dagger == False:
            battle(Grizzly, west_tower, ["baseball bat", "bat", "bat", "weapon"])
        elif silver_dagger:
            battle(Grizzly, west_tower, ["silver dagger", "dagger", "blade", "blade", "weapon"])
        rings_taken = True
        defense_activated = False
        grizzly_killed = True
        print "\nThe bear growls with fury."
        print "\nHe backslaps you sending you flying across the room."
        print "\nYour body slams into the wall with violence, making a weapon display fall next to you."
        print "\nThe spear in the weapon unbounds itself from the display when hitting the ground."
        print "\nYou seize it while the bear is coming at full speed towards you."
        print "\nYou wait until the last moment to lift the lance and the animal impales his head right on the lance."
        print "\nHe stops right in his motion only a few centimeters away from your face."
        p_scroll()
        print "\nA blue light shines from where the spear punctured the body."
        print "\nIt grows bigger and bigger until it blinds you."
        print "\nThe bear disintegrates in a blue halo while wind gushes through the manor."
        print "\nAfter some moments, everything settles down."
    elif defense_activated == False:
        print "\nThis is a vast and luxurious room."
        print "\nIt is heavily decorated with paintings, antique weapons and hunting trophies."
        if grizzly_killed:
            print "\n%sDue to the battle with the grizzly, some of the decorations are broken and have fallen to the floor.%s" % (bold, default)
        print "\nA fireplace facing the opposite end of the entrance door lights up the room with a warm light."
        print "\nA large balcony on the second floor with six animal statues stands above it."
        print "\nThe stairs leading to the balcony starts right to the left of the manor's entrance." 
        if balcony_visited == False:
            print "\nYou'd need to climb upstairs to see better but you definitely can see\na double door separating the statues."
        elif balcony_visited:
            print "\nA double door separates the row of statues on the balcony."
        print "\nThere is a white door to the left of the fireplace. Further left, still under the balcony,\nis a library with shelves full of books and a few artifacts."
        if grizzly_killed:
            print "\n%sBooks and objects have been thrown off the shelves.%s" % (bold, default)
        print "\nTorches on the walls accompany the fireplace creating slow dancing shadows."
        if grizzly_killed == False:
            print "\nIn the middle of the room is a large dining table with fine silverwear, plates and glasses."
        elif grizzly_killed:
            print "\n%sThe dining table has been displaced by a few feet and most of the silverwear has fallen to the floor.%s" % (bold, default)
        print "\nOn the right hand of the fireplace is what you would describe as a living room, with three\nsiting chairs centered around a small table."
        if grizzly_killed:
            print "\n%sOne of the living room chairs has fallen to the floor also.%s" % (bold, default)
        print "\nNext to the living room is a medieval metal armor."
        print "\nOld pictures are hanged in the stairway."
        if grizzly_killed:
            print "\n%sA couple of pictures have fallen in the midst of the battle.%s" % (bold, default)
        if grizzly_killed == False:
            print "\nA very large stuffed grizzly bear in a threatening pose is up against the east wall."
        if grizzly_killed == False:
            print "\nRight in the corner next to the bear is a full bar with two stools."
        if grizzly_killed:
            print "\nRight in the corner next to where the bear was standing is a full bar with %sone stool\nstanding and the other broken to pieces.%s" % (bold, default)
        if grizzly_killed == False:
            print "\nThe whole place although neatly kept, is covered in dust and cobwebs..."
        if grizzly_killed:
            print "\n%sThe place is a mess.%s" % (bold, default)
        if april_freed:
            print "\n%sApril is mumbling while passed out on your back.%s" % (bold, default)
    choice = p_choice()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2

        elif ["go", "door"] in choice:
            print "\nWhich one?"
        elif "go" in choice:
            if "main" in choice:
                print "\nYou're already in the main room."
            elif "yard" in choice or "outside" in choice or "double" in choice or "entrance" in choice:
                print "\nYou exit the manor."
                yard()
            elif "kitchen" in choice or "white" in choice:
                print "\nThe door opens with a faint squeak."
                kitchen()
            elif "upstairs" in choice or "stairs" in choice or "up" in choice or "balcony" in choice or "second" in choice:
                print "\nYou climb up the stairs."
                balcony()
            elif "windows" in choice or "window" in choice:
                print windows
            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "room"] == choice:
                print specific_search
            elif ["search", "table"] == choice or ["search", "door"] == choice:
                print "\nWhich one?"
            elif "paintings"  in choice:
                print "\nPortraits of white haired people in mythological sceneries."
            elif "trophies" in choice:
                print "\nThere are two mounted above the fireplace, a bufallo and a mountain lion."
            elif "weapons" in choice:
                print "\nThere are weapons around the room mounted on wooden displays."
                print "\nThere is a cimtar, a metal spear, and a roman sword."
                print "\nThere also is a centurion helmet."
                print "\nThey are too high for you to touch them."
                if silver_dagger == False:
                    print "\nAt least you have your baseball bat..."
                elif silver_dagger and altar_dispell == False:
                    print "\nThe silver dagger is more than enough."
            elif "bar" in choice or "bottle" in choice:
                if bottle_switch_found:
                    print "\nYou find a particularly shaped silver bottle."
                if bottle_switch_found == False:
                    bottle_switch_found = True
                    print "\nDifferent kinds of liquor and glasses compose the bar."
                    print "\nYou find a particularly shaped silver bottle."
                    print "\nThe stamp is a wolf sigil decoration, underneath it is written: \"Ulfhednar\"."
                    print "\nTrying to grab it, it is attached to the shelf."
                    print "\nThis bottle is some sort of %sswitch%s." % (magenta, default)
                if bottle_switch_found: 
                    while True:
                        if bottle_switch_on == False:
                            print "\n\nDo you wish to pull the bottle %sswitch%s on%s?" % (magenta, bold, default)
                            choice = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()
                            if "yes" in choice:
                                bottle_switch_on = True
                                print "\nYou pull on the bottle and hear a mechanical sound."
                                if paw_switch_on:
                                    print "\n%sIt sounds like something big moved upstairs%s." % (bold, default)
                                    altar = True
                                    bedroom_trap = False
                                elif paw_switch_on == False:
                                    bedroom_trap = True
                                break
                            elif "no" in choice:
                                print "\nYou leave it alone."
                                break
                            else:
                                print invalid

                        elif bottle_switch_on:
                            print "\n\nDo you wish to pull the bottle %sswitch%s off%s?" % (magenta, bold, default)
                            choice = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()
                            if "yes" in choice:
                                bottle_switch_on = False
                                print "\nYou pull on the bottle and hear a mechanical sound."
                                if altar:
                                    print "\n%sIt sounds like something big moved upstairs%s." % (bold, default)
                                altar = False
                                break
                            elif "no" in choice:
                                print "\nYou leave it alone."
                                break
                            else:
                                print invalid
            elif "library" in choice or "bookshelf" in choice or "shelves" in choice or "books" in choice:
                if grizzly_killed:
                    print "\nSome of the books are now on the floor."
                print "\nOld books and strange objects are on the shelves:"
                print "\nA bronze world-globe, a human skull and a crow claw, amongst other things."
                print "\nSome of the books have unreadable hieroglyphs."
            elif "table" in choice:
                if "living" in choice and "room" in choice:
                    print "\nA finely decorated table."
                    if grizzly_killed:
                        print "\nIt has taken damage from the battle."
                elif "dining" in choice or "middle" in choice:
                    if grizzly_killed == False:
                        print "\nThe table is covered in dust and cobwebs, it looks like it hasn't been touched in a while."
                    elif grizzly_killed:
                        print "\nThe table has been shaken so bad there's barely anything left on it. Most of the items are on the floor."
                else:
                    print nothing
            elif "living" in choice and "room" in choice:
                print "\nFinely decorated furniture. Comfortable chairs and table."
                if grizzly_killed:
                    print "\nIt has taken damage from the battle."
            elif "statues" in choice or "balcony" in choice:
                print "\nYou'd need to climb upstairs to the balcony to do that."
            elif "fireplace" in choice:
                print "\nThe fireplace has no wood in it. You don't understand how there can even be fire..."
            elif "armor" in choice or ("metal" in choice and "armor" in choice):
                print "\nA wolf's sigil is on the breastplate. Looks heavy."
            elif "grizzly" in choice or "bear" in choice and grizzly_killed == False:
                print "\nIt looks like it's about to slap your head off. Scary."
            elif "grizzly" in choice or "bear" in choice and grizzly_killed:
                print "\nThe bear has disappeared."
            elif "photos" in choice or "photographs" in choice or "pictures" in choice or "pics" in choice or "stairway" in choice or "stairs" in choice:
                if grizzly_killed:
                    print "\nSome pictures have fallen to the floor while you were fighting the grizzly."
                print "\nA white haired man appears in most pictures."
                if silver_dagger:
                    print "\nThis is the man in the casket."
                print "\nThey have been taken around the world."
                print "\nOther similar haired people appear also."
                print "\nThese pictures are very old."
                pictures = True
            elif "windows" in choice:
                print windows
            else:
                print nothing
        else:
            print invalid
        choice = p_choice()
    main_room()


#CELLAR: Items -  Entrance Key.

def cellar():
    global manor_key, bucket1, prison_key, prison_unlocked, saved_player_HP, flashlight, bucket1, bucket2

    print "\n..."
    time.sleep(3)
    print "\n%s//// CELLAR (FLOOR -1) \\\\\\\\\%s" % (cyan, default)
    print "\nThe room is a moist and dimly lit stone walled cellar."
    if flashlight == False:
        print "\nThe few rays of moonlight coming from the windows cast light on what seem to be old wine kegs."
    elif flashlight:
        print "\n%sYour flashlight shows a row of three wine kegs." % bold
        print "\nThe place is covered in dust.%s" % default
    print "\nA smell of rancid vinegar reaches your nostrils."
    if flashlight == False:
        print "\nYou can barely see anything."
    print "\nThere's a bucket next to the wooden door."
    print "\nYou distinguish a heavy steel door at the opposite end of the room."
    choice = p_choice()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2

        elif ["go", "door"] == choice:
            print "\nWhich one?"
        elif "go" in choice:
            if "cellar" in choice:
                print "\nYou're already in the cellar."
            elif "path" in choice or "gravel" in choice or "outside" in choice or "wooden" in choice:
                print "\nYou walk back out."
                gravel_path()
            elif "door" in choice or "prison" in choice:
                if "prison" in choice or "steel" in choice or "metal" in choice or "heavy" in choice and "inside" in choice:
                    if prison_unlocked:
                        print "\nYou enter the prison."
                        prison()
                    elif prison_key:
                        prison_unlocked = True
                        print "\nThe %ssteel key%s fits perfectly in the hole and the door unlocks with a mechanical sound." % (magenta, default)
                        print "\n..."
                        time.sleep(3)
                        print "\nYou enter the prison."
                        prison()
                    elif manor_key:
                        print "\nThis isn't the appropriate %skey%s... The door is locked." % (magenta, default)
                    else:
                        print "\nThe door is locked."
            elif "windows" in choice or "window" in choice:
                print windows
            else:
                 print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "room"] == choice or ["search", "cellar"] == choice:
                print specific_search
            elif ["search", "door"] == choice:
                print "\nWhich one?"
            elif "bucket" in choice:
                print "\nInside you find skulls and bones from rodents of some kind."
                if bucket1 == False:
                    bucket1 = True
                    print "\nOne of the skulls has a tiny piece of %sfolded paper%s." % (magenta, default)
                    print "\nOn it is handwritten:"
                    print paper1
                    print "\nYou stuff it in your pocket."
                    print "\n%s(Type \"%s%s\" any time to read the paper again.)%s" % (gray, paper, gray, default)
                elif bucket1:
                    print "\nThere is nothing else to find."
            elif "kegs" in choice or "keg" in choice:
                if manor_key:
                    print "\nThere is nothing else to find."
                else:
                    manor_key = True
                    print "\nYou find an %siron key%s under one of the wine kegs. This might come in handy..." % (magenta, default)
                    print "\nYou take it with you."
            elif "door" in choice and ("heavy" in choice or "steel" in choice or "metal" in choice):
                print "\nThe steel door has a small barred opening at head's height." 
                if silver_dagger:
                    print "\nThe inside of the room is lit by the blue light coming from the open casket."
                if silver_dagger == False:
                    print "\nThe inside of the room is pitch black."
            elif "windows" in choice:
                print windows
            elif "key" in choice:
                print specific_search
            else:
                print nothing
        elif "drink" in choice and ("wine" in choice or "keg" in choice):
            print "\nThis is probably a bad idea."
        else:
            print invalid
        choice = p_choice()
    cellar()
 
# GRAVEL PATH:

def gravel_path():
    global first, greta_dead, silver_dagger, player_HP, saved_player_HP, bucket1, bucket2
    print "\n..."
    time.sleep(3)
    print "\n%s//// GRAVEL PATH (FLOOR 1) \\\\\\\\%s" % (cyan, default)
    if silver_dagger and greta_dead == False:
        print "\n%sYou hear a wolf howling in the distance.%s" % (bold, default)
    print "\nYou are standing on a gravel path located on a patch of well kept grass."
    print "\nThe property walls surround you on the south and east side."
    print "\nAn impressive pine tree stands in the corner, close to the walls."
    print "\nOn the north side is a wooden door leading underneath the manor."
    print "\nThe gravel marks a left curved way from the gate to the door, ending by lowering steps."
    if greta_dead == True:
        print "\nThe wind still blows."
    if greta_dead == False:
        print "\nThe wind still blows %sand the tree branches crack.%s" % (bold, default)
    choice = p_choice()
    while ["look", "around"] != choice:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2
        elif "go" in choice:
            if "path" in choice:
                print "\nYou're already on the gravel path."
            elif ("door" in choice or "cellar" in choice or "inside" in choice or "manor" in choice) and greta_dead:
                print "\nYou push and walk through the wooden door."
                cellar()
            elif ("yard" in choice or "gate" in choice) and greta_dead:
                print "\nYou open the rusty gate and walk back to the yard."
                yard()
            elif ("door" in choice or "cellar" in choice or "inside" in choice or "manor" in choice or "yard" in choice or "gate" in choice) and greta_dead == False:
                first = "enemy"
                if "yard" in choice or "gate" in choice:
                    print "\nRight as you're about to push the gate open, you hear a shriek coming from behind you."
                elif "door" in choice or "cellar" in choice or "inside" in choice or "manor" in choice:
                    print "\nAs soon as you touch the wooden door you hear a shriek coming from behind you."
                print "\nSomething jumps on your back and you then feel a knife sting in your right arm."
                p_scroll()
                print "\nYou roll over to the side and throw whatever is on your back to the ground."
                print "\nIt's the woman again. Her head is hanging from her neck, swinging from side to side."
                print "\nThere is no way she could be alive."
                print "\nShe's crouched on the floor with a knife in her hand."
                silver_dagger = False
                battle(Greta_ghoul, prison, ["weapon", "silver dagger", "dagger", "dagger", "blade"])
                silver_dagger = True
                print "\nShe is startled from the hit for a few seconds."
                print "\nThis time you are giving your very best shot."
                print "\nYou swing your bat with the strongest intent you've ever had in your life."
                print "\nThis hits her in the back so hard your baseball bat breaks in half."
                print "\nShe falls to the ground screaming with pain."
                p_scroll()
                print "\nYou firmly grab your silver dagger and repeatidly stab her in the chest with it."
                print "\nShe screams with agony while she contorts."
                print "\nYou watch with horror as her skin starts peeling and smoking like it's burning."
                print "\nHer skin melts off in a dark goo leaving her flesh and bones to be seen."
                print "\nYou stand there and watch her suffer. The smell is almost unbearable."
                p_scroll()
                print "\nSoon, there is nothing left of her, the goo has burned into smoke."
                print "\nAfter gathering yourself, you toss the two useless pieces of the baseball bat."
                greta_dead = True

            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "area"] == choice:
                print specific_search
            elif "tree" in choice and greta_dead == False:
                first = "player"
                print "\nYou hear a faint sound: like someone heavily breathing."
                print "\nIt's almost like there is a presence staring at you."
                p_scroll()
                print "\nLooking up in the branches there definitely is something there, alive."
                print "\nFlashing your light up there, you see what the shape is."
                print "\nIt's the woman again. She's crouched on one of the branches staring at you."
                print "\nHer head is hanging from her neck, swinging from side to side."
                print "\nThere is no way she could be alive."
                print "\nThe light blinds her and she growls."
                print "\nSuddenly, she jumps down."
                print "\nShe lands like a cat, you notice a knife in her right hand."
                silver_dagger = False
                battle(Greta_ghoul, prison, ["baseball bat", "bat", "silver dagger", "dagger", "blade"])
                silver_dagger = True
                print "\nShe is startled from the hit for a few seconds."
                print "\nThis time you are giving your very best shot."
                print "\nYou swing your bat with the strongest intent you've ever had."
                print "\nThis hits her in the back so hard your baseball bat breaks in half."
                print "\nShe falls to the ground screaming with pain."
                p_scroll()
                print "\nYou firmly grab your silver dagger and repeatidly stab her in the heart with it."
                print "\nShe screams with agony while she contorts."
                print "\nYou watch with horror as her skin starts peeling and smoking like it's burning."
                print "\nHer skin melts off in a dark goo leaving her flesh to be seen."
                print "\nYou stand there and watch her suffer. The smell is almost unbearable."
                print "\nSoon, there is nothing left of her, the goo has burned into smoke."
                greta_dead = True
            elif "windows" in choice:
                print "\nThere are no windows here."
            else:
                print nothing
        else:
            print invalid
        choice = p_choice()
    gravel_path()
                
 
# GAME STARTS HERE:

def yard():
    global manor_key, manor_unlocked, april_freed, bucket1, bucket2
    print "\n..."
    time.sleep(3)
    print "\n%s///// YARD (FLOOR 1) \\\\\\\\%s" % (cyan, default)
    print "\nAs you look around, you find yourself in the yard located in front of the building."
    print "\nFacing north of the tall gate is the main entrance: A large double door made of wood."
    print "\nThe manor is painted white, although time has given it a greyish tone."
    print "\nAn alley surrounded by tall trimed bushes on each side leads from the entrance gate to the manor."
    print "\nThe bushes on the east side are cut in the middle by another, smaller iron gate."
    print "\nA gloomy light is shined on the manor by the moon."
    print "\nThere are barred windows on the second floor from which warm light can be seen."
    print "\nThe wind blows making the bush leaves sing."
    if april_freed:
        print "\n%sSouth of the alley, on the other side of the tall double gated entrance, your car awaits.%s" % (bold, default)
    choice = p_choice()
    while choice != ["look", "around"]:
        if "list" in choice:
            print command_list
            if bucket1 and bucket2:
                print "\n\t    Type \"%s\" to read the handwritten papers you found." % paper
            elif bucket1 or bucket2:
                print "\n\t    Type \"%s\" to read the handwritten paper you found." % paper
        elif "paper" in choice and (bucket1 or bucket2):
            if bucket1:
                print paper1
            if bucket2:
                print paper2
        elif "go" in choice:
            if "yard" in choice:
                print "\nYou're already in the yard."
            elif april_freed and ("car" in choice or "entrance" in choice or "gate" in choice):
                print "\nWith one hand holding April, you push the tall gate open and exit the property."
                ending()
            elif "gate" in choice or "path" in choice:
                print "\nThe gate is rusty but by pushing hard you manage to open it."
                gravel_path()
            elif "manor" in choice or "building" in choice or "main" in choice or "entrance" in choice or "door" in choice or "inside" in choice:
                if manor_unlocked:
                    print "\nYou enter the manor."
                    main_room()
                elif manor_key:
                    manor_key = False
                    manor_unlocked = True
                    print "\nThe %siron key%s unlocks the door." % (magenta, default)
                    print "\n..."
                    time.sleep(2)
                    print "\nYou enter the manor."
                    main_room()
                else:
                    print "\nThe entrance door is locked."
            elif "windows" in choice:
                print windows
            else:
                print invalid
        elif "search" in choice:
            if ["search"] == choice or ["search", "area"] == choice or ["search", "yard"] == choice or "key" in choice:
                print specific_search
            elif "windows" in choice:
                print windows
            else:
                print nothing
        else:
            print invalid
        choice = p_choice()
    yard()

        
#WAKE UP TO START GAME:

def wake_up():

    global name

    print "\n..."
    time.sleep(3)
    wake_prompt = "\n\nWould you like to wake up?\n\n%s(Type \"yes\" to wake up or \"no\" to restart the tutorial.)%s\n" % (gray, default)
    print wake_prompt
    tcflush(sys.stdin, TCIFLUSH)
    choice = raw_input("> ").lower().split()
    while True:
        if "no" in choice and "yes" not in choice:
            print "\n\nAre you sure you want to restart the tutorial?"
            tcflush(sys.stdin, TCIFLUSH)
            sure = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()

            while True:
                if "yes" in sure and "no" not in sure:
                    dream()
                elif "no" in sure and "yes" not in sure:
                    break
                else:
                    print invalid
                print "\n\nAre you sure you want to restart the tutorial?"
                tcflush(sys.stdin, TCIFLUSH)
                sure = raw_input("\n%s(Type \"yes\" or \"no\".)%s\n\n> " % (gray, default)).lower().split()

        elif "yes" in choice and "no" not in choice:
            print "\nThis was just a dream..."
            print "\n..."
            time.sleep(3)
            print "\n%s//// CAR \\\\\\\\%s" % (cyan, default)
            print "\nYou wake up startled and gasping for air."
            print "\nAs your brain turns back on, you start remembering..."
            print "\nYou drove 14 hours straight and fell alseep from exhaustion."
            print "\nYou check the time: 2:53 AM."
            print "\nYou remember what you're doing asleep in the driver seat of your car\nin the middle of the night."
            p_scroll()
            print "\n\n%sYou're searching for your missing daughter April.%s\n" % (red, default)
            p_scroll()
            print "\nThe last time you heard from her was 5 days ago when she went camping\nwith her boyfriend Joshua."
            print "\nShe should've been back two days ago. You know her damn well, and Josh is a good kid: something's off." 
            print "\nHer phone tracking app's last signal leads here: an isolated and old looking building."
            print "\nYou open the car and step outside, the cold hits you."
            print "\nYou head for the trunk and grab your nailed baseball bat:\n\n\"Better be safe than sorry...\""
            p_scroll()
            print "\nImposing spiked walls define the property perimeter."
            print "\nA double gate with silver ornaments serves as the entrance."
            print "\nPeeking through the gate you distinguish what you would describe as a spooky two story manor\nwith two towers located on the north east end and north west end of the manor."
            print "\nChills run down your spine as you push the gate open and enter..."
            p_scroll()
            print "\nThe entrance gate closes behind you with a loud metalic clank."
            yard()
        else:
            print invalid
            print "\nYou should wake up."
        print wake_prompt
        choice = raw_input("\n> ").lower().split()

    
# COMMAND TUTORIAL: Here the player learns the following commands:

# -block, -dodge, -attack, -look around, -go and -search. 

def commands():
    fail = "\n%sInvalid command.%s Pay closely attention and follow the instructions in the prompt.\n" % (red, default)
    wake = "\n\"YOU GOTTA WAKE UP!\"\n"
    block_prompt = "\n\nType \"%s\" to block the attack from hitting you.\n" % block
    print block_prompt
    tcflush(sys.stdin, TCIFLUSH)
    choice = raw_input("> ").lower().split()

# Block command
    while "block" not in choice:
        print fail
        print block_prompt
        tcflush(sys.stdin, TCIFLUSH)
        choice = raw_input("> ").lower().split()
    print "\nYou learned the %s command!" % block
    p_scroll()
    print "\nThe punch lands on your right forearm as you succesfully block."

# Dodge command
    print "\nYou hear Joe's voice: \"Nice! Now dodge the next one %s!" % name
    dodge_prompt = "\n\nType \"%s\" to dodge the next punch.\n" % dodge
    print dodge_prompt
    tcflush(sys.stdin, TCIFLUSH)
    choice = raw_input("> ").lower().split()

    while "dodge" not in choice:
       print fail
       print dodge_prompt
       tcflush(sys.stdin, TCIFLUSH)
       choice = raw_input("> ").lower().split()
    print "\nYou learned the %s command!" % dodge
    p_scroll()

# Attack command

    attack_prompt = "\n\nType \"%s\" to punch the man.\n" % attack
    print "\nThe drunk man misses and stumbles. He looks confused for a few split seconds.\n"
    print "Again, Joe says: \"Perfect! Now is your chance! Knock him with one of those nasty uppercuts you got!\"" 
    print attack_prompt
    tcflush(sys.stdin, TCIFLUSH)
    choice = raw_input("> ").lower().split() 

    while "attack" not in choice:
        print fail
        print attack_prompt 
        tcflush(sys.stdin, TCIFLUSH)
        choice = raw_input("> ").lower().split() 
    print "\nYou learned the %s command!" % attack
    p_scroll()
    print "\nYou learned the \"%s\", \"%s\" and \"%s\" commands." % (block, dodge, attack)
    print "\n%sNote:%s These commands are only used in combat sequences." % (bold, default)
    p_scroll()
    print "\nYou hit him so hard he instantly gets knocked out and falls to the ground."
    print "\nA few moments later he gets back up and shamefuly leaves without saying a word."
    print "\nAfter this \"conversation\", you need a %scigarette%s. But where are they?" % (magenta, default)
    print "\n%s(During the game, %simportant items%s are highlighted in pink.)%s" % (gray, magenta, gray, default)
    print "\nYou can't find them on you so you tell your co-workers you're going to look for them in your car."
    print "\nA quick glance around helps you to locate yourself and know your surroundings." 
    look_prompt = "\n\nType \"%s\" to have a descripion of where you are.\n" % look
    print look_prompt
    tcflush(sys.stdin, TCIFLUSH)
    choice = raw_input("> ").lower().split() 

# Look around command

    while ["look", "around"] != choice:
        print fail
        print look_prompt
        tcflush(sys.stdin, TCIFLUSH)
        choice = raw_input("> ").lower().split()
    print "\nYou learned the %s command!" % look
    p_scroll()
    print "\n..."
    time.sleep(3)
    print "\n%s//// PARKING LOT \\\\\\\\%s" % (cyan, default)
    print "\nThe street is dark and humid."
    print "\nVapor is coming out of the sewers and night dwellers are busy doing who knows what."
    print "\nYou can faintly hear the music coming from within the club."
    print "\nYou see your car at the end of the street."
    
# Go to command
 
    go_prompt = "\n\nType \"%s %scar%s\", where car is the %slocation%s you want to go to.\n" % (go, cyan, default, cyan, default)
    print go_prompt
    tcflush(sys.stdin, TCIFLUSH)
    choice = raw_input("> ").lower().split()
    while "go" not in choice or "car" not in choice:
        if ["go"] == choice:
            print "\nOk but %sWHERE\033%s do you want to %s?" % (cyan, default, go)
        elif "go" in choice and "club" in choice:
            print "\nYou're working, this isn't the time to party."
        else:
            print fail
        print go_prompt
        tcflush(sys.stdin, TCIFLUSH)
        choice = raw_input("> ").lower().split() 
    print "\nYou learned the %s command!" % go
    print "\n%sNote:%s In game, the %s command is used to move from one area described: %s//// AREA \\\\\\\\%s to another, adjacent %s//// AREA \\\\\\\\\%s." % (bold, default, go, cyan, default, cyan, default)
    print "\nYou may use words such as \"%soutside%s\" or \"%sdownstairs%s\" for example, according to the situation." % (cyan, default, cyan, default)
    print "\nYou do not need %s to move within the area, only from one to another." % go
    p_scroll()
    print "\nYou head towards your car."
    print "\n..."
    time.sleep(3)
    print "\n%s//// CAR \\\\\\\\%s" % (cyan, default)
    print "\nA black 2008 Buick Enclave."
    print "\nYou open the vehicle and enter it."
    print "\nYou now remember your %scigarettes%s are in the glovebox." % (magenta, default)
    search_prompt = "\n\nType \"%s %sglovebox%s\", where glovebox is %swhere%s you are searching.\n" % (search, yellow, default, yellow, default)
    print search_prompt
    tcflush(sys.stdin, TCIFLUSH)
    choice = raw_input("> ").lower().split()

# Search command
    while "search" not in choice or "glovebox" not in choice:
        if ["search"] == choice:
            print fail
            print specific_search
        elif "search" in choice and "trunk" in choice:
            print "\nThe trunk is closed and you know for sure the %scigarettes%s are in the %sglovebox%s." % (magenta, default, yellow, default)
        elif "search" in choice and "car" in choice:
            print specific_search
            print "\nYou know for sure the %scigarettes%s are in the %sglovebox%s." % (magenta, default, yellow, default)
        else:
            print fail
        print search_prompt
        tcflush(sys.stdin, TCIFLUSH)
        choice = raw_input("> ").lower().split()                   
    print "\nYou learned the %s command!" % search
    p_scroll()
    print "\n\n%sRecap:%s You have learned the following commands: \"%s\", \"%s\" and \"%s\"." % (bold, default, search, go, look)
    print "\nThese are the only commands that you can use in the game."
    print "\nThe %s command needs an item after it to specify %swhere%s you are searching." % (search, yellow, default)
    print "\nThe %s command is used to move from one %s//// AREA \\\\\\\\%s to another adjacent %s//// AREA \\\\\\\\%s." % (go, cyan, default, cyan, default)
    print "\nThe %s command is useful to refresh the area description." % look
    print "\nType \"%s\" while playing to have a command recap.\n" % list0

    p_scroll()
    print "\nYou find the cigarettes and light one up."
    print "\nAs you inhale the smoke you ease up a little."
    print "\n\"This job sucks.\" you think to yourself as you blow smoke out.\n"
    print "You hear a familiar voice: \"So how've you been %s?\"\n" % name
    p_scroll()
    print "\nYou turn to your right and on the passenger seat is Joe."
    print "\nYour jaw drops."
    print "\nYou just can't understand what he's doing in your car. He's eating a slice of pizza as usual.\n"
    print "\"Joe?! What on earth are you doing here? How did you get in my car?! You died like 4 years ago!\""
    print "\nHe grins at you and says: \"Tell me about it! There's no pizza up there!\""
    print "\nHe bites into the slice of pizza and continues: \"I'm here to tell you something...\""
    print "\nThis makes no sense to you. You listen, confused and unable to speak.\n"
    p_scroll()
    print "\n\"I'm here to tell you that you gotta wake up!\""
    print "\nYou stay silent."
    print "\n\"You gotta wake up %s!\"" % name
    print "\nHis eyes turn black and his teeth seem to be sharp as razors..."
    print "\nA twisted smile appears on his face as he screams louder and louder:"
    print wake
    p_scroll()
    print "\nHe starts lascerating you with his arms while repeatidly shouting:\n"
    print wake
    time.sleep(1)
    print wake
    time.sleep(1)
    print wake
    time.sleep(1)
    wake_up()

#DREAM INTRO:

def dream():

    global name
    print "\n\n\n"
    print "\n..."
    time.sleep(3)
    print "\n\n%s//// TUTORIAL \\\\\\\\\%s" % (cyan, default)
    print "\nOn a late thursday night in front of the Shogun club where you work as a bouncer,"
    print "a guy who obviously has had too many drinks starts being aggressive with you."
    print "\nHe drunkenly asks you:\n"
    print "\"What's your name buddy?\"\n\n"

    tcflush(sys.stdin, TCIFLUSH)
    name = raw_input("%sName ? > " % bold).strip().capitalize()
    while name.isalpha() == False:
        print "\n\n%s(You may only type in letters.)%s\n" % (gray, default)
        name = raw_input("%sName ? > " % bold).strip().capitalize()

    print "\n\n%s\"And how much time have you been a bouncer here for %s? I've never seen your face before.\"" % (default, name)
    print "\nYou answer: \"I moved here a couple of months ago with my...\""
    print "\nHe barely listens and starts arguing:"
    print "\n\"Why won't you let me in man? My daughter's in there you know!\""
    p_scroll()
    print "\nYou calmly respond that he's too drunk to enter and that maybe he shouldn't be going"
    print "out with his daughter on a weekday."
    print "\n\"And who the hell are you to be telling me what to do?\""
    print "\nYou patiently answer: \"I'm the guy that has the power to let you in or not.\""
    p_scroll()
    print "\nYou've apparently made him mad, and he clumsily tries to punch you."
    print "\nAt that moment, you remember Joe, your gym trainer, back in your boxing career days,"
    print "screaming at you while fighting in the ring: \"Block the first blow %s!\"" % name
    commands()

# GAME STARTS HERE:

def start():
    print "\n\n\n"
    print "%s//// SEARCHING FOR APRIL \\\\\\\\%s" % (red, default)
    print """\n\n%sWelcome to SEARCHING FOR APRIL !\n
    Instructions :%s\n 
    Read the prompt and descriptions carefully.
    They sometimes change according to events in the game.
    Enter commands when "%s> %s" is displayed.
    Type "CTRL-C" at any moment to quit the game.
    (Progress will not be saved.)
    
    Thanks for playing! Good luck and have fun!\n""" % (bold, default, bold, default)
    p_scroll()
    dream()
#yard()
start()   
#gravel_path()
#cellar()
#wake_up()
#main_room()
#kitchen()
#storage()
#prison()
#balcony()
#bedroom()
#ending()
