import random

print("\n\n\t\t*********************************************************")
print("\t\t                    BREAKER OF CHAINS                        ")
print("\t\t*********************************************************\n")
print("\t\t\t-----------------PROBLEM 2-----------------\n")
print("\n______________\n")
print("KINGDOM\tEMBLEM\nSpace\tMonkey\nLand\tPanda\nWater\tOctopus\nIce\tMammoth\nAir\tOwl\nFire\tDragon")
print("\n_______________\n")


#---- Getter Methods ---
def getRuler():
    global ruler
    maxAllies=0
    for k,v in competitor.items():
        if(len(v)>maxAllies):
            maxAllies=len(v)
            ruler=k
    print(ruler)

def getRulerAllies():
    global ruler
    a=""
    if ruler!='None':
        for i in competitor[ruler]:
            a=a+i+" "
        print(a)
    else:
        print('None')
        
def getInput_KingdomsCompeting():
    print ("------- Press N/n to end the Enrollment ---------")
    while(True):
        print ("Enter Input:")
        k=input()
        if any(s in k for s in('N','n')):
            #print(competitor)
            sendMessage()
            ballotResult()
            break
        elif any(s in k for s in ('Air','Water','Land','Fire','Ice','Space')):
            competitor[k]=[]
        else:
            print('\n ------------- Incorrect Kingdom ----------------')
            
def sendMessage():
    for sender in competitor:
        print('*************************************************************************')
        print('Hi '+sender+' King, to which kingdom you are going to the send messages!!')
        print('*************************************************************************')
        messages=getRandomMessage()
        #print(messages)
        #print(len(messages))
        print('\n')
        for m in messages:
            print('Message: {}'.format(m))
            print('To:')
            receiver=str(input())
            if any(s in receiver for s in ('Air','Water','Land','Fire','Ice','Space')):
                if any(s in receiver for s in (competitor.keys())): print('**** Access Denied!! ****')
                else:
                    checkAllies(sender,receiver,m)
            else: print('\n ------------- Incorrect Kingdom ----------------\n')  

    #print(competitor)

def getRandomMessage():
    #Getting six random numbers between 0 to 25
    #(since there are 25 lines in txt file)
    randomLines=[]
    randomMessages=[]
    randomLines=random.sample(range(0, 25), 6)
    randomLines.sort()

    #print(randomLines)

    #Getting the Random Message from the txt file
    with open("messages.txt") as fp:
        for i, line in enumerate(fp):
            if i in randomLines:
                #print(line)
                randomMessages.append(line.rstrip('\n'))
    return randomMessages

def checkAllies(sender,receiver,msg):
    if receiver == 'Land':
        land={'p','n','d'}
        decipherMsg(sender, receiver, msg, land, 'a', 2)
    elif receiver == 'Water':
        water={'c','t','p','u','s'}
        decipherMsg(sender, receiver, msg, water, 'o', 2)
    elif receiver == 'Ice':
        ice={'a','o','t','h'}
        decipherMsg(sender, receiver, msg, ice,' m', 3)
    elif receiver == 'Air':
        air={'o','w','l'}
        decipherMsg(sender, receiver, msg, air, '\0', 0)
    elif receiver == 'Fire':
        fire={'d','r','a','g','o','n'}
        decipherMsg(sender, receiver, msg, fire, '\0', 0)
    elif receiver == 'Space':
        space={'m','o','n','k','e','y'}
        decipherMsg(sender, receiver, msg, space, '\0', 0)

def decipherMsg(sender, receiver, msg,secretCode,alphabet, alpha_occurance):
    #print('---Deciphering the msg----')
    msg=msg.lower()
    alpha=0 #variable to count the alphabet occurance in the given message
    m=set(msg) #set fun will remove all the duplicates
    sc=secretCode
    v=m.intersection(sc) #gets the common value of given msg and the secret Code

    #Process to count the emblem which has more than one occrance in a msg
    if alphabet!='\0':
        l=list(msg)
        for i in l:
            if alphabet in i:
                alpha = alpha + 1

    #add the valid allies to the list  
    if alpha>=alpha_occurance and len(v)==len(sc):
        for s in competitor.values():
            if receiver in s: return
        competitor[sender].append(receiver)
    

def ballotResult():
    global rounds
    ballot=[]
    print("\nResults after round {} ballot count".format(str(rounds)))
    for k,v in competitor.items():
        print("Allies for "+k+" : "+str(len(v)))
        ballot.append(len(v))
    if max(ballot)==min(ballot):
        rounds=rounds+1
        sendMessage()
        ballotResult()
                
                           
if __name__=='__main__':

    ruler="None"
    competitor={}
    rounds=1
    
    while(True):
        print('1. Who is the ruler of southern?\n2. Allies of Ruler?\n3. Enter the kingdoms competing to be the ruler.\n4. Exit')
        try:
            n=int(input())
            if n==1:
                getRuler()
            elif n==2:
                getRulerAllies()
            elif n==3:
                getInput_KingdomsCompeting()
            else:
                break
        except:
            print('Invalid Input')
    
