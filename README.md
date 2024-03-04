# timer.py
A fullscreen countdown timer that accepts a variety of time formats for display

This script demonstrates the use of the curses library to create a fullscreen
terminal interface, the dateutil library for flexible date/time parsing, and
the pyfiglet library for rendering ASCII art text. It supports absolute time
formats (e.g., "3:23pm"), relative time durations (e.g., "10s" for 10 seconds,
"2m" for 2 minutes, "1h" for 1 hour), and combinations thereof
(e.g., "1h 2m 30s").

Requirements:
- Python 3.6 or newer
- python-dateutil: For parsing date and time from various formats.
- pyfiglet: For generating ASCII art text for the countdown display.
- curses: Standard library module used for creating the terminal interface.

Usage:
Run the script from the command line, passing the time string as an argument
Examples:
- ./timer.py "5 minutes"
- ./timer.py "2h 15m"
- ./timer.py "3:23pm"

To install required external packages, use:
pip install python-dateutil pyfiglet

Note: Intended for Unix-like systems where the curses library is available.

Author: Brady Cox (brady@beard.sh)
