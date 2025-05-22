from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20


def main():
    print("Random Circles")
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw N_CIRCLES random circles
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)


def draw_random_circle(canvas):
    """
    Draws a single circle at a random position with a random color on the canvas.
    """
    # Generate random position for the circle
    # Make sure the circle stays within canvas bounds by accounting for circle size
    x = random.randint(CIRCLE_SIZE // 2, CANVAS_WIDTH - CIRCLE_SIZE // 2)
    y = random.randint(CIRCLE_SIZE // 2, CANVAS_HEIGHT - CIRCLE_SIZE // 2)

    # Get a random color
    color = random_color()

    # Create and draw the circle
    circle = canvas.create_oval(
        x - CIRCLE_SIZE // 2,
        y - CIRCLE_SIZE // 2,
        x + CIRCLE_SIZE // 2,
        y + CIRCLE_SIZE // 2,
        color,
    )


def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested.
    """
    colors = ["blue", "purple", "salmon", "lightblue", "cyan", "forestgreen"]
    return random.choice(colors)


if __name__ == "__main__":
    main()
