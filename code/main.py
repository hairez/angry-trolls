#Use this to install:
#pip install tk
#or
#sudo apt install python3-tk
import tkinter
from tkinter import messagebox

from PIL import ImageTk, Image

#Use this to install:
#pip install screeninfo
import screeninfo #library to get the width and height of user screen.
import time

class trollButton:
   def __init__(self, currX, currY,frame):
      self.button = tkinter.Button(frame, text ="Put troll here!", command = self.disableButton)
      #self.button.place(x=currX,y=currY) 
      self.button.pack(side="right")

   def disableButton(self):
      #TODO add picture of troll in the same spot

      #img = ImageTk.PhotoImage(Image.open("./code/sprites/troll.png"))
      #self.button.configure(image=img)

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

   #creating n x n buttons
   for i in range(1,n+1):
      #TODO add n frames, where each frame is stacked vertically ontop of each otehr, and add n buttons to each frame.
      buttonFrames.append(tkinter.Frame(rightFrame))
      buttonFrames[-1].pack(fill="both", expand=True, padx=20, pady=20)

      for j in range(1,n+1):
         buttons.append(trollButton(150*i,50*j,buttonFrames[-1])) #TODO put the buttons between 0 and screenheight-200



         #TODO update the buttons positions if the window changes sizea



   undoButton.pack(side="bottom") 
   undoButton['state'] = tkinter.DISABLED


   #trying the enableButton function:
   while 0:
      if input()=="NO":
         buttons[-1].enableButton()
      else:
         print(history)


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
      labelVar.set("That is not an integer. Try again! \n Write an integer larger than 3: ")
      return #exit the function and the loop until a new value has been entered


   #remove all buttons from the main menu
   textLabel.place_forget()
   inputBox.place_forget()
   sizeSelectionButton.place_forget()

   startGame(n)



window = tkinter.Tk() #initialize window
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



