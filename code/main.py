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


class TrollButton:
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
         n = len(currGrid)    #The size of the grid is always the number of rows in the grid
         moreMoves=0
         for x in range(n):
            for y in range(n):
               if checkValidMove(x,y):    #True if checkValidMove(x,y)==1, and False if checkValidMove(x,y)==0
                  moreMoves=1
         
         #If there are no more moves, then the game ends, and the player has won
         if moreMoves==0:
            gameWon()
         
      else:
         #If the move is not valid, then player loses
         gameLost()

   def undoMove(self):
      self.button.configure(bg = "gray", text ="Put troll here!", command = self.placeTroll)
      currGrid[self.y][self.x] = 0  #Sets the corresponding cell to 0, indicating that there is no troll on that cell

#Checks if a troll could be placed at position (x, y). Returns 1 if it is a valid move, otherwise 0.
def checkValidMove(x, y):
   n = len(currGrid)    #The size of the grid is always the number of rows in the grid

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
def countTrolls(grid):
   trolls=sum(sum(row) for row in grid)   #Number of trolls is equal to the sum of all numbers in the grid
   return trolls

def openFile(gridSize):
   #Finds the directory of where the code is running, and opens the result-file for the current grid size
   file = open(__file__[:-7]+f"results/{gridSize}.txt", "r", encoding="utf-8")
   fileRows=file.readlines()
   file.close()

   gameResults=[]       #Each element in this array will contain a past result for the current grid size
   for row in fileRows:
      gameResults.append([*map(eval,row.split(","))])    #The information for each game is stored seperated with commas on a row
   return gameResults,file
   
def updateFile(allResults, gridSize):
   file = open(__file__[:-7]+f"results/{gridSize}.txt", "w", encoding="utf-8")
   for trolls,trollTime in allResults:
      file.write(f"{trolls},{trollTime}\n")
   file.close()

def checkResult(newTime, trolls, gridSize):
   allResults,file=openFile(gridSize)

   #We want to sort by most number of trolls, and then lowest time.
   allResults.append([-trolls,newTime])   #.sort() will sort the array with the smallest element first. By having a negative number of trolls, the more trolls, the lower index in the array it will have.
   allResults.sort()

   #Update the relevant file, and only save the top 10 scores
   updateFile(allResults[:10], gridSize)

   return allResults.index([-trolls,newTime])+1    #The index is off by 1 compared to the placing.

#Calculate the time from start to finish
def calculateTime():
   return round(time.time()-timer[-1],2)  #Calculate the result rounded to 2 decimal seconds.

def finishBoard():
   n = len(currGrid)    #The size of the grid is always the number of rows in the grid
   
   def fillGrid(x, y, notValidGrid):      #Fill in the grid notValidGrid everywhere where you cannot put a troll if there is a troll on (x, y)
      occupied = [row[:] for row in notValidGrid]
      #Occupied is a grid keeping track of all occupied cells.

      for i in range(n):
         occupied[y][i]=1  #Fill in all cells on the same row
         occupied[i][x]=1  #Fill in all cells on the same column

      #Fill in cells on the same diagonal \
      tempX, tempY = x-min(x,y), y-min(x,y)
      while tempX<n and tempY<n:
         occupied[tempY][tempX]=1
         tempX+=1
         tempY+=1
      
      #Checks if there is a troll on the / diagonal and above (x,y)
      i=1
      while x+i<n and 0<=y-i:
         occupied[y-i][x+i]=1
         i+=1
      
      #Checks if there is a troll on the / diagonal and under (x,y)
      i=1
      while 0<=x-i and y+i<n:
         occupied[y+i][x-i]=1
         i+=1
      
      return occupied
      
   def generateInvalidSquares(trollGrid):    #Given a grid with all trolls, return a grid with all invalid squares
      occupied=[[0]*n for _ in range(n)]
      for x in range(n):
         for y in range(n):
            if trollGrid[y][x]:
               occupied = fillGrid(x,y,occupied)
      return occupied
   
   def solve(occupied, currState, row=0):    #Try all possible combination of trolls if all rows about row is already determined

      if row==n:
         return countTrolls(currState), currState  #Return number of trolls and the placement
      
      if sum(occupied[row]) == n:  #If there is no free spots on this row
         return solve(occupied, currState, row+1)     #Skip this row and go to the next row
      
      bestScore=0
      bestState=currState
      for x,cell in enumerate(occupied[row]):   #Try placing a troll on every avaiable cell on every row
         if cell:
            continue
         score,tempState = solve(fillGrid(x,row,occupied), filledInCell(x,row,currState), row+1)   #Attempts to solve the grid if there is a troll on (x, row)

         if score>bestScore:     #Save the positions with the highest score
            bestScore=score
            bestState=[row[:] for row in tempState]
         
         if score==n: #It can never reach more than n points, so if it ever reaches n points, that would be the optimal answer
            break
      
      return bestScore,bestState
      
   def filledInCell(x,y,grid):      #Returns another grid where (x, y) is filled in to be 1
      tempGrid = [row[:] for row in grid]
      tempGrid[y][x]=1
      return tempGrid

   notValid=generateInvalidSquares(currGrid)    #Find all invalid cells to place a troll

   #Remove references to currgrid to not accidentally put any trolls in the original grid
   tempNotValid=[row[:] for row in notValid]
   tempState=[row[:] for row in currGrid]    

   score, bestState = solve(tempNotValid, tempState)  #Find the optimal solution from the current board position

   for button in buttons:  #Clear the text on all the trollButtons
      button.button.configure(text=" "*22)   

   #Turn all the trolls in bestState that were not placed by the player to red 
   for x in range(n):
      for y in range(n):
         if bestState[y][x] and not currGrid[y][x]:
            buttons[y*n+x].button.configure(bg = "red")  #y is the row number, and x is the column number. The index of the button will be y*n+x because there are n elements on each row

   disableAllGameButtons()
   restartButton.pack(side="right")

def gameWon():
   resultTime = calculateTime()
   trolls=countTrolls(currGrid)
   
   n=len(currGrid)
   currentPlacing = checkResult(resultTime, trolls, n)   #Update the results, and check the current placing

   disableAllGameButtons()

   resultMessage=f"Well done! You took {resultTime} seconds! \nYou put down {trolls} trolls without any troll getting angry! \nYou are placed #{currentPlacing} on a {n}x{n}-grid."
   if currentPlacing==11:  #If the result is placed number 11, then the result is not saved.
      resultMessage+="\n Sadly since you didn't place top 10, your result will not be saved. Better luck next time!"
   tkinter.messagebox.showinfo(title="Game Won! ", message=resultMessage)

   #Show restartButton
   restartButton.pack(side="right")

def gameLost():
   #A message box displaying that the game is over.
   messagebox.showwarning(title="Game Lost", message="Oh no! The trolls just got angry. Try again! ")

   disableAllGameButtons()

   #Show restartButton
   restartButton.pack(side="right")

def disableAllGameButtons():     #Disable all TrollButtons and the finish button
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

def startGame(n):
   #Creating n x n buttons
   for y in range(n):
      for x in range(n):
         buttons.append(TrollButton(rightFrame, x, y)) 
   
   #Creating a grid where all current trolls could be tracked on.
   for _ in range(n):
      currGrid.append([0]*n)

   #Put down the main left and right frames to the window
   leftFrame.pack(side="left")
   rightFrame.pack(side="right")

   #Push down and enable the finishButton
   finishButton.pack(side="top", padx=20, pady=20)
   finishButton["state"]=tkinter.NORMAL

   timer.append(time.time())  #Start a new time

def setSize(): 
   try:  #Felhantering
      n = inputBox.get(1.0, "end-1c")
      n = int(n)
      if n<4 or n>9: #Guarantees that the gridsize is between 4 and 9, inclusive
         labelVar.set("That is not an integer larger than 3 and less than 10! Try again! \n Write an integer larger than 3 and less than 10: ") 
         return #exit the function and the loop until a new value has been entered
   except:
      labelVar.set("That is not an integer. Try again! \n Write an integer larger than 3 and less than 10: ")
      return #exit the function and the loop until a new value has been entered
   
   #When the size of the grid is set,
   #remove all buttons from the main menu
   textLabel.place_forget()
   inputBox.place_forget()
   sizeSelectionButton.place_forget()
   startGame(n)

def startMenu():
   rules = "Welcome to Angry Trolls! Here are the rules: \n 1. Select a size of the board. \n 2. Click on a button to place a troll there, and it will turn green. \n 3. Fill in as many trolls as you can, until you can't fill in any more trolls. \n \
4. You can click on a green button to undo that move.\n 5. Try to place as many trolls as possible, and as fast as possible.\n \
         \n Note that no 2 trolls can share the same row, column, or diagonal. If you put a troll where it is not allowed, the game ends immediately.\n \
         \n You can always click on \"Finish the board for me!\" to autofill the rest of the cells as good as possible. The autofilled trolls will turn red. However, clicking on this button will also make the current game end immediately, and the result will not be saved. \n Good luck!"
   tkinter.messagebox.showinfo(title="Game Rules", message=rules)

   #Set label-text:
   labelVar.set("Write an integer larger than 3 and less than 10: ")

   #Set position of textLabel:
   textLabel.place(x=windowWidth//2-400,y=windowHeight//2-200)

   #Set position for inputBox
   inputBox.place(x=windowWidth//2,y=windowHeight//2-50)

   #Set position for sizeSelectionButton
   sizeSelectionButton.place(x=windowWidth//2,y=windowHeight//2+40) 

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

buttons=[]     #An array keeping all relevant TrollButtons
currGrid=[]    #A grid tracking the current state of the game
timer=[]       #An array keeping track of time stamps

startMenu()
window.mainloop()
