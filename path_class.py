import pandas as pd

class Path:
    startpoint = ''
    endpoint = ''
    group = ''
    type = ''

    dataframe = pd.DataFrame(columns=['Cap', 'Slew', 'Delay', 'Time', 'Arrow?', 'Description'])

    def __init__(self):
        self.startpoint = 'Nan'
        self.endpoint = 'Nan'
        self.group = 'Nan'
        self.type = 'Nan'
        self.dataframe = 'Nan'

    def __int__(self, start, end, group, type, data):
        self.startpoint = start
        self.endpoint = end
        self.group = group
        self.type = type
        self.dataframe = data
    