import tkinter
from tkinter import messagebox

class trollButton:
   def __init__(self,currX,currY):
      self.button = tkinter.Button(window, text ="Put troll here!", command = self.disableButton)     
      self.button.place(x=currX,y=currY) 

   def disableButton(self):
      #TODO add picture of troll in the same spot
      history.append(self.button)
      self.button['state'] = tkinter.DISABLED

      
      undoButton['state'] = tkinter.NORMAL #enable the undo button
   
   def enableButton(self):
      self.button['state'] = tkinter.NORMAL

      if not history:
         undoButton['state'] = tkinter.DISABLED #disable the undo button if there is nothing to undo


window = tkinter.Tk() #initialize window
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
history=[]     #history over the users recent moves
buttons=[]

#creating 3x3 buttons TODO make it take in an input n
for i in range(1,4):
   for j in range(1,4):
      buttons.append(trollButton(150*i,50*j)) #TODO put the buttons between 0 and screenheight-200

def undoLastMove():
   #TODO add this feature
   return

undoButton = tkinter.Button(window, text ="Undo last move", command = undoLastMove)   
undoButton.place(x=50,y=window.winfo_screenheight()-200) 
undoButton['state'] = tkinter.DISABLED
#winfo_width() 
#winfo_screenwidth()




#trying the enableButton function:
while 0:
   if input()=="NO":
      buttons[-1].enableButton()
   else:
      print("okay")
      print(history)


window.mainloop()