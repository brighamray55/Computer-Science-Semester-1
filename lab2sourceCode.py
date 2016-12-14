# start of the game
print(" You will play as either the king of the chipmunks or squirrels ")
print(" with Trump as king of the squirrels and Hillary as queen of the ")
print(" chipmunks.")
print(" You are battling to have nuts for the winter. Whoever")
print(" has the most nuts wins!!!")
# this is the first user choice between hillary and trump
user_choice = input(" Who will you play as: Trump or Hillary: ")
if user_choice == "Trump":
    print(" interesting choice, may the squirrels make the forest")
    print(" great again")
    print(" To begin the battle, we must gather an ")
    print(" army. Choose your arsenal: ")
# start of trumps 2nd order
    first_trump_order = input(" Swordsmen, Archers, or nukes: ")

    if first_trump_order == "Swordsmen":
        print(" Hillary's army has weak shields. You progress")
        print(" to their Redwood kingdom.")
        print(" You can either CHOP DOWN TREE WITH SWORDS or RAID THE TREE")
        second_trump_order = input(" which do you choose: ")
# start of trumps 1st order
        if second_trump_order == "CHOP DOWN TREE WITH SWORDS":
            print(" Trump's army cut the wrong side. The tree")
            print(" Falls on him and his army.  YOU LOSE!!!!!")
        elif second_trump_order == "RAID THE TREE":
            print(" Hillary hid her nuts like she hid her emails")
            print(" You found them better than the FBI could.")
            print(" YOU WIN!!!!!")
        else:
            print(" That's not an option. Idiot.")
    elif first_trump_order == "Archers":
        print(" Hillary's army deflected the arrows. You are pushed back.")
        print(" Luckily Trump has a few tricks up his sleeve.")
        print(" He has FLAMING MALATOVS or THE BEST ADVISORS.")
        second_trump_order = (" Which one do you choose?")
        if second_trump_order == "FLAMING MALATOVS":
            print(" You burned down Hillary's tree, smart choice.")
            print(" Turns out trees are made of wood. YOU WIN!!!!")
        elif second_trump_order == "THE BEST ADVISORS":
            print(" Unfortunately, those advisors went to Trump")
            print(" University. They say more arrows, it doesn't")
            print(" work, you LOSE!")
        else:
            print(" That's not an option. Idiot.")
    elif first_trump_order == "nukes":
        print(" God help us all... but you manange to survive.")
        print(" The nuclear war that was set into place was great")
        print(" and destructive destroying all the nuts in the world")
        print(" You see Hillary in the distance and have a sword or")
        print(" an arrow next to you")

        second_trump_order = input(" which weapon will you use ")
        if second_trump_order == "sword":
            print(" Hillary had unknown ninja skills")
            print(" you were defeated")
        elif second_trump_order == "arrow":
            print(" Hillary was just as dumb and picked up one too.")
            print(" It was an epic battle, but Hillary had a seizure.")
            print(" You coup de gras and gain 20 million nuts.")
            print(" YOU WIN!!!!!")
        else:
            print(" That's not an option. Idiot.")
# if the user chooses hilary
elif user_choice == "Hillary":
    print(" the chipmunks are stronger together!")
    print(" To begin the battle, we must gather an ")
    print(" army. Choose your arsenal: ")
# start of first hillary order
    first_hillary_order = input(" Swordsmen, Archers, or nukes:")

    if first_hillary_order == "Swordsmen":
        print(" Trump's army has weak shields. You progress to their Redwood")
        print(" kingdom.")
        print(" You can either CHOP DOWN TREE WITH SWORDS or RAID THE TREE")
        second_hillary_order = input(" which do you choose?")
# start of seond hillary order
        if second_hillary_order == "CHOP DOWN TREE WITH SWORDS":
            print(" Hillary's army cut the wrong side. The tree")
            print(" Falls on him and his army.  YOU LOSE!!!!!")
        elif second_hillary_order == " RAID THE TREE":
            print(" Trump hid his nuts like he hid his illegal immigrants")
            print(" Looks like you caught him and his nuts.")
            print(" YOU WIN!!!!!")
        else:
            print(" That's not an option. Idiot.")
    elif first_hillary_order == "Archers":
        print(" Trump's army deflected the arrows. You are pushed back.")
        print(" Luckily Hillary has a few tricks up her sleeve.")
        print(" She has FLAMING MALATOVS or THE BEST ADVISORS.")
        second_hillary_order = (" Which one do you choose?")
        if second_hillary_order == "FLAMING MALATOVS":
            print(" you burned down Trump's tree, smart choice.")
            print(" Turns out trees are made of wood. YOU WIN!!!!")
        elif second_hillary_order == "THE BEST ADVISORS":
            print(" Unfortunately, those advisors went to Trump")
            print(" University. They say more arrows, it doesn't")
            print(" work, you LOSE!")
        else:
            print(" That's not an option. Idiot.")
    elif first_hillary_order == "nukes":
        print(" God help us all... but you manange to survive.")
        print(" The nuclear war that was set into place was great")
        print(" and destructive destroying all the nuts in the world")
        print(" You see Trump in the distance and have a sword or")
        print(" an arrow next to you")

        second_hillary_order = input(" which weapon will you use: ")
        if second_hillary_order == "sword":
            print(" Trump had unknown ninja skills")
            print(" You were defeated")
        elif second_hillary_order == "arrow":
            print(" Trump was just as dumb and picked up one too.")
            print(" It was an epic battle, but Trump had tiny hands.")
            print(" You coup de gras and gain 20 million nuts.")
            print(" YOU WIN!!!!!")
        else:
            print(" That's not an option. Idiot.")
else:
    print(" third parties don't exist in this forest!")
    print(" You're tried for treason and you die.")
