import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

data_file_path = 'C:\codes\data.csv'

unfiltered_player_data = pd.read_csv(data_file_path)

y = unfiltered_player_data.Overall

features = ['Crossing','Finishing','HeadingAccuracy','ShortPassing','Volleys','Dribbling','Curve','FKAccuracy','LongPassing','BallControl','Acceleration','SprintSpeed','Agility','Reactions','Balance','ShotPower','Jumping','Stamina','Strength','LongShots','Aggression','Interceptions','Positioning','Vision','Penalties','Composure','Marking','StandingTackle','SlidingTackle','GKDiving','GKHandling','GKKicking','GKPositioning','GKReflexes']

X = unfiltered_player_data[features]

filtered_columns_player_data = unfiltered_player_data.drop(unfiltered_player_data.columns.difference(features), axis=1)

filtered_player_data = filtered_columns_player_data.dropna(axis=0)

t = filtered_player_data.isnull().sum(axis = 0)

overall_player_score_model = RandomForestRegressor(random_state=1)

train_X, val_X, train_y, val_y = train_test_split(X,y, random_state= 1)

train_X.fillna(method = 'ffill', inplace = True)
val_X.fillna(method = 'ffill', inplace = True)

overall_player_score_model.fit(train_X, train_y)

overall_player_score_model_pred = overall_player_score_model.predict(val_X)
print(mean_absolute_percentage_error(val_y, overall_player_score_model_pred))
