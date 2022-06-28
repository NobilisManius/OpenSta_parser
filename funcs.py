import pandas as pd
import pyparsing as pp


def parse(file_name):
    file = open(file_name, mode="rt")
    just_a_list = []
    for line in file:
        if line != '---------------------------------------------------------------------------------------\n':
            just_a_list.append(line)

    for each in just_a_list:
        print(each)
def Print():
    pass