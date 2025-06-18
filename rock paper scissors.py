
print("rock paper scissors game thingy")
print("type 'rock' 'paper' or 'scissors'")
string1 = "rock"
string2 = "paper"
string3 = "scissors"
string4 = "your turn: "
string5 = "that is invalid, sorry!"
flag = True
while flag:
    answer = input (string4).lower()
    if answer == "paper":
        print("scissors - better luck next time!")
    elif answer == "scissors":
        print("rock - better luck next time!")
    elif answer == "rock":
        print("paper - better luck next time!")
    elif answer == "gun":
        print("I surrender!")
        flag = False
        print("you win! (but at what cost?)")
    elif answer == "no":
        print("yes")
    elif answer == "cheese":
        print("burger - with fries please")
    elif answer == "yes":
        print("no")
    elif answer == "apple":
        print("orange")
    elif answer == "orange":
        print("apple")
    elif answer == "alphabet":
        print("soup")

    elif answer == "a":
        print("b")
    elif answer == "b":
        print("c")
    elif answer == "c":
        print("d")
    elif answer == "d":
        print("e")
    elif answer == "e":
        print("f")
    elif answer == "f":
        print("g")
    elif answer == "g":
        print("h")
    elif answer == "h":
        print("i")
    elif answer == "i":
        print("j")
    elif answer == "j":
        print("k")
    elif answer == "k":
        print("l")
    elif answer == "l":
        print("m")
    elif answer == "m":
        print("n")
    elif answer == "n":
        print("o")
    elif answer == "o":
        print("p")
    elif answer == "p":
        print("q")
    elif answer == "q":
        print("r")
    elif answer == "r":
        print("s")
    elif answer == "s":
        print("t")
    elif answer == "t":
        print("u")
    elif answer == "u":
        print("v")
    elif answer == "v":
        print("w")
    elif answer == "w":
        print("x")
    elif answer == "x":
        print("y")
    elif answer == "y":
        print("z")
    elif answer == "z":
        print("https://en.wikipedia.org/wiki/Z")
    else:
        print(string5)
