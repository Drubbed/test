import sys 
weapon_power=1
level=1
health=weapon_power*100
name=input("Hello, who are you?")
Words=input("Hello, "+name+" I am Wing Su, I am comunicating through you through a 	hologram (press enter)")
question=input("I have a favor for you will you help me?(yes or no)")
if question=="yes":
    Weapon=input("Alright, now which weapon will you choose? (bow/axe/sword)")
else:
    quit("okay come back if you change your mind :)")
while not Words==quit:
    Words=input("your current weapon is "+str(Weapon)+" here are the commands you can use: train, fight (to fight the boss which gives you a new substance for the "+Weapon+" ), stats, or quit")
    if Words=="quit":
        print("your stats for your weapon power is "+str(weapon_power)+" your weapon is "+Weapon+" your level to fight "+str(level)+", your health in total is "+str(health)+"press enter")
        print("bye I hope you have a great life :D")
        break
    elif Words=="train":
        weapon_power=weapon_power+1
    elif Words=="stats":
        stats=input("your stats for your weapon power is " +str(weapon_power)+ " your weapon is " +Weapon+ " your level is " +str(level)+ ", your health in total is " +str(health)+ " press enter")
        Words=input(name+", here are the commands you can use: train, fight (to fight the boss which gives you a new substance for the "+Weapon+"), stats, or quit")
    elif Words=="Fight":
        fight=input("This will be a later function (press enter)")
