from graphics import Canvas
import random

CANVAS_WIDTH = 600  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300  # Height of drawing canvas in pixels

BRICK_WIDTH = 30  # The width of each brick in pixels
BRICK_HEIGHT = 12  # The height of each brick in pixels
BRICKS_IN_BASE = 14  # The number of bricks in the base


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Calculate the total height of the pyramid
    pyramid_height = BRICKS_IN_BASE * BRICK_HEIGHT

    # Starting y position (bottom of canvas, working upward)
    start_y = CANVAS_HEIGHT - pyramid_height

    # Draw each row of the pyramid (from top to bottom)
    for row in range(BRICKS_IN_BASE):
        # Number of bricks in current row (starts with 1 at top, increases going down)
        bricks_in_row = row + 1

        # Calculate y position for current row
        y = start_y + (row * BRICK_HEIGHT)

        # Calculate starting x position to center the row
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) // 2

        # Draw all bricks in current row
        for brick in range(bricks_in_row):
            x = start_x + (brick * BRICK_WIDTH)

            # Draw the brick
            canvas.create_rectangle(
                x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT, "yellow", "black"
            )


if __name__ == "__main__":
    main()
