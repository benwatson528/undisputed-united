import pandas as pd
from pandas import Series


def main():
    current_champion = None
    changes = pd.DataFrame()
    for match in find_all_united_matches().itertuples():
        if match.result != 'D' and (
                current_champion is None or match.home == current_champion or match.visitor == current_champion):
            winner = get_winner(match)
            if winner != current_champion and is_valid_winner(match):
                print(f'New champion {winner} in match {match}')
                current_champion = winner
                changes = changes.append([match])
    print(f'The Undisputed United as of 2020-03-10 is {current_champion}')
    print(f'{changes}')


def find_all_united_matches():
    used_cols = ['result', 'Date', 'tier', 'home', 'visitor', 'FT']
    historic = pd.read_csv('league-matches-to-2020-03-10.zip', dtype='str', usecols=used_cols)
    current_season = pd.read_csv('epl-2020-2021.csv')
    current_season.columns = ['round', 'Date', 'location', 'home', 'visitor', 'FT']
    current_season['tier'] = '1'
    current_season['result'].apply(lambda x: x['FT'] + '10')

    return historic[
        (historic['home'].str.contains('United')) & (historic['visitor'].str.contains('United'))]


def is_valid_winner(match: Series):
    """
    Manchester United were called Newton Heath until 24th April 1902, and so aren't included until then. However the
    dataset refers to them as Manchester United, so any matches referring to them must be ignored here.

    :param match: the full match information
    :return: true if the winner isn't Manchester before 1902-04-24
    """
    return not ((match.home == "Manchester United" or match.visitor == "Manchester United")
                and match.Date < '1902-04-24')


def get_winner(match: Series):
    return match.home if match.result == 'H' else match.visitor


if __name__ == "__main__":
    main()
