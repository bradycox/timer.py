# timer.py
A fullscreen countdown timer that accepts a variety of time formats for display

This script uses the curses library to create a fullscreen
terminal display, the dateutil library for flexible date/time parsing, and
the pyfiglet library for rendering ASCII art text. It supports absolute time
formats (e.g., "3:23pm"), relative time durations (e.g., "10s" for 10 seconds,
"2m" for 2 minutes, "1h" for 1 hour), and combinations thereof
(e.g., "1h 2m 30s").

Requirements:
- Python 3.6 or newer
- python-dateutil: For parsing date and time from various formats.
- pyfiglet: For generating ASCII art text for the countdown display.
- curses: Standard library module used for creating the terminal display.

To install required external packages, use:

`pip install python-dateutil pyfiglet`

For Arch:

`sudo pacman -S python-pyfiglet python-dateutil`

Usage:
Run the script from the command line, passing the time string as an argument:

`./timer.py <time>`

Where `<time>` can be:
- 2h 15m
- two hours and fifteen minutes
- 5 minutes
- 3:23pm
- 1:49:22 am
- 1 hour, 32 minutes and 5 seconds

or if you're nuts:
- 10s 3 mins and 1 hoursssess
- Forsooth I verily do indubitably inquire, time me for three hr and 75 mmminoiuts and how about 300 secktandss my good chap
- 4 minnits and 1 horse
- twenty horses and fifteen mice

Maximum allowable timer length at the time of writing is **69,914,649 hours** (python won't let me go later than 01 Jan 10000)

If you need a longer timer than ~7,975 years, consider immortality.

:heart: Designed as a Linux command line utility.

Author: Brady Cox (brady@beard.sh)
