from tkinter import *
import subprocess
import os

orignl_value = subprocess.check_output("brightnessctl g", shell=True, text=True)

max_value = subprocess.check_output("brightnessctl m", shell=True, text=True)
def change_brightness():
	os.system("brightnessctl s {}".format(scale.get()))
	orignl_value = scale.get()
	label["text"] = orignl_value

root = Tk()
root.title('Change Brightness')
v1 = DoubleVar()
scale = Scale(root, variable = v1, from_ = 10, to = int(max_value), orient = HORIZONTAL, length=600)
scale.set(orignl_value)
scale.pack()
label = Label(root, text="Current Value: {}".format(orignl_value))
label.pack()
button = Button(root, text='Save', command = change_brightness )
button.pack()
exit = Button(root, text="Exit", command = quit)
exit.pack()
root.mainloop()
