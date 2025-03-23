import pandas as pd
import numpy as np
try:
    movies = pd.read_csv('movies.csv')
except FileNotFoundError:
    movies = pd.DataFrame({
        'title': ['The Avengers', 'Die Hard', 'Mad Max', 'Inception'],
        'genre': ['Action', 'Action', 'Action', 'Thriller'],
        'rating': [8.0, 7.8, 7.6, 8.8]
    })

print("DataFrame Attributes and Methods:")
print("1. Shape:", movies.shape)
print("2. Columns:", movies.columns.tolist())
print("3. Data Types:\n", movies.dtypes)
print("4. Index:", movies.index)
print("5. Head:\n", movies.head(2))
print("6. Describe:\n", movies.describe())
print("7. Info:")
movies.info()

action_high = movies[(movies['genre'] == 'Action') & (movies['rating'] > 7.5)]
print("\nAction movies with rating >7.5:\n", action_high)

try:
    ipl = pd.read_csv('ipl-matches.csv')
except FileNotFoundError:
    ipl = pd.DataFrame({
        'City': ['Kolkata', 'Mumbai', 'Kolkata', 'Chennai'],
        'Team1': ['CSK', 'MI', 'KKR', 'RCB'],
        'Team2': ['RCB', 'CSK', 'CSK', 'MI'],
        'TossWinner': ['CSK', 'MI', 'CSK', 'RCB'],
        'WinningTeam': ['CSK', 'MI', 'CSK', 'MI']
    })

csk_wins = ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'CSK')]
print("\nCSK wins in Kolkata:", len(csk_wins))

toss_win_percent = (np.mean(ipl['TossWinner'] == ipl['WinningTeam']) * 100)
print(f"Toss winner match win %: {toss_win_percent:.1f}%")

print("\n10 Match Samples:\n", ipl.sample(min(10, len(ipl))))

matches_played = pd.concat([ipl['Team1'], ipl['Team2']]).value_counts()
print("\nMatches per team:\n", matches_played)

try:
    deliveries = pd.read_csv('deliveries.csv')
except FileNotFoundError:
    deliveries = pd.DataFrame({
        'batsman': ['Kohli', 'Rohit', 'Kohli', 'Dhoni', 'Rohit'],
        'batsman_runs': [6, 4, 4, 6, 6],
        'over': [18, 19, 20, 16, 17],
        'match_id': [1, 1, 2, 2, 3],
        'bowling_team': ['MI', 'CSK', 'RCB', 'KKR', 'DC']
    })

top_batsmen = deliveries.groupby('batsman')['batsman_runs'].sum().nlargest(10)
print("\nTop 10 Batsmen:\n", top_batsmen)

sixes = deliveries[deliveries['batsman_runs'] == 6]
six_hitters = sixes['batsman'].value_counts().head(1)
print("\nMost Sixes:\n", six_hitters)

last_5 = deliveries[deliveries['over'] > 15]
boundary_hitters = last_5[last_5['batsman_runs'].isin([4,6])]
boundary_counts = boundary_hitters['batsman'].value_counts().head(1)
print("\nMost Boundaries in Last 5 Overs:\n", boundary_counts)

kohli_record = deliveries[deliveries['batsman'] == 'Kohli']
kohli_record = kohli_record.groupby('bowling_team')['batsman_runs'].sum()
print("\nKohli's Record vs Teams:\n", kohli_record)

def highest_score(batsman):
    return deliveries[deliveries['batsman'] == batsman].groupby('match_id')['batsman_runs'].sum().max()
print("\nKohli's Highest Score:", highest_score('Kohli'))

list_data = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
df_list = pd.DataFrame(list_data, columns=['Name', 'Age'])

dict_data = {'Name': ['Diana', 'Evan'], 'Age': [28, 32]}
df_dict = pd.DataFrame(dict_data)

series_names = pd.Series(['Frank', 'Grace'])
series_ages = pd.Series([40, 45])
df_series = pd.DataFrame({'Name': series_names, 'Age': series_ages})

combined_df = pd.concat([df_list, df_dict, df_series])
combined_df = combined_df.rename(columns={'Name': 'FullName'})
combined_df.set_index('FullName', inplace=True)

print("\nFilter Operations:")
print("1. Age >30:\n", combined_df[combined_df['Age'] > 30])
print("2. First 3 rows:\n", combined_df.head(3))
print("3. Specific columns:\n", combined_df[['Age']])
print("4. Index selection:\n", combined_df.iloc[1:3])
print("5. Loc selection:\n", combined_df.loc[combined_df['Age'] < 40])
print("6. Query:\n", combined_df.query("Age == 45"))
print("7. Sorted:\n", combined_df.sort_values('Age', ascending=False))
print("8. Drop columns:\n", combined_df.drop(columns=['Age']))
print("9. Null check:\n", combined_df[combined_df.isnull().any(axis=1)])
print("10. Multiple conditions:\n", combined_df[(combined_df['Age'] > 25) & (combined_df['Age'] < 40)])

grouped = combined_df.groupby('Age').size()
pivot = pd.pivot_table(combined_df.reset_index(), values='Age', index=['FullName'])
print("\nGroupBy:\n", grouped)
print("\nPivot Table:\n", pivot)