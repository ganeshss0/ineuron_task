import tkinter as T
from setting import SET

class handler:
    def __init__(self, user_interface: object):
        self.UI = user_interface



    def ButtonInput(self, key: str):
        if key in '.0':
            self.HandleZeroDot(key)
        else:
            self.UI.entry_primary.insert(T.END, key)
    
    def ClearEntryPrimary(self):
        self.UI.entry_primary.delete(0, T.END)

    def ClearEntrySecondary(self):
        self.UI.secondaryvar.set('')

    def backspace(self):
        if (Number := self.UI.entry_primary.get()) != '':
            Number = Number[:-1]
            self.ClearEntryPrimary()
            self.UI.entry_primary.insert(0, Number)
        
    def HandleZeroDot(self, key: str):
        Number = self.UI.entry_primary.get()
        if Number:
            dot_count = Number.count('.')
            if key == '0' and dot_count == 1 :
                self.UI.entry_primary.insert(T.END, key)
            elif key == '.' and dot_count == 0:
                self.UI.entry_primary.insert(T.END, key)
        else:
            if key == '0':
                enter  = '0'
            elif key == '.':
                enter = '0.'
            self.UI.entry_primary.insert(T.END, enter)
        
    def KeyPress(self, event):
        if not self.UI.entry_primary.get():
            self.UI.entry_primary.insert(T.END, '0.')
    
    def reset(self):
        self.ClearEntryPrimary()
        self.ClearEntrySecondary()

    def OptionSelectedTOP(self, option):
        if (Number := self.UI.entry_primary.get()) != '':
            Number = float(Number)
            converted_number = self.convertor(Number, option, self.UI.optionScnDflt.get())
            self.ClearEntrySecondary()
            self.UI.secondaryvar.set(converted_number)

    def OptionSelectedBTM(self, option):
        if (Number := self.UI.entry_primary.get()) != '':
            Number = float(Number)
            converted_number = self.convertor(Number, self.UI.optionPriDflt.get(), option)
            self.ClearEntrySecondary()
            self.UI.secondaryvar.set(converted_number)
        
    
    def convertor(self, number: float, name, convert):
        grams = SET.weight_option[name] * number
        convert_grams = grams / SET.weight_option[convert]
        return str(convert_grams)

    def validate_primary(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                Number = float(value_if_allowed)
                converted_number = self.convertor(Number, self.UI.optionPriDflt.get(), self.UI.optionScnDflt.get())
                self.ClearEntrySecondary()
                self.UI.secondaryvar.set(converted_number)
                return True              
            except ValueError:
                return False
        else:
            self.ClearEntryPrimary()
            self.ClearEntrySecondary()
            return False
    

        
    def vcmd(self, frame: object, validator):
        return frame.register(validator), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'