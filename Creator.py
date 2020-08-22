from tkinter import *
# size = '500x400'
# bgcolor = 'black'
# gui = Tk(bg=bgcolor)
# gui.geometry(size)

preprint = ["from tkinter import *", "size = '500x400'", "bgcolor = 'black'", "textcolor = 'white'", "gui = Tk()", "gui.geometry(size)", "gui.configure(bg=bgcolor)"]
labels = 0
buttons = 0
entry = 0
ask = input('Do you want Labels(Y/n) $')
if ask.lower() == 'y':
    ask = input('How many Labels $ ')
    labels = ask


ask = input('Do you want Buttons(Y/n) $ ')
if ask.lower() == 'y':
    ask = input('How many Buttons $ ')
    buttons = ask


ask = input('Do you want Entrys(Y/n) $ ')
if ask.lower() == 'y':
    ask = input('How many Entrys $ ')
    entry = ask

print()

for x in preprint:
    print(x)

if int(labels) >=1:
    for x in range(0, int(labels)):
        print("Label(text='', fg=textcolor, bg=bgcolor).pack()")

if int(buttons) >=  1:
    for x in range(0, int(buttons)):
        print("Button(text='', fg=textcolor, bg=bgcolor).pack()")

if int(entry) >= 1:
    for x in range(0, int(entry)):
        print("Entry(text='', fg=textcolor, bg=bgcolor).pack()")

print('mainloop()')
