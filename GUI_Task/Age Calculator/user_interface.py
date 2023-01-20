import tkinter as T
import tkinter.ttk as ttk
from setting import SET
from event_handle import handler


class interface(T.Tk):
    def __init__(self, *args, **kwargs):
        T.Tk.__init__(self, *args, **kwargs)
        self.geometry(SET.geometry)
        self.title(SET.title)
        self.resizable(False, False)
        self.handle = handler(self)
        self.__Frame()
        self.__Labels()
        self.__Variables(self.frame_date)
        self.__DropDowns(self.frame_date)
        self.__GridIt()
        self.__binder()
        
        
    def __Frame(self):
        self.frame_date = T.Frame(self)
        self.frame_display = T.Frame(self)

    def __Labels(self):
        self.label_header = ttk.Label(self, text = 'Difference between dates', font = SET.font_2)
        self.label_from = ttk.Label(self.frame_date, text = 'From')
        self.label_to = ttk.Label(self.frame_date, text = 'To')
        self.label_diff = ttk.Label(self.frame_display, text = 'Difference', font = SET.font_1)
        self.label_result = ttk.Label(self.frame_display, text = 'Same Date', font = SET.font_2)
        self.label_days = ttk.Label(self.frame_display)
        

    def __DropDowns(self, frame):
        argument = dict(master = frame, justify = 'left', width = 8, state = 'readonly')

        self.dropDown_from_year = ttk.Combobox(textvariable = self.Top_year, values = SET.year, **argument)
        self.dropDown_from_month = ttk.Combobox(textvariable = self.Top_month, values = SET.month_names, **argument)
        self.dropDown_from_day = ttk.Combobox(textvariable = self.Top_day, values = self.handle._days(), postcommand = self.handle.get_days_top,   **argument)

        self.dropDown_to_year = ttk.Combobox(textvariable = self.Btm_year, values = SET.year, **argument)
        self.dropDown_to_month = ttk.Combobox(textvariable = self.Btm_month, values = SET.month_names, **argument)
        self.dropDown_to_day = ttk.Combobox(textvariable = self.Btm_day, values = self.handle._days(), postcommand = self.handle.get_days_btm, **argument)
        
        
    def __Variables(self, frame):
        self.Top_year = T.IntVar(frame)
        self.Top_year.set(SET.today.year)

        self.Top_month = T.StringVar(frame)
        self.Top_month.set(SET.current_month())

        self.Top_day = T.IntVar(frame)
        self.Top_day.set(SET.today.day)

        self.Btm_year = T.IntVar(frame)
        self.Btm_year.set(SET.today.year)

        self.Btm_month = T.StringVar(frame)
        self.Btm_month.set(SET.current_month())

        self.Btm_day = T.IntVar(frame)
        self.Btm_day.set(SET.today.day)
    
    def __binder(self):
        self.dropDown_from_year.bind('<<ComboboxSelected>>', lambda evnt, key = 'top': self.handle.CorrectDay(key))
        self.dropDown_from_month.bind('<<ComboboxSelected>>', lambda evnt, key = 'top': self.handle.CorrectDay(key))
        self.dropDown_from_day.bind('<<ComboboxSelected>>', lambda evnt, key = 'top': self.handle.CorrectDay(key))
        self.dropDown_to_year.bind('<<ComboboxSelected>>', lambda evnt, key = 'btm': self.handle.CorrectDay(key))
        self.dropDown_to_month.bind('<<ComboboxSelected>>', lambda evnt, key = 'btm': self.handle.CorrectDay(key))
        self.dropDown_to_day.bind('<<ComboboxSelected>>', lambda evnt, key = 'btm': self.handle.CorrectDay(key))

    
    def __GridIt(self):
        self.label_header.place(x = 10, y = 2)
        self.frame_date.place(x = 10, y = 50)
        self.frame_display.place(x = 10, y = 150)
        
        self.label_from.grid(row = 1, sticky = T.W, columnspan = 3)
        self.dropDown_from_day.grid(row = 2, column = 0)
        self.dropDown_from_month.grid(row = 2, column = 1)
        self.dropDown_from_year.grid(row = 2, column = 2)

        self.label_to.grid(row = 3, columnspan = 3, sticky = T.W)
        self.dropDown_to_day.grid(row = 4, column = 0)
        self.dropDown_to_month.grid(row = 4, column = 1)
        self.dropDown_to_year.grid(row = 4, column = 2)

        self.label_diff.grid(row = 0, sticky = T.W, column = 0)
        self.label_result.grid(row = 1)
        self.label_days.grid(row = 2, sticky = T.W, column = 0)