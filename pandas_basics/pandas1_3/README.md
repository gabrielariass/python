# Merging & Joining DataFrames

A Jupyter Notebook exploring how to combine DataFrames in pandas using merge, join, and concat, applied to a Lord of the Rings fellowship dataset.

## Description

This notebook uses two related CSV files based on the Fellowship of the Ring to practice combining DataFrames. It covers all major merge strategies — inner, outer, left, right, and cross — as well as joining on indexes and concatenating DataFrames side by side. The LOTR theme makes it easy to visualize what each join type keeps and drops.

## Concepts Covered

- The `pandas` library
- Reading multiple CSV files
- `.merge()` with `how` parameter — `inner`, `outer`, `left`, `right`, `cross`
- Merging on single and multiple columns with `on`
- `.join()` with suffix handling (`lsuffix`, `rsuffix`)
- Index-based joins using `set_index()`
- `pd.concat()` with `axis=1` and `join='inner'`

## Goals

- Understand the difference between each merge/join strategy
- Practice combining datasets on shared keys
- Learn when to use `.merge()` vs `.join()` vs `pd.concat()`
- Handle column name conflicts using suffixes
- Apply DataFrame combining techniques to a real structured dataset
