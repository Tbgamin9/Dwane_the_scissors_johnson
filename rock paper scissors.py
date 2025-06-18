
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
    elif answer == "no":
        print("yes")
    elif answer == "cheese":
        print("burger - with fries please")
    elif answer == "yes":
        print("no")
    else:
        print(string5)
