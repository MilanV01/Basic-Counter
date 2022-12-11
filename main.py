from cProfile import label
from tkinter import *

# create the main window
root = Tk()
root.title("RainCounter")

root.geometry("300x200")
root.attributes("-topmost", True)
counter = 0
def increment():
  global counter
  counter += 1
  count_label["text"] = f"Count: {counter}"
def restart():
  global counter
  counter = 0
  count_label["text"] = f"Count: {counter}"
button = Button(root, text="Increment", command=increment)
button.pack()
restart_button = Button(root, text="Restart", command=restart)
count_label = Label(root, text=f"Count: {counter}")
count_label["font"] = ("Arial", 24)
count_label.pack()
restart_button.pack(side=BOTTOM)
root.mainloop()
