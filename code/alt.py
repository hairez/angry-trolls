import tkinter


top = tkinter.Tk()
top.geometry("900x900")
def helloCallBack():
   msg=tkinter.messagebox.showinfo( "Hello Python", "Hello World")



buttons=[]
for i in range(1,4):
   for j in range(1,4):
      buttons.append(tkinter.Button(top, text ="Put troll here!", command = helloCallBack))
      buttons[-1].place(x=150*i,y=50*j)

top.mainloop()