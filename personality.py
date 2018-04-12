#Intro to Programming
#Author : Susan Cantoni
#Date : 04-11-18
#Personality.py

#personality matrix below

p = [[3,0,0,5],
     [3,0,0,0],
     [5,2,2,5],
     [3,4,2,3],
     [3,0,5,3],
     [3,0,2,3]]

def getInteraction():
    #get interaction from user and assign an interger to userAction
    #while True:
    userAction = input("\nChoose an action (reward, punish, threaten, joke): ")
    if userAction == "reward":
        userAction = 0
    if userAction == "punish":
        userAction = 1
    if userAction == "threaten":
        userAction = 2
    if userAction == "joke":
        userAction = 3
    return userAction

def lookupEmotion (userAction, currEmotion):
    i = currEmotion 
    j = userAction
    reaction = p[i][j]
    
    if reaction == 0:
        feeling = "anger"
        print ("You make me so angry sometimes!")
        return 0, feeling
        
    if reaction == 1:
        feeling = "disgust"
        print ("Ugh, I am #DISGUSTED")
        return 1, feeling
        
    if reaction == 2:
        feeling = "fearful"
        print ("AHH I'm scared!")
        return 2, feeling
        
    if reaction == 3:
        feeling = "happiness"
        print ("Aww you made me happy!")
        return 3, feeling
        
    if reaction == 4:
        feeling = "sadness"
        print ("Boooo you made me sad")
        return 4, feeling
        
    if reaction == 5:
        feeling = "surprised"
        print("I was not expecting that!! You surprised me!")
        return 5, feeling
    
    return currEmotion, feeling
        


def main():
    print ("Welcome to the Artificial Intelligence Program. This program will")
    print ("take an action of your choosing and determine how the AI will feel.")
    print ("It will work based on its current emotion, which will change as you go.")
    currEmotion = 3
    while True:
        userAction = getInteraction()
        currEmotion, feeling = lookupEmotion (userAction, currEmotion)
        print ("I am feeling... ", feeling)

main()
