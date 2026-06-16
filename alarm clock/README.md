# Alarm Clock

A simple command-line alarm clock that counts in real time and triggers an alert when the set time is reached.

## Description

This program asks the user to input an alarm time in `HH:MM:SS` format, then enters a loop that checks the current time every second. Once the current time matches the alarm time, it prints a wake-up message and stops. The current time is displayed on each iteration so you can watch it tick in real time.

## Concepts Covered

- Functions
- The `datetime` module
- The `time` module (`time.sleep()`)
- Loops (`while`)
- String formatting (`.strftime()`)
- F-strings
- User input
- Conditional logic

## Goals

- Practice working with Python's `datetime` module
- Use `time.sleep()` to control program timing
- Build a real-time loop that reacts to live data
- Get comfortable formatting and comparing time strings
