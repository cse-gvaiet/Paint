from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):
   
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title("My_Paint")
        photo=PhotoImage(file="pen.png")
        photo1=PhotoImage(file="brush.png")
        photo2=PhotoImage(file="palette.png")
        photo3=PhotoImage(file="eraser.png")
        photo4=PhotoImage(file="rec.png")
        photo5=PhotoImage(file="squ.png")
        photo6=PhotoImage(file="cir.png")
        photo7=PhotoImage(file="line.png")
        self.pen_button = Button(self.root, image=photo , command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root,image=photo1 , command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root,image=photo2 , command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root,image=photo3 , command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.cicbutton = Button(self.root,image=photo4,command=self.rect)
        self.cicbutton .grid(row=3, column=0)

        self.cicbutton = Button(self.root,image=photo5 ,command=self.square)
        self.cicbutton .grid(row=3, column=1)

        self.cicbutton = Button(self.root,image=photo6 ,command=self.circle)
        self.cicbutton .grid(row=3, column=2)

        self.cicbutton = Button(self.root,image=photo7  ,command=self.line)
        self.cicbutton .grid(row=3, column=3)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=7, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)
        
    
    def rect(self):
        canvas = self.c
        a=canvas.create_rectangle(200, 100, 300, 300, width=3)
        print(a)

    def square(self):
        canvas = self.c
        b=canvas.create_rectangle(200, 200, 300, 300, width=3)
        print(b)

    def circle(self):
        canvas = self.c
        c=canvas.create_oval(224,71, 278, 121,   width=4)
        print(c)
        
    def line(self):
        canvas = self.c
        a=canvas.create_line(200, 200, 300, 300, width=5)
        print(a)
        

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
