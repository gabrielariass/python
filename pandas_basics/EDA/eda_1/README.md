# World Population — Exploratory Data Analysis

A Jupyter Notebook performing exploratory data analysis (EDA) on a world population dataset using pandas, seaborn, and matplotlib.

## Description

This notebook dives into the world population dataset with a full EDA workflow — inspecting the data, checking for nulls, analyzing correlations, grouping by continent, and visualizing population trends across decades. It combines statistical summaries with visual tools like heatmaps and line charts to uncover patterns in global population growth.

## Concepts Covered

- The `pandas` library
- The `seaborn` library
- The `matplotlib` library
- Reading CSV files
- Display formatting (`pd.set_option()`)
- Data inspection (`df.info()`, `df.describe()`)
- Null checks (`isnull().sum()`)
- Unique value counts (`nunique()`)
- Sorting and filtering
- Correlation matrix (`df.corr()`)
- Heatmaps (`sns.heatmap()`)
- GroupBy with `.mean()`
- String filtering with `.str.contains()`
- Transposing DataFrames and plotting trends

## Goals

- Practice a complete EDA workflow from inspection to visualization
- Learn how to identify correlations and interpret a heatmap
- Use groupby to summarize data by category
- Visualize historical trends across multiple time periods
- Get comfortable combining pandas with seaborn and matplotlib
