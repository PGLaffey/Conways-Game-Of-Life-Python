#Purpose: Conway's Game of Life
#Author: Patrick Laffey
#Date: 5/4/2016 -

import time
from tkinter import *

class __init__():
    def main():
        """Runs the initialization of the program"""
        master = Tk()
        canvas = Canvas(master, width="270", height="270", bg="beige")
        canvas.pack()
        spawn = __init__.generate(master,canvas)
        box = spawn[0]
        alive = spawn[1]
        master.bind("<Button-1>",lambda event,master=master,canvas=canvas,box=box,alive=alive:__init__.change_alive(event,master,canvas,box,alive))
        master.mainloop()

    def generate(master,canvas):
        """Generates the set of boxes and assigns them to variables in the list box"""
        countx = 0
        county = 0
        box = [[],[],[],[],[]]
        while county < 5:
            while countx < 5:
                box[county].append(canvas.create_rectangle(10+(countx*50),10+(county*50),60+(countx*50),60+(county*50),fill="white",outline="dark grey"))
                countx += 1
            county += 1
            countx = 0
        alive = [[],[],[],[],[]]
        countx = 0
        county = 0
        while county < 5:
            while countx < 5:
                alive[county].append(False)
                countx += 1
            county += 1
            countx = 0
        return [box,alive]


    def change_alive(event,master,canvas,box,alive):
        column = 0
        row = 0
        count = 0
        while row < 5:
            while column < 5:
                if event.y < (61+row*50) and event.y > (10+row*50):
                    if event.x < (61+column*50) and event.x > (10+column*50):
                        if alive[row][column] == False:
                            canvas.itemconfig(box[row][column],fill="black")
                            alive[row][column] = True
                        elif alive[row][column] == True:
                            canvas.itemconfig(box[row][column],fill="white")
                            alive[row][column] = False
                        else:
                            canvas.itemconfig(box[row][column],fill="cyan")
                    column += 1
                else:
                    row += 1
            row += 1

                
#lambda event,username_entry=username_entry,password_entry=password_entry:blazin.logon(username_entry,password_entry)
        
__init__.main()
