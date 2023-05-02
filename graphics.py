from tkinter import Tk, BOTH, Canvas

Class Window:

    def __init__(self,width,height):
        self.__root = Tk()
        self.__title = sekf.__root.title("Maze Solver")
        self.__Canvas = Canvas(self.__root,bg = "white",width,height)
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
        m
        
        

   