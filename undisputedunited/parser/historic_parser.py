import pandas as pd
from pandas import DataFrame

from undisputedunited.parser.result_parser import Parser


class HistoricParser(Parser):

    def parse(self, file_name: str) -> DataFrame:
        """
        Extracts league data from 1888 to 10th March 2020 from https://github.com/jalapic/engsoccerdata.
        The 2019/2020 season was paused on 10th March 2020, at which point this source stopped collecting results.
        The 1st tier United vs United matches that took place during the rest of the season (17th June 2020 to 26th
        July 2020) have been appended. This data is already sorted, filtered to only contain matches between Uniteds,
         and contains the correct columns in the correct format.

        :param file_name: the file name containing league results
        :return: the DataFrame containing all matches between Uniteds
        """
        return pd.read_csv(file_name, dtype='str')
