#displays message to the user 
print ("Welcome to Open Water Adventure")
print ("You wake up on a small shipping boat without any recollection of how you got there.")
print ("There are 2 others on the boat with you in addition to the captain at the steer.")
print ("You look around your quarters and see a large folded sheet of paper on the nightstand that says read me.") 
print ("You pick it up and find that it is a map of a deserted island with 3 large X's marked on it.") 
print ("You are advised that you will be needing to depart the ship upon landfall and that the map is your only ticket off the island, but only if you are successful at finding the treasure.")
print ("You arrive on shore and see a beach full of huts to your right and a trail that leads to a forest on the left?")
print ("Which way do you proceed left or right?") 

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left.")
    print("Proceed to the forest.")
    print("The forest is overrun with vegetation. You cannot proceed through the forest without tools to assist you.")
    print("You back out of the forest and make your way to the huts.")
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose right.")
    print("Proceed towards the huts.")
    #displays message to the user 
print ("You decide to explore the huts to see if there is any food, drink, supplies or tools you could gather.")
print ("Upon searching the second hut you find the following:")

#displayed to the user using a for loop with list 
items = ['axe', 'coconuts', 'rope', 'key', 'duffel bag']
for item in items:
    print (item)
    
print ("You load the axe, coconuts, rope, key and map that you've brought with you all into the duffel bag.")
print ("You need to determine how many coconuts you want to take with you")
print ("You can't decide, so this will be done at random for you")
print("You've collected this many coconuts:")
#generates random number for item selection
import random
num = random.randint(2, 6)
print(num)
print ("and have packed them in to your duffel bag")
print ("You check the remaining huts and find it's been ransacked.")
print ("You proceed back to the original position you were on the beach and retrieve your map to examine it further.")
print ("The map says the first X says to move towards the forest, so you continue on that route.")
print ("The path becomes obstructed by overgrown tree roots, thorny bushes and poison ivy plants.")
print ("You retrieve the axe from your bag and cut down the vegetation blocking your route.")
print ("You've come to a fork on the path in the forest.")
print ("One goes left towards the mountain side and the other goes right towards an open field of what looks like a farm of fresh fruits and vegetables.")
print ("You refer back to your map and see the X lays near the mountainside.") 
print ("You feel hungry but you know you only have a limited amount of daylight hours remaining.")
print ("Do you risk going right towards the farm for fresh fruits and vegetables or do you go left and carry on with your coconuts that provide both food and liquid and move towards the mountainside? ")
print ("Which option do you prefer, left or right?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left")
    print ("You decide to just carry on with your coconuts and proceed towards the mountain.") 
    
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose right.")
    print("Proceed towards the farm.")
    print("You spend a few hours harvesting and eating all the fruits and vegetables.")
    print("Let's see what you harvested:")

    harvest = [["apples", "bananas", "papayas", "oranges"],
        ["cucubmer", "tomato", "carrots", "zucchini"]]

    for collection in harvest:
        for food in collection:
            print(food)
        
    print("You over ate, you decide to take a nap on the ground, under a tree nearby.")
    print("After waking from your nap, you hear growling nosies in the distance, realizing it is now time to make a run for it.")
    print("You decide to look for somewhere to hide in the mountain.")

else: 
    #displays output message to the user 
    print("Invalid selection. Please enter left or right")
    
#displays output message to the user 
print ("As you get closer to the mountain, you notice there is an opening to a dark cave of some sort.")
print ("You make your way towards that cave with the thought that when nightfall comes you will not only have shelter but a relatively safe place to stay from the preying eyes of vicious animals.")
print ("As you approach the dark cave you see 2 tunnels, one on the right and one on the left.")
print ("Which tunnel do you take?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left.")
    print("Proceed to the tunnel on the left.")
    print("The tunnel goes on and on without any outlet, it's been over an hour now.")
    print("You begin to think you made the wrong decision and retrace your steps back to the beginning.")
    print("Finally, you've reached the starting point.")
    print("You proceed towards the tunnel on the right.")
        
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose to take the tunnel to the right.")
else: 
    #displays output message to the user 
    print("Invalid selection. Please enter left or right.")

#displays output message to the user    
print ("As you walk deeper into the tunnel you see two more tunnels down the way.")
print ("Again, there is one tunnel to the left and one tunnel to the right.")
print ("The tunnel to the right is dimly lit, showing very little light shining through, while the tunnel to the left is completely dark.")
print ("Which way do you proceed?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
#displays output message to the user  
    print("You chose left.")
    print("Proceed to the dark tunnel.")
    print("As you go deeper into the tunnel, you realize it really is dark in here.")
    print("You're thinkging you really wish you had a flashlight right about now.")
    print("You hear some rocks shuffling on the ground behind you, but can't see anything.")
    print("The shuffling gets louder and closer.")
    print("Oh no! You turn back and it's a huge python!! He opens his large mouth and devours you!")
    print("You are now dead! Sorry no treasure for you! Game over!")
    print("Would you like to play the game again?")

elif(directionChoice == "right"):
    print("You chose right")
    #displays output message to the user 
    print ("You begin making your way to the tunnel on the right.")
    print("Proceed towards the dimly lit tunnel.")
    print ("As you walk further into the tunnel you find yourself approaching an even larger cave.") 
    print ("You are now in the larger cave and find yourself perched upon a cliff next to a waterfall.")
    print ("You retrieve the rope from your bag, find a rock to secure it to and rappel down the cliff.")
    print ("You reach the bottom of the cliff and you see a door under the waterfall.")
    print ("You walk towards that door and see a keyhole.")
    print ("You retrieve the key from your duffel bag then insert the key into the keyhole.")
    print ("The door is very heavy but you manage to open it.")
    print ("Beyond the door you find a treasure box.") 
    print ("The same key you used to open the door opens the treasure box.")
    print ("Inside the treasure box you find some crown jewels, gold coins, and aleft satellite phone.") 
    print ("Congratulations! You've found the treasure!")
    print ("You turn on the satellite phone and call the only number stored in it.") 
    print ("The call is placed to an operator of a remote helicopter company not too far from the island.") 
    print ("This is your ticket home but you must forfeit half of the treasure to the company as payment for getting you off the island.")
    print ("Would you like to play the game again?")

else:
    #displays output message to the user  
    print("Invalid selection. Please enter left or right")

#Prompt user for a choice 
answerChoice = input(" yes > no (presss q to quit): ")   

while not (answerChoice == "yes"):
    #displays output message to the user 
    print("Goodbye! Thanks for playing.")  
    answerChoice = input("Play again or press (q to quit)")
#The game ends here, but I do not know how to make the entire game loop here so I've just added the code again after this point
else:   
    print ("Welcome to Open Water Adventure")
print ("You wake up on a small shipping boat without any recollection of how you got there.")
print ("There are 2 others on the boat with you in addition to the captain at the steer.")
print ("You look around your quarters and see a large folded sheet of paper on the nightstand that says read me.") 
print ("You pick it up and find that it is a map of a deserted island with 3 large X's marked on it.") 
print ("You are advised that you will be needing to depart the ship upon landfall and that the map is your only ticket off the island, but only if you are successful at finding the treasure.")
print ("You arrive on shore and see a beach full of huts to your right and a trail that leads to a forest on the left?")
print ("Which way do you proceed left or right?") 

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left.")
    print("Proceed to the forest.")
    print("The forest is overrun with vegetation. You cannot proceed through the forest without tools to assist you.")
    print("You back out of the forest and make your way to the huts.")
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose right.")
    print("Proceed towards the huts.")
    #displays message to the user 
print ("You decide to explore the huts to see if there is any food, drink, supplies or tools you could gather.")
print ("Upon searching the second hut you find the following:")

#displayed to the user using a for loop with list 
items = ['axe', 'coconuts', 'rope', 'key', 'duffel bag']
for item in items:
    print (item)
    
print ("You load the axe, coconuts, rope, key and map that you've brought with you all into the duffel bag.")
print ("You need to determine how many coconuts you want to take with you")
print ("You can't decide, so this will be done at random for you")
print("You've collected this many coconuts:")
#generates random number for item selection
import random
num = random.randint(2, 6)
print(num)
print ("and have packed them in to your duffel bag")
print ("You check the remaining huts and find it's been ransacked.")
print ("You proceed back to the original position you were on the beach and retrieve your map to examine it further.")
print ("The map says the first X says to move towards the forest, so you continue on that route.")
print ("The path becomes obstructed by overgrown tree roots, thorny bushes and poison ivy plants.")
print ("You retrieve the axe from your bag and cut down the vegetation blocking your route.")
print ("You've come to a fork on the path in the forest.")
print ("One goes left towards the mountain side and the other goes right towards an open field of what looks like a farm of fresh fruits and vegetables.")
print ("You refer back to your map and see the X lays near the mountainside.") 
print ("You feel hungry but you know you only have a limited amount of daylight hours remaining.")
print ("Do you risk going right towards the farm for fresh fruits and vegetables or do you go left and carry on with your coconuts that provide both food and liquid and move towards the mountainside? ")
print ("Which option do you prefer, left or right?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left")
    print ("You decide to just carry on with your coconuts and proceed towards the mountain.") 
    
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose right.")
    print("Proceed towards the farm.")
    print("You spend a few hours harvesting and eating all the fruits and vegetables.")
    print("Let's see what you harvested:")

    #using a for loop to determine to display items to the user 
    harvest = [["apples", "bananas", "papayas", "oranges"],
        ["cucubmer", "tomato", "carrots", "zucchini"]]

    for collection in harvest:
        for food in collection:
            print(food)
        
        
    print("You over ate, you decide to take a nap on the ground, under a tree nearby.")
    print("After waking from your nap, you hear growling nosies in the distance, realizing it is now time to make a run for it.")
    print("You decide to look for somewhere to hide in the mountain.")

else: 
    #displays output message to the user 
    print("Invalid selection. Please enter left or right")
    
#displays output message to the user 
print ("As you get closer to the mountain, you notice there is an opening to a dark cave of some sort.")
print ("You make your way towards that cave with the thought that when nightfall comes you will not only have shelter but a relatively safe place to stay from the preying eyes of vicious animals.")
print ("As you approach the dark cave you see 2 tunnels, one on the right and one on the left.")
print ("Which tunnel do you take?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left.")
    print("Proceed to the tunnel on the left.")
    print("The tunnel goes on and on without any outlet, it's been over an hour now.")
    print("You begin to think you made the wrong decision and retrace your steps back to the beginning.")
    print("Finally, you've reached the starting point.")
    print("You proceed towards the tunnel on the right.")
        
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose to take the tunnel to the right.")
else: 
    #displays output message to the user 
    print("Invalid selection. Please enter left or right.")

#displays output message to the user    
print ("As you walk deeper into the tunnel you see two more tunnels down the way.")
print ("Again, there is one tunnel to the left and one tunnel to the right.")
print ("The tunnel to the right is dimly lit, showing very little light shining through, while the tunnel to the left is completely dark.")
print ("Which way do you proceed?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
#displays output message to the user  
    print("You chose left.")
    print("Proceed to the dark tunnel.")
    print("As you go deeper into the tunnel, you realize it really is dark in here.")
    print("You're thinkging you really wish you had a flashlight right about now.")
    print("You hear some rocks shuffling on the ground behind you, but can't see anything.")
    print("The shuffling gets louder and closer.")
    print("Oh no! You turn back and it's a huge python!! He opens his large mouth and devours you!")
    print("You are now dead! Sorry no treasure for you! Game over!")
    print("Would you like to play the game again?")

elif(directionChoice == "right"):
    print("You chose right")
    #displays output message to the user 
    print ("You begin making your way to the tunnel on the right.")
    print("Proceed towards the dimly lit tunnel.")
    print ("As you walk further into the tunnel you find yourself approaching an even larger cave.") 
    print ("You are now in the larger cave and find yourself perched upon a cliff next to a waterfall.")
    print ("You retrieve the rope from your bag, find a rock to secure it to and rappel down the cliff.")
    print ("You reach the bottom of the cliff and you see a door under the waterfall.")
    print ("You walk towards that door and see a keyhole.")
    print ("You retrieve the key from your duffel bag then insert the key into the keyhole.")
    print ("The door is very heavy but you manage to open it.")
    print ("Beyond the door you find a treasure box.") 
    print ("The same key you used to open the door opens the treasure box.")
    print ("Inside the treasure box you find some crown jewels, gold coins, and aleft satellite phone.") 
    print ("Congratulations! You've found the treasure!")
    print ("You turn on the satellite phone and call the only number stored in it.") 
    print ("The call is placed to an operator of a remote helicopter company not too far from the island.") 
    print ("This is your ticket home but you must forfeit half of the treasure to the company as payment for getting you off the island.")
    print ("Would you like to play the game again?")

else:
    #displays output message to the user  
    print("Invalid selection. Please enter left or right")

#Prompt user for a choice 
answerChoice = input(" yes > no (presss q to quit): ")   


while not (answerChoice == "yes"):
    #displays output message to the user 
    print("Goodbye! Thanks for playing.")  
    answerChoice = input("Play again or press (q to quit)")
else:
    print ("Welcome to Open Water Adventure")
print ("You wake up on a small shipping boat without any recollection of how you got there.")
print ("There are 2 others on the boat with you in addition to the captain at the steer.")
print ("You look around your quarters and see a large folded sheet of paper on the nightstand that says read me.") 
print ("You pick it up and find that it is a map of a deserted island with 3 large X's marked on it.") 
print ("You are advised that you will be needing to depart the ship upon landfall and that the map is your only ticket off the island, but only if you are successful at finding the treasure.")
print ("You arrive on shore and see a beach full of huts to your right and a trail that leads to a forest on the left?")
print ("Which way do you proceed left or right?") 

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left.")
    print("Proceed to the forest.")
    print("The forest is overrun with vegetation. You cannot proceed through the forest without tools to assist you.")
    print("You back out of the forest and make your way to the huts.")
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose right.")
    print("Proceed towards the huts.")
    #displays message to the user 
print ("You decide to explore the huts to see if there is any food, drink, supplies or tools you could gather.")
print ("Upon searching the second hut you find the following:")

#displayed to the user using a for loop with list 
items = ['axe', 'coconuts', 'rope', 'key', 'duffel bag']
for item in items:
    print (item)
    
print ("You load the axe, coconuts, rope, key and map that you've brought with you all into the duffel bag.")
print ("You need to determine how many coconuts you want to take with you")
print ("You can't decide, so this will be done at random for you")
print("You've collected this many coconuts:")
#generates random number for item selection
import random
num = random.randint(2, 6)
print(num)
print ("and have packed them in to your duffel bag")
print ("You check the remaining huts and find it's been ransacked.")
print ("You proceed back to the original position you were on the beach and retrieve your map to examine it further.")
print ("The map says the first X says to move towards the forest, so you continue on that route.")
print ("The path becomes obstructed by overgrown tree roots, thorny bushes and poison ivy plants.")
print ("You retrieve the axe from your bag and cut down the vegetation blocking your route.")
print ("You've come to a fork on the path in the forest.")
print ("One goes left towards the mountain side and the other goes right towards an open field of what looks like a farm of fresh fruits and vegetables.")
print ("You refer back to your map and see the X lays near the mountainside.") 
print ("You feel hungry but you know you only have a limited amount of daylight hours remaining.")
print ("Do you risk going right towards the farm for fresh fruits and vegetables or do you go left and carry on with your coconuts that provide both food and liquid and move towards the mountainside? ")
print ("Which option do you prefer, left or right?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left")
    print ("You decide to just carry on with your coconuts and proceed towards the mountain.") 
    
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose right.")
    print("Proceed towards the farm.")
    print("You spend a few hours harvesting and eating all the fruits and vegetables.")
    print("Let's see what you harvested:")

    harvest = [["apples", "bananas", "papayas", "oranges"],
        ["cucubmer", "tomato", "carrots", "zucchini"]]

    for collection in harvest:
        for food in collection:
            print(food)
        
    print("You over ate, you decide to take a nap on the ground, under a tree nearby.")
    print("After waking from your nap, you hear growling nosies in the distance, realizing it is now time to make a run for it.")
    print("You decide to look for somewhere to hide in the mountain.")

else: 
    #displays output message to the user 
    print("Invalid selection. Please enter left or right")
    
#displays output message to the user 
print ("As you get closer to the mountain, you notice there is an opening to a dark cave of some sort.")
print ("You make your way towards that cave with the thought that when nightfall comes you will not only have shelter but a relatively safe place to stay from the preying eyes of vicious animals.")
print ("As you approach the dark cave you see 2 tunnels, one on the right and one on the left.")
print ("Which tunnel do you take?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
    #displays output message to the user 
    print("You chose left.")
    print("Proceed to the tunnel on the left.")
    print("The tunnel goes on and on without any outlet, it's been over an hour now.")
    print("You begin to think you made the wrong decision and retrace your steps back to the beginning.")
    print("Finally, you've reached the starting point.")
    print("You proceed towards the tunnel on the right.")
        
elif(directionChoice == "right"):
    #displays output message to the user 
    print("You chose to take the tunnel to the right.")
else: 
    #displays output message to the user 
    print("Invalid selection. Please enter left or right.")

#displays output message to the user    
print ("As you walk deeper into the tunnel you see two more tunnels down the way.")
print ("Again, there is one tunnel to the left and one tunnel to the right.")
print ("The tunnel to the right is dimly lit, showing very little light shining through, while the tunnel to the left is completely dark.")
print ("Which way do you proceed?")

#Prompt user for a choice 
directionChoice = input("> ")

#If, Elif, Else statments executed for specific or multiple conditions based on user input
if(directionChoice == "left"):
#displays output message to the user  
    print("You chose left.")
    print("Proceed to the dark tunnel.")
    print("As you go deeper into the tunnel, you realize it really is dark in here.")
    print("You're thinkging you really wish you had a flashlight right about now.")
    print("You hear some rocks shuffling on the ground behind you, but can't see anything.")
    print("The shuffling gets louder and closer.")
    print("Oh no! You turn back and it's a huge python!! He opens his large mouth and devours you!")
    print("You are now dead! Sorry no treasure for you! Game over!")
    print("Would you like to play the game again?")

elif(directionChoice == "right"):
    print("You chose right")
    #displays output message to the user 
    print ("You begin making your way to the tunnel on the right.")
    print("Proceed towards the dimly lit tunnel.")
    print ("As you walk further into the tunnel you find yourself approaching an even larger cave.") 
    print ("You are now in the larger cave and find yourself perched upon a cliff next to a waterfall.")
    print ("You retrieve the rope from your bag, find a rock to secure it to and rappel down the cliff.")
    print ("You reach the bottom of the cliff and you see a door under the waterfall.")
    print ("You walk towards that door and see a keyhole.")
    print ("You retrieve the key from your duffel bag then insert the key into the keyhole.")
    print ("The door is very heavy but you manage to open it.")
    print ("Beyond the door you find a treasure box.") 
    print ("The same key you used to open the door opens the treasure box.")
    print ("Inside the treasure box you find some crown jewels, gold coins, and aleft satellite phone.") 
    print ("Congratulations! You've found the treasure!")
    print ("You turn on the satellite phone and call the only number stored in it.") 
    print ("The call is placed to an operator of a remote helicopter company not too far from the island.") 
    print ("This is your ticket home but you must forfeit half of the treasure to the company as payment for getting you off the island.")
    print ("Would you like to play the game again?")

else:
    #displays output message to the user  
    print("Invalid selection. Please enter left or right")

#Prompt user for a choice 
answerChoice = input(" yes > no (presss q to quit): ")   


while not (answerChoice == "yes"):
    #displays output message to the user 
    print("Goodbye! Thanks for playing.")  
    answerChoice = input("Play again or press (q to quit)")
    












