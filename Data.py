"""
creator: MJ Naderi
Email: mnaderi@okstate.edu
"""
import pandas as pd
from io import StringIO
import re


class Data:
    def __init__(self, input_data=None):
        self.input_data_name = input_data
        self.read_data()


    def read_data(self):

        with open(self.input_data_name, 'r') as file:
            lines = file.readlines()
            lines = [line.lstrip() for line in lines if len(line.split()) != 0]
            for i in range(len(lines)):
                if re.sub(r'[^0-9]', '', lines[i].split()[0]).isdigit():
                    firstRecord = i
                    break
            for i in range(firstRecord, (len(lines))):
                if re.sub(r'[^0-9]', '', lines[i].split()[0]).isdigit():
                    lastRecord = i

        if self.input_data_name == "w_data.dat":
            columns = lines[firstRecord - 1]

            allLinesString = ""
            for i in range(firstRecord, lastRecord + 1):
                if re.sub(r'[^0-9]', '', lines[i].split()[0]).isdigit():
                    allLinesString += lines[i]

            self.df = pd.read_fwf(StringIO(columns + allLinesString))

        if self.input_data_name == "soccer.dat":
            columns_list = lines[firstRecord - 1].split()
            lines = lines[firstRecord:lastRecord+1]

            for i in range(len(lines)):
                lines[i] = lines[i].replace("-", "")
                lines[i] = lines[i].split()
                lines[i] =lines[i][1:]

            self.df = pd.DataFrame(lines, columns=columns_list)
            self.df.dropna(how='all',inplace=True)

    def find_smallest_temperature_spread(self):
        self.df["temperature_spread"] = self.df["MxT"].apply(lambda x: int(re.sub(r'[^0-9]', '', x))) - \
                                        self.df["MnT"].apply(lambda x: int(re.sub(r'[^0-9]', '', x)))
        print("days with maximum temperature spread:\n",
              self.df.loc[self.df["temperature_spread"] == self.df["temperature_spread"].max(), "Dy"].tolist())

    def find_team_with_smallest_difference_in_goals(self):
        self.df["smallest_difference_in_goals"] = self.df["F"].apply(lambda x: int(x)) - \
                                        self.df["A"].apply(lambda x: int(x))
        print("smallest_difference_in_goals:\n",
              self.df.loc[self.df["smallest_difference_in_goals"] == self.df["smallest_difference_in_goals"].min(), "Team"].tolist())

