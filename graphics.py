from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self,width,height):
        self.__root = Tk()
        self.__title = self.__root.title("Maze Solver")
        self.__Canvas = Canvas(self.__root,bg = "white",width=width,height=height)
        self.__Canvas.pack()
        self.__Window_Running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def Redraw(self):
        #we can call this to redraw all the graphics in the window
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__Window_Running =True
        while self.__Window_Running is True:
            self.Redraw()
        print("Window closed ")
        
    def close(self):
        self.Window_Running = False

    def draw_line(self,line,fill_color="black"):
        line.draw(self.__Canvas,fill_color)


class Point:

    def __init__(self,x,y):
        self.x =x
        self.y=y

class Line:

    def __init__(self,p1,p2):
        self.p1 =p1
        self.p2 = p2

    def draw(self,Canvas,fill_color):
        Canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        Canvas.pack(fill = BOTH,expand =1)
        

   