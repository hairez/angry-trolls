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
   def __init__(self, frame, x, y):
      self.button = tkinter.Button(frame, text ="Put troll here!", command = self.placeTroll)
      self.button.pack(side="right")
      
      #The position of the button on the grid. The upper left button is (0,0). The y-coord is the row number, and x-coord is column number.
      self.x = x
      self.y = y

   def placeTroll(self):

      if checkValidMove(self.x, self.y):
         currGrid[self.y][self.x] = 1  #If a troll is placed on a position (x,y), then currGrid[y][x] will be 1, otherwise 0.
         history.append(self)
         self.button['state'] = tkinter.DISABLED
         undoButton['state'] = tkinter.NORMAL #enable the undo button

         #TODO if a move has been played, check if there are any valid moves left.

      else:
         #TODO if not valid move, end the game.
         pass
   
   def enableButton(self):
      self.button['state'] = tkinter.NORMAL
      currGrid[self.y][self.x] = 0

      if not history:
         undoButton['state'] = tkinter.DISABLED #disable the undo button if there is nothing to undo


#Checks if a troll could be placed at position (x,y)
def checkValidMove(x, y):
   
   n = len(currGrid)

   for i in range(n):
      if currGrid[y][i]:#Checks if there is a troll on the same row
         return 0
      if currGrid[i][x]:#Checks if there is a troll on the same column
         return 0
   

   #Check if there is a troll on the \ diagonal
   tempX, tempY = x-min(x,y), y-min(x,y)
   while tempX<n and tempY<n:
      if currGrid[tempY][tempX]:
         return 0
      tempX+=1
      tempY+=1
   

   #Checks if there is a troll on the / diagonal and above (x,y)
   i=1
   while x+i<n and 0<=y-i:
      if currGrid[y-i][x+i]:
         return 0
      i+=1
   
   #Checks if there is a troll on the / diagonal and under (x,y)
   i=1
   while 0<=x-i and y+i<n:
      if currGrid[y+i][x-i]:
         return 0
      i+=1

   #If no troll has been found, then it is a valid move
   return 1      




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
   pass


def calculateTime():
   #TODO räknar ut resultatet av spelet, hur lång tid det tar och sparar resultatet i en fil.
   #kallar på updateFile()
   pass

def finishBoard():
   #TODO skapa en knapp i mainGame som kallar på denna funktion, som fyller i resterande troll där man kan.
   #kör en bruteforce recursive algo som backtrackar och testar alla troll
   #borde lösas i O(n^2)
   pass


def gameLost():

   pass



def startGame(n, windowWidth=screeninfo.get_monitors()[0].width, windowHeight=screeninfo.get_monitors()[0].height):
   
   #Creating n x n buttons
   for y in range(n):
      currGrid.append([0]*n)
      buttonFrames.append(tkinter.Frame(rightFrame))
      buttonFrames[-1].pack(fill="both", expand=True, padx=20, pady=20)

      for x in range(n):
         buttons.append(trollButton(buttonFrames[-1], x, y)) 



   undoButton.pack(side="bottom", padx=20, pady=20) 
   undoButton['state'] = tkinter.DISABLED

   finishButton.pack(side="top", padx=20, pady=20)




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
finishButton = tkinter.Button(leftFrame, text ="Finish the board for me", command = finishBoard)

rightFrame=tkinter.Frame(window)
rightFrame.pack(side="right")

buttonFrames=[]
history=[]     #history over the users recent moves
buttons=[]

currGrid=[]    #the current game grid
startMenu()



