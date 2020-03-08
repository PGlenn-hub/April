import random


def battletest():

    curr_prompt = "\nWhat do you do?\n"
    print curr_prompt
    choice = " player choice: block"
    command_choice = ["attack", "dodge", "block"]


    global ennemy_dead 
    ennemy_dead = False
    while ennemy_dead == False: 

        correct_choice1 = random.choice(command_choice)
        correct_choice2 = random.choice(command_choice) 

        print "C1:", correct_choice1
        print "C2:", correct_choice2
        print choice

        player_weapon = "baseball bat"


       # ENNEMY RANDOMIZED NARRATIVE SENTENCE 
        ennemy_name = ["the woman", "she"]
        ennemy_name_picked = random.choice(ennemy_name)
        ennemy_possessive_pronoun = "her"
        ennemy_reflexive_pronoun = "herself"

        actions = ["runs at you", "attacks you", "goes for you", "tries to strike you"]
        action_used = random.choice(actions) # format 1
        weapons = ["knife", "knife"]
        weapon_used = random.choice(weapons) # format 2
        adjectives = ["fearcefully", "aggresively", "mercilessly", "dangerously", "swiftly"]
        adjective_picked = random.choice(adjectives) # format 3
        target_synonyms = ["aiming for", "headed for", "going for", "trying to hit", "targetting"]
        synonym_picked = random.choice(target_synonyms) # format 4
        body_part = ["heart", "neck", "face", "stomach", "liver", "throat"]
        body_part_aimed = random.choice(body_part) # format 5
        ennemy_attack = "\n%s %s %s with %s %s while %s your %s." % (ennemy_name_picked.capitalize(), adjective_picked, action_used, ennemy_possessive_pronoun, weapon_used, synonym_picked, body_part_aimed)


        if "attack" in choice or "dodge" in choice or "block" in choice:
            if ("dodge" in correct_choice1 or "dodge" in correct_choice2) and "dodge" in choice:
                print "\nYou roll over to the side, dodging a powerful and probably fatal blow."
                print "\n%s misses and crashes into the wall."
                print "\n%s is staggered and gathers %s." % (ennemy_name_picked.capitalize(), ennemy_reflexive_pronoun)
            elif ("block" in correct_choice1 or "block" in correct_choice2) and "block" in choice:
                print "\nYou block the attack."
                print "\nThe opponent is much stronger than you thought."
                print curr_prompt
                choice = raw_input("> ").lower()
                if "attack" in choice: 
                    print "You hit back right in the back of %s head so hard you here a crunch sound." % ennemy_possessive_pronoun
            elif ("attack" in correct_choice1 or "attack" in correct_choice2) and "attack" in choice:
                print "\nYou get close enough to swing your %s at %s as hard as you can." % (player_weapon, ennemy_possessive_pronoun)
                print "\n%s falls to the ground with a growl." % (ennemy_name_picked.capitalize())
            elif (choice != correct_choice1) or (choice != correct_choice2):
                print "\nYou have no time to react."
                print "\nThe %s reaches your %s dealing a lethal blow." % (weapon_used, body_part_aimed)
                print "You died."
        else:
            print "\nInvalid command"

        print ennemy_attack

        print curr_prompt
        choice = raw_input("> ").lower()


    print "You won!"
    ennemy_dead = True
    print "She crumbles to the ground, now that was a fight !"
battletest()
