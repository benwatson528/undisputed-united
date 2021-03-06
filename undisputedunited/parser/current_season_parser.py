from datetime import datetime
from typing import Dict

import pandas as pd
from pandas import DataFrame

from undisputedunited.parser.parser import Parser


class CurrentSeasonParser(Parser):

    def parse(self, file_name: str) -> DataFrame:
        """
        Extracts league data from the current season.

        :param file_name: the file name containing league results
        :return: the DataFrame containing all matches between Uniteds
        """

        used_cols = ['Date', 'Home Team', 'Away Team', 'Result']
        df = pd.read_csv(file_name, dtype='str', usecols=used_cols)
        df.columns = ['date', 'home', 'away', 'result']
        df = df[df['result'].notna()]
        team_name_replacements = {'Utd': 'United', 'West Ham': 'West Ham United', 'Newcastle': 'Newcastle United',
                                  'Man': 'Manchester'}
        df['home'] = [self.replace_all(x, team_name_replacements) for x in df['home']]
        df['away'] = [self.replace_all(x, team_name_replacements) for x in df['away']]
        df = df[(df['home'].str.contains('United')) & (df['away'].str.contains('United'))]
        df['date'] = [datetime.strptime(x, '%d/%m/%Y %H:%M').strftime('%Y-%m-%d') for x in df['date']]
        df['score'] = [str(x).replace(" ", "") for x in df['result']]
        df['tier'] = '1'
        df['result'] = df['score'].map(self.find_winner)
        return df[['date', 'home', 'away', 'score', 'tier', 'result']]

    @staticmethod
    def replace_all(s: str, replacements: Dict) -> str:
        for x, y in replacements.items():
            s = s.replace(x, y)
        return s

    @staticmethod
    def find_winner(s: str) -> str:
        split_score = s.split("-")
        home_score, away_score = split_score[0], split_score[1]
        if home_score > away_score:
            return 'H'
        elif home_score < away_score:
            return 'A'
        else:
            return 'D'
