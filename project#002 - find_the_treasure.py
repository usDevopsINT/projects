"""
---find the treasure---
-first step-
1)make a new file or delete the file at the start.
2)inside the file, there are numbers 0-9 (chronological order).
3)every number will appear randomly 1-20 times.
4)after the last "9" number, write the word "TREASURE", and after that, write again 1-20 times (runrandomly), 9-0 in a chronological order (9,8...)
-second step-
1)open the file in a read mode only.
2)the player need to move right or left.
3)each time print the "landing" charecter that the user's cursor was on it.
4)when the player, land on one of the charecter of the word "TREASURE", finish the game.
5)after the game has been finished, print how much turn it take to find a latter of "TREASURE".
*6)build a table of the 10 best score.
"""

import random
#------------map file------------

def map():
    """
    define the "map" of the game
    :return:
    """
    mapFile=open("map.txt", "w", 1)
    for i in range(10): #loop 0-9 - game map numbers
        for j in range(1,random.randint(2,21)): #define the couple of times the same number appear
            mapFile.write(str(i))
    mapFile.write("TREASURE")
    for i in range(9,-1,-1):
        for j in range(1,random.randint(2,21)):
            mapFile.write(str(i))
    mapFile.close()


lenMap=0
def lenMap():
    """
    understerd the initial boundaries of the map
    :return: None
    """
    global lenMap
    mapFile=open("map.txt","r",1)
    print(mapFile.readline()) #test# print the map
    mapFile.seek(0) #reset cursor position
    lenMap=len(mapFile.read())
    #print(lenMap)
    #print(mapFile.tell())
    mapFile.seek(0) #reset cursor position
    mapFile.close()
    return None

def input_check_move(userInput):
    """
    check that the input of moving input is valid
    :param userInput: input  from the user
    :return: according to the input.
    """
    try:
        userInput=int(userInput)
    except:
        if userInput=="q" or userInput=="Q":
            return "q"
        else:
            print("Worng input, please insert a valid option.")
            return -1
    global lenMap
    if  0<userInput<=lenMap:
        #print("valid input") #test# valid input
        return userInput
    elif userInput==0 or userInput=="0":
        print("Do you want to rest?:)")
        return userInput
    elif 0>userInput or userInput>=lenMap:
        print ("out of boundaries!, try again:")
        return -1
    else:
        print("Worng input, please insert a valid option.")
        return -1

def input_check_WS(userInput):
    """
    check that the input of moving forwards/backwards is valid
    :param userInput: input  from the user
    :return: according to the input.
    """
    try:
        userInput=int(userInput)
    except:
        if userInput=="q" or userInput=="Q":
            return "q"
        else:
            print("Worng input, please insert a valid option.")
            return -1
    if  userInput==1:
        return 1  #forwards
    elif userInput==2:
        return 2 #backwards
    else:
        print("Worng input, please insert a valid option.")
        return -1

def  mapToList():
    """
    change the map into list, because file.seek can't work backwards
    :return: map as list
    """
    mapFile=open("map.txt","r")
    mapList=[]
    for i in mapFile.readline():
        mapList.append(i)
    #print(mapList)
    mapFile.close()
    return mapList

def checkTreasure(userSteps,mapList):
    """
    check if you fall into a "treasure" characters
    :param userSteps: user's step
    :param mapList: the map as a list
    :return: 1 if win, 0 if lose
    """
    treasure=["T","R","E","A","S","U","R","E"]
    for i in treasure:
        if mapList[userSteps]==i:
            print("you find the treasure:)")
            print("-----The game is over-----")
            return 1
    print("you didn't find the treasure, please try again.")
    return 0

def move(userSteps,ws):
    """
    move the "cursor"
    :param userSteps: user's step
    :param ws: 1-forwards 2-backwards
    :return:
    """
    if ws==1: #forwards
        global carriage
        carriage+=userSteps
        return carriage
    elif ws==2: #backwards
        carriage-=userSteps
        return carriage

print('-welcome to the "find the treasure" game-')
userName=input("please write your name (press Enter to continue):")

map()
lenMap()
carriage=0
userCounter=0
while True:
    print("enter q if you want to exit the game (game will not be saved!)")
    ws=input_check_WS(input("Where you want to move? [1-forwards 2-backwards]"))
    if ws=="q":
        break
    elif ws==-1:
        continue
    userSteps=input_check_move(input("How many characters?"))
    userCounter+=1
    if userSteps=="q":
        break
    elif userSteps==-1:
        continue
    else:
        mapList=mapToList()
        findT=checkTreasure(move(userSteps,ws),mapList)
        if findT==1:
            break
        print(mapList[carriage])
