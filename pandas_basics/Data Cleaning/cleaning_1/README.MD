# Customer Call List — Data Cleaning

A Jupyter Notebook that takes a messy customer call list and cleans it into a structured, ready-to-use dataset using pandas.

## Description

This notebook walks through a full data cleaning pipeline on a real-world style customer dataset. It removes duplicates, drops useless columns, standardizes phone numbers, splits addresses into separate fields, normalizes Yes/No values, handles null-like entries, and filters out customers who should not be contacted or have no phone number on record.

## Concepts Covered

- The `pandas` library
- Reading Excel files (`pd.read_excel()`)
- Removing duplicates (`drop_duplicates()`)
- Dropping columns (`drop()`)
- String cleaning (`str.strip()`, `str.replace()`)
- Regex with `str.replace()`
- Lambda functions
- Splitting columns (`str.split()` with `expand=True`)
- Replacing null-like values (`replace()`, `fillna()`)
- Filtering rows with boolean conditions
- Resetting the index (`reset_index()`)

## Goals

- Practice a complete data cleaning workflow from start to finish
- Learn how to handle inconsistent and messy real-world data
- Use string methods and regex to standardize column values
- Filter out unusable records before analysis or outreach
- Produce a clean, consistent dataset ready for further use
