# view/decomposer.py
from __future__ import annotations

from maze_solver.models.border import Border
from maze_solver.view.primitives import DisjointLine
from maze_solver.view.primitives import Line
from maze_solver.view.primitives import NullPrimitive
from maze_solver.view.primitives import Point
from maze_solver.view.primitives import Polygon
from maze_solver.view.primitives import Polyline
from maze_solver.view.primitives import Primitive


def decompose(border: Border, top_left: Point, square_size: int) -> Primitive:
    top_right: Point = top_left.translate(x=square_size)
    bottom_right: Point = top_left.translate(x=square_size, y=square_size)
    bottom_left: Point = top_left.translate(y=square_size)

    top = Line(top_left, top_right)
    bottom = Line(bottom_left, bottom_right)
    left = Line(top_left, bottom_left)
    right = Line(top_right, bottom_right)

    if border is Border.LEFT | Border.TOP | Border.RIGHT | Border.BOTTOM:
        return Polygon([top_left, top_right, bottom_right, bottom_left])

    if border is Border.BOTTOM | Border.LEFT | Border.TOP:
        return Polyline(
            [
                bottom_right,
                bottom_left,
                top_left,
                top_right,
            ],
        )

    if border is Border.BOTTOM | Border.LEFT | Border.TOP:
        return Polyline(
            [
                bottom_right,
                bottom_left,
                top_left,
                top_right,
            ],
        )

    if border is Border.LEFT | Border.TOP | Border.RIGHT:
        return Polyline(
            [
                bottom_right,
                top_left,
                top_right,
                bottom_right,
            ],
        )

    if border is Border.TOP | Border.RIGHT | Border.BOTTOM:
        return Polyline(
            [
                top_left,
                top_right,
                bottom_right,
                bottom_left,
            ],
        )

    if border is Border.RIGHT | Border.BOTTOM | Border.LEFT:
        return Polyline(
            [
                top_right,
                bottom_right,
                bottom_left,
                top_left,
            ],
        )

    if border is Border.LEFT | Border.TOP:
        return Polyline([bottom_left, top_left, top_right])

    if border is Border.TOP | Border.RIGHT:
        return Polyline([top_left, top_right, bottom_right])

    if border is Border.BOTTOM | Border.LEFT:
        return Polyline(
            [
                bottom_right,
                bottom_left,
                top_left,
            ],
        )

    if border is Border.RIGHT | Border.BOTTOM:
        return Polyline(
            [
                top_right,
                bottom_right,
                bottom_left,
            ],
        )

    if border is Border.LEFT | Border.RIGHT:
        return DisjointLines([left, right])

    if border is Border.TOP | Border.BOTTOM:
        return DisjointLines([top, bottom])

    if border is Border.TOP:
        return top

    if border is Border.BOTTOM:
        return bottom

    if border is Border.LEFT:
        return left

    if border is Border.RIGHT:
        return right

    return NullPrimitive()
