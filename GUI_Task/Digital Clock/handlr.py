from matplotlib import colors
import datetime
import numpy as np

class handle:
    def __init__(self, user_interface: object):
        self.UI = user_interface

    def formatter(self, time):
        if (hour := time.hour) > 12:
            hour -= 12
            meridian = 'PM'
        else:
            meridian = 'AM'
        
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
        return hour + time.strftime(':%M:%S ') + meridian

    def __getTime(self):
        current = datetime.datetime.now()
        return self.formatter(current), current.strftime('%d-%h-%Y')

    
    def UpdateTime(self):
        date_time = self.__getTime()
        self.UI.clock_time.config(text = date_time[0])
        self.UI.clock_date.config(text = date_time[1])
       
        self.UI.canvas.itemconfig(1, outline = colors.to_hex(self.get_color()))
        self.UI.after(1000, self.UpdateTime)

    def get_color(self):
        return np.random.rand(3).tolist()
        