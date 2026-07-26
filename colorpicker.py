from tkinter import Tk,colorchooser
root=Tk()
root.withdraw()
color=colorchooser.askcolor(title="Choose a color")
print("RGB value:",color[0])
print("Hex value:",color[1])