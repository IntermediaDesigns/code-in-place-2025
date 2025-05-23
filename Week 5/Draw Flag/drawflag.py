from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here

    # Draw the red rectangle for the top half of the Indonesian flag
    # The rectangle should start at (0, 0) and go to (CANVAS_WIDTH, CANVAS_HEIGHT/2)
    red_stripe = canvas.create_rectangle(
        0,  # left_x
        0,  # top_y
        CANVAS_WIDTH,  # right_x
        CANVAS_HEIGHT // 2,  # bottom_y (half the canvas height)
        "red",  # color
    )


if __name__ == "__main__":
    main()
