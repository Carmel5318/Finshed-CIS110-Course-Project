import sys
import time
def slowprint(string):
    for char in range(len(string)):
        print(string[char], end="")
        time.sleep(1./35)


slowprint("\nMy name is Carmel. Do I have a tale to tell you, but the path of this tale is in your hands.  ")
slowprint("\nWe can continue I need for you to answer a few questions for me.  ")
slowprint("\nAfter typing your answer be sure to press the enter key.")
slowprint("\nPress the enter key to continue...")

userName = input("\nEnter your name:  ")
while (len(userName) == 0) :
    userName = input("\nI am sorry you cannot leave this blank.  Please enter your name: ")

if userName.lower() == "niki decker":
    slowprint("\nMy creator," + userName + ". Pleasure to serve you!")
else:
    slowprint("\nHello, " + userName +". Nice to meet you!")
keepGoing = "y"
while keepGoing.lower() == "y":
  
    
    seaTurtle = input("\nWhat would you like to name your sea turtle?  ").lower()
    while (len(seaTurtle) == 0) :
        seaTurtle = input("\nThis can not be left blank. Please give your sea turtle a name:  ").lower()


    oceanName = input("\nCan you name an ocean? ").lower()
    while (len(oceanName) == 0) :
        oceanName = input("\nPlease name an ocean. i.e. Atlantic, Pacific, Indian, Arctic:  ").lower()

    islandName = input("\nWhat is an Island you want to visit?  ").lower()
    while (len(islandName) == 0) :
        islandName = input("\nPlease enter and Island that you would like to visit or have visited:  ").lower()


    number = input("\nWhat are last two digits of your birth year?  ")
    while not number.isdigit() : 
        number= input("\nI need two digits any two digits will do. (i.e. 3).  Please enter a numeric value: ")

    favoriteBeach = input("\nWhat is the name of your favorite beach?  ").lower()
    while (len(favoriteBeach) == 0) :
        favoriteBeach = input("\nPlease enter your favorite beach or a beach you would like to visit:  ").lower()
    
    turtleType = input("\nPlease choose one of the three given types of turtles? Enter green sea turtles, leatherback sea turtles, or loggerhead sea turtles:  ").lower()
    while turtleType != "green sea turtles" and turtleType != "leatherback sea turtles" and turtleType != "loggerhead sea turtles" :
        turtleType = input("\nPlease enter green sea turtles, leatherback sea turtles, or loggerhead sea turtles: ").lower()
  

    if turtleType.lower() == "green sea turtles" : 
        slowprint("Are you ready? Let's go!")
        slowprint("\n")

        slowprint("\nOnce upon a time there was a beautiful " +  str(turtleType) + " named " + str(seaTurtle) + ". ")
        slowprint("\n " + str(seaTurtle) + " loved to play on the beach.  ")
        slowprint("\nOne day " + str(seaTurtle) + " was playing on the beach and the time passed by him quickly.  ")
        slowprint("\n " + str(seaTurtle) + " noticed he was no longer able to see family.  ")
        slowprint("\nSo " +  str(seaTurtle) + " searched all around the island and the beach. His family was nowhere around.  ")
        slowprint("\nHe then decides to go search the " + str(oceanName) + " ocean in hopes of finding his family.  ")
        slowprint("\nAfter searching the " + str(oceanName)+ " ocean for " + str(number) + " days.  ")
        slowprint("\n " + str(seaTurtle) + " comes across " +  str(islandName) + " Island.  ")
        slowprint("\nHe wonders if his family could be at " +  str(favoriteBeach) + " beach on " + str(islandName) + " Island.  ")

        checkOutbeach = input("\nShould " + str(seaTurtle)+ " go check the beach for his fmaily?  Type yes or no:")
        while checkOutbeach.lower() != "yes" and checkOutbeach.lower() != "no" :
            checkOutbeach = input("\nPlease type yes or no: ")
        if checkOutbeach.lower() == "yes" :

            slowprint("\n " + str(seaTurtle) + " decides to go to " + str(islandName) + " Island to search " +  str(favoriteBeach) + " beach in hopes of finding his family.  ")
            slowprint("\nOnce " + str(seaTurtle) + " arrives to " + str(favoriteBeach) + " beach and starts searching for his family.  ")
            slowprint("\n " +  str(seaTurtle) + " comes across " + str(turtleType) + ", just like him, and he gets distracted by playing with them, and he loses track of time.  ")
            slowprint("\nBefore he knew it " + str(seaTurtle) + " had spent " + str(number) + " days on " +  str(islandName) + " Island he begins to miss his family.  ")
            slowprint("\nSo ," + str(seaTurtle) + " sets back out to the " +  str(oceanName) + " ocean to search for him family.  ")
            slowprint("\n " + str(seaTurtle) + " has searched the " + str(oceanName) + " ocean for " +  str(number) + "weeks and still no sign of his family.  ")                               
        else:

            slowprint("\nAfter carefully thinking about it he decides not to seach "+ str(favoriteBeach) + " on " + str(islandName) + " because he does not think his family would be there. ")
            slowprint("\n " + str(seaTurtle) + " continues to search the " + str(oceanName) + " in the hope that he will soon find his family that he has lost. ")

            slowprint("\nUntil one day while searching for his family " +str(seaTurtle) + " sees a family of " + str(turtleType) +" up ahead and is curious if they could be his family. ")
           
        seaTurtlefamily =input("\nShould " + str(seaTurtle)+ " check to see if the family of " + str(turtleType)+ " is his family or not? Type yes or no:  ")
        while seaTurtlefamily.lower() != "yes" and seaTurtlefamily.lower() != "no" :
            seaTurtlefamily = input("\nPlease type yes or no :")

        if seaTurtlefamily.lower() == "yes" :
            slowprint("\n " + str(seaTurtle) + " decides to check and see if they are his family.  ")
            slowprint("\nAs " + str(seaTurtle) + " gets closer, he soon realized that the family of " + str(turtleType)+ " is the family he has been searching for.  ")
            slowprint("\n " + str(seaTurtle) + " is happy he has finally found his family and is not alone anymore.  ")
        else:
            slowprint("\n " + str(seaTurtle) + " decides not to check because the family of " + str (turtleType)+ " does not look like his family. ")
            slowprint("\n " + str(seaTurtle) + " continues his search for the family that he has lost.  ")

        if checkOutbeach.lower() == "yes" and seaTurtlefamily.lower() == "yes":
            slowprint("\nAfter traveling the " + str(oceanName)+ " ocean " + str(seaTurtle)+  " and his family decide to go to " + str(islandName)+ " Island.  ")
            slowprint("\nTo make a home on " + str(favoriteBeach)+ " beach, and live their remaining years happy together on " + str(islandName)+ " Island.  ")
        elif checkOutbeach.lower() == "yes" and seaTurtlefamily.lower() == "no":
            slowprint("\nAfter playing and makeing new friends at " + str(islandName)+ " and searching the " + str(oceanName)+ " for " + str(number)+ " years. ")
            slowprint("\nStill unable to find his family " + str(seaTurtle)+ " decides to go back to the " + str(islandName)+ " and be with his friend there on " + str(favoriteBeach)+ ".")
            slowprint("\nSo " + str(seaTurtle)+ " is not all alone."  )
        else:
            slowprint("\nAfter deciding to not search " + str(islandName)+ " and keep searching the " + str(oceanName)+ " for his family.  ")
            slowprint("\n" +str(seaTurtle) + " continues to search until he finds his lost family. He will search even if it takes " + str(number)+ " years.  ")
            slowprint("\n" + str(seaTurtle) + " is not going to give up on finding his family.  " )
        
   
    elif turtleType == "leatherback sea turtles" :
         slowprint("\nLet's get ready to rumble!!!")
         slowprint("\n")
         slowprint("\nIt was a bright sunny day not a cloud in the sky." + str(seaTurtle)+ " decides that he wants to play on" + str(favoriteBeach) + " beach and enjoy the sun. ")
         slowprint("\nOnce " + str(seaTurtle) + " got to the beach it was so beautiful and the sun rays felt so good. ")
         slowprint("\nAs " + str(seaTurtle) + " is playing he sees something is the distance coming towards him. He gets scared what should " + str(seaTurtle) + " do? ")
         checkItout = input("\nShould  " + str(seaTurtle)+ " check it out?  Type yes or no:")
         while checkItout.lower() != "yes" and checkItout.lower() != "no":
             checkItout = input("\nPlease type yes or no :")
         if checkItout.lower() == "yes" :
            slowprint("\n " + str(seaTurtle) + " decides to check it out. As "+ str(seaTurtle) + " gets closer he sees that it is humans with nets, and they are headed straight towards a nest of newly hatched" +str(turtleType) + ".")
            slowprint("\n " + str(seaTurtle) + " starts to get closer and the humans spot him and start to walk towards "+ str(seaTurtle) + " with a net")
            slowprint("\n " + str(seaTurtle) + " runs in the opposite direction to lead the poachers in the other direction. ")
             
         if checkItout.lower() == "no" :
            slowprint("\n " + str(seaTurtle) + " decided that it would be in his best interest not to get involved and goes the other way. ")
            slowprint("\n " + str(seaTurtle) + " returns to the other side of " + str(favoriteBeach) + " beach and sits there and enjoys the waves and the rays from the sun. ")
            slowprint("\n " + str(number) + " hours have passed by and " + str(seaTurtle) + " wakes up to see humans with nets closing in on him. ") 
              
         sandRun = input("\nWhat should " + str(seaTurtle) + " do? Throw sand or run away and save himself? Type Sand or Run: ")
         while sandRun.lower() != "sand" and sandRun.lower() != "run":
             sandRun = input("\nPlease type sand or run : ")
         if sandRun.lower() == "sand" :
             slowprint("\n " + str(seaTurtle) + " then throws sand in the humans faces " + str(number) + " times.")
             slowprint("\nWhile the humans are distracted " + str(seaTurtle) + " then starts to attack the humans.")
             slowprint("\nAfter non-stop attacks from " + str(seaTurtle) + " for " +  str(number) + " minutes. The humans get up and run away. " ) 
  
         else:
             slowprint("\n " + str(seaTurtle) + " decided that it is to dangerous for him to get involved and runs away into the " + str(oceanName) + " ocean.")
             slowprint("\nLeaving the baby " + str(turtleType) + " to fend for themselves. ")
    
         if checkItout.lower() == "yes" and sandRun.lower() == "sand":
             slowprint("\n " + str(seaTurtle) + " after " + str(number) + " days on " + str(islandName) + " island. ")
             slowprint("\n " + str(seaTurtle) + " has rescued family of " + str(turtleType) + " and ran of the poachers.     " ) 
             slowprint("\n " + str(seaTurtle) + " swims out into the " + str(oceanName) + " ocean with the baby " + str(turtleType) + " and spend his days protecting the baby " + str(turtleType) + " until they do not need him anymore. ")
         elif checkItout.lower() == "yes" and sandRun.lower() == "run" :
             slowprint("\n " + str(seaTurtle) + " helped rescue a family of baby " + str(turtleType) + ".")
             slowprint("\n " + str(seaTurtle) + " even out ran the poachers by going in to the " + str(oceanName) + " ocean and lives " + str(number) + " months swiming around the " + str(oceanName) + " ocean wondering what he will do next. ")
         else:
             slowprint("\n " + str(seaTurtle) + " has only looked out for himself. ")
             slowprint("\n " + str(seaTurtle) + " also escaped the poachers and he is all alone on " + str(favoriteBeach)+ " beach.")
             slowprint("\n " + str(seaTurtle) + " lived " + str(number) + " years on " + str(islandName) + " island until he passed away from being alone. ")
            

    if turtleType == "loggerhead sea turtles" :
        slowprint("\nAre you ready for this? Let's get it!!!")
        slowprint("\n ")
        slowprint("\nIt was a beautiful day out in the "  + str(oceanName) + " ocean and " + str(seaTurtle) + " was swimming around. ")
        slowprint("\nAfter " + str(number) + " hours of swimming around " + str(seaTurtle) + " saw another " + str(turtleType)+ " up ahead and decided to see if they would like to hang out. " )
        slowprint("\nAs he gets closer " + str(seaTurtle) + " he notices a beautiful " + str(turtleType) + ".")
        slowprint("\n " + str(seaTurtle) + " swims up to the " + str(turtleType) + " and introduces himself and find out her name is " + str(userName) + ".")
        slowprint("\n " + str(seaTurtle) + " wonders if " + str(userName) + " would like to go visit " + str(islandName) + " island and play on " + str(favoriteBeach) + " beach." )
        toAskorNot = input("\nShould " + str(seaTurtle)+ " invite " + str(userName) + " to " + str(favoriteBeach) + " beach on "  + str(islandName) + " island to hang out? Type Ask or No : ")
        while toAskorNot.lower() != "ask" and toAskorNot.lower() != "no":
            toAskorNot = input("\n Please type ask or no : ")
        if  toAskorNot.lower() == "ask":
            slowprint("\n " + str(seaTurtle) + " asks " + str(userName) + " if they would like to go hang out on " +str(favoriteBeach) + " beach and " + str(userName) + " says yes. " )
            slowprint("\n " + str(seaTurtle) + " and " + str(userName) + " swim together to " + str(favoriteBeach) + " beach."  )
            slowprint("\nWhere they spend " + str(number) + " days together enjoying each others company and exploring " + str(islandName) + " island having a blast. "  )
            slowprint("\n " + str(seaTurtle) + " wants to ask " + str(userName) + "to marry him. "  )
            
        else: 
            slowprint("\n " + str(seaTurtle) + " chickens out and does not ask " + str(userName) + " to go " + str(favoriteBeach) + " beach on " + str(islandName)  + " island." )
            slowprint("\n " + str(seaTurtle) + " swims arount the " + str(oceanName) + " ocean for " + str(number) + " hours thinking to himself and finally decides to go to " + str(favoriteBeach) + " beach on " + str(islandName) + " island with the other " + str(turtleType) + ". " )
            slowprint("\n " + str(seaTurtle)  + " simply can not get " + str(userName) + " out of his mind. "  )
            slowprint("\nSo " + str(seaTurtle) + " rushes to " + str(favoriteBeach) + " beach to search for " + str(userName) + "." )
            slowprint("\n " + str(seaTurtle) + " wants to ask " + str(userName) + " to marry him. "  )
        
        iDoiDont = input("\nHow should " + str(userName) + " answer " + str(seaTurtle) + " proposal?  Please type  do or  dont : " )
        while iDoiDont.lower() != "do" and iDoiDont.lower() != "dont" :
            toAskorNot = input("\nPlease type  do or  dont : " )
        
        if iDoiDont.lower() == "do" :
            slowprint("\n " + str(seaTurtle) + " asks " + str(userName) + " to marry him and she says yes!"   )
            slowprint("\n " + str(seaTurtle) + " and  " + str(userName) + " are so happy. "  ) 

        else:
            slowprint("\n " + str(userName) + " tells " + str(seaTurtle) + " I am already with someone I am sorry. "  )
            slowprint("\n " + str(seaTurtle) + " runs off heartbroken. " )


        if toAskorNot.lower() == "ask" and iDoiDont.lower() == "do":
            slowprint("\n "  + str(seaTurtle) + " and " + str(userName) + " hurry to tell all their friends and family. "  )
            slowprint("\n "  + str(number) + " hours later they are having their wedding on " + str(favoriteBeach) + " beach and they live happily ever after! "   ) 
        
        elif toAskorNot.lower() == "ask" and iDoiDont.lower() == "dont" :
            slowprint("\n " + str(seaTurtle) + " leaves " + str(favoriteBeach) + " beach heartbroken and heads back to the " + str(oceanName) + " ocean wondering if he will ever find a mate. " )
            slowprint("\nBut until then " + str(seaTurtle) + " will continue to stay with his family and continue the search for his one true love")
            slowprint("\n " + str(seaTurtle) + " believes that she is out there some where waiting. "  )
        else:
            slowprint("\nAfter being rejected twice " + str(seaTurtle) + " sets off determined to find the one " + str(turtleType)+ " that he is destined to be with. "   )
            slowprint("\n " + str(seaTurtle) + " spend " +str(number) + " years searching for his true love, but he is arfraid that he will never find her. "  ) 
        
        
    slowprint("\nAre you feeling lucky? Do you wanna try again?  ")

    keepGoing = input("\nWell are ya? Enter y or n:")
 
    for seconds in range(60, 0, -2):
        print(seconds, end = " \r")
        import time
        time.sleep(1)
    print("\n")
