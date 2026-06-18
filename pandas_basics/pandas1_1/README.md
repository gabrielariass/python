# World Population Data Analysis

A Jupyter Notebook exploring world population data using pandas, covering filtering, indexing, and sorting techniques.

## Description

This notebook loads a world population CSV dataset and applies a series of pandas operations to explore and query the data. It covers filtering rows by rank, searching for specific countries, setting a custom index, selecting columns, and sorting results — serving as a hands-on introduction to data exploration with pandas.

## Concepts Covered

- The `pandas` library
- Reading CSV files (`pd.read_csv()`)
- DataFrame filtering with conditions
- `.isin()` for filtering by a list of values
- `.str.contains()` for string-based filtering
- Setting a custom index (`set_index()`)
- `.filter()` with `items` and `like` parameters
- Label-based indexing (`.loc[]`)
- Position-based indexing (`.iloc[]`)
- Sorting with `.sort_values()` and multiple keys

## Goals

- Get comfortable loading and exploring real-world datasets
- Practice filtering and querying DataFrames in multiple ways
- Understand the difference between `.loc[]` and `.iloc[]`
- Learn how to sort data by multiple columns with custom order
- Build a foundation for more advanced data analysis projects
