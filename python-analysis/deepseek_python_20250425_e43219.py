import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("fifa_wc_2022.csv")

# Basic checks
print(df.info())
print(df.describe())

# Convert date & time
df['date'] = pd.to_datetime(df['date'])
df['hour'] = pd.to_datetime(df['hour']).dt.hour

# Possession to numeric
df['possession_team1'] = df['possession_team1'].str.rstrip('%').astype(float)
df['possession_team2'] = df['possession_team2'].str.rstrip('%').astype(float)

# New metrics
df['total_goals'] = df['number of goals team1'] + df['number of goals team2']
df['shot_accuracy_team1'] = df['number of goals team1'] / df['total attempts team1']
df['shot_accuracy_team2'] = df['number of goals team2'] / df['total attempts team2']

# Visualizations
# Goals distribution
sns.histplot(df['total_goals'], bins=10)
plt.title("Distribution of Total Goals per Match")

# Possession vs. Goals
sns.scatterplot(x='possession_team1', y='number of goals team1', data=df)
plt.title("Possession vs. Goals Scored (Team 1)")

# Defensive pressures comparison
sns.boxplot(x='category', y='defensive pressures applied team1', data=df)
plt.title("Defensive Pressures by Match Stage")