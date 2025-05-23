from graphics import Canvas
import math
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Create black space background
    background = canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "black")

    # Galaxy center coordinates
    center_x = CANVAS_WIDTH // 2
    center_y = CANVAS_HEIGHT // 2

    # Create glowing galaxy center
    center_glow = canvas.create_oval(
        center_x - 15, center_y - 15, center_x + 15, center_y + 15, "#FFFF80", "#FFAA00"
    )
    center_core = canvas.create_oval(
        center_x - 8, center_y - 8, center_x + 8, center_y + 8, "#FFFFFF", "#FFDD00"
    )

    # Store spiral arm objects
    spiral_arms = []
    stars = []

    # Create initial spiral arms and stars
    for arm in range(3):  # 3 spiral arms
        arm_objects = []
        for i in range(30):  # Points along each arm
            angle_offset = arm * (2 * math.pi / 3)  # 120 degrees apart
            radius = i * 4 + 20
            angle = (i * 0.3) + angle_offset

            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)

            # Create spiral arm segments with varying colors
            if radius < 60:
                color = "#FFAA44"
            elif radius < 100:
                color = "#AAAA88"
            else:
                color = "#6688AA"

            if 0 <= x <= CANVAS_WIDTH and 0 <= y <= CANVAS_HEIGHT:
                size = max(1, 6 - i // 8)
                obj = canvas.create_oval(x - size, y - size, x + size, y + size, color)
                arm_objects.append(
                    {"obj": obj, "radius": radius, "base_angle": i * 0.3}
                )

        spiral_arms.append(arm_objects)

    # Create random background stars
    for _ in range(50):
        x = random.randint(0, CANVAS_WIDTH)
        y = random.randint(0, CANVAS_HEIGHT)
        size = random.randint(1, 2)
        brightness = random.choice(["#FFFFFF", "#FFFFAA", "#AAAAFF", "#FFAAAA"])
        star = canvas.create_oval(x - size, y - size, x + size, y + size, brightness)
        stars.append(star)

    # Animation loop
    rotation_angle = 0
    frame_count = 0

    while True:
        # Update spiral arms rotation
        for arm_idx, arm_objects in enumerate(spiral_arms):
            angle_offset = arm_idx * (2 * math.pi / 3)

            for point in arm_objects:
                radius = point["radius"]
                base_angle = point["base_angle"]

                # Calculate new position with rotation
                angle = base_angle + angle_offset + rotation_angle
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)

                # Move the object to new position
                if 0 <= x <= CANVAS_WIDTH and 0 <= y <= CANVAS_HEIGHT:
                    canvas.moveto(point["obj"], x, y)
                    canvas.set_hidden(point["obj"], False)
                else:
                    canvas.set_hidden(point["obj"], True)

        # Pulse the galaxy center
        pulse = math.sin(frame_count * 0.1) * 0.3 + 0.7
        center_size = int(15 * pulse)
        core_size = int(8 * pulse)

        # Update center glow
        canvas.moveto(center_glow, center_x - center_size, center_y - center_size)
        canvas.moveto(center_core, center_x - core_size, center_y - core_size)

        # Twinkle random stars
        if frame_count % 10 == 0:
            for _ in range(3):
                star = random.choice(stars)
                colors = ["#FFFFFF", "#FFFFAA", "#AAAAFF", "#FFAAAA"]
                canvas.set_color(star, random.choice(colors))

        # Check for user input to exit
        key = canvas.get_last_key_press()
        if key == "q":
            break

        # Update rotation and frame count
        rotation_angle += 0.02
        frame_count += 1

        # Small delay for smooth animation
        time.sleep(0.05)

    # Keep the final image displayed
    canvas.wait_for_click()


if __name__ == "__main__":
    main()
