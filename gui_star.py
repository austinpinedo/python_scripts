#star perfect

import tkinter

class MyGUIStar:
    def __init__(self):
        self.main_window = tkinter.Tk()                         #creating window
        
        self.canvas = tkinter.Canvas(self.main_window, width=500, height=525)           #setting canvas
        
        self.draw_star()            #drawing star

        self.invert_button = tkinter.Button(self.canvas, text='Austin Pinedo', command=self.toggle)         #making button that sends to function toggle
        
        self.canvas.pack()          #packing canvas
        self.invert_button.pack(padx=210, pady=250)                 #putting in middle of star kinda
        
        self.invert = 0                 #making variable 0 so will invert star
        
        tkinter.mainloop()          #looping the window
        
    def draw_star(self):
        
        polygon_list = [250, 0, 325, 175, 500, 175, 350, 300, 425, 525, 250, 400, 75, 525, 150, 300, 0, 175, 175, 175]      #points for polygon
        
        self.star = self.canvas.create_polygon(polygon_list, outline="black", fill="white")         #creating polugon with points 

    def toggle(self):                   #function toggle that send button click to either invert_star() or undo()
        if self.invert == 0:
            self.invert_star()
        else:
            self.undo()

    def invert_star(self):                      #invert colors
        self.canvas.delete(self.star)           #deleting my original star to replace with new star
        
        polygon_list = [250, 0, 325, 175, 500, 175, 350, 300, 425, 525, 250, 400, 75, 525, 150, 300, 0, 175, 175, 175]      #same list
        
        self.star = self.canvas.create_polygon(polygon_list, outline="white", fill="black")         #changing colors
        self.invert_button.configure(text='Austin Pinedo')      #keeping text as name for button
        
        self.invert = 1         #changing variable to 1 to senf back thru toggle

    def undo(self):             #undo to og colors
        self.canvas.delete(self.star)       #deleting previous star
        
        polygon_list = [250, 0, 325, 175, 500, 175, 350, 300, 425, 525, 250, 400, 75, 525, 150, 300, 0, 175, 175, 175] #same
        
        self.star = self.canvas.create_polygon(polygon_list, outline="black", fill="white")     #repeat of before
        self.invert_button.configure(text='Austin Pinedo')
        
        self.invert = 0         #variable to 0 to toggle

if __name__ == '__main__':
    my_gui_star = MyGUIStar()
