#Use this to install:
#pip install tk
#or
#sudo apt install python3-tk
import tkinter
from tkinter import messagebox

#Use this to install:
#pip install screeninfo
import screeninfo #library to get the width and height of user screen.


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


window = tkinter.Tk() #initialize window
windowWidth=screeninfo.get_monitors()[0].width
windowHeight=screeninfo.get_monitors()[0].height
window.geometry(f"{windowWidth}x{windowHeight}")
history=[]     #history over the users recent moves
buttons=[]

def undoLastMove():
   button = history.pop()
   button.enableButton()
   return

undoButton = tkinter.Button(window, text ="Undo last move", command = undoLastMove)   



n=0
def setSize(): #TODO have different funcitons. one for setSize, one for mainMenu and so on
   #TODO move the inputBox creation and sizeSelectionBUtton in this function
   global n
   n = inputBox.get(1.0, "end-1c") 
   #TODO felhantering av n


   inputBox.place_forget()
   sizeSelectionButton.place_forget()
   mainGame(n)



#Creating the textbox for input
inputBox = tkinter.Text(window, height = 5, width = 5) 
inputBox.place(x=windowWidth//2,y=windowHeight//2-50)

#grid layout or pack (flow) layout?
#inputBox.pack() 
  
#Input button
sizeSelectionButton = tkinter.Button(window, text = "Set Board Size",command = setSize)
sizeSelectionButton.place(x=windowWidth//2,y=windowHeight//2+40) 
#sizeSelectionButton.pack() 

def mainGame(n):

   #creating 3x3 buttons 
   #TODO make it take in an input n
   for i in range(1,4):
      for j in range(1,4):
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


window.mainloop()


