import tkinter as T
import tkinter.ttk as ttk
from setting import SET
from event_handler import handler

class interface(T.Tk):
    def __init__(self, *args, **kwargs):
        T.Tk.__init__(self, *args, **kwargs)
        self.handle = handler(self)
        self.geometry(SET.geometry)
        self.title(SET.title)
        app_icon = T.PhotoImage(file = SET.app_icon_file)
        self.iconphoto(True, app_icon)
        self.resizable(False, False)

        self.__frame()
        self.__display(self.frame_display)
        self.__dropDownList(self.frame_dropDown)
        self.__buttons(self.frame_button)
        self.__gridWidget()
        self.bind('.', self.handle.KeyPress)

    def __frame(self):
        self.frame_dropDown = ttk.Frame(self)
        self.frame_display = ttk.Frame(self)
        self.frame_button = ttk.Frame(self)

    def __display(self, frame):
        ttk.Style().configure('TEntry', width = 15)
        entry_argument = dict(master = frame, font = SET.screen_font, justify = SET.screen_justify)

        validate = self.handle.vcmd(frame, self.handle.validate_primary)
        self.secondaryvar = T.StringVar(frame)
        self.entry_primary = ttk.Entry(validate = 'key', validatecommand= validate, **entry_argument)
        self.entry_secondary = ttk.Entry(state = 'readonly', textvariable=self.secondaryvar, **entry_argument)
        self.entry_primary.focus()

    def __dropDownList(self, frame):
        self.optionPriDflt = T.StringVar(frame)
        self.optionScnDflt = T.StringVar(frame)


        self.option_primary = ttk.OptionMenu(frame, self.optionPriDflt, SET.dropDown_primary_dflt,command = self.handle.OptionSelectedTOP, *SET.weight_option)

        self.option_secondary = ttk.OptionMenu(frame, self.optionScnDflt, SET.dropDown_secodary_dflt, command = self.handle.OptionSelectedBTM, *SET.weight_option)
    
    def __buttons(self, frame):
        ttk.Style().configure('TButton', width  = 10)
        btn_argument = dict(master = frame)

        self.btn_1 = ttk.Button(text = '1', command = lambda key = '1': self.handle.ButtonInput(key), **btn_argument)
        self.btn_2 = ttk.Button(text = '2', command = lambda key = '2': self.handle.ButtonInput(key), **btn_argument)
        self.btn_3 = ttk.Button(text = '3', command = lambda key = '3': self.handle.ButtonInput(key), **btn_argument)
        self.btn_4 = ttk.Button(text = '4', command = lambda key = '4': self.handle.ButtonInput(key), **btn_argument)
        self.btn_5 = ttk.Button(text = '5', command = lambda key = '5': self.handle.ButtonInput(key), **btn_argument)
        self.btn_6 = ttk.Button(text = '6', command = lambda key = '6': self.handle.ButtonInput(key), **btn_argument)
        self.btn_7 = ttk.Button(text = '7', command = lambda key = '7': self.handle.ButtonInput(key), **btn_argument)
        self.btn_8 = ttk.Button(text = '8', command = lambda key = '8': self.handle.ButtonInput(key), **btn_argument)
        self.btn_9 = ttk.Button(text = '9', command = lambda key = '9': self.handle.ButtonInput(key), **btn_argument)
        self.btn_dt = ttk.Button(text = '.', command = lambda key = '.': self.handle.ButtonInput(key), **btn_argument)
        self.btn_0 = ttk.Button(text = '0', command = lambda key = '0': self.handle.ButtonInput(key), **btn_argument)
        self.btn_bk = ttk.Button(text = '<<', command = self.handle.backspace, **btn_argument)
        self.btn_ac = ttk.Button(text = 'AC', command = self.handle.reset, **btn_argument)
    

    
    def __gridWidget(self):
        self.frame_dropDown.place(x = 5, y = 20)
        self.frame_display.place(x = 98, y = 20)
        self.frame_button.place(x = 60, y = 110)

        self.option_primary.grid(row = 0)
        self.option_secondary.grid(row = 1)

        self.entry_primary.grid(row = 0)
        self.entry_secondary.grid(row = 1)

        self.btn_ac.grid(row = 0, column = 0)
        self.btn_bk.grid(row = 0, column = 2)

        self.btn_7.grid(row = 1, column = 0)
        self.btn_8.grid(row = 1, column = 1)
        self.btn_9.grid(row = 1, column = 2)

        self.btn_4.grid(row = 2, column = 0)
        self.btn_5.grid(row = 2, column = 1)
        self.btn_6.grid(row = 2, column = 2)

        self.btn_1.grid(row = 3, column = 0)
        self.btn_2.grid(row = 3, column = 1)
        self.btn_3.grid(row = 3, column = 2)

        self.btn_0.grid(row = 4, column = 1)
        self.btn_dt.grid(row = 4, column = 2)
    



