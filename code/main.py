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
   def __init__(self,currX,currY):
      self.button = tkinter.Button(window, text ="Put troll here!", command = self.disableButton)     
      self.button.place(x=currX,y=currY) 

   def disableButton(self):
      #TODO add picture of troll in the same spot
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


def startGame(n):

   #creating 3x3 buttons 
   #TODO make it take in an input n
   for i in range(1,n+1):
      for j in range(1,n+1):
         buttons.append(trollButton(150*i,50*j)) #TODO put the buttons between 0 and screenheight-200
         #TODO update the buttons positions if the window changes size



   undoButton.place(x=50,y=windowHeight-200) 
   undoButton['state'] = tkinter.DISABLED


   #trying the enableButton function:
   while 0:
      if input()=="NO":
         buttons[-1].enableButton()
      else:
         print(history)


def startMenu():
   global windowWidth, windowHeight, history, buttons
   windowWidth=screeninfo.get_monitors()[0].width
   windowHeight=screeninfo.get_monitors()[0].height
   history=[]     #history over the users recent moves
   buttons=[]

   global window
   window = tkinter.Tk() #initialize window
   window.geometry(f"{windowWidth}x{windowHeight}")

   global textLabel,labelVar
   labelVar = tkinter.StringVar()
   labelVar.set("Write an integer larger than 3: ")
   textLabel = tkinter.Label(window, textvariable=labelVar, height = 5, width = 52)
   textLabel.place(x=windowWidth//2-400,y=windowHeight//2-200)



   #Creating the textbox for input
   global inputBox
   inputBox = tkinter.Text(window, height = 5, width = 5) 
   inputBox.place(x=windowWidth//2,y=windowHeight//2-50)

   #grid layout or pack (flow) layout?
   #inputBox.pack() 

   #Input button
   global sizeSelectionButton
   sizeSelectionButton = tkinter.Button(window, text = "Set Board Size and Start Game",command = setSize)
   sizeSelectionButton.place(x=windowWidth//2,y=windowHeight//2+40) 
   
   #sizeSelectionButton.pack() 

   global undoButton
   undoButton = tkinter.Button(window, text ="Undo last move", command = undoLastMove)

   window.mainloop()



def setSize(): #TODO have different funcitons. one for setSize, one for mainMenu and so on
   #TODO move the inputBox creation and sizeSelectionBUtton in this function
   global n

   while True:
      try:
         n = inputBox.get(1.0, "end-1c")
         n=int(n)
         if n>3:
            break
         else:
            labelVar.set("That is not an integer larger than 3! Try again! \n Write an integer larger than 3: ") 
      
      except:
         labelVar.set("That is not an integer. Try again! \n Write an integer larger than 3: ")
         
   #TODO felhantering av n


   textLabel.place_forget()
   inputBox.place_forget()
   sizeSelectionButton.place_forget()

   startGame(n)


startMenu()



