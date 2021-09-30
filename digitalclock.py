from tkinter import Tk ,Label


window =Tk()
window.title("digital clock")
window.geometry("600x600")
window.configure(bg="pink")
label =Label(window,font=("aerial darkblack ",79,'bold'),text="welcome!",bg="pink",fg="white")
label.pack(pady=100)
window.mainloop()