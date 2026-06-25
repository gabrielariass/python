import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/world_population.csv")

# Display floats with 2 decimal places
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Dataset overview
df.info()
df.describe()

# Check for missing values
df.isnull().sum()

# Count unique values per column
df.nunique()

# Top 10 most populated countries in 2022
df.sort_values(by='2022 Population', ascending=False).head(10)

# Correlation matrix
df.corr(numeric_only=True)

# Heatmap of correlations
plt.rcParams['figure.figsize'] = (30, 8)
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# Average stats grouped by continent
df.groupby('Continent').mean(numeric_only=True)

# Filter Oceania
df[df['Continent'].str.contains('Oceania')]

# Average population per continent across decades
df2 = df.groupby('Continent')[['1970 Population', '1980 Population', '1990 Population',
                                '2000 Population', '2010 Population', '2015 Population',
                                '2020 Population', '2022 Population']].mean(numeric_only=True).sort_values(by='2022 Population', ascending=False)

# Transpose and plot population trends over time
df2 = df2.transpose()
df2.plot()
plt.show()
