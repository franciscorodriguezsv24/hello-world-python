# Overview

My goal with this project was to set up and verify a complete software development
workflow before starting more advanced work: a local development environment, an
editor, version control, and a public repository where finished software can be
shared and reviewed by others.

The software itself is a small command-line greeting program written in Python. It
prints "Hello, World!" inside a simple text banner, reads the system clock to choose
a greeting that matches the time of day, and then prints the same greeting in four
languages. It is intentionally small, but it exercises the pieces that show up in
every program I will write: functions, type hints, a dictionary, string formatting,
a loop, and a `main()` entry point.

I wrote this software to confirm that my tools work end to end and to establish the
habits I want to carry forward — readable functions, clear naming, docstrings, and
code that is easy to walk someone else through.

[Software Demo Video](https://www.loom.com/share/cb25222aded542cb99ef04a857db6af3)

# Development Environment

I developed this software using Visual Studio Code as my editor and Git for version
control, with the finished repository published on GitHub. I ran and tested the
program from the macOS terminal.

The program is written in Python 3.14. It uses only the Python standard library —
specifically the `datetime` module, which supplies the current date and time used
for the time-of-day greeting. No third-party packages are required.

# Useful Websites

* [Python Documentation - datetime](https://docs.python.org/3/library/datetime.html)
* [Python Documentation - Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
* [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [Markdown Guide - Basic Syntax](https://www.markdownguide.org/basic-syntax/)
* [Git Documentation](https://git-scm.com/doc)

# Future Work

* Accept a name as a command-line argument so the program can greet a specific person.
* Move the greetings into an external data file so new languages can be added without editing the code.
* Add unit tests for `time_of_day()` and `banner()` to verify the boundary hours and box width.
* Handle very long input strings so the banner does not wrap awkwardly in narrow terminals.
