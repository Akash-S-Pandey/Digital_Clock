from tkinter import Tk, Label
from datetime import datetime


window = Tk()
window.title("digital clock")
window.geometry("600x600")
window.configure(bg="red")
label = Label(window, font=("aerial darkblack ",
              79, 'bold'), bg="steelblue", fg="white")
label.pack(pady=100)


def clock():

  time = datetime.now().strftime("%H:%M:%S")
  label.configure(text=time)
  label.after(500, clock)
clock()
window.mainloop()
