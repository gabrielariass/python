import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset and set Date as index
df = pd.read_csv("data/ice_cream_ratings.csv")
df.set_index('Date', inplace=True)

# Line chart
df.plot(kind='line', title='Ice Cream Ratings', xlabel='Daily Ratings', ylabel='Scores')

# Stacked bar chart
df.plot(kind='bar', stacked=True)

# Scatter plot
df.plot.scatter(x='Texture Rating', y='Overall Rating')

# Histogram
df.plot.hist(bins=5)

# Box plot
df.boxplot()

# Area chart
df.plot.area(figsize=(10, 5))

# Pie chart
df.plot.pie(y='Flavor Rating')

plt.show()
