## Assignment

Let's practice making graphics with lots of repeated elements. This will help us get familiar with working with multiple shapes and pixel calculations!

Make a line of boxes as shown below, such that the boxes fill the bottom of the canvas. Each box should have a width and height of BOX_SIZE, making a total of 5 boxes perfectly in line with one another:

There are 5 shapes on the canvas. White rectangle with black outline starting at (0, 120) and ending at (80, 200). White rectangle with black outline starting at (80, 120) and ending at (160, 200). White rectangle with black outline starting at (160, 120) and ending at (240, 200). White rectangle with black outline starting at (240, 120) and ending at (320, 200). White rectangle with black outline starting at (320, 120) and ending at (400, 200).

To make each individual box visible instead of making a single rectangular box, add optional arguments to your create_rectangle(...) call. The first optional argument is the fill color (in this case "white") and the second optional argument is the outline color (in this case "black"). Calling the function when you add these should look like this:

# Creates a white rectangle

# with a black outline

canvas.create_rectangle(
left_x,
top_y,
right_x,
bottom_y,
"white",
"black"
)

You should use a for loop to create your row. As an aside: it is possible to solve this problem without a for loop, but that would defeat the point of the assignment!

for i in range(N_BOXES):
The most elegant solution is to use the value of i to compute the left_x of the current box.

Once you're done, push the "Check Correct" button.

As an extension, change CANVAS_HEIGHT to be 400 and see if you can fill the entire canvas with boxes to make a 5x5 grid of squares!
