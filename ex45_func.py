def dict(search):
    dict = { 0 : ["number you can't win with","because it reserved","a special"],
             1 : ["red", "odd", "low"],
             2 : ["black", "even", "low"],
             3 : ["red", "odd", "low"],
             4 : ["black", "even", "low"],
             5 : ["red", "odd", "low"],
             6 : ["black", "even", "low"],
             7 : ["red", "odd", "low"],
             8 : ["black", "even", "low"],
             9 : ["red", "odd", "low"],
            10 : ["black", "even", "low"],
            11 : ["black", "odd", "low"],
            12 : ["red", "even", "low"],
            13 : ["black", "odd", "low"],
            14 : ["red", "even", "low"],
            15 : ["black", "odd", "low"],
            16 : ["red", "even", "low"],
            17 : ["black", "odd", "low"],
            18 : ["red", "even", "low"],
            19 : ["red", "odd", "high"],
            20 : ["black", "even", "high"],
            21 : ["red", "odd", "high"],
            22 : ["black", "even", "high"],
            23 : ["red", "odd", "high"],
            24 : ["black", "even", "high"],
            25 : ["red", "odd", "high"],
            26 : ["black", "even", "high"],
            27 : ["red", "odd", "high"],
            28 : ["black", "even", "high"],
            29 : ["black", "odd", "high"],
            30 : ["red", "even", "high"],
            31 : ["black", "odd", "high"],
            32 : ["red", "even", "high"],
            33 : ["black", "odd", "high"],
            34 : ["red", "even", "high"],
            35 : ["black", "odd", "high"],
            36 : ["red", "even", "high"]
             }
    return dict[search]

def rouletteboard():
    print """
    #     N U M B E R S     #    #      G R O U P S      #
    |-----------------------|    |-----------------------|
    |           0           |    | B L A C K |   R E D   |
    |-----------------------|    |-----------------------|
    |   1   |#  2  #|   3   |    |  E V E N  |   O D D   |
    |-----------------------|    |-----------------------|
    |#  4  #|   5   |#  6  #|    |   L O W   |  H I G H  |
    |-----------------------|    |-----------------------|
    |   7   |#  8  #|   9   |
    |-----------------------|     # numbers are black
    |# 1 0 #|# 1 1 #|  1 2  |      1 - 18 = low
    |-----------------------|     19 - 36 = high
    |# 1 3 #|  1 4  |# 1 5 #|
    |-----------------------|
    |  1 6  |# 1 7 #|  1 8  |
    |-----------------------|
    |  1 9  |# 2 0 #|  2 1  |
    |-----------------------|
    |# 2 2 #|  2 3  |# 2 4 #|
    |-----------------------|
    |  2 5  |# 2 6 #|  2 7  |
    |-----------------------|
    |# 2 8 #|# 2 9 #|  3 0  |
    |-----------------------|
    |# 3 1 #|  3 2  |# 3 3 #|
    |-----------------------|
    |  3 4  |# 3 5 #|  3 6  |
    |-----------------------|
    """
    return(" ")



def print_vipercasino():
    print """
     __     __  ______  _______   ________  _______          ______    ______    ______   ______  __    __   ______
    |  \   |  \|      \|       \ |        \|       \        /      \  /      \  /      \ |      \|  \  |  \ /
    | $$   | $$ \$$$$$$| $$$$$$$\| $$$$$$$$| $$$$$$$\      |  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$| $$\ | $$|  $$$$$$
    | $$   | $$  | $$  | $$__/ $$| $$__    | $$__| $$      | $$   \$$| $$__| $$| $$___\$$  | $$  | $$$\| $$| $$  | $$
     \$$\ /  $$  | $$  | $$    $$| $$  \   | $$    $$      | $$      | $$    $$ \$$    \   | $$  | $$$$\ $$| $$  | $$
      \$$\  $$   | $$  | $$$$$$$ | $$$$$   | $$$$$$$\      | $$   __ | $$$$$$$$ _\$$$$$$\  | $$  | $$\$$ $$| $$  | $$
       \$$ $$   _| $$_ | $$      | $$_____ | $$  | $$      | $$__/  \| $$  | $$|  \__| $$ _| $$_ | $$ \$$$$| $$__/ $$
        \$$$   |   $$ \| $$      | $$     \| $$  | $$       \$$    $$| $$  | $$ \$$    $$|   $$ \| $$  \$$$ \$$    $$
         \$     \$$$$$$ \$$       \$$$$$$$$ \$$   \$$        \$$$$$$  \$$   \$$  \$$$$$$  \$$$$$$ \$$   \$$  \$$$$$$

    """
    return(" ")



def rules():
    print """
    T H E   R U L E S:

    Playing roulette the french way.
    One random number from the range of 0 to 36 is shuffled
    and you have to bid on them before.

    Depending on your stake, the number or group shuffeld you win different amounts of money back.

    Black numbers are marked with a # hash #
    Red numbers are unmarked
    Even numbers are all numbers divided by 2 with no remainder (except 0).
    Odd numbers are all other numbers
    Low numbers are between 1 and 18
    High numbers are between 19 and 36

    You cannot bet on the number 0. When the 0 appears all money goes into the bank.

    If you correctly bid on a black, red, even, odd, low or high number
    you recieve your stake doubled back.

    If you bid successfully on a single number you recieve your stake 36x times back.

    Good luck.

    Programmed with Python 2.7 by Marius Richter
    December 2017

    Press ENTER to start the game. To cancel press CTRL + C.
    """
    raw_input(">")

    return(" ")
