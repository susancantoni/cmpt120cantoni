#Intro to Programming
#Author : Susan Cantoni
#Date : 04-11-18
#Personality.py

#personality matrix below

p = [[3,0,0,5],
     [3,0,0,0],
     [5,2,2,5],
     [3,1,2,3],
     [3,4,5,3],
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
        
    if reaction == 1:
        currEmotion = "disgust"
        print ("Ugh, I am #DISGUSTED")
        
    if reaction == 2:
        currEmotion = "fear"
        print ("AHH I'm scared!")
        
    if reaction == 3:
        currEmotion = "happiness"
        print ("Aww you made me happy!")
        
    if reaction == 4:
        currEmotion = "sadness"
        print ("Boooo you made me sad")
        
    if reaction == 5:
        currEmotion = "surprise"
        print("I was not expecting that!! You surprised me!")

    return currEmotion
        


def main():
    currEmotion = 3
    userAction = getInteraction()
    currEmotion = lookupEmotion (userAction, currEmotion)
    print(currEmotion)

main()
