myInput=raw_input("What\'s your name?\n")

while myInput.isdigit():
    myInput=raw_input("Your name cannot be a number\n")

print  "Hello %s!" %myInput
