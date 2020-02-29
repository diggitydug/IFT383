#!/usr/bin/python

#=================================================================================

#IFT383 Extra Credit Assignment
#Spring 2020 Session A

"""
IMPORTANT NOTE: This python was written on a windows computer using a standard installation
of python 3.7.4. While the installation is standard the application uses the Tkinter libraries
to create a GUI which are included in most installations of Python including those from the official site, but not all.
The ASU general server does not have Tkinter installed on it, and therefore will not run on the ASU General Server
however a host windows/linux machine with a default install of python is able to run the application with no problems.
"""

#primary source for all things gui: https://docs.python.org/3/library/tkinter.html as well as directly linked sites
#=================================================================================

#imports the necessary libraries to create a GUI
from tkinter import *
from tkinter.colorchooser import askcolor


class Shapes(object):

    #Sets some default variables
    DEFAULT_COLOR = 'black'
    stype = 'Ellipse'
    color = DEFAULT_COLOR
    bordercol = DEFAULT_COLOR
    borderw = 0

    def __init__(self):

        #creates the container that holds all of the tkinter elements
        self.root = Tk()
        self.root.title("Shape Drawing - IFT383 Python OOP EC")

        #creates monitorable variables for the check boxes
        self.hweq = IntVar()
        self.centered = IntVar(value=1)

        self.hweqques = 'Length & Width Equal?' #Text for a label
        self.errorText = StringVar()

        #label for spacing
        Label(self.root, text = '                      ').grid(row = 1, column = 1)

        #declarations used to create drop down menu
        self.stype = StringVar(self.root)
        self.stypechoices = {'Ellipse', 'Rectangle'}
        self.stype.set('Ellipse')
        Label(self.root, text = "Choose a Shape to Draw").grid(row=0, column = 0, columnspan = 2)
        self.shape_dropdown = OptionMenu(self.root, self.stype, *self.stypechoices)
        self.shape_dropdown.grid(row=1, column=0, columnspan = 2)

        #Creates width entry box
        Label(self.root, text = 'Width: ').grid(row = 6, column = 0)
        self.width = Entry(self.root, width = 5)
        self.width.insert(0,'100')                   #writes in a default value
        self.width.grid(row = 6, column = 1)

        #Declaration of checkbox that sets shape to be square
        Checkbutton(self.root, text = self.hweqques, variable=self.hweq).grid(row = 7, column = 0, sticky= 'w', columnspan = 2)

        #creates checkbox that centers shape
        Checkbutton(self.root, text = "Centered?", variable = self.centered).grid(row = 10, column = 0, sticky = 'w', columnspan = 2)

        #Creates height entry box
        Label(self.root, text = 'Height: ').grid(row = 8, column = 0)
        self.height = Entry(self.root, width = 5)
        self.height.insert(0,'100')                   #writes in a default value
        self.height.grid(row = 8, column = 1)

        #adds the draw and clear buttons
        self.draw_buttom = Button(self.root, text='Draw', command = self.draw, width = 20)
        self.draw_buttom.grid(row=27, column=0, columnspan = 2)
        self.clear_button = Button(self.root, text = 'Clear', command = self.clear, width = 20)
        self.clear_button.grid(row = 28, column = 0, columnspan = 2)

        #Creates the buttons to click to change color of the fill and border
        Label(self.root, text = "Fill Color: ").grid(row=4, column = 0)
        self.color_button = Button(self.root, text = '          ', bg = self.color, command = self.choose_color)
        self.color_button.grid(row = 4, column = 1)
        Label(self.root, text = "Border Color: ").grid(row=5, column = 0)
        self.bcolor_button = Button(self.root, text = '          ', bg = self.bordercol, command = self.choose_bcolor)
        self.bcolor_button.grid(row = 5, column = 1)

        #creates an entry box for the border width
        Label(self.root, text = 'Border Width: ').grid(row = 9, column = 0)
        self.borderw = Entry(self.root, width = 5)
        self.borderw.insert(0,'0')
        self.borderw.grid(row = 9, column = 1)

        #declares the canvas that shapes will be drawn on
        self.c = Canvas(self.root, bg='white', width=602, height=602)
        self.c.grid(row=0, rowspan=30, column=3)

        #creates and hides dimension error label
        self.dim_error = Label(self.root, fg='red',text = 'Dimension Error: Must be \npositive integer and\nless than 600')
        self.dim_error.grid(row= 29, column = 0, columnspan = 2)
        self.dim_error.grid_remove()

        #Creates x position entry box
        Label(self.root, text = 'X-Position: ').grid(row = 11, column = 0)
        self.xpos = Entry(self.root, width = 5, state = DISABLED)
        self.xpos.grid(row = 11, column = 1)

        #Creates y position entry box
        Label(self.root, text = 'Y-Position: ').grid(row = 12, column = 0)
        self.ypos = Entry(self.root, width = 5, state = DISABLED)
        self.ypos.grid(row = 12, column = 1)

        #listens for the box that makes the shape square to be clicked
        self.hweq.trace('w', self.square)

        #listens for the checkbox to determine if the shape is centered or not
        self.centered.trace('w', self.center)

        #displays the GUI
        self.root.mainloop()

    #This function verifies the input of the boxes, and then draws the shapes based on the options selected
    def draw(self):

        shape = self.stype.get()

        #Checks if the length and width are valid displays error if not
        if(len(self.width.get()) != 0 and int(self.width.get()) <= 600):
            width = int(self.width.get())
        else:
            self.dim_error.grid()
            return
        
        #checks if square button is checked and sets height and width appropriately
        if (self.hweq.get() == 1):
            height = width
        elif (len(self.height.get()) != 0 and int(self.height.get()) <= 600):
            height  = int(self.height.get())
        else:
            self.dim_error.grid()
            return

        if(self.centered.get() == 1):
            if (shape == 'Ellipse'):
                self.c.create_oval(300-width/2+1, 300 -height/2, 300+width/2+1, 300 +height/2, fill = self.color, outline = self.bordercol, width = int(self.borderw.get()))

            if (shape == 'Rectangle'):
                self.c.create_rectangle(300-width/2, 300 -height/2, 300+width/2, 300 +height/2, fill = self.color, outline = self.bordercol, width = int(self.borderw.get()))
        else:
            x = int(self.xpos.get())
            y = int(self.ypos.get())
            if (shape == 'Ellipse'):
                self.c.create_oval(x+2, y+2, x+width, y+height, fill = self.color, outline = self.bordercol, width = int(self.borderw.get()))

            if (shape == 'Rectangle'):
                self.c.create_rectangle(x+2, y+2, x+width, y+height, fill = self.color, outline = self.bordercol, width = int(self.borderw.get()))



    #called when the centered button is modified, disables/enables position parameters
    def center(self, *args):
        if (self.centered.get() == 0):
            self.xpos.configure(state=NORMAL)
            self.ypos.configure(state=NORMAL)
            self.xpos.insert(0,'0')
            self.ypos.insert(0,'0')
        else:
            self.xpos.delete(0,'end')
            self.ypos.delete(0,'end')
            self.xpos.configure(state=DISABLED)
            self.ypos.configure(state=DISABLED)


    #Called when the make square box is checked, disables height entry
    def square(self, *args):
        if (self.hweq.get() == 1):
            self.height.configure(state = DISABLED)
        else:
            self.height.configure(state = NORMAL)

    #Deletes shape from canvas and removes error message
    def clear(self):
        self.c.delete("all")
        self.dim_error.grid_remove()

    #updates background color on color change button for fill
    def choose_color(self):
        self.color = askcolor(color=self.color)[1]
        self.color_button.configure(bg = self.color)

    #performs same function as choose color for the border
    def choose_bcolor(self):
        self.bordercol = askcolor(color=self.bordercol)[1]
        self.bcolor_button.configure(bg = self.bordercol)

        
#creates the object and opens the gui
if __name__ == '__main__':
    Shapes()