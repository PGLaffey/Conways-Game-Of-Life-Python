#Purpose: Conway's Game of Life
#Author: Patrick Laffey
#Date: 5/4/2016 -

import time
from tkinter import *
import sys

class __init__():
    def main():
        """Runs the initialization of the program"""
        master = Tk()
        canvas = Canvas(master, width="765", height="615", bg="beige")
        canvas.pack()
        spawn = __init__.generate(master,canvas)
        box = spawn[0]
        alive = spawn[1]
        Button(master,text="Max",command=speedy.maxi,width="20").pack(side='left')
        Button(master,text="Fast",command=speedy.fast,width="20").pack(side='left')
        Button(master,text="Med",command=speedy.medium,width="20").pack(side='left')
        Button(master,text="Slow",command=speedy.slow,width="20").pack(side='left')
        Button(master,text="Min",command=speedy.mini,width="20").pack(side='left')
        master.bind("<Button-1>",lambda event,master=master,canvas=canvas,box=box,alive=alive:__init__.change_alive(event,master,canvas,box,alive))
        master.bind("<Return>", lambda event,master=master,canvas=canvas,box=box,alive=alive:running.start(event,master,canvas,box,alive))
        master.mainloop()

    def generate(master,canvas):
        """Generates the set of boxes and assigns them to variables in the list box"""
        countx = 0
        county = 0
        box = []
        count = 0
        while count < 40:
            box.append([])
            count += 1
        while county < 40:
            while countx < 50:
                box[county].append(canvas.create_rectangle(10+(countx*15),10+(county*15),25+(countx*15),25+(county*15),fill="white",outline="dark grey"))
                countx += 1
            county += 1
            countx = 0
        alive = []
        count = 0
        while count < 40:
            alive.append([])
            count += 1
        countx = 0
        county = 0
        while county < 40:
            while countx < 50:
                alive[county].append(False)
                countx += 1
            county += 1
            countx = 0
        return [box,alive]


    def change_alive(event,master,canvas,box,alive):
        """Change idividial items alive value to or from alive to dead"""
        column = 0
        row = 0
        count = 0
        while row < 40:
            while column < 50:
                if event.y < (31+row*15) and event.y > (10+row*15):
                    if event.x < (31+column*15) and event.x > (10+column*15):
                        if alive[row][column] == False:
                            canvas.itemconfig(box[row][column],fill="black")
                            alive[row][column] = True
                        elif alive[row][column] == True:
                            canvas.itemconfig(box[row][column],fill="white")
                            alive[row][column] = False
                    column += 1
                else:
                    row += 1
            row += 1

class running():
    def start(event,master,canvas,box,alive):
        time.sleep(speed)
        column = 0
        row = 0
        a_neighbours = 0
        count = 0
        neighbour = []
        while count < 40:
            neighbour.append([])
            count += 1
        while row < 40:
            while column < 50:
                a_neighbours = running.neighbours(alive,row,column)
                neighbour[row].append(a_neighbours)
                column += 1
            row += 1
            column = 0
        canvas.update()
        running.move(master,canvas,alive,box,neighbour)

    def move(master,canvas,alive,box,neighbour):
        """checks which cells should be alive and which should be dead after
           one movement cycle and changes their colour accordingly"""
        column = 0
        row = 0
        while row < 40:
            while column < 50:
                if alive[row][column] == True:
                    if neighbour[row][column] < 2:
                        canvas.itemconfig(box[row][column],fill="white")
                    elif neighbour[row][column] > 3:
                        canvas.itemconfig(box[row][column],fill="white")
                elif alive[row][column] == False:
                    if neighbour[row][column] == 3:
                        canvas.itemconfig(box[row][column],fill="black")
                column += 1
            row += 1
            column = 0
        canvas.update()
        running.repopulate(master,canvas,alive,box,neighbour)

    def repopulate(master,canvas,alive,box,neighbour):
        """Changes the living state of cells according to their colour"""
        row = 0
        column = 0
        while row < 40:
            while column < 50:
                if canvas.itemcget(box[row][column],"fill") == "black":
                    alive[row][column] = True
                elif canvas.itemcget(box[row][column],"fill") == "white":
                    alive[row][column] = False
                column += 1
            row += 1
            column = 0
        canvas.update()
        running.start(None,master,canvas,box,alive)

    def neighbours(alive,row,column):
        """Test to find how many alive neighbours an individual alive block has"""
        a_neighbours = 0
        if row != 0 and row != 39 and column != 0 and column != 49:
            if alive[row][column+1] == True:
                a_neighbours += 1
            if alive[row][column-1] == True:
                a_neighbours += 1        
            if alive[row+1][column] == True:
                a_neighbours += 1
            if alive[row-1][column] == True:
                a_neighbours += 1
            if alive[row+1][column+1] == True:
                a_neighbours += 1
            if alive[row-1][column-1] == True:
                a_neighbours += 1
            if alive[row+1][column-1] == True:
                a_neighbours += 1
            if alive[row-1][column+1] == True:
                a_neighbours += 1
        elif row == 0 and column == 0:
            if alive[row][column+1] == True:
                a_neighbours += 1    
            if alive[row+1][column] == True:
                a_neighbours += 1
            if alive[row+1][column+1] == True:
                a_neighbours += 1
        elif row == 0 and column == 49:
            if alive[row][column-1] == True:
                a_neighbours += 1        
            if alive[row+1][column] == True:
                a_neighbours += 1
            if alive[row+1][column-1] == True:
                a_neighbours += 1
        elif row == 39 and column == 49:
            if alive[row][column-1] == True:
                a_neighbours += 1        
            if alive[row-1][column] == True:
                a_neighbours += 1
            if alive[row-1][column-1] == True:
                a_neighbours += 1
        elif row == 39 and column == 0:
            if alive[row][column+1] == True:
                a_neighbours += 1      
            if alive[row-1][column] == True:
                a_neighbours += 1
            if alive[row-1][column+1] == True:
                a_neighbours += 1
        elif row == 0:
            if alive[row][column+1] == True:
                a_neighbours += 1
            if alive[row][column-1] == True:
                a_neighbours += 1        
            if alive[row+1][column] == True:
                a_neighbours += 1
            if alive[row+1][column+1] == True:
                a_neighbours += 1
            if alive[row+1][column-1] == True:
                a_neighbours += 1
        elif row == 39:
            if alive[row][column+1] == True:
                a_neighbours += 1
            if alive[row][column-1] == True:
                a_neighbours += 1        
            if alive[row-1][column] == True:
                a_neighbours += 1
            if alive[row-1][column-1] == True:
                a_neighbours += 1
            if alive[row-1][column+1] == True:
                a_neighbours += 1
        elif column == 0:            
            if alive[row][column+1] == True:
                a_neighbours += 1       
            if alive[row+1][column] == True:
                a_neighbours += 1
            if alive[row-1][column] == True:
                a_neighbours += 1
            if alive[row+1][column+1] == True:
                a_neighbours += 1
            if alive[row-1][column+1] == True:
                a_neighbours += 1
        elif column == 49:
            if alive[row][column-1] == True:
                a_neighbours += 1        
            if alive[row+1][column] == True:
                a_neighbours += 1
            if alive[row-1][column] == True:
                a_neighbours += 1
            if alive[row-1][column-1] == True:
                a_neighbours += 1
            if alive[row+1][column-1] == True:
                a_neighbours += 1               
        return a_neighbours
    #make it run the three that all must follow and then sperate sub routines
    #for each following one to save space, so that the subroutine just needs
    #to be called rather than all the if statements

class speedy():
    def maxi():
        global speed
        speed = 0
    def mini():
        global speed
        speed = 1
    def fast():
        global speed
        speed = 0.1
    def medium():
        global speed
        speed = 0.2
    def slow():
        speed = 0.5

        
speed = 0.2      
__init__.main()
