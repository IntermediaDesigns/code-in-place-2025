## Assignment

Students in Code in Place are from 150 different countries! Wow. Let's celebrate our international class by drawing flags. To start out, one of the most straightforward flags to draw using Python graphics is the flag of Indonesia:

There is 1 shape on the canvas. Red rectangle with transparent outline starting at (0, 0) and ending at (450, 150).

The dimensions of your flag should be based off the provided constants:

# The width of the canvas

CANVAS_WIDTH = 450

# The height of the canvas

CANVAS_HEIGHT = 300
To draw the Indonesian flag all you need to do is to draw a single red rectangle which covers the top half of the graphics canvas. You don't need to draw the white stripe, the canvas is white by default.

Recall the graphics method for drawing a colored rectangle:

# Draws a rectangle with specified color

rect = canvas.create_rectangle(
left_x,
top_y,
right_x,
bottom_y,
color
)

Once you have drawn the Indonesian flag, push the "check correct" button underneath the canvas to get it graded.

After that, feel free to get creative. Consider making up your own flag! Can you think of a design that would represent your friends, family, or a group that doesn't have a flag?
