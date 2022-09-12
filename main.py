"""
creator: MJ Naderi
Email: mnaderi@okstate.edu
"""
from Data import Data

def main():
    data_weather = Data(input_data="w_data.dat")
    data_weather.find_smallest_temperature_spread()
    data_soccer = Data(input_data="soccer.dat")
    data_soccer.find_team_with_smallest_difference_in_goals()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
