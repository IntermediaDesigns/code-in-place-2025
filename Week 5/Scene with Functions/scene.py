from graphics import Canvas
import math

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw sky background
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "lightblue")

    # Draw ground
    canvas.create_rectangle(
        0, CANVAS_HEIGHT - 50, CANVAS_WIDTH, CANVAS_HEIGHT, "lightgreen"
    )

    # Draw three clouds at different positions
    draw_cloud(canvas, 140, 10, "white")
    draw_cloud(canvas, 20, 30, "lightgray")
    draw_cloud(canvas, 280, 20, "white")

    # Draw three trees at different positions
    draw_tree(canvas, 80, "brown", "darkgreen")
    draw_tree(canvas, 200, "saddlebrown", "forestgreen")
    draw_tree(canvas, 320, "brown", "green")

    # Above and Beyond: Add extra elements
    draw_sun(canvas, 350, 50, "yellow")
    draw_flower(canvas, 50, TREE_BOTTOM_Y + 10, "red", "yellow")
    draw_flower(canvas, 150, TREE_BOTTOM_Y + 15, "purple", "orange")
    draw_flower(canvas, 250, TREE_BOTTOM_Y + 12, "pink", "yellow")


def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in
    different values of x and y (the location of the cloud) and
    color (the color of the cloud).
    """
    cloud_bottom_start_y = y + (1 / 3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1 / 4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3 / 4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, cloud_bottom_start_y, x + (3 / 4) * CLOUD_WIDTH, cloud_bottom_end_y, color
    )
    canvas.create_oval(
        x + (1 / 4) * CLOUD_WIDTH,
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color,
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x, y, cloud_top_end_x, y + (2 / 3) * CLOUD_HEIGHT, color
    )


def draw_tree(canvas, x, trunk_color, leaves_color):
    """
    This function draws one tree with a rectangular trunk and circular leaves.
    x: x-position where the tree should be centered
    trunk_color: color of the tree trunk
    leaves_color: color of the tree leaves
    """
    # Calculate trunk position (centered on x)
    trunk_left = x - TRUNK_WIDTH // 2
    trunk_right = x + TRUNK_WIDTH // 2
    trunk_top = TREE_BOTTOM_Y - TRUNK_HEIGHT
    trunk_bottom = TREE_BOTTOM_Y

    # Draw trunk
    canvas.create_rectangle(
        trunk_left, trunk_top, trunk_right, trunk_bottom, trunk_color
    )

    # Calculate leaves position (centered on trunk)
    leaves_left = x - LEAVES_SIZE // 2
    leaves_right = x + LEAVES_SIZE // 2
    leaves_top = trunk_top - LEAVES_SIZE // 2
    leaves_bottom = trunk_top + LEAVES_SIZE // 2

    # Draw leaves
    canvas.create_oval(
        leaves_left, leaves_top, leaves_right, leaves_bottom, leaves_color
    )


def draw_sun(canvas, x, y, color):
    """
    Draws a sun with rays at the given position.
    """
    sun_size = 30

    # Draw sun rays (lines extending from center)
    ray_length = 20
    for angle in range(0, 360, 45):  # 8 rays
        angle_rad = math.radians(angle)
        start_x = x + (sun_size // 2) * math.cos(angle_rad)
        start_y = y + (sun_size // 2) * math.sin(angle_rad)
        end_x = x + (sun_size // 2 + ray_length) * math.cos(angle_rad)
        end_y = y + (sun_size // 2 + ray_length) * math.sin(angle_rad)
        canvas.create_line(start_x, start_y, end_x, end_y, color)

    # Draw sun circle
    canvas.create_oval(
        x - sun_size // 2,
        y - sun_size // 2,
        x + sun_size // 2,
        y + sun_size // 2,
        color,
    )


def draw_flower(canvas, x, y, petal_color, center_color):
    """
    Draws a simple flower with petals and center.
    """
    petal_size = 8
    center_size = 6

    # Draw 5 petals around the center
    for angle in range(0, 360, 72):  # 5 petals
        angle_rad = math.radians(angle)
        petal_x = x + 12 * math.cos(angle_rad)
        petal_y = y + 12 * math.sin(angle_rad)
        canvas.create_oval(
            petal_x - petal_size // 2,
            petal_y - petal_size // 2,
            petal_x + petal_size // 2,
            petal_y + petal_size // 2,
            petal_color,
        )

    # Draw flower center
    canvas.create_oval(
        x - center_size // 2,
        y - center_size // 2,
        x + center_size // 2,
        y + center_size // 2,
        center_color,
    )


if __name__ == "__main__":
    main()
