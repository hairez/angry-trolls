#Use this to install:
#pip install tk
#or
#sudo apt install python3-tk
import tkinter
from tkinter import messagebox

#Use this to install:
#pip install screeninfo
import screeninfo #library to get the width and height of user screen.
windowWidth=screeninfo.get_monitors()[0].width
windowHeight=screeninfo.get_monitors()[0].height

import time

#TODO add comments to everything
#TODO sort the functions nicely?


class trollButton:
   def __init__(self, frame, x, y):
      self.button = tkinter.Button(frame, text ="Put troll here!", command = self.placeTroll, activebackground="blue", bg = "gray")
      self.button.grid(row=y, column=x, padx=20, pady=10)
      
      #The position of the button on the grid. The upper left button is (0,0). The y-coord is the row number, and x-coord is column number.
      self.x = x
      self.y = y

   def placeTroll(self):
      if checkValidMove(self.x, self.y):
         currGrid[self.y][self.x] = 1  #If a troll is placed on a position (x,y), then currGrid[y][x] will be 1, otherwise 0.
         self.button.configure(bg = "green", text = "Undo this move!", command = self.undoMove)

         #Check if there are any possible moves left:
         n = len(currGrid)
         moreMoves=0
         for x in range(n):
            for y in range(n):
               if checkValidMove(x,y):
                  moreMoves=1
         
         if moreMoves==0:
            gameWon()
         

      else:
         gameLost()

   
   def undoMove(self):
      self.button.configure(bg = "gray", text ="Put troll here!", command = self.placeTroll)
      currGrid[self.y][self.x] = 0

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

#Count number of trolls that are placed out
def countTrolls():
   n=len(currGrid)
   trolls=0
   for x in range(n):
      for y in range(n):
         if currGrid[x][y]:
            trolls+=1
   return trolls

def openFile(gridSize):
   #Finds the directory of where the code is running, and opens the result-file for the current grid size
   file = open(__file__[:-7]+f"results/{gridSize}.txt", "r", encoding="utf-8")

   fileRows=file.readlines()

   file.close()

   gameResults=[]
   for row in fileRows:
      gameResults.append([*map(eval,row.split(","))])

   return gameResults,file
   
def updateFile(allResults, gridSize):
   file = open(__file__[:-7]+f"results/{gridSize}.txt", "w", encoding="utf-8")
   for trolls,trollTime in allResults:
      file.write(f"{trolls},{trollTime}\n")
   file.close()

def checkResult(newTime, trolls, gridSize):
   allResults,file=openFile(gridSize)

   #We want to sort by most number of trolls, and then lowest time.
   allResults.append([-trolls,newTime])
   allResults.sort()

   #Update the relevant file, and only save the top 10 scores
   updateFile(allResults[:10], gridSize)

   return allResults.index([-trolls,newTime])+1

#Calculate the time from start to finish
def calculateTime():
   return round(time.time()-timer[-1],2)

def finishBoard():
   #TODO skapa en knapp i mainGame som kallar på denna funktion, som fyller i resterande troll där man kan.
   #kör en bruteforce recursive algo som backtrackar och testar alla troll
   #borde lösas i O(n^2)
   pass

def gameWon():
   #Calculate the resulting time to 2 decimal seconds. Units is seconds.
   resultTime = calculateTime()

   n=len(currGrid)

   trolls=countTrolls()
   
   currentPlacing = checkResult(resultTime, trolls, n)

   disableAllGameButtons()

   resultMessage=f"Well done! You took {resultTime} seconds! \nYou put down {trolls} trolls without any troll getting angry! \nYou are placed #{currentPlacing} on a {n}x{n}-grid."

   tkinter.messagebox.showinfo(title="Game Won! ", message=resultMessage)

   #Show restartButton
   restartButton.pack(side="right")

def disableAllGameButtons():
   #Disable all other buttons
   for button in buttons:
      button.button["state"] = tkinter.DISABLED
   finishButton["state"] = tkinter.DISABLED

def restartGame():
   #Hide all buttons form main game
   for button in buttons:
      button.button.grid_forget()
   finishButton.pack_forget()
   restartButton.pack_forget()
   leftFrame.pack_forget()
   rightFrame.pack_forget()

   #Clearing up currGrid and buttons so new game could be started
   buttons.clear()
   currGrid.clear()
   #Clearing up timer, since the saved time stamp is useless if the game is restarting
   timer.clear()

   #Starting the menu
   startMenu()

def gameLost():
   #A message box displaying that the game is over.
   messagebox.showwarning(title="Game Lost", message="Oh no! The trolls just got angry. Try again! ")

   disableAllGameButtons()

   #Show restartButton
   restartButton.pack(side="right")

def startGame(n):
   #Creating n x n buttons
   for y in range(n):
      for x in range(n):
         buttons.append(trollButton(rightFrame, x, y)) 
   
   #Creating a grid where all current trolls could be tracked on.
   for _ in range(n):
      currGrid.append([0]*n)

   #Add the main left and right frames to the window
   leftFrame.pack(side="left")
   rightFrame.pack(side="right")

   #Add the finishButton
   finishButton.pack(side="top", padx=20, pady=20)
   finishButton["state"]=tkinter.NORMAL

   timer.append(time.time())


def startMenu():
   #TODO add explanation of how the game works
   #TODO Explain what the buttons does
   #TODO Explain that finish the game means to give up

   #Set label-text:
   labelVar.set("Write an integer larger than 3 and less than 10: ")

   #Set position of textLabel:
   textLabel.place(x=windowWidth//2-400,y=windowHeight//2-200)

   #Set position for inputBox
   inputBox.place(x=windowWidth//2,y=windowHeight//2-50)

   #Set position for sizeSelectionButton
   sizeSelectionButton.place(x=windowWidth//2,y=windowHeight//2+40) 

def setSize(): 
   try:
      n = inputBox.get(1.0, "end-1c")
      n = int(n)
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
window.title("Angry Trolls - The Game")
window.geometry(f"{windowWidth}x{windowHeight}")

#Initializing all other labels in the window
labelVar = tkinter.StringVar()
textLabel = tkinter.Label(window, textvariable=labelVar, height = 5, width = 52)
inputBox = tkinter.Text(window, height = 5, width = 5) 
sizeSelectionButton = tkinter.Button(window, text = "Set Board Size and Start Game",command = setSize)
rightFrame=tkinter.Frame(window)
leftFrame=tkinter.Frame(window)
finishButton = tkinter.Button(leftFrame, text = "Finish the board for me", command = finishBoard)
restartButton = tkinter.Button(leftFrame, text = "Restart Game", command = restartGame)

buttons=[]     #An array keeping all relevant trollButtons
currGrid=[]    #A grid tracking the current state of the game
timer=[]       #An array keeping track of time stamps

startMenu()
window.mainloop()
