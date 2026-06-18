import pandas as pd

# Load dataset
df = pd.read_csv("data/world_population.csv")

# Preview full dataset
df

# Filter top 10 countries by rank
df[df['Rank'] <= 10]

# Filter by specific countries
specific_countries = ['Bangladesh', 'Brazil']
df[df['Country'].isin(specific_countries)]

# Filter countries containing 'United'
df[df['Country'].str.contains('United')]

# Set Country as index
df2 = df.set_index('Country')

# Select specific columns
df2.filter(items=['Continent', 'CCA3'], axis=1)

# Select specific row by country name
df2.filter(items=['Zimbabwe'], axis=0)

# Filter rows containing 'United'
df2.filter(like='United', axis=0)

# Label-based lookup
df2.loc['United States']

# Position-based lookup
df2.iloc[3]

# Top 10 sorted by Continent (desc) and Country (desc)
df[df['Rank'] <= 10].sort_values(by=['Continent', 'Country'], ascending=[False, False])
