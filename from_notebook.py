import requests, json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ______________________________________________________________________________________________________________________
# I. CREATE EVENTS PANDAS DATAFRAME
url = 'https://fantasy.premierleague.com/api/'
api_result = requests.get(url + 'bootstrap-static/').json()
events = api_result['events']

df_events_tot = pd.json_normalize(events)
df_events = df_events_tot.drop(columns='chip_plays')  # DO NASTĘPNEJ TABELI

floats = list(df_events.select_dtypes(include=['float64']).columns)  # SELECT FLOAT COLUMNS
df_events[floats] = df_events[floats].fillna(0.0).astype(int)  # CONVERT FLOATS TO INT

df_events.set_index('id', inplace=True)  # SET ID AS INDEX
df_events

df_events = df_events.drop(columns=['deadline_time', 'release_time'])  # DROP IRRELEVANT COLUMNS

df_events['deadline_time_epoch'] = pd.to_datetime(df_events['deadline_time_epoch'], unit='s')  # CONVERT TO DATETIME

df_events

# I.1 EVENTS CHARTS

# AVERAGE POINTS IN TIME
fig, ax = plt.subplots(figsize=(20, 7))
ax.set_title('Average points in time')
ax.set_xticklabels(df_events.name, rotation=45, ha='right')
ax.set_ylabel('Points')
sns.lineplot(data=df_events, x=df_events['name'], y=df_events['average_entry_score'], ax=ax)

# TRANSFERS
fig, ax = plt.subplots(figsize=(20, 7))
ax.set_title('Transfers made per Gameweek')
ax.set_xticklabels(df_events.name, rotation=45, ha='right')
ax.set_ylabel('Transfers')
sns.lineplot(data=df_events, x=df_events['name'], y=df_events['transfers_made'], ax=ax)
# ______________________________________________________________________________________________________________________

# ______________________________________________________________________________________________________________________
# II. CREATE CHIPS PANDAS DATAFRAME
chips = pd.json_normalize(df_events_tot['chip_plays'])

df_chips_bboost = pd.json_normalize(chips[0])
df_chips_bboost = df_chips_bboost.rename(columns={'num_played': 'bboost'})
df_chips_bboost = df_chips_bboost.drop(columns='chip_name')

df_chips_freehit = pd.json_normalize(chips[1])
df_chips_freehit = df_chips_freehit.rename(columns={'num_played': 'freehit'})
df_chips_freehit = df_chips_freehit.drop(columns='chip_name')

df_chips_wildcard = pd.json_normalize(chips[2])
df_chips_wildcard = df_chips_wildcard.rename(columns={'num_played': 'wildcard'})
df_chips_wildcard = df_chips_wildcard.drop(columns='chip_name')

df_chips_3xc = pd.json_normalize(chips[3])
df_chips_3xc = df_chips_3xc.rename(columns={'num_played': '3xc'})
df_chips_3xc = df_chips_3xc.drop(columns='chip_name')

df_chips = df_chips_3xc.join([df_chips_wildcard, df_chips_freehit, df_chips_bboost])
df_chips

df_chips = df_chips.fillna(0.0).astype(int)  # CONVERT FLOATS TO INT
df_chips

df_chips['id'] = pd.RangeIndex(1, len(df_chips) + 1)  # SET ID AS INDEX
df_chips.set_index('id', inplace=True)

df_chips['name'] = df_events['name']

df_chips

# II.1 CHIPS CHARTS

# TRIPLE CAPTAINS PLAYED
fig, ax = plt.subplots(figsize=(20, 7))
ax.set_title('Triple captain chip played in time')
ax.set_xticklabels(df_events.name, rotation=45, ha='right')
ax.set_ylabel('No. of 3xc')
sns.lineplot(data=df_chips, x=df_chips['name'], y=df_chips['3xc'], ax=ax)

# WILDCARDS PLAYED
fig, ax = plt.subplots(figsize=(20, 7))
ax.set_title('Wildcard chip played in time')
ax.set_xticklabels(df_events.name, rotation=45, ha='right')
ax.set_ylabel('No. of wildcards')
sns.lineplot(data=df_chips, x=df_chips['name'], y=df_chips['wildcard'], ax=ax)

# FREEHIT PLAYED
fig, ax = plt.subplots(figsize=(20, 7))
ax.set_title('Freehit chip played in time')
ax.set_xticklabels(df_events.name, rotation=45, ha='right')
ax.set_ylabel('No. of freehits')
sns.lineplot(data=df_chips, x=df_chips['name'], y=df_chips['freehit'], ax=ax)

# BENCHBOOST PLAYED
fig, ax = plt.subplots(figsize=(20, 7))
ax.set_title('Benchboost chip played in time')
ax.set_xticklabels(df_events.name, rotation=45, ha='right')
ax.set_ylabel('No. of bboosts')
sns.lineplot(data=df_chips, x=df_chips['name'], y=df_chips['bboost'], ax=ax)
# _______________________________________________________________________________________________________________________

# III. CREATE PLAYERS PANDAS DATAFRAME
players = api_result['elements']
df_players = pd.json_normalize(players)
player_columns = list(df_players.columns)
player_columns_reoder = ['second_name', 'first_name', 'id', 'team', 'element_type', 'total_points', 'points_per_game',
                         'chance_of_playing_next_round',
                         'chance_of_playing_this_round',
                         'code',
                         'cost_change_event',
                         'cost_change_event_fall',
                         'cost_change_start',
                         'cost_change_start_fall',
                         'dreamteam_count',
                         'ep_next',
                         'ep_this',
                         'event_points',
                         'form',
                         'in_dreamteam',
                         'news',
                         'news_added',
                         'now_cost',
                         'photo',
                         'selected_by_percent',
                         'special',
                         'squad_number',
                         'status',
                         'team_code',
                         'transfers_in',
                         'transfers_in_event',
                         'transfers_out',
                         'transfers_out_event',
                         'value_form',
                         'value_season',
                         'web_name',
                         'minutes',
                         'goals_scored',
                         'assists',
                         'clean_sheets',
                         'goals_conceded',
                         'own_goals',
                         'penalties_saved',
                         'penalties_missed',
                         'yellow_cards',
                         'red_cards',
                         'saves',
                         'bonus',
                         'bps',
                         'influence',
                         'creativity',
                         'threat',
                         'ict_index',
                         'starts',
                         'expected_goals',
                         'expected_assists',
                         'expected_goal_involvements',
                         'expected_goals_conceded',
                         'influence_rank',
                         'influence_rank_type',
                         'creativity_rank',
                         'creativity_rank_type',
                         'threat_rank',
                         'threat_rank_type',
                         'ict_index_rank',
                         'ict_index_rank_type',
                         'corners_and_indirect_freekicks_order',
                         'corners_and_indirect_freekicks_text',
                         'direct_freekicks_order',
                         'direct_freekicks_text',
                         'penalties_order',
                         'penalties_text',
                         'expected_goals_per_90',
                         'saves_per_90',
                         'expected_assists_per_90',
                         'expected_goal_involvements_per_90',
                         'expected_goals_conceded_per_90',
                         'goals_conceded_per_90',
                         'now_cost_rank',
                         'now_cost_rank_type',
                         'form_rank',
                         'form_rank_type',
                         'points_per_game_rank',
                         'points_per_game_rank_type',
                         'selected_rank',
                         'selected_rank_type',
                         'starts_per_90',
                         'clean_sheets_per_90']

df_players = df_players.reindex(columns=player_columns_reoder)
df_players = df_players.sort_values(['element_type', 'team'])
df_players.index = np.arange(1, len(df_players) + 1)
df_players

# III.1 CREATE PANDAS DATAFRAME FOR EACH POSITION

# GOALKEEPERS
df_goalkeepers = df_players.loc[df_players.element_type == 1]
df_goalkeepers

# DEFENDERS
df_defenders = df_players.loc[df_players.element_type == 2]
df_defenders.index = np.arange(1, len(df_defenders) + 1)
df_defenders

# MIDFIELDERS
df_midlefielders = df_players.loc[df_players.element_type == 3]
df_midlefielders.index = np.arange(1, len(df_midlefielders) + 1)
df_midlefielders

# FORWARDS
df_forwards = df_players.loc[df_players.element_type == 4]
df_forwards.index = np.arange(1, len(df_forwards) + 1)
df_forwards
# _______________________________________________________________________________________________________________________

# IV. CREATE TEAMS PANDAS DATAFRAME
teams = api_result['teams']
df_teams = pd.json_normalize(teams)

df_teams.set_index('id', inplace=True)  # SET ID AS INDEX
list(df_teams.columns)
teams_columns_reorder = ['code', 'name', 'short_name', 'win',
                         'draw',
                         'loss',
                         'played',
                         'points',
                         'position', 'form',
                         'strength',
                         'team_division',
                         'strength_overall_home',
                         'strength_overall_away',
                         'strength_attack_home',
                         'strength_attack_away',
                         'strength_defence_home',
                         'strength_defence_away',
                         'pulse_id',
                         'unavailable']

df_teams = df_teams.reindex(columns=teams_columns_reorder)

df_teams
#_______________________________________________________________________________________________________________________

#_______________________________________________________________________________________________________________________
# V. GET INFO ON CHOSEN PLAYER PERFROMANCE

def get_info(player_id):
    url_player = f'https://fantasy.premierleague.com/api/element-summary/{player_id}/'
    api_result_player = requests.get(url_player).json()
    stats = api_result_player['history']
    df_stats = pd.json_normalize(stats)
    df_stats.index = np.arange(1, len(df_stats) + 1)
    exp = ['expected_goals', 'expected_assists', 'expected_goal_involvements', 'expected_goals_conceded']
    df_stats[exp] = df_stats[exp].astype('float64')

    if int(df_players['element_type'].loc[df_players['id'] == player_id]) == [1, 2]:

        fig, ax = plt.subplots(nrows=11, ncols=1, figsize=(20, 35))

        # MINUTES PLAYED
        ax[0].set_title('Minutes played')
        ax[0].set_ylabel('Minutes')
        ax[0] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['minutes'], ax=ax[0])

        # POINTS PER GAMEWEEK
        ax[1].set_title('Total points')
        ax[1].set_ylabel('Points')
        ax[1] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['total_points'], ax=ax[1])

        # CLEAN SHEETS
        ax[2].set_title('Clean sheets')
        ax[2].set_ylabel('Clean sheets')
        ax[2] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['clean_sheets'], ax=ax[2])

        # GOALS SCORED
        ax[3].set_title('Goals scored')
        ax[3].set_ylabel('Goals')
        ax[3] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['goals_scored'], ax=ax[3])

        # ASSISTS
        ax[4].set_title('Assists')
        ax[4].set_ylabel('Assists')
        ax[4] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['assists'], ax=ax[4])

        # EXPECTED GOALS CONCEDED
        ax[5].set_title('Expected goals conceded')
        ax[5].set_ylabel('xGC')
        ax[5] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['expected_goals_conceded'], ax=ax[5])

        # EXPECTED GOALS
        ax[6].set_title('Expected goals')
        ax[6].set_ylabel('xG')
        ax[6] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['expected_goals'], ax=ax[6])

        # EXPECTED ASSISTS
        ax[7].set_title('Expected assists')
        ax[7].set_ylabel('xA')
        ax[7] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['expected_assists'], ax=ax[7])

        # VALUE
        ax[8].set_title('Value in time')
        ax[8].set_ylabel('Value')
        ax[8] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['value'], ax=ax[8])

        # TRANSFERS IN
        ax[9].set_title('No. of transfers in')
        ax[9].set_ylabel('Transfers')
        ax[9] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['transfers_in'], ax=ax[9])

        # TRANSFERS OUT
        ax[10].set_title('No. of transfers out')
        ax[10].set_ylabel('Transfers')
        ax[10] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['transfers_out'], ax=ax[10])

    else:

        fig, ax = plt.subplots(nrows=9, ncols=1, figsize=(20, 35))

        # MINUTES PLAYED
        ax[0].set_title('Minutes played')
        ax[0].set_ylabel('Minutes')
        ax[0] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['minutes'], ax=ax[0])

        # POINTS PER GAMEWEEK
        ax[1].set_title('Total points')
        ax[1].set_ylabel('Points')
        ax[1] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['total_points'], ax=ax[1])

        # GOALS SCORED
        ax[2].set_title('Goals scored')
        ax[2].set_ylabel('Goals')
        ax[2] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['goals_scored'], ax=ax[2])

        # ASSISTS
        ax[3].set_title('Assists')
        ax[3].set_ylabel('Assists')
        ax[3] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['assists'], ax=ax[3])

        # EXPECTED GOALS
        ax[4].set_title('Expected goals')
        ax[4].set_ylabel('xG')
        ax[4] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['expected_goals'], ax=ax[4])

        # EXPECTED ASSISTS
        ax[5].set_title('Expected assists')
        ax[5].set_ylabel('xA')
        ax[5] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['expected_assists'], ax=ax[5])

        # VALUE
        ax[6].set_title('Value in time')
        ax[6].set_ylabel('Value')
        ax[6] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['value'], ax=ax[6])

        # TRANSFERS IN
        ax[7].set_title('No. of transfers in')
        ax[7].set_ylabel('Transfers')
        ax[7] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['transfers_in'], ax=ax[7])

        # TRANSFERS OUT
        ax[8].set_title('No. of transfers out')
        ax[8].set_ylabel('Transfers')
        ax[8] = sns.lineplot(data=df_stats, x=df_stats.index, y=df_stats['transfers_out'], ax=ax[8])

    return df_players['second_name'].loc[df_players['id'] == player_id]
#_______________________________________________________________________________________________________________________

#_______________________________________________________________________________________________________________________

# VI. GET INFO ON CHOSEN MANAGER PERFORMANCE
def get_manager_info(manager_id):
    url_manager = f'https://fantasy.premierleague.com/api/entry/{manager_id}/'
    api_result_manager = requests.get(url_manager).json()
    manager_info = pd.json_normalize(api_result_manager)

    manager_info_columns = ['id', 'player_first_name', 'player_last_name', 'years_active',
                            'summary_overall_points', 'summary_overall_rank', 'summary_event_points',
                            'summary_event_rank']
    manager_info_stripped = manager_info[manager_info_columns]
    manager_info_stripped.set_index(manager_info_stripped.id, inplace=True, drop=True)

    url_manager_transfers = f'https://fantasy.premierleague.com/api/entry/{manager_id}/transfers/'
    api_result_manager_transfers = requests.get(url_manager_transfers).json()
    transfers_info = pd.json_normalize(api_result_manager_transfers)
    transfers_info['time'] = pd.to_datetime(transfers_info['time']).dt.tz_localize(None).dt.date
    transfers_number = pd.DataFrame(transfers_info.groupby('event').count().element_in.rename('transfers_per_gameweek'))
    transfers_number

    url_team_gw = f'https://fantasy.premierleague.com/api/entry/{manager_id}/event/1/picks/'
    api_team_gw = requests.get(url_team_gw).json()
    team_gw = pd.json_normalize(api_team_gw)
    team_gw_columns = ['active_chip', 'entry_history.event',
                       'entry_history.points', 'entry_history.total_points',
                       'entry_history.rank', 'entry_history.rank_sort',
                       'entry_history.overall_rank', 'entry_history.percentile_rank',
                       'entry_history.bank', 'entry_history.value',
                       'entry_history.event_transfers', 'entry_history.event_transfers_cost',
                       'entry_history.points_on_bench']
    team_gw = team_gw[team_gw_columns]

    for i in range(2, 27):  # NALEŻY ZNALEŹĆ AUTOMATYZACJĘ ILOŚCI GW + JAK WPISZESZ ZA DUŻĄ WARTOŚĆ JEST KAPLICA
        url_team_new_gw = f'https://fantasy.premierleague.com/api/entry/{manager_id}/event/{i}/picks/'
        api_team_new_gw = requests.get(url_team_new_gw).json()
        team_new_gw = pd.json_normalize(api_team_new_gw)
        team_new_gw = team_new_gw[team_gw_columns]
        team_gw = pd.concat([team_gw, team_new_gw], join='inner', axis=0)

    team_gw.index = np.arange(1, len(team_gw) + 1)


    # CHARTS
    fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(20, 35))

    # Points per GW
    ax[0].set_title('Points per Gameweek')
    ax[0].set_ylabel('Points in GW')
    ax[0] = sns.lineplot(data=team_gw, x=team_gw.index, y=team_gw['entry_history.points'], ax=ax[0])

    # Total points in time
    ax[1].set_title('Total points in time')
    ax[1].set_ylabel('Points')
    ax[1] = sns.lineplot(data=team_gw, x=team_gw.index, y=team_gw['entry_history.total_points'], ax=ax[1])

    # Rank per GW
    ax[2].set_title('Gameweek rank')
    ax[2].set_ylabel('Rank')
    ax[2] = sns.lineplot(data=team_gw, x=team_gw.index, y=-team_gw['entry_history.rank_sort'], ax=ax[2])

    # Overall rank in time
    ax[3].set_title('Rank')
    ax[3].set_ylabel('Rank')
    ax[3] = sns.lineplot(data=team_gw, x=team_gw.index, y=-team_gw['entry_history.overall_rank'], ax=ax[3])
#_______________________________________________________________________________________________________________________

#_______________________________________________________________________________________________________________________
# VII. GET INFO ON CHOSEN MANAGER'S TEAM ON CHOSEN GAMEWEEK
def manager_team_gw(manager_id, gameweek):
    url = f'https://fantasy.premierleague.com/api/entry/{manager_id}/event/{gameweek}/picks/'
    api_result_team_gw = requests.get(url).json()
    team_gw = pd.json_normalize(api_result_team_gw)
    team_gw_df = pd.json_normalize(team_gw.picks)
    team_gw_df = team_gw_df.melt()
    team_gw_df = pd.json_normalize(team_gw_df.value)
    team_gw_df.set_index(team_gw_df.position, drop=True, inplace=True)

    team_gw_df['points'] = 0
    for i in range(1, 16):
        player = int(team_gw_df['element'].loc[team_gw_df.index == i])
        url_player = f'https://fantasy.premierleague.com/api/element-summary/{player}/'
        api_result_player = requests.get(url_player).json()
        stats = api_result_player['history']
        df_stats = pd.json_normalize(stats)
        df_stats.index = np.arange(1, len(df_stats) + 1)
        df_stats.loc[df_stats.index == gameweek].total_points
        team_gw_df['points'].loc[team_gw_df.index == i] = int(df_stats.loc[df_stats.index == gameweek].total_points)

    return team_gw_df


manager_team_gw(5391518, 5)
