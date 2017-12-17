from sys import exit
from random import randint
import ex45_func

class start_money():
    values = [500,600,700,800,900,1000] #the startmaoney is random number out of those

    def giving_start_money(user_money):
        user_money = start_money.values[randint(0,5)]
        # print "You just got ", user_money #tester if the function is returing right
        return user_money

def welcome():
    print ex45_func.print_vipercasino()
    print "Welcome to Viper Casino."

    user_money = start_money().giving_start_money() #get the random money out of the start_money class
    print "You just recieved", user_money, "Euros to play Roulette with us."
    print "Do we need to explain the rules to you? Yes or No?"

    input_explain_rules = raw_input("> ").upper()

    if input_explain_rules == "YES":
        print ex45_func.rules()
        start_game(user_money)
    elif input_explain_rules == "NO":
        start_game(user_money)
    else:
        lost("Sorry, we only let people in which can articulate themselves correctly.", user_money)

def start_game(user_money):

    print ex45_func.rouletteboard() #get the rouletteboard here and print it
    print "Where do you want to bid on? Numbers or groups?"

    while True:
        input_num_or_groups = raw_input("> ").upper()

        if input_num_or_groups == "NUMBERS":
            # print "numbers input correct"
            group_ident = None
            bid_nums = bidding(user_money, group_ident).bid_nums(user_money) #transfer the data to the bidding class

        elif input_num_or_groups == "GROUPS":
            # print "groups input correct"
            group_ident = None
            bid_groups = bidding(user_money, group_ident).bid_groups(user_money) #trasnferring the data to the bidding class
        else:
            print "Please write 'numbers' or 'groups'."


class bidding():

    def __init__(self, user_money, group_ident):
        self.user_money = user_money
        self.group_ident = group_ident

    def bid_nums(self, user_money):
        print "On which number do you want to bid on? Enter 1 - 36."
        input_number = input("> ")

        while True: #check that it can't be zero or higher than 36
            if input_number == 0:
                print "Sorry, you can't bid on the 0."
                play_again(user_money)
            elif input_number > 36  :
                print "Sorry, that number is to high."
                play_again(user_money)
            else:
                break

        print "How much do you want to bid on the number" , input_number, "? You have currently", user_money, "Euros."
        input_money = input("> ")

        if input_money > user_money:
            print "You don't have that much money. You can only spend what you have."
            play_again(user_money)
        else:
            pass

        print "You are going to bid ", input_money, " Euros on the number", input_number
        if user_money >= input_money:
            user_money = user_money - input_money
            print "You have ", user_money, " Euros left."
            group_ident = None
            rouletteshuffle = roulette(user_money, input_number, input_money, group_ident).rouletteshuffle(user_money, input_number, input_money, group_ident)
        else:
            lost("You don't have that much money. So you cannot play. What a pitty.", user_money)


    def bid_groups(self, user_money):
        print "On which group do you want to bid on? Type BLACK, RED, EVEN, ODD, LOW or HIGH"
        input_group = raw_input("> ").upper() #get the name of the group

        if input_group == "BLACK":
            group_ident = "black"
            pass
        elif input_group == "RED":
            group_ident = "red"
            pass
        elif input_group == "EVEN":
            group_ident = "even"
            pass
        elif input_group == "ODD":
            group_ident = "odd"
            pass
        elif input_group == "LOW":
            group_ident = "low"
            pass
        elif input_group == "HIGH":
            group_ident = "high"
            pass
        else:
            lost ("You had an typo.", user_money)


        group_ident = bidding(user_money, group_ident).group_money(user_money, group_ident) #transfer to the group_money metho

    def group_money(self, user_money, group_ident):
        print "How much do you want to bid on the", group_ident, "numbers? You have currently", user_money, "Euros."
        input_money = input("> ")

        if input_money > user_money:
            print "You don't have that much money. You can only spend what you have."
            play_again(user_money)
        else:
            pass

        print "You are going to bid", input_money,"Euros on the", group_ident, "numbers."
        user_money = user_money - input_money #substract the money
        print "You have", user_money, "Euros left."
        input_number = None
        rouletteshuffle_groups = roulette(user_money, input_number, input_money, group_ident).rouletteshuffle_groups(user_money, input_number, input_money, group_ident)

class roulette():

    def __init__(self, user_money, input_number, input_money, group_ident):
        self.user_money = user_money
        self.input_number = input_number
        self.input_money = input_money
        self.group_ident = group_ident

        #print user_money, input_number, input_money #tester for the variables

    def rouletteshuffle(self, user_money, input_number, input_money, group_ident):
        print " "
        print "=== " * 15
        rouletteshuffle = randint(0, 36)
        print "Roulette number is", rouletteshuffle
        print "=== " * 15
        print " "

        if input_number == rouletteshuffle:
            print "Yeah. Maximum win. You will become your invest 36 times back"
            factor = 36
            won_money = win_calc(user_money, factor, input_money).won_money(user_money, factor, input_money) #36 will be the factor the user bidded on
        else:
            lost("Uh, you didn't win. What a pitty.", user_money)

    def rouletteshuffle_groups(self, user_money, input_number, input_money, group_ident):

        print " "
        print "=== " * 15
        rouletteshuffle = randint(0, 36)
        print "Roulette number is:", rouletteshuffle, "- a", ex45_func.dict(rouletteshuffle)[0], ",", ex45_func.dict(rouletteshuffle)[1], "and", ex45_func.dict(rouletteshuffle)[2], "number."
        print "=== " * 15
        print " "

        #the following block is cycling through the list coming from the dict and testing if the user_input matches
        j = 0
        for i in range (0, len(ex45_func.dict(rouletteshuffle))):
            #print ex45_func.dict(rouletteshuffle)[i] #tester for which list element is tested
            if group_ident == ex45_func.dict(rouletteshuffle)[i]:
                print "Hurray. You win the double amount back."
                factor = 2
                won_money = win_calc(user_money, factor, input_money).won_money(user_money, factor, input_money)
            else:
                j = j+1
                if j == 3:
                    lost("Unfortunately you didn't win.", user_money)
                else:
                    pass


class win_calc():
    def __init__(self, user_money, factor, input_money):
        self.user_money = user_money
        self.factor = factor
        self.input_money = input_money

    def won_money(self, user_money, factor, input_money): #factor for the multiplication of the money the user bidded on
        won_money_calced = input_money * factor
        print "In total you won", won_money_calced
        user_money = user_money + won_money_calced
        print "Your balance is now:", user_money

        play_again(user_money)


def lost(reason, user_money):
    print reason, "But you still have", user_money, "Euros left."
    play_again(user_money)

def play_again(user_money):
    print "Want to play another round? Yes or No?"
    input_play_again = raw_input("> ").upper()

    if input_play_again == "YES":
        start_game(user_money)
    elif input_play_again == "NO":
        print "Your final score is", user_money,"Euros."
        print "Thanks for visiting. Hope to see you again soon."
        exit(0)
    else:
        print "I think you miss typed. Try again"
        play_again(user_money)


welcome()
