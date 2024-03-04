#!/usr/bin/python3
"""
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

Note: Designed for Linux :heart:

Author: Brady Cox (brady@beard.sh)
"""

__author__ = "Brady Cox"
__version__ = "1.0"
__license__ = "MIT"

import time
import sys
import re
from datetime import datetime, timedelta
import curses
import pyfiglet
from dateutil.parser import parse as parse_date

# Set the pyfiglet font
PYFIGFONT = 'dos_rebel'


def parse_absolute_time(input_time):
    """Parse an absolute time input into a datetime object."""
    target_time = parse_date(input_time, fuzzy=True)
    if target_time < datetime.now():
        target_time += timedelta(days=1)
    return target_time


def parse_relative_time(input_time):
    """
    Parse a relative time input and return the total duration in seconds.
    """
    total_seconds = 0
    # Updated regex to include different abbreviations and plural forms
    pattern = re.compile(
        r'(\d+)\s*'
        r'(hours?|hrs?|minutes?|mins?|seconds?|secs?|h|m|s)',
        re.IGNORECASE
    )

    matches = pattern.findall(input_time)
    for amount, unit in matches:
        amount = int(amount)
        if unit.startswith(('h', 'hour', 'hr')):
            total_seconds += amount * 3600
        elif unit.startswith(('m', 'min')):
            total_seconds += amount * 60
        elif unit.startswith(('s', 'sec')):
            total_seconds += amount

    return total_seconds


def parse_time(input_time):
    """Determine if input is absolute or relative and parse accordingly."""
    if ":" in input_time:
        return parse_absolute_time(input_time)
    else:
        return parse_relative_time(input_time)


def display_large_text(stdscr, text):
    """Use pyfiglet to display large text and center it in the window."""
    height, width = stdscr.getmaxyx()
    ascii_art = pyfiglet.figlet_format(text, font=PYFIGFONT)
    for i, line in enumerate(ascii_art.split("\n")):
        x = max(0, width // 2 - len(line) // 2)
        y = height // 2 - len(ascii_art.split("\n")) // 2 + i
        try:
            stdscr.addstr(y, x, line)
        except curses.error:
            # Ignore errors if the text doesn't fit in the screen
            pass


def countdown(stdscr, target_time):
    """Display the countdown timer fullscreen with large text."""
    curses.curs_set(0)  # Hide the cursor for a cleaner display
    stdscr.nodelay(True)  # Make getch non-blocking

    # Determine end time based on the type of target_time
    if isinstance(target_time, int):
        end_time = datetime.now() + timedelta(seconds=target_time)
    else:
        end_time = target_time

    try:
        while True:
            now = datetime.now()
            if now >= end_time:
                break  # Stop the loop when the countdown is finished

            remaining = end_time - now
            hours, remainder = divmod(int(remaining.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)

            # Format the remaining time
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

            stdscr.erase()  # Erase the window content
            display_large_text(stdscr, time_str)
            stdscr.refresh()  # Refresh the screen to update the display

            # Sleep for a short time to avoid high CPU usage
            time.sleep(0.1)

            # Break if any key is pressed
            if stdscr.getch() != curses.ERR:
                break
    finally:
        curses.curs_set(1)  # Ensure the cursor is visible again when exiting


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Usage: ./timer.py [time]")
            sys.exit(1)

        input_time = " ".join(sys.argv[1:])
        target_time = parse_time(input_time)
        curses.wrapper(countdown, target_time)
    except KeyboardInterrupt:
        print("\nDone early, OK!")
