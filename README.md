
## My habit tracker app project

This project consist of a Python CLI (Command-Line Interface) for a habit tracking application that includes the following features:
. User registration
. User can select habits (name, frequency, and optional end date).
. the users inputs are via the command line.
. Integration with your existing Habit and HabitTracker classes.

Following are the requirements of the application:

. the system tracks when it has been created, and the date and time the habit tasks have been completed

. For each predefined habit, the user should enter an End date, if not the default will be set for a period of 4 weeks

. You need some way of storing, or persisting, habit data in between user sessions

. Your solution has an analytics module that return a list of all currently tracked habits  and the longest streak of all the habits,  daily and weekly.

. The validity of your habit tracking components and the analytics module has been tested by providing a unit test suite that can be run following the instructions provided with the solution.


## Installation
pip install -r requirements.txt


## Usage
Start
Python main.py
and follow instructions on screen

## Test
pytest .