import tkinter as T
from setting import SET
import calendar as Clndr
from datetime import date


class handler:
    def __init__(self, user_interface: object) -> None:
        self.UI = user_interface
        self.cal_dict = {key : value + 1 for value, key in enumerate(SET.month_names)}
        self.selected_date_top = SET.today
        self.selected_date_btm = SET.today

    def _days(self, year = SET.today.year, month = SET.today.month):
        total_days = Clndr.monthrange(year, month)[1]
        return list(range(1, total_days + 1))
    
    

    def get_days_top(self):
        month = self.cal_dict[ self.UI.Top_month.get() ]
        year = self.UI.Top_year.get()

        month_days = self._days(year, month)
        self.UI.dropDown_from_day.config(values = month_days)
        if not self.UI.Top_day.get() in month_days:
            self.UI.Top_day.set(month_days[-1])
        day = self.UI.Top_day.get()
        self.selected_date_top = date(year, month, day)
        self.CalculateDate()
    
    def get_days_btm(self):
        month = self.cal_dict[ self.UI.Btm_month.get() ]
        year = self.UI.Btm_year.get()

        month_days = self._days(year, month)
        self.UI.dropDown_to_day.config(values = month_days)
        if not self.UI.Btm_day.get() in month_days:
            self.UI.Btm_day.set(month_days[-1])
        day = self.UI.Btm_day.get()
        self.selected_date_btm = date(year, month, day)
        self.CalculateDate()
        
    
    def CorrectDay(self, key):
        if key == 'top':
            self.get_days_top()
            self.CalculateDate()
        else:
            self.get_days_btm()
            self.CalculateDate()


    def CalculateDate(self):
        if not self.selected_date_top == self.selected_date_btm:
            self.difference = abs(self.selected_date_top - self.selected_date_btm).days
            years = self.difference // 365
            months = (self.difference - (years * 365)) // 12
            weeks = (self.difference - (years * 365) - (months * 12)) // 7
            days = (self.difference - (years * 365) - (months * 12))
            self.UI.label_result.config(text = f'{years} years {months} months {weeks} weeks {days} days')
            self.UI.label_days.config(text = str(self.difference) + ' days')
        else:
            self.UI.label_result.config(text = 'Same Date')
            self.UI.label_days.config(text = '')
        
    