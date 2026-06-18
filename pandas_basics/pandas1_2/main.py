import pandas as pd

# Load dataset
df = pd.read_csv("data/world_population.csv")

# Preview full dataset
df

# Load with Country as index directly
df = pd.read_csv("data/world_population.csv", index_col="Country")

# Reset index back to default
df.reset_index(inplace=True)

# Set index (saved)
df.set_index('Country', inplace=True)

# Label-based lookup
df.loc["Albania"]

# Position-based lookup
df.iloc[1]

# Reset index
df.reset_index(inplace=True)

# Set multi-level index
df.set_index(['Continent', 'Country'], inplace=True)

# Display settings and sort
pd.set_option('display.max.rows', 235)
df.sort_index()

# Filter by continent
df.loc['Africa']
df.loc['South America']

# Filter by continent + country
df.loc['Africa', 'Angola']

# Position-based lookup
df.iloc[42]
