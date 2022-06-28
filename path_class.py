import pandas as pd


class Path:
    startpoint = ''
    endpoint = ''
    group = ''
    type = ''
    data_required = ''
    data_arrival = ''
    slack = ''

    dataframe = pd.DataFrame(columns=['Cap', 'Slew', 'Delay', 'Time', 'Arrow?', 'Description'])

    def __init__(self):
        self.startpoint = 'Nan'
        self.endpoint = 'Nan'
        self.group = 'Nan'
        self.type = 'Nan'
        self.dataframe = 'Nan'
        self.data_required = 'Nan'
        self.data_arrival = 'Nan'
        self.slack = 'Nan'

    def __init__(self, start, end, group, type, data, data_required, data_arrival, slack):
        self.startpoint = start
        self.endpoint = end
        self.group = group
        self.type = type
        self.dataframe = data
        self.data_required = data_required
        self.data_arrival = data_arrival
        self.slack = slack
