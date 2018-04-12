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
    userAction = input("Choose an action (reward, punish, threaten, joke): ")
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
        currEmotion = "anger"
        print ("You make me so angry sometimes!")
        return 0
        
    if reaction == 1:
        currEmotion = "disgust"
        print ("Ugh, I am #DISGUSTED")
        return 1
        
    if reaction == 2:
        currEmotion = "fear"
        print ("AHH I'm scared!")
        return 2
        
    if reaction == 3:
        currEmotion = "happiness"
        print ("Aww you made me happy!")
        return 3
        
    if reaction == 4:
        currEmotion = "sadness"
        print ("Boooo you made me sad")
        return 4
        
    if reaction == 5:
        currEmotion = "surprise"
        print("I was not expecting that!! You surprised me!")
        return 5
    print(currEmotion)
    return currEmotion
        


def main():
    print ("Welcome to the Artificial Intelligence Program. This program will")
    print ("take an action of your choosing and determine how the AI will feel.")
    print ("It will work based on its current emotion, which will change as you go.")
    currEmotion = 3
    while True:
        userAction = getInteraction()
        currEmotion = lookupEmotion (userAction, currEmotion)

main()
