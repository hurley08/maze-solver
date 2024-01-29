# run_it.py
from __future__ import annotations

from pathlib import Path

from maze_solver.models.solution import Solution
from maze_solver.view.renderer import SVGRenderer

from mazes.mini_test import mini_maze
from mazes.mini_test2 import mini_maze as mini_maze2
from mazes.pacman import build_maze


solution = Solution(squares=tuple(mini_maze[i] for i in (8, 11, 7, 6, 2)))
renderer = SVGRenderer()
svg = SVGRenderer().render(mini_maze, solution)
renderer.render(mini_maze).preview()

renderer.render(mini_maze2).preview()

with Path('maze.svg').open(mode='w', encoding='utf-8') as file:
    file.write(svg.xml_content)


solution = Solution(squares=tuple(mini_maze2[i] for i in (8, 11, 7, 6, 2)))
svg = SVGRenderer().render(mini_maze2, solution)

with Path('maze2.svg').open(mode='w', encoding='utf-8') as file:
    file.write(svg.xml_content)

pacman = build_maze()

solution = Solution(squares=tuple(pacman[i] for i in ))
