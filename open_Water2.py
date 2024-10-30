#Setting up a function to be called later 
def game():
    #Multi-line string format to make output to user easier to read 
    a = """" 
    Welcome to Open Water Adventure
    You wake up on a small shipping boat without any recollection of how you got there. There are 2 others on the boat with you in addition to the captain at the steer. You look around your quarters
    and see a large folded sheet of paper on the nightstand that says read me. You pick it up and find that it is a map of a deserted island with 3 large X's marked on it. You are advised that you will
    be needing to depart the ship upon landfall and that the map is your only ticket off the island, but only if you are successful at finding the treasure. You arrive on shore and see a beach full of huts
    to your right and a trail that leads to a forest on the left. Which way do you proceed left or right?
    """
    print(a)

    #Prompt user for a choice 
    directionChoice = input("> ")

    #If statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game. 
    if(directionChoice == "left"):
        #Multi-line string format to make output to user easier to read 
        a = """ 
        You chose left. The forest is overrun with vegetation. You cannot proceed through the forest without tools to assist you. Turn around and make your way to the huts.
        """
        print(a)
    #Elif statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game.       
    elif(directionChoice == "right"):
        #Multi-line string format to make output to user easier to read 
        a = """
        You chose right. Proceed towards the huts.
        """
        print(a)
    #Else statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game.        
    else: 
        #displays output message to the user 
        print("Invalid selection. Please enter left or right")
        
    #Multi-line string format to make output to user easier to read  
    a = """
    You decide to explore the huts to see if there is any food, drink, supplies or tools you could gather. Upon searching the second hut you find the following:
    """
    print(a)
        
    #displayed to the user using a for loop with list - Loop 1
    items = ['axe', 'coconuts', 'rope', 'key', 'duffel bag']
    for item in items:
        #outputs the list of items to the user 
        print (item)    
    #Multi-line string format to make output to user easier to read     
    a = """
    You load the items you've collected, including the map that you've brought with you, all into the duffel bag. But you need to determine how many coconuts you 
    want to take with you. You can't decide, so this will be done at random for you. You've collected this many coconuts:
    """
    print(a)

    #generates a random number for the specific item from the previous list
    import random
    num = random.randint(2, 6)
    #outputs the random number selected to the user 
    print(num)
    #Multi-line string format to make output to user easier to read 
    a = """ 
    and have packed them in to your duffel bag. You check the remaining huts and find it's been ransacked. You proceed back to the original position you were on the beach and retrieve your map to examine it further.
    The map says the first X says to move towards the forest, so you continue on that route. The path becomes obstructed by overgrown tree roots, thorny bushes and poison ivy plants. You retrieve the axe from
    your bag and cut down the vegetation blocking your route. You've come to a fork on the path in the forest. One goes left towards the mountain side and the other goes right towards an open field of what looks like a
    farm of fresh fruits and vegetables. You refer back to your map and see the X lays near the mountainside. You feel hungry, but you know you only have a limited amount of daylight hours remaining.
    Do you risk going right towards the farm for fresh fruits and vegetables or do you go left and carry on with your coconuts that provide both food and liquid and move towards the mountainside? 
    Which option do you prefer, left or right?
    """
    print(a)   

    #Prompt user for a choice 
    directionChoice = input("> ") 

    #If statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game. 
    if(directionChoice == "left"):
        #Multi-line string format to make output to user easier to read  
        a = """ 
        You chose left, you decide to just carry on with your coconuts and proceed towards the mountain.
        """ 
        print(a)
    #Elif statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game.       
    elif(directionChoice == "right"):
        #Multi-line string format to make output to user easier to read #displays output message to the user 
        a = """ 
        You chose right. Proceed towards the farm. You spend a few hours harvesting and eating all the fruits and vegetables. Let's see what you harvested:
        """ 
        print(a)
        
        #Nested for loop - Loop 2, variables defined with lists 
        descriptor = ["tasty"]
        vegetables = ["apple", "bananas","papayas", "oranges","carrots","zucchini"]

        for x in descriptor:
            for y in vegetables:
                print(x, y)
        #Multi-line string format to make output to user easier to read     
        a = """ 
        You over ate, you decide to take a nap on the ground, under a tree nearby. After waking from your nap, you hear growling nosies in the distance, realizing it is now time to make a run for it.
        You decide to look for somewhere to hide in the mountain.
        """
        print(a)
    #Else statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game.    
    else: 
        #displays output message to the user 
        print("Invalid selection. Please enter left or right")
        
    #Multi-line string format to make output to user easier to read 
    a = """ 
    As you get closer to the mountain, you notice there is an opening to a dark cave of some sort. You make your way towards that cave with the thought that when nightfall comes you will not only have shelter
    but a relatively safe place to stay, away from preying eyes of vicious animals. As you approach the dark cave you see 2 tunnels, one dimly lit tunnel on the right and one dark tunnel on the left. Which 
    tunnel do you take, left or right?
    """
    print(a)

    #Prompt user for a choice 
    directionChoice = input("> ")

    #If statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game.
    if(directionChoice == "left"):
       #Multi-line string format to make output to user easier to read 
        a = """ 
        You chose left. Proceed into the dark tunnel. As you go deeper into the tunnel, you realize it is really dark in here, you're wishing you had a flashlight right about now.
        The tunnel goes on and on without any outlet. You begin to think you've made the wrong decision. You hear some rocks shuffling on the ground behind you, but can't see anything.
        The shuffling gets louder and closer. Oh no! You turn back and it's a huge python!! He opens his large mouth and devours you! You are now dead! Sorry no treasure for you! Game over!
        Would you like to play the game again?
        """
        print(a)
    #Elif statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game.        
    elif(directionChoice == "right"):
        #Multi-line string format to make output to user easier to read  
        a = """ 
        You chose to take the tunnel on the right. Proceed towards the dimly lit tunnel. As you walk further into the tunnel you find yourself approaching an even larger cave. Upon entering the 
        larger cave, you noticed you are perched on a cliff, next to a waterfall. You retrieve the rope from your bag and find a rock to secure it to so that you can rappel down the cliff.
        You reach the bottom of the cliff and see a door underneath the waterfall. Walking towards that door, you see a keyhole. You retrieve the key from your duffel bag, then insert the key 
        into the keyhole. The door is very heavy but you manage to open it. Beyond the door you find a treasure box. Inside that treasure box are some crown jewels, gold coins, and a satellite phone.
        Congratulations! You've found the treasure! You turn on the satellite phone and call the only number stored in it. The call is placed to an operator of a remote helicopter company not too far 
        from the island. This is your ticket home but you must forfeit half of the treasure to the company as payment for getting you off the island. Would you like to play the game again?
        """
        print(a)
    #Else statment executed after user the inputs left or right direction. Each direction has it's own specific event based on input, creating different paths and end result to the game.        
    else: 
        #displays output message to the user 
        print("Invalid selection. Please enter left or right.")
#end of function         
game()

#Calling a function in a while loop that runs indefinitely - Loop 3
def main():
    #Defining variable equal to specific string
    choices = {'yes'}
    #Prompts user for input
    userInput = input('Do you want to continue playing? Type yes > no (presss q to quit): ')
    #function that is called if the condition is met/true
    print(game)
    #while loop executes the function when the condition is true
    while True: 
        game()
        #checks to see if the input from user is an option in choices variable 
        if userInput not in choices:
         #Outputs this message to the user when the condition is no longer met/true
         print('Goodbye! Thanks for playing.')
         #statement that stops the loop 
         break
#end of function 
main()