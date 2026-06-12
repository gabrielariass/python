# Hangman

A command-line Hangman game with ASCII art that updates as you make wrong guesses. The program picks a random word from a wordlist, displays blanks for each letter, and lets you guess one letter at a time until you spell out the word or run out of attempts.

## Description

This program randomly selects a word from an external wordlist file and represents it as a series of underscores. The player guesses one letter at a time, and the hint updates to reveal correctly guessed letters. An ASCII art hangman figure builds up with each incorrect guess. The game ends when the player either guesses the full word (win) or reaches the maximum number of wrong guesses (loss).

## Concepts Covered

- Functions
- Dictionaries
- Tuples
- Loops (`while`, `for`)
- Conditionals (`if`, `elif`, `else`)
- The `random` module
- Sets
- String methods (`.lower()`, `.isalpha()`, `.join()`)
- Importing from another module/file
- Input validation

## Goals

- Practice organizing code with functions
- Work with dictionaries to map game states to visuals
- Use sets to track guessed letters efficiently
- Separate data (wordlist) from logic for cleaner code structure
- Build a more interactive, stateful command-line game
