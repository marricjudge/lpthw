from sys import exit

def start():
    print "--------------------------"
    print " "
    print "You are walking in the forest and a little monster jumpes out of the woods."
    print "Monster: 'I won't let you pass here. Unless you're paying me 100 Euros.' "
    print "--------------------------- "
    print "What do you do? Do you either PAY, RUN or FIGHT?"
    print "Type one of the options here."

    for i in range (1, 6):
        pay_run_fight_input = raw_input("> ").upper()
        #print pay_run_fight_input #testprint for input
        if pay_run_fight_input == "PAY":
            pay()
            break
        elif pay_run_fight_input == "RUN":
            run()
            break
        elif pay_run_fight_input == "FIGHT":
            fight()
            break
        elif i <= 4:
            print "Please try again"
        else:
            print "Sorry, so you don't want to play."

def pay():
    print "Pay? Are you rich? Yes or No?"

    are_you_rich_input = raw_input("> ").upper()
    #print "After entering the input"
    #print are_you_rich_input
    if are_you_rich_input == "YES":
        success("Yes? Well, then you can afford it.")
    elif are_you_rich_input == "NO":
        dead("No? Too bad. It's human for dinner")
    else:
        dead("The monster loves to eat humans with typing mistakes!")


def run():
    print "Are you trained enough to run away? Yes or No?"

    trained_input = raw_input("> ").upper()

    if trained_input == "YES":
        success("Better get your running shoes on then.")
    elif trained_input == "NO":
        dead("Too bad. The monster catched you on your run")
    else:
        dead("Too slow. The monster loves to eat humans with typing mistakes!")


def fight():
    print "Fight? Ok. Are you strong?"
    strong_input = raw_input("> ").upper()

    if strong_input == "YES":
        dead ("While warming up your muscles the monster hit you to death.")
    elif strong_input == "NO":
        smart()
    else:
        dead("While inserting the wrong input the monster hit you to death.")

def smart():
    print "Well, if you're not strong then at least smart?"
    smart_input = raw_input("> ").upper()

    if smart_input == "YES":
        success("You tricked the monster.")
    elif smart_input == "NO":
        dead ("Either strong nor smart - and no luck today")

def dead(why):
    print why
    print " "
    print "-------------------"
    print " "
    print "Thanks for playing. Wanna try again? Yes or No?"
    play_again_input = raw_input("> ").upper()
    if play_again_input == "YES":
        print "Ok, let's go"
        print " "
        start()
    else:
        print "Good bye"
        exit(0)

def success(why):
    print why
    print " "
    print "----------------------------"
    print " "
    print "Yeah. You made it. Congraz."
    print "Thanks for playing."
    exit(0)

start()
