import pandas as pd

used_cols = ['result', 'Date', 'tier', 'home', 'visitor']
all_matches = pd.read_csv('../data/league-matches-to-2020-03-10.csv', dtype='str', usecols=used_cols)

filtered_uniteds = all_matches[
    (all_matches['home'].str.contains('United')) & (all_matches['visitor'].str.contains('United'))]


def find_first_united(filtered_uniteds):
    return "Sheffield United"


def find_next():
    # https://stackoverflow.com/questions/19151/build-a-basic-python-iterator
    return "Sheffield United"
