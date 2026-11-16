# Falling Blocks — Python Survival Game

A small interactive survival game I developed in Python as part of my programming practice. The player controls a stick-figure character and tries to avoid blocks falling from above. The challenge becomes more difficult the longer the player survives.

## Features

- **Player movement:** Move the character left or right to avoid obstacles.
- **Random obstacles:** Falling blocks appear at random horizontal positions and vary in size.
- **Increasing difficulty:** Obstacles spawn more frequently over time, and their falling speed increases later in the game.
- **Collision detection:** The game ends when a falling block collides with the character.
- **Timed victory condition:** Survive until the progress bar is full to win.
- **Progress tracking:** A bar at the top shows progress toward victory, and a bar at the bottom displays the best survival time achieved during the current session.
- **Restart:** Start a new round after winning or losing.

## Technologies

- Python
- `random` module
- Kepoco's `display` and button interfaces

The game uses the **Kepoco** Python environment. It is not a standalone game that runs directly in a standard Python terminal without that environment.

## Controls

| Input | Action |
| --- | --- |
| Left button | Move left |
| Right button | Move right |
| A button | Nudge the character to the right during gameplay; restart after a win or loss |

## How the game works

The game runs at a target of 30 frames per second. Blocks spawn at random positions and move downward. As the survival timer increases, the delay between new blocks decreases. Obstacle speed also increases as the game progresses.

A collision triggers the **Game Over** screen. Reaching the survival target of 800 game frames triggers the **Victory** screen. The progress bars help the player track their current run and best run within the session.

## Files

- [`FallingBlocks.py`](FallingBlocks.py) — Game source code.

## What I learned

This project helped me practise Python programming logic, functions, loops, game-state management, collision detection, randomisation and simple graphics using pixel-based drawing functions.

## Project status

The source code is included for reference. It has not been independently tested outside its original Kepoco environment.
