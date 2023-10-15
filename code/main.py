#Use this to install:
#pip install tk
#or
#sudo apt install python3-tk
import tkinter
from tkinter import messagebox

#Use this to install:
#pip install screeninfo
import screeninfo #library to get the width and height of user screen.
import time

class trollButton:
   def __init__(self, frame, index):
      self.button = tkinter.Button(frame, text ="Put troll here!", command = self.disableButton)
      self.button.pack(side="right")
      self.index = index

   def disableButton(self):
      history.append(self)
      self.button['state'] = tkinter.DISABLED
      undoButton['state'] = tkinter.NORMAL #enable the undo button
   
   def enableButton(self):
      self.button['state'] = tkinter.NORMAL

      if not history:
         undoButton['state'] = tkinter.DISABLED #disable the undo button if there is nothing to undo





def undoLastMove():
   button = history.pop()
   button.enableButton()
   return


def openFile():
   #TODO öppnar filen där den sparar alla resultat. prob en CSV fil
   #sparar nuvarande top resultat i en array
   assert 1

def updateFile():
   #TODO updaterar resultaten i filen efter att ha uppdaterat den med det nya resultatet. 
   #kan lösas med en array
   assert 1


def calculateTime():
   #TODO räknar ut resultatet av spelet, hur lång tid det tar och sparar resultatet i en fil.
   #kallar på updateFile()
   assert 1

def finishBoard():
   #TODO skapa en knapp i mainGame som kallar på denna funktion, som fyller i resterande troll där man kan.
   #kör en bruteforce recursive algo som backtrackar och testar alla troll
   #borde lösas i O(n^2)
   assert 1


def startGame(n, windowWidth=screeninfo.get_monitors()[0].width, windowHeight=screeninfo.get_monitors()[0].height):
   index=0
   #Creating n x n buttons
   for _ in range(1,n+1):
      buttonFrames.append(tkinter.Frame(rightFrame))
      buttonFrames[-1].pack(fill="both", expand=True, padx=20, pady=20)

      for _ in range(1,n+1):
         #Each button gets an index from 0 to n**2-1
         buttons.append(trollButton(buttonFrames[-1],index)) 
         index+=1


   undoButton.pack(side="bottom") 
   undoButton['state'] = tkinter.DISABLED



def startMenu(windowWidth=screeninfo.get_monitors()[0].width, windowHeight=screeninfo.get_monitors()[0].height):
   

   #Set label-text:
   labelVar.set("Write an integer larger than 3 and less than 10: ")

   #Set position of textLabel:
   textLabel.place(x=windowWidth//2-400,y=windowHeight//2-200)



   #Set position for inputBox
   inputBox.place(x=windowWidth//2,y=windowHeight//2-50)

   #grid layout or pack (flow) layout?
   #inputBox.pack() 

   #Set position for sizeSelectionButton
   sizeSelectionButton.place(x=windowWidth//2,y=windowHeight//2+40) 
   
   #sizeSelectionButton.pack() 

   

   window.mainloop()



def setSize(): 
   try:
      n = inputBox.get(1.0, "end-1c")
      n=int(n)
      if n<4 or n>9:
         labelVar.set("That is not an integer larger than 3 and less than 10! Try again! \n Write an integer larger than 3 and less than 10: ") 
         return #exit the function and the loop until a new value has been entered
   except:
      labelVar.set("That is not an integer. Try again! \n Write an integer larger than 3 and less than 10: ")
      return #exit the function and the loop until a new value has been entered


   #Remove all buttons from the main menu
   textLabel.place_forget()
   inputBox.place_forget()
   sizeSelectionButton.place_forget()

   startGame(n)



window = tkinter.Tk() #Initialize window
windowWidth=screeninfo.get_monitors()[0].width
windowHeight=screeninfo.get_monitors()[0].height
window.geometry(f"{windowWidth}x{windowHeight}")

#Initializing all other labels in the window
labelVar = tkinter.StringVar()
textLabel = tkinter.Label(window, textvariable=labelVar, height = 5, width = 52)
inputBox = tkinter.Text(window, height = 5, width = 5) 
sizeSelectionButton = tkinter.Button(window, text = "Set Board Size and Start Game",command = setSize)


#TODO add a left frame (where i put the undo button and finish board button) and a right frame (containing all frames in buttonFrames)

leftFrame=tkinter.Frame(window)
leftFrame.pack(side="left")

undoButton = tkinter.Button(leftFrame, text ="Undo last move", command = undoLastMove)


rightFrame=tkinter.Frame(window)
rightFrame.pack(side="right")

buttonFrames=[]
history=[]     #history over the users recent moves
buttons=[]
startMenu()



