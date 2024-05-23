def pickanumber():
   while True:
        choice = float(input("Choose a number (S to exit): "))
        if choice is not "s":
            modchoice = choice / 2
            print("Your entered number is: " + str(choice))
            print("Your number divided by 2 is: " + str(modchoice))
        



pickanumber()
