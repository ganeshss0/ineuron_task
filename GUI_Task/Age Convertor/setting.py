import numpy as np
import datetime
import calendar as Clndr

class SET:
    title = 'Date Calculator'
    geometry = '325x400'
    min_year = 1970
    max_year = 2101
    year = np.arange(min_year, max_year).tolist()
    today = datetime.date.today()
    current_month = lambda x = today.month: Clndr.month_abbr[x]
    month_names = Clndr.month_abbr[1:]
    font_1 = 'Microsoft Sans Serif', 12
    font_2 = 'Segoe UI', 15,
