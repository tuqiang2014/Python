print("You enter a dark room with two doors. Do you go though door #1 or door #2?")

door = input("> ")

if door == "1":
    print("there's a giant bear here esting a cheese cake. What do you do ?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    
    if bear =="1":
        print("The bear eats your face off. Good job!")
    elif bear =="2":
        print("The bear eats your legs off. Good job!")
    else:
        print("well, doing %s is probably better. Bear runs awsy." % bear)

elif door == "2":
    print("You stare into the endless abyss at Ctulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insantity = input("> ")

    if insantity == "1" or insantity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insantity rots your eye into a pool of muck. Good job!")

else:
    print("You stumble around and fall on a kinfe and die. Good job!")
