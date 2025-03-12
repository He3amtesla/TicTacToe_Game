# TicTacToe Game

A simple command-line implementation of the classic Tic-Tac-Toe game written in Python.

## Description

This project is a text-based version of Tic-Tac-Toe that allows two players to take turns marking spaces on a 3x3 grid. The game randomly selects which player (X or O) goes first, and continues until one player wins by getting three of their marks in a row, column, or diagonal, or until the board is filled resulting in a draw.

## Features

- Command-line interface with clear board visualization
- Random selection of the first player
- Input validation for cell selection
- Win condition detection for rows, columns, and diagonals
- Draw condition detection

## How to Play

1. Run the game using Python:
   `
   python src/main.py
   `

2. The game will display the board with numbered positions (1-9) and randomly select whether X or O goes first.

3. Players take turns entering a number from 1 to 9 to place their mark (X or O) in the corresponding cell.

4. The game ends when a player gets three marks in a row, column, or diagonal, or when the board is filled.

## Board Layout

The board positions are numbered as follows:
```
1  |  2  |  3
-- -- -- -- -
4  |  5  |  6
-- -- -- -- -
7  |  8  |  9
```

## Requirements

- Python 3.x
- No external libraries required
