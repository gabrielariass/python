# Python Encryption

A simple command-line encryption program that creates a randomized substitution cipher and uses it to encrypt a user-provided message. Each character in the original message is replaced with a corresponding character from a shuffled key.

## Description

This program generates two character lists: one containing letters, numbers, punctuation, and spaces, and another shuffled version that acts as the encryption key. When the user enters a message, the program looks up each character's position in the original list and replaces it with the character at the same position in the shuffled key. The result is an encrypted version of the message.

## Concepts Covered

- Lists
- The `random` module
- The `string` module
- List methods (`.copy()`, `random.shuffle()`)
- User input (`input()`)
- Loops (`for`)
- String concatenation
- Indexing and searching (`.index()`)
- F-strings

## Goals

- Learn how substitution ciphers work
- Practice working with lists and indexes
- Use the `random` module to create a shuffled encryption key
- Understand how characters can be mapped from one set to another
- Build a basic encryption tool using Python
- Gain experience processing strings character by character
