class Message:
    '''
    otherMessage: A string message for the entity being spoken to
    userOptions: A list of string dialog options from which the user can choose
    messageLinks: A list of Message objects indicating the Message that follows each userOption.
                  The index of each item messageLinks must correspond with the index of an item in userOptions.
    prevMessage: The message that lead to this message. 
    '''
    def __init__(self, otherMessage, userOptions, messageLinks=None):
        self.otherMessage = otherMessage 
        self.userOptions = userOptions 
        self.messageLinks = messageLinks 
        self.prevMessage = None
    

def getNumLeading(s, char):
    num = 0
    pos = 0
    while pos<len(s) and s[pos]==char:
        num+=1
        pos+=1
    return num

#Construct message tree from file
def loadMessage(fileName):
    fh = open(fileName)
    root = Message("", []) #empty root to which real root will be attached
    lastMsg = root #previous message processed
    prevLevel = 0 #level of message on last pass
    for line in fh:
        line = line.strip()
        if len(line)==0:
            continue
        parts = line.split(";")
        print parts
        #Get other entity's message text
        otherMsg = parts[0].strip()
        #Get array of string user responses by splitting on the '|'
        user = [x.strip() for x in parts[1].split("|")]
        #get count of leading '.' before the other to determine position in dialog tree
        level = getNumLeading(otherMsg, '.')
        #Create new Message to add to dialog
        newMsg = Message(otherMsg[level:],user)

        if level == prevLevel:
            newMsg.prevMessage = lastMsg.prevMessage
            lastMsg.prevMessage.messageLinks.append(newMsg)
            
        elif level > prevLevel:
            newMsg.prevMessage = lastMsg
            if lastMsg.messageLinks == None:
                lastMsg.messageLinks = [newMsg]
            else:
                lastMsg.messageLinks.append(newMsg)
            
        else: #level < prevLevel
            newMsg.prevMessage = lastMsg.prevMessage.prevMessage
            lastMsg.prevMessage.prevMessage.messageLinks.append(newMsg)
            #If fewer links than user options in lastMsg, then need to fill
            #links with None values
            nOpts=len(lastMsg.prevMessage.userOptions)
            nLinks=len(lastMsg.prevMessage.messageLinks)
            while nOpts > nLinks:
                lastMsg.prevMessage.messageLinks.append(None)
                nLinks+=1
            
        lastMsg=newMsg
        prevLevel = level
    return root.messageLinks[0]

#Run the dialog from a root    
def showDialog(rootMessage):
    current = rootMessage
    while current!=None:
        print "\nNPC: "+current.otherMessage
        choice = 1
        for option in current.userOptions:
            print str(choice)+". "+option
            choice+=1

        nextIndex = raw_input("Select an option: ")
        if current.messageLinks==None:
            current = current.messageLinks
        else:
            current = current.messageLinks[int(nextIndex)-1]
    

data = loadMessage("convo1.dat")
showDialog(data)
