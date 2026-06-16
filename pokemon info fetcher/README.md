# Pokémon Info Fetcher

A command-line tool that fetches Pokémon data from the PokéAPI and saves it to a text file.

## Description

This program asks the user for a Pokémon name, then makes a GET request to the PokéAPI to retrieve its data. If the request is successful, it extracts the Pokémon's name, ID, height, and weight, and appends that information to a local text file. Each search adds a new entry to the file, building up a personal Pokédex over time.

## Concepts Covered

- The `requests` library
- REST APIs and HTTP requests
- JSON parsing
- File handling (`open()`, `"a"` append mode)
- Functions
- F-strings
- Status code handling
- Constants and project structure

## Goals

- Learn how to interact with a public REST API
- Practice parsing and extracting data from JSON responses
- Get comfortable reading and writing to files
- Handle failed requests gracefully with status code checks
- Build a simple but complete data-fetching program
