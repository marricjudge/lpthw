# import json
#
# some_date = raw_input("> ")
# date = raw_input("> ")
#
# your_dictionary = {some_date : date}
# f = open('test.txt', 'w+')
# f.write(json.dumps(your_dictionary.update({"some_date": "date"})))
#
#
# f = open('test.txt', 'r')
# your_dictionary = json.loads(f.read())
# print your_dictionary

#
# user_money = input("> ")
# name = raw_input("> ")
#
# highscore = {user_money : "name"}
# highscorefile = open('test.txt', 'w')
# highscorefile.highscore.update({user_money: "name"})

#highscore = {400 : "Marius"}

import pickle

# load the previous score if it exists
try:
    with open('test.txt', 'rb') as file:
        score = pickle.load(file)
except:
    score = 0

print "High score: %d" % score

# your game code goes here
# let's say the user scores a new high-score of 10
score = 20;

# save the score
with open('test.txt', 'wb') as file:
    pickle.dump(score, file)
