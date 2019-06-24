print("\n\n\t\t*********************************************************")
print("\t\t                    A GOLDEN CROWN                       ")
print("\t\t*********************************************************\n")
print("\t\t\t----------------PROBLEM 1-----------------\n")
print("\n______________\n")
print("KINGDOM\tEMBLEM\nSpace\tMonkey\nLand\tPanda\nWater\tOctopus\nIce\tMammoth\nAir\tOwl\nFire\tDragon")
print("\n_______________\n")

#---- Getter Methods ---
def getRuler():
    if len(allies)>=3:
        global ruler
        ruler = "King Shan"
    print(ruler)

def getAllies():
    a=len(allies)
    if a==0:
        print("None")
    else:
        print(allies)

def sendMessage():
    print('" Send your secret message to the Kingdoms, My King!! "\nInput: ')
    msg=input()
    #Seprate the input (eg: Air, "o11w22l33") into kingdom and message 
    m=msg.split(', ')
    kingdom=m[0]
    msg=m[1]
    checkAllies(kingdom,msg)

def checkAllies(kingdom,msg):
    
    #This method checks whether emblem of each Kingdom is in the given message
    if kingdom == 'Land':
        land={'p','n','d'}
        decipherMsg(kingdom, msg, land,'a', 2)
    elif kingdom == 'Water':
        water={'c','t','p','u','s'}
        decipherMsg(kingdom, msg, water,'o', 2)
    elif kingdom == 'Ice':
        ice={'a','o','t','h'}
        decipherMsg(kingdom, msg, ice, 'm', 3)
    elif kingdom == 'Air':
        air={'o','w','l'}
        decipherMsg(kingdom, msg, air,'\0', 0)
    elif kingdom == 'Fire':
        fire={'d','r','a','g','o','n'}
        decipherMsg(kingdom, msg, fire, '\0', 0)
    elif kingdom == 'Space':
        space={'m','o','n','k','e','y'}
        decipherMsg(kingdom, msg, space,'\0', 0)
    else:
        print('\n ------------- Incorrect Kingdom ----------------')  
        
        
def decipherMsg(kingdom, msg, secretCode, alphabet,alpha_occurance):
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
        if kingdom not in allies:
            allies.append(kingdom)
    
    
if __name__=='__main__':
    
    ruler="None"
    allies=[]
    
    while(True):
        print('1. Who is the ruler of southern?\n2. Allies of Ruler?\n3. Input\n4. Exit')
        try:
            n=int(input())
            if n==1:
                getRuler()
            elif n==2:
                getAllies()
            elif n==3:
                sendMessage()
            else:
                break
        except:
            print("Invalid Input!!")



