#Intro to Programming
#Author : Susan Cantoni
#Date : 04-11-18
#Personality.py

#personality matrix below

p = [[3,0,0,5],
     [3,0,0,0],
     [5,2,2,5],
     [3,1,2,3],
     [3,1,5,3],
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
    #break
    return userAction
    
        #TODO return an emotion
#        return userAction

def lookupEmotion (userAction):
    currEmotion = 3
    userAction = [col]
    print("You got here")
    currEmotion = [row]
    if p[row][col] == 0:
        currEmotion = anger
        
    if p[row][col] == 1:
        currEmotion = disgust
        
    if p[row][col] == 2:
        currEmotion = fear
        
    if p[row][col] == 3:
        currEmotion = happiness
        
    if p[row][col] == 4:
        currEmotion = sadness
        
    if p[row][col] == 5:
        currEmotion = surprise
        
    print (currEmotion)
    return currEmotion, userAction
    #takes current emotion and the interaction and determines next emotion
    #return emotion



def main():
    getInteraction()
    lookupEmotion (userAction)
    print(currEmotion)

main()
