from collections import OrderedDict
import os

class SET:
    geometry = '330x250+400+300'
    title = 'Weight Convertor'
    btn_numbers_font = ('Microsoft Sans Serif', 12)
    btn_numbers_color = 'white'
    screen_font = ('Microsoft Sans Serif', '15')
    screen_justify = 'right'
    btn_width = 10
    weight_option = OrderedDict(Tonne = 1000000, Kilogram = 1000, Gram = 1, Milligram = 0.001,
    Microgram = 1e-6, Quintal = 100000, Pound = 453.59237, Ounce = 28.3495231, Carat = 0.2)
    dropDown_primary_dflt = 'Kilogram'
    dropDown_secodary_dflt = 'Gram'
    app_icon_file  = os.path.join(os.path.dirname(__file__), 'images/weight.png')