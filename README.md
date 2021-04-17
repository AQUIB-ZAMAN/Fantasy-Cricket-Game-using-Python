# Fantasy-Cricket-Game-using-Python
A GUI based game in python using PyQt5 software for designing the UI and integrated the application with a SQLite database for storing the data of the players. It is an online game where one can create a virtual team of real cricket players and score points depending on how your chosen players perform in real life matches.

## Contents

- [Description](#description)
- [Screenshots](#screenshots)
- [Features](#features)
- [Requirements](#requirements)
- [Run](#run)

## Description
Fantasy Cricket Game is built in python using "PyQt5" library specifically  "QtDesigner"(`QtCore`  `QtGui`  `QtWidgets`) for **GUI** development and using Relational Database Management System "SqliteStudio(`sqlite3-DB-API-2.0`)" for **Back end database connectivity**.

## Features
  * Create your own dream team.
  * Save your team and evaluate it later as per **Match.**
  * Initially a Owner will be provided with `1000 Points` to purchase players.
  * Team selection follows basic cricketing rules. 
  * Not more than 5 Batsman/Bowler.
  * Only a Single Wicket Keeper.
  * Following rules are followed in the game:
    * Batting
      * 1 point for 2 runs scored
      * Additional 5 points for half century
      * Additional 10 points for century
      * 2 points for strike rate (runs/balls faced) of 80-100
      * Additional 4 points for strike rate>100
      * 1 point for hitting a boundary (four) and 2 points for over boundary (six)
    * Bowling
      * 10 points for each wicket
      * Additional 5 points for three wickets per innings
      * Additional 10 points for 5 wickets or more in innings
      * 4 points for economy rate (runs given per over) between 3.5 and 4.5
      * 7 points for economy rate between 2 and 3.5
      * 10 points for economy rate less than 2
    * Fielding
      * 10 points each for catch/stumping/run out

## Screenshots
- Creating a New Team
><img width="440" alt="pic1" src="https://user-images.githubusercontent.com/64305732/114379896-08896d80-9ba7-11eb-990f-d3c2a41e7513.png">

- Selecting Team Members
><img width="440" alt="pic1" src="https://user-images.githubusercontent.com/64305732/114380234-7cc41100-9ba7-11eb-8799-ff9fd2557df7.png">


- Evaluation of the Team
><img width="440" alt="pic1" src="https://user-images.githubusercontent.com/64305732/114380481-c0b71600-9ba7-11eb-8d6a-8f9dbb530440.png">


## Requirements
### Install Some Necessary Packages and Softwares

 1) Install PyQT5 Package
 * Open Command Prompt.
 * Type following command in cmd :-
      * pip install pyqt5
 2) Install sqlite3 Package
 * Open Command Prompt by using Shortcut (Window key+R) and type cmd.
 * Type following command in cmd :-
      * pip install db-sqlite3
 3) [Install](https://sqlitestudio.pl/index.rvt?act=download) Sqlite3 Studio
 
 ## Run 
 - Run`Fantasy_Cricket (MAIN).py` file on CMD.
 
 
 
 
