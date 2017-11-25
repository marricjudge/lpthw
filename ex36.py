from sys import exit

def start():
    print "You are walking in the forest and a little monster jumpes out of the woods."
    print "Monster: 'I won't let you pass here.' ", "Unless you're paying me 100 Euros."
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
            #function Here
            print "run successfull"
        elif pay_run_fight_input == "FIGHT":
            #function here
            print "fight sucessfull"
        elif i <= 4:
            print "Please try again"
        else:
            print "Sorry, so you don't want to play."

def pay():
    print "Pay? Are you rich? Yes or No?"
    are_you_rich_input = raw_input("> ").upper()
    print "After entering the input"
    print are_you_rich_input

    if are_you_rich_input == "YES" or "1" or "Y":
        print "Yes? Well then you can afford it."
        success()
    elif are_you_rich_input == "NO" or "0" or "N":
        dead("No? Too bad. It's human for dinner")

def run():
    print "Are you trained enough to run away? Yes or No?"

    trained_input = raw_input("> ").upper()

    if trained_input == "YES" or "1" or "Y":
        print "Better get your running shoes on then."
        success()
    elif trained_input == "NO" or "0" or "N":
        dead("Too bad. It's human for dinner")

def dead(why):
    print why
    print "Thanks for playing. Wanna try again? Yes or No?"
    play_again_input = raw_input("> ")
    if play_again_input == "YES" or "1" or "Y":
        print "Ok, let's go"
        print " "
        start()
    elif play_again_input == "NO" or "0" or "N":
        exit(0)

def success():
    print "Yeah. You made it. Congraz."
    print "Thanks for playing."

start()
