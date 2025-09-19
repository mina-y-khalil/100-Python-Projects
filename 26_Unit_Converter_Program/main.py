import tkinter

#creating window
window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)



#label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24 , "bold"))
my_label.pack()  #this will place it in the center of the program this pack is important


# to keep the window open and this has to be in the very end of the program
window.mainloop()