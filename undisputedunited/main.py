import pandas as pd

from undisputedunited.parser.current_season_parser import CurrentSeasonResultParser
from undisputedunited.parser.historic_parser import HistoricResultParser
from undisputedunited.template.readme_updater import update_readme


def main():
    current_champion = None
    changes = pd.DataFrame()
    for match in build_datasets().itertuples():
        if match.result != 'D' and (
                current_champion is None or match.home == current_champion or match.away == current_champion):
            winner = match.home if match.result == 'H' else match.away
            if winner != current_champion:
                current_champion = winner
                changes = changes.append([match])
    print(f'The current Undisputed United are {current_champion}')
    update_readme(changes.iloc[-1])
    changes.to_csv("all_title_changes.csv")


def build_datasets():
    historic_df = HistoricResultParser().parse('undisputedunited/data/top_four_leagues_1888_2020.csv')
    current_df = CurrentSeasonResultParser().parse('https://fixturedownload.com/download/epl-2020-GMTStandardTime.csv')
    return pd.concat([historic_df, current_df])


if __name__ == "__main__":
    main()
