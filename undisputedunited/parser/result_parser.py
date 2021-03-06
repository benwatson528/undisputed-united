from abc import ABC, abstractmethod

from pandas import DataFrame


class Parser(ABC):
    @abstractmethod
    def parse(self, file_name: str) -> DataFrame:
        """
        Parses a given file containing football match results into a DataFrame containing only matches between two
        Uniteds.

        The output columns should be: date (YYYY-MM-DD), home, away, score (x-y), tier (1 to 4), result (H, A or D).
        Team names should not contain "FC" or any other suffixes, for example "Newcastle United" and not "Newcastle
        United FC".

        :param file_name: the name of the file containing football match results
        :return: the DataFrame containing all matches between Uniteds
        """
        pass
