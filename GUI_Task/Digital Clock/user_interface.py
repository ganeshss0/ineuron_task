import tkinter as T
import tkinter.ttk as ttk
from handlr import handle


class interface(T.Tk):
    def __init__(self, *args, **kwargs):
        T.Tk.__init__(self, *args, **kwargs)
        self.title('Clock')
        self.geometry('400x400')
        self.resizable(False,False)
        
        self.handle = handle(self)
        
        self.__Frames()
        self.__canvas(self.frame_canvas)
        self.__Clock(self.frame_clock)
        self.__Gridit()
        self.handle.UpdateTime()

    def __Frames(self):
        self.frame_canvas = T.Frame(self)
        self.frame_clock = T.Frame(self)

    def __canvas(self, frame):
        self.canvas = T.Canvas(frame, width = 400, height = 400)
        self.canvas.create_oval(50, 50, 350, 350,  width = 18, outline = '#ff0000')
    
    def __Clock(self, frame):
        self.clock_time = ttk.Label(frame, font = ('Microsoft Sans Serif', 30, 'bold'))
        self.clock_date = ttk.Label(frame, font = ('Segoe UI', 20))
    
    def __Gridit(self):
        self.frame_canvas.place(x = 0, y = 0)
        self.frame_clock.place(x = 80, y = 160)

        self.canvas.grid(row = 0)

        self.clock_time.grid(row = 0)
        self.clock_date.grid(row = 1)