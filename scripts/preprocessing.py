import pandas as pd

# read in raw data
raw_games_df = pd.read_csv('../data/nba.games.stats-raw.csv', header=0, index_col=0)

# reduce to only Home games to avoid duplicated inputs
raw_games_df = raw_games_df[raw_games_df.Home == "Home"]

raw_games_df.to_csv('../data/nba.games.stats-clean.csv')
