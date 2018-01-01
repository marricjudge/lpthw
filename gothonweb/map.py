class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
start_scene = Scene("Lonely forest walk", "start_scene",
"""
You are walking in the forest and a little monster jumpes out of the woods.
Monster: 'I won't let you pass here. Unless you're paying me 100 Euros.'
What do you do? Do you either PAY, RUN or FIGHT? Type one of the options here.
""")

pay = Scene("Paying money to the monster", "pay",
"""
So you really want to pay? Can you afford this amount of money?
Yes or No?
""")

pay_yes = Scene("Yes, you pay", "pay_yes",
"""
Well you pay the monster 100 Euros but it wants more than that.
'At least 1000 Euros'. Are you still going to pay? Or run or fight?
""")

run = Scene("Run", "run",
"""
Are you trained enough to run away? Yes or No?
""")

fight = Scene("Fight against the monster", "fight",
"""
Are you trained enough to run away. Yes or No?
""")

smart = Scene("When you're not trained enough", "smart",
"""
Well, if you're not strong then at least smart? Yes or No?
""")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
Congratulation. You made it against the monster
""")

generic_death = Scene("Death...", "death", "You died.")

# Define the action commands available in each scene
run.add_paths({
    'yes': the_end_winner,
    'yes': the_end_winner,
    'no' : generic_death,
    'No' : generic_death
})

pay_yes.add_paths({
    'pay': the_end_winner,
    'yes': the_end_winner,
    'run': run,
    'fight' : fight
})

fight.add_paths({
    'Yes' : the_end_winner,
    'yes' : the_end_winner,
    'no'  : smart,
    'No'  : smart
})

smart.add_paths({
    'Yes' : the_end_winner,
    'yes' : the_end_winner,
    'no'  : generic_death,
    'No'  : generic_death

})

pay.add_paths({
    'yes': pay_yes,
    'Yes': pay_yes,
    'no': generic_death,
    'No': generic_death

})

start_scene.add_paths({
    'run':run,
    'pay':pay,
    'fight': fight
})

SCENES = {
    start_scene.urlname : start_scene,
    pay.urlname : pay,
    pay_yes.urlname : pay_yes,
    run.urlname : run,
    the_end_winner.urlname : the_end_winner,
    generic_death.urlname : generic_death,
    fight.urlname : fight,
    smart.urlname : smart,
}
START = start_scene
