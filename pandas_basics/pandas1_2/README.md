# World Population — Indexing & Multi-Index

A Jupyter Notebook focused on indexing techniques in pandas using a world population dataset, including single and multi-level indexes.

## Description

This notebook builds on basic pandas usage by diving deeper into index management. It covers how to set, reset, and use indexes for lookups, as well as how to create a multi-level index using both Continent and Country. The notebook also demonstrates how to sort and filter data using label-based and position-based indexing across a hierarchical index.

## Concepts Covered

- The `pandas` library
- Reading CSV files with `index_col`
- `reset_index()` and `set_index()` with `inplace`
- Label-based indexing (`.loc[]`)
- Position-based indexing (`.iloc[]`)
- Multi-level (hierarchical) indexing
- Sorting with `sort_index()`
- Display options (`pd.set_option()`)

## Goals

- Understand the difference between setting an index at load time vs. after
- Practice resetting and reassigning indexes
- Learn how multi-level indexes work and when to use them
- Get comfortable filtering data using `.loc[]` with hierarchical indexes
- Build on foundational pandas skills toward more complex data analysis
