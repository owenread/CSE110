'''
I added some extra questions and secret endings. I also
really enjoyed putting in ending achievements. Hopefully one day I can learn
how to show the user what endings they have achieved. I also added a loop and more paths after
you get the correct answer. 

I really hope you enjoy! I have spent a lot of time and dedication for this program 
and I hope it shows!

Author: Owen Read
'''

# Welcome the player to the game. 
print("You've found yourself on a small path in the middle of a tall forest. \n" \
"You're unsure of why you're there or where you've come from. \n" \
"You must get to safety soon. It is getting dark after all.")

print("")
# Start the choices

# Starting point
direction_choice = input("You hear the sound of water flowing from coming from " \
"below,\n but there seems to be a steep cliff in the way.\n Head towards the water or" \
" continue down the small path? [RIVER]/[PATH] ").lower()

# Main River direction
if direction_choice == "river":
    print("")
    print('You start climbing down to the edge of the cliff. \n' \
    'You see an old brown vine that seems to go all the way to the bottom.')
    print("")
    
    vine_or_climb = input("Trust the vine or try and climb down the side of the cliff? " \
    "[VINE]/[CLIMB] ").lower()
    print("")
    # Vine direction
    if vine_or_climb == "vine":
        print("Oh no! The vine was a sleeping Collossal-Giant's beard! You've made him mad.")

        plea_or_run = input("You've fallen pretty far but you don't seem hurt. \n" \
        "Do you plea for your life or run? [PLEA]/[RUN] ").lower()
        # Plea direction
        if plea_or_run == "plea":
            print("You move onto your knees and begin to plea for your life. \n" \
            "The Giant hears your please and brings you back to safety.")
            print("")
            #Ending "collosal salvation"
            print("Congratulations! You've achieved the 'Collossal-Salvation award'. \n" \
            "Play again to see what other endings you can achieve.")
        # Run direction
        elif plea_or_run == "run":
            print("You start running away as fast as you can. \n " \
            "You only get about 30 feet away from the Giant before you make it to the river. \n" \
            "You realize you have nowhere else to run.")
            print("")

            swim_or_build = input("In a panic, you realize there might be enough vines and fallen trees to build a raft. \n" \
            "Do you risk trying to swim in the river or do you try and build a raft?"
            " [SWIM]/[BUILD] ").lower()
            print("")
            # Swim choice
            if swim_or_build == "swim":
                print("You jump in the water and try to swim. You quickly realize the water is too strong, \n" \
                "You quickly run out of strength. Instantly, you get pulled under water.\n" \
                "Between the blinding moments of the crashing water, \n" \
                "you see a school of turtles holding you close to the water's surface. \n" \
                "The school of turtles bring you safely to beach where a camp has been set up. \n" \
                "The campers spot you and run to the shore to help you.")
                print("")
                #Ending "future ninja-turtles?"
                print("Congratulations! You've achieved the 'future ninja-turtles?' ending! \n" \
                "Play again to see what other endings you can achieve.")
            # Build choice
            elif swim_or_build == "build":
                print("You quickly fashion the vines and fallen trees into a Black Pearl on a budget." \
                "You sail off down the river like a cousin of Jack Sparrow!")
            # Else fainted ending
            else:
                print("Exhausted from running, you decided to lay down and take a nap.")
                print("")
                print("Congratulations! You have achieved the 'sleepy head' ending\n" \
                "Play again to see what other endings you can achieve.")
        
        # Pet ending
        else:
            print("That response doesn't make sense. The Collossal-Giant thinks you're too small to eat. \n" \
            "He brings you into his cave and makes you his pet.")
            print("")
            print(" Congrats! You have achieved the 'Pet' ending. \n" \
            "Play again to see what other endings you can achieve.")
    # Climb direction
    elif vine_or_climb == "climb":
        print("You decide to climb down the side of the cliff instead of risking the old vines.\n" \
        "The cliff seems to be moving and you lose your footing.\n" \
        "As you're falling you land on the back of a quickly moving griffin.\n" \
        "The griffin seems to be flying in an army of griffins fighting and army of pegasus mid-air!")
        print("")

        griffin_or_pegasus = input("Do you choose to stay on the griffin's back or jump onto a pegasus?" \
        "[GRIFFIN]/[PEGASUS] ").lower()
        print("")
        # Griffin choice
        if griffin_or_pegasus == "griffin":
            print("The griffin you're riding on seems to be hurt. It dives out of the battle and returns to it's nest.\n" \
            "The griffins adopt you as one of their babies thinking you simply haven't grown your wings yet.")
            print("")
            print("Congratulations! You have achieved the 'griffin chick or egg?' ending!\n" \
            "Play again to see what other endings you can achieve.")
        # Pegasus choice
        elif griffin_or_pegasus == "pegasus":
            print("In a moment of courage and luck, you slide off the back of the griffin and fall on the back of a pegasus.\n" \
            "The fall knocked you out. You wake up and look around. You see a tall muscular man\n" \
            "with a shiny emblem of lightning on his belt. You realize you're now a guest of Hercules.")
            print("")
            print("Congratulations! You have achieved the 'you can go the distance!' ending.\n" \
            "Play again to see what other endings you can achieve.")

        else:
            print("The lack of decision or clear judgment frustrates the griffin and flings you off.\n" \
            "...\n Your grandpa closes the story book and tells you it's time for bed and kisses your forhead.")
            print("")
            print("Congratulations! You've found the 'goodnight grandpa' ending.\n" \
            "Play again to see what other endings you can achieve.")
    else:
        print("You wake up in bed and realize that everything was just a dream.\n" \
        "Although, where did this leaf come from?")
        print("")
        print("Congratulations! You have achieved the 'it was all a dream?' ending.\n" \
        "Play again to see what other endings you can achieve.")
# Main Path direction
elif direction_choice == "path":
    print("You decide to walk down the small narrow path.")
    print("")
    print("As you walk, the path disappears. You continue to walk where you think the path is going. \n" \
    "You've come to a clearing, and you see a giant sleeing ogre.")

    wake_ogre_or_let_sleep = input("Do you wake the sleeping Orge up or let the orge sleep?"
    " [WAKE]/[LEAVE] ").lower()
    print("")
    
    # going to try out a loop here:
    if wake_ogre_or_let_sleep == "wake":
        print('The Orge snarls and snares. Angry, the orge stands up and towers over you. \n' \
        'The orge says to you, "What a small creature.' \
        ' I will spare you life if you answer this riddle."')
        print("")
        
        riddle_answers = ["candle", "a candle" ]
        
        # I do understand that all choices need to be shown in caps. However, because this is a riddle, 
        # I don't want to give away the answer so no choice is displayed in caps. Hope you understand!
        while True:
            riddle_response = input("I'm tall when I'm young and short when I'm old> What am I?: ").strip().lower()

            if riddle_response in riddle_answers:
                print('The ogre laughs and says, "Congratulations little one. I have got a little prize for you.\n' \
                'Here, it is right over there under that cover. Enjoy little creature.')
                print("")

                # Choice take the gift or go home
                take_or_leave = input("Would you like to take the gift or leave it for someone else? [TAKE]/[LEAVE] ").lower()
                print("")

                if take_or_leave == "take":
                    print("You walk over to the gift and pull off the cover. It's... it's a wardrobe?\n" \
                    "You decide to open the wardrobe. As you peer into the wardrobe you realize that there's something behind the clothes.\n" \
                    "You brush the clothes to the side and see that the back of the wardrobe has an entire world inside!")
                    print("")
                    print("Congrats! You have achieve the 'Lion the Witch and the Wardrobe' ending!\n" \
                    "Play again to see what other endings you can achieve.")
                
                elif take_or_leave == "leave":
                    print("You give your gratitude to the orge and walk away. As you're walking way, you feel like something is near you.\n" \
                    "You look around and realize a lion has been walking by your side. You continue your journey with the lion by your side.")
                    print("")
                    print("Congratulations! You have achieved the 'Aslan never leaves you' ending!\n" \
                    "Play again to see what other endings you can achieve.")
                # Haha Double pun ending
                else:
                    print(f"The ogre scratches his head in confusion of your choice '{take_or_leave}'.\n" \
                          "You both laugh and you decide to help the ogre challange travelers with new riddles.")
                    print("")
                    print("Congrats! You have achieved 'the riddler on the ogre' ending!\n" \
                    "Play again to see what other endings you can achieve.")
                break

            else:
                print("The ogre grumbles, that's not correct. Try again...")
    # Ogre leave choice
    elif wake_ogre_or_let_sleep == "leave":
        print("You've decided to let the ogre sleep and quietly sneak past to the other side of the clearing.\n" \
        "When you reach the tree-line, you see a small purple ball. You take the ball and continue walking.\n" \
        "As you search for anything that resembles a path, you see a small bear.")   
        print("")

        throw_or_give = input("You look down at the purple ball. Do you throw the ball near the bear or\n" \
        "do you attempt to get closer and give the ball to the bear? [THROW]/[GIVE] ").lower()
        print("")
        # Throw choice
        if throw_or_give == "throw":
            print("You steady yourself, wind up, and throw the ball towards the bear.\n" \
            "a shining light appears from the ball. You've caight a wild teddy bear!")
            print("")
            print("Congratulations! You have achieved the 'gotta catch 'em all' ending!\n" \
            "Play again to see what other endings you can achieve.")
        # Give choice
        elif throw_or_give == "give":
            print("You crouch down and get closer to the bear. The bear quickly turns around!\n" \
            "You startle and the purple ball flies out of your hand!\n" \
            "A shining light appears and a Collossal-Giant comes out of the purple ball!\n" \
            "The bear is owned by the local champion! Collossal-Giant and bear go blow for blow in an epic battle!\n" \
            "The battle ends and you alongside Collossal-Giant are victorious and are awarded the title of champion.")
            print("")
            print("Congratulations! You have achieved the 'champion dueler' ending!" \
            "Play again to see what other endings you can achieve.")
        
        else:
            print(f"Unsure of what {throw_or_give} means, you hesitantly back away.\n" \
            "You run off until you can find a road. This experiance must have been a hallucination.\n" \
            "This purple ball is still a cool souvenir!")
            print("")
            print("Congratulations! You have achieved the 'cliff hanger for a sequal' ending!\n" \
            "Play again to see what other endings you can achieve.")
    # Practicing some string formatting
    else:
        print(f"You're not thinking straight! {wake_ogre_or_let_sleep.capitalize()}, doesn't make any sense!\n"
        "Try again.")        

# Main else direction. Clear instruction as this is probably the first mistake for an input. 
else:
    print("You must still be gaining conciousness.\n" \
    "Your only two options for survival are [RIVER]/[PATH].\n" \
    "Please try again.")    





