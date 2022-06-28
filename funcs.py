import pandas as pd
import path_class

def parse_the_line(line):
    print(line)

def parse(file_name):
    file = open(file_name, mode="rt")
    just_a_list = []
    cells = []
    parsed_cells = []
    separator = "---------------------------------------------------------------------------------------\n"

    for line in file:
        just_a_list.append(line)

    indexes = [i for i, ltr in enumerate(just_a_list) if ltr == separator]

    for i in range(0, len(indexes) - 2, 3):
        cells.append(just_a_list[(indexes[i] - 6):(indexes[i + 2] + 2)])

    for i in range(0, len(cells)):
        startpoint = cells[i][0].split()[1]
        endpoint = cells[i][1].split()[1]
        pathgroup = cells[i][2].split()[1]
        pathtype = cells[i][3].split()[1]
        indexes = [i for i, ltr in enumerate(cells[i]) if ltr == separator]

        for j in range(indexes[1] - indexes[0]):
            parse_the_line(cells[i][j])

        data_req = cells[i][indexes[2] - 2].split()[0]
        data_arr = cells[i][indexes[2] - 1].split()[0]

        slack = cells[i][indexes[2] + 1].split()[0]

        parsed_cells.append(path_class.Path(startpoint, endpoint, pathgroup, pathtype,' ', data_req, data_arr, slack))

    return parsed_cells

