from graphics import *
from time import sleep

acceptableSizes = [5, 7, 9]
acceptableColours = ["red", "green", "blue", "magenta", "orange", "pink"]
abbbrevColours = ['r', 'g', 'b', 'm', 'o', 'p']

def drawPatch3(win, x, y, colour):
    """
    Params:
    -------
        win: window to be drawn in
        x,y : positions of patches
        colour: the colour of Patch
    
    Return:
    -------
        The Third Patch of the Graph in last third part
    """
    circleRadius = 10
    circleY = circleRadius
    circleX = circleRadius
    
    for row in range(1, 6):
        for col in range(1, 6):
            # Calculate circle x,y.
            circleY = y + (row * (circleRadius * 2)) - circleRadius
            circleX = x + (col * (circleRadius * 2)) - circleRadius
            
            circle = Circle(Point(circleX, circleY), circleRadius)
            circle.setOutline(colour)
            
            # If row is odd, set color to specified colour else white.
            if row % 2 == 1:
                circle.setFill(colour)
            else:
                circle.setFill("white")
            
            circle.draw(win)

def drawBorderLines(win, x, y, colour):
    """
    Border lines to deffrentiate between patches and each other 

    Params:
    -------
        win: window to be drawn in
        x,y : positions of patches
        colour: the colour of Patch
    
    Return:
    -------
        The Third Patch of the Graph in last third part
    """
    # Vertical lines.
    for vx in range(1, 4):
        lineX = x + (vx * 25)
        lineBreak = Line(Point(lineX, y), Point(lineX, y + 100))
        lineBreak.draw(win)
        
    # Horizontal lines.
    for hy in range(1, 4):
        lineY = y + (hy * 25)
        lineBreak = Line(Point(x, lineY), Point(x + 100, lineY))
        lineBreak.draw(win)
        
def drawH(win, x, y, width, height, color, flip, invert):
    # Space per row.
    widthSpace = width / 5
    heightSpace = height / 5
    
    # Invert color if specified.
    fillColor = color
    spaceColor = "white"
    if invert:
        fillColor = "white"
        spaceColor = color
    
    # Draw background.
    background = Rectangle(Point(x, y), Point(x + width, y + height))
    background.setFill(fillColor)
    background.setOutline(fillColor)
    background.draw(win)
    
    # Calculate position of top element depending on x,y,w,h and flip status.
    topPos1 = Point(x + widthSpace, y)
    topPos2 = Point(x + (width - widthSpace), y + ((height / 2) - (heightSpace / 2)))
    if flip:
        topPos1 = Point(x, y + heightSpace)
        topPos2 = Point(x + ((width / 2) - (widthSpace / 2)), y + (height - heightSpace))
    
    # Draw top element.
    topElement = Rectangle(topPos1, topPos2)
    topElement.setFill(spaceColor)
    topElement.setOutline(spaceColor)
    topElement.draw(win)
    
    # Calculate position of top element depending on x,y,w,h and flip status.
    bottomPos1 = Point(x + widthSpace, y + ((height / 2) + (heightSpace / 2)))
    bottomPos2 = Point(x + (width - widthSpace), y + height)
    if flip:
        bottomPos1 = Point(x + ((width / 2) + (widthSpace / 2)), y + heightSpace)
        bottomPos2 = Point(x + width, y + (height - heightSpace))
    
    # Draw bottom element.
    bottomElement = Rectangle(bottomPos1, bottomPos2)
    bottomElement.setFill(spaceColor)
    bottomElement.setOutline(spaceColor)
    bottomElement.draw(win)
        
def drawPatch1(win, x, y, colour):
    """
    First Patch to be drawn in final Graph

    Params:
    -------
        win: window to be drawn in
        x,y : positions of patches
        colour: the colour of Patch
    
    Return:
    -------
        The Third Patch of the Graph in last first part
    """  
    for row in range(4):
        for col in range(4):
            # Calculate x and y for each H.
            hX = x + (col * 25)
            hY = y + (row * 25)
            
            # Invert colours if row is odd.
            invert = col > 1
            if row % 2 == 1:
                invert = col < 2
                
            # Draw H function.
            drawH(win, hX, hY, 25, 25, colour, col % 2, invert)
    
    # Draw black border lines.
    drawBorderLines(win, x, y, "black")
    
def drawPatchwork(size, colourList):
    """
    Params:
    ------
        size: eligible sizes of final window (5x5, 7x7, 9x9)
        colourList: eligible colour to make shapes colored with (red, green, blue, magenta, orange, pink)

    Return:
    ------
        Draws final shape
    """
    # Initalize window.
    win = GraphWin("Patchwork", size * 100, size * 100)
    
    # Draw grid of patches.
    for row in range(size):
        for col in range(size):
            # Calculate x, y for each patch.
            x = col * 100
            y = row * 100
            
            # Colour depending on position of patch.
            patchColour = colourList[0]
            
            # Diagonal and below.
            yDiff = ((size * 100) - y)
            if (x + 100) == yDiff:
                patchColour = colourList[1]
            elif (x + 100) > yDiff:
                patchColour = colourList[2]
            
            # Vertical and Horizontal.
            sideValue = (size - 1) * 100
            if (x == sideValue) or (y == sideValue):
                patchColour = colourList[1]
                
            
            # If even and below diagonal then draw patch 1 else patch 3.
            if (col % 2 == 0) and ((x + 100) >= yDiff):
                drawPatch3(win, x, y, patchColour)
            else:
                drawPatch1(win, x, y, patchColour)

def draw_shape(win, center, size, color, shape_type):
    """
    Draw a square on the graphics window.

    Params:
    ------
        win: GraphWin object, the graphics window
        center: Point object, the center of the square
        size: int, the size of the square
        color: str, the fill color of the square
        shape_type: type of shape
    """
    half_size = size / 2
    x, y = center.getX(), center.getY()

    if shape_type == "square":
        shape = Rectangle(Point(x - half_size, y - half_size), Point(x + half_size, y + half_size))
    elif shape_type == "circle":
        shape = Circle(center, half_size)
        shape.setOutline(color)

    shape.setFill(color)
    shape.draw(win)

def draw_combined_shape(win, center, size, color, shape_type="combined_circles", spacing=-17):
    """
    Draw a shape on the graphics window.

    Parameters:
    - win: GraphWin object, the graphics window
    - center: Point object, the center of the shape
    - size: int, the size of the shape (radius for circles)
    - color: str, the fill color of the shape
    - shape_type: str, the type of shape to draw
    """
    x, y = center.getX(), center.getY()

    if shape_type == "combined_circles":
       # Draw two circles intersecting to form a combined shape
        half_size = size / 2

        # Draw the rectangle
        rectangle = Rectangle(Point(x - half_size - spacing, y - half_size), Point(x + half_size + spacing, y + half_size))
        rectangle.setFill(color)
        rectangle.setOutline(color)
        rectangle.draw(win)

        # Calculate the radius of the circles based on the size of the rectangle
        circle_radius = size / 2

        # Draw the circles on the sides of the rectangle with spacing
        circle1 = Circle(Point(x - half_size - spacing, y), circle_radius)
        circle1.setFill(color)
        circle1.setOutline(color)
        circle1.draw(win)

        circle2 = Circle(Point(x + half_size + spacing, y), circle_radius)
        circle2.setFill(color)
        circle2.setOutline(color)
        circle2.draw(win)

def draw_circles_with_tangent_point(win, center, grid_size=5, initial_radius=-2, increment=4, color='orange', IncX=42, IncY=30, col=1):
    """
    Draws circles on a GraphWin with a common tangent point.

    Params:
    ------
        grid_size (int): The size of the grid (5, 7, or 9).
        num_circles (int): The number of additional circles to draw.
        initial_radius (int): The radius of the initial circle.
        increment (int): The increment in radius for each additional circle.
    """

    # # Calculate window dimensions based on the grid size
    # win_width = grid_size * 5
    # win_height = grid_size * 10

    # Set the x-axis at the center of the window
    if col == 1:
        x_axis = center.getX() //2 + IncX
        y_axis = center.getY() + IncY
        # Calculate the center of the initial circle with the bottom touching the bottom of the window
        initial_center_x = x_axis +10
        initial_center_y = y_axis - initial_radius +10
    else:
        x_axis = center.getX() //2 + IncX+ col*6
        y_axis = center.getY() + IncY 
        # Calculate the center of the initial circle with the bottom touching the bottom of the window
        initial_center_x = x_axis +13*col
        initial_center_y = y_axis - initial_radius +10*col

    if grid_size == 5 : num_circles=7
    elif grid_size == 7: num_circles=7
    elif grid_size ==9 : num_circles=7

    # Create a Point object for the center of the initial circle
    initial_center_point = Point(initial_center_x, initial_center_y)

    # Draw the initial circle
    initial_circle = Circle(initial_center_point, initial_radius)
    initial_circle.setOutline(color)
    initial_circle.draw(win)

    # Set the common tangent point
    tangent_point_x = initial_center_x
    tangent_point_y = y_axis

    # Draw additional circles with increasing radii and the same tangent point
    for i in range(1, num_circles + 1):
        radius = initial_radius + i * increment  # You can adjust the increment as needed

        # Calculate the center of the current circle
        center_x = tangent_point_x
        center_y = tangent_point_y - radius

        # Create a Point object for the center of the current circle
        center_point = Point(center_x, center_y)

        # Draw the current circle
        current_circle = Circle(center_point, radius)
        current_circle.setOutline(color)
        current_circle.draw(win)

def draw_Penultimate_digit(win, center, color, col):
    """
    Draws multiple rectangles with circles on both sides in a graphics window.

    Parameters:
    - movement (int): The amount of movement to the right.
    - upwards (int): The vertical offset.
    - color (str): The color of the shapes.
    - rect_width (int): The width of the rectangle.
    - rect_height (int): The height of the rectangle.
    - circle_radius (int): The radius of the circles.
    - grid_size (int): The number of rows in the grid.

    Returns:
    - None
    """
    x = center.getX()
    y = center.getY()
    # Create a graphics window
    if col > 1:
        if col == 2: 
            x = center.getX() -25 +col -4
            y = center.getY() -25 
        elif col == 3:
            x = center.getX() - 25 +col -4 
            y = center.getY() -25 
        elif col ==4:
            x = center.getX() - 25 +col - 4
            y = center.getY() -25
        elif col ==5:
            x = center.getX() - 25 +col - 4
            y = center.getY() -25
        elif col ==6:
            x = center.getX() - 25 +col +3
            y = center.getY() -25
        elif col ==7:
            x = center.getX() - 25 +col +20
            y = center.getY() -25 
        elif col ==8:
            x = center.getX() - 25 +col-5
            y = center.getY() -25
        elif col ==9:
            x = center.getX() - 25 +col-10
            y = center.getY() -25
    else:

        x = center.getX() - 25
        y = center.getY() - 25

    if col ==1:
        movement=12 +x
    elif col ==2 :
        movement=12 +x +1
    elif col==3:
        movement=12 +x + 4
    elif col ==6:
        movement=12 +x -10
    elif col ==7:
        movement=12 +x -5
    elif col ==8:
        movement=12 +x -5
    else:
        movement=12 +x

    upwards=4 + y 
    rect_width=7
    rect_height=7
    circle_radius=3.7

    grid_size=5

    normal_upwards = upwards
    ARRG = 5

    for row in range(0, grid_size):
        # Set the rectangle parameters
        if row % 2 != 0:
            if col == 2:
                rectangle = Rectangle(Point(ARRG+50, upwards), Point(ARRG +50+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +53, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+50, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+50, upwards + rect_height/2), circle_radius)

            elif col == 3:
                rectangle = Rectangle(Point(ARRG+103, upwards), Point(ARRG +103+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +107, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+103, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+103, upwards + rect_height/2), circle_radius)

            elif col == 4:
                rectangle = Rectangle(Point(ARRG+151, upwards), Point(ARRG +151+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +155, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+151, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+151, upwards + rect_height/2), circle_radius)

            elif col == 5:
                rectangle = Rectangle(Point(ARRG+202, upwards), Point(ARRG +202+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +205, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+202, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+202, upwards + rect_height/2), circle_radius)

            elif col == 6:
                rectangle = Rectangle(Point(ARRG+248, upwards), Point(ARRG +248+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +252, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+248, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+248, upwards + rect_height/2), circle_radius)

            elif col == 7:
                rectangle = Rectangle(Point(ARRG+298, upwards), Point(ARRG +298+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +302, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+298, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+298, upwards + rect_height/2), circle_radius)
            
            elif col == 8:
                rectangle = Rectangle(Point(ARRG+348, upwards), Point(ARRG +348+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +352, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+348, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+348, upwards + rect_height/2), circle_radius)

            elif col == 9:
                rectangle = Rectangle(Point(ARRG+398, upwards), Point(ARRG +398+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +402, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+398, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+398, upwards + rect_height/2), circle_radius)

            else:
                rectangle = Rectangle(Point(ARRG+2, upwards), Point(ARRG +2+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +4, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width, upwards + rect_height/2), circle_radius)
        else:
            extra_circle = Circle(Point(movement  - circle_radius*2, upwards + rect_height/2), circle_radius)
            rectangle = Rectangle(Point(movement, upwards), Point(movement + rect_width, upwards + rect_height))
            # Set the circle parameters
            left_circle = Circle(Point(movement, upwards + rect_height/2), circle_radius)
            right_circle = Circle(Point(movement + rect_width, upwards + rect_height/2), circle_radius)

        rectangle.setFill(color)
        rectangle.setOutline(color)
        
        left_circle.setFill(color)
        left_circle.setOutline(color)
        right_circle.setFill(color)
        right_circle.setOutline(color)
        extra_circle.setFill(color)
        extra_circle.setOutline(color)

        rectangle.draw(win)
        left_circle.draw(win)
        right_circle.draw(win)
        extra_circle.draw(win)

        # Update the vertical offset for the next duplicate
        upwards += rect_height + 2  # Adjust the vertical spacing

    movement = movement*3.1
    upwards = normal_upwards
    ARRG = 30

    for row in range(0, grid_size):
        # Set the rectangle parameters
        if row % 2 != 0:
            if col == 2:
                rectangle = Rectangle(Point(ARRG+50, upwards), Point(ARRG +50+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +53, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+50, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+50, upwards + rect_height/2), circle_radius)

            elif col == 3:
                rectangle = Rectangle(Point(ARRG+103, upwards), Point(ARRG +103+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +107, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+103, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+103, upwards + rect_height/2), circle_radius)

            elif col == 4:
                rectangle = Rectangle(Point(ARRG+151, upwards), Point(ARRG +151+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +155, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+151, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+151, upwards + rect_height/2), circle_radius)

            elif col == 5:
                rectangle = Rectangle(Point(ARRG+202, upwards), Point(ARRG +202+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +205, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+202, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+202, upwards + rect_height/2), circle_radius)

            elif col == 6:
                rectangle = Rectangle(Point(ARRG+248, upwards), Point(ARRG +248+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +252, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+248, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+248, upwards + rect_height/2), circle_radius)

            elif col == 7:
                rectangle = Rectangle(Point(ARRG+298, upwards), Point(ARRG +298+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +302, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+298, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+298, upwards + rect_height/2), circle_radius)
            
            elif col == 8:
                rectangle = Rectangle(Point(ARRG+348, upwards), Point(ARRG +348+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +352, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+348, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+348, upwards + rect_height/2), circle_radius)

            elif col == 9:
                rectangle = Rectangle(Point(ARRG+398, upwards), Point(ARRG +398+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +402, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG+398, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width+398, upwards + rect_height/2), circle_radius)

            else:
                rectangle = Rectangle(Point(ARRG+2, upwards), Point(ARRG +2+ rect_width, upwards + rect_height))
                extra_circle = Circle(Point(ARRG + rect_width + circle_radius +4, upwards + rect_height/2), circle_radius)
                # Set the circle parameters
                left_circle = Circle(Point(ARRG, upwards + rect_height/2), circle_radius)
                right_circle = Circle(Point(ARRG + rect_width, upwards + rect_height/2), circle_radius)
        else:
            extra_circle = Circle(Point(movement  - circle_radius*2, upwards + rect_height/2), circle_radius)
            rectangle = Rectangle(Point(movement+10, upwards), Point(movement + rect_width, upwards + rect_height))
            # Set the circle parameters
            left_circle = Circle(Point(movement, upwards + rect_height/2), circle_radius)
            right_circle = Circle(Point(movement + rect_width, upwards + rect_height/2), circle_radius)

        rectangle.setFill(color)
        rectangle.setOutline(color)
        rectangle.draw(win)

        left_circle.setFill(color)
        left_circle.setOutline(color)
        right_circle.setFill(color)
        right_circle.setOutline(color)
        extra_circle.setFill(color)
        extra_circle.setOutline(color)

        left_circle.draw(win)
        right_circle.draw(win)
        extra_circle.draw(win)

        # Update the vertical offset for the next duplicate
        upwards += rect_height + 2  # Adjust the vertical spacing

def draw_PatchWorkAns(window_size:int,
                 color_list:list):
    """
    Draw a pattern of squares with specified colors on a graphics window.

    The user is prompted to choose the size of the window (5x5, 7x7, or 9x9).
    The pattern includes blue squares in the first and last rows and columns,
    and a triangular pattern of red squares with orange squares filling the rest.
    """
    # Create a graphics window
    win_size = window_size * 50  # Adjust the window size based on the square size
    win = GraphWin("Patchwork Output", win_size, win_size)

    # Define square parameters
    shape_size = 50
    num_rows = window_size
    num_cols = window_size

    # Define colors
    first_last_row_column_color = color_list[0]
    third_color = color_list[2]

    # Draw patches of flat squares with specified colors
    for row in range(num_rows):
        for col in range(num_cols):
            x = (col + 0.5) * shape_size
            y = (row + 0.5) * shape_size
            center = Point(x, y)

            if row == 0 or row == num_rows - 1 or col == 0 or col == num_cols - 1:
                color = first_last_row_column_color
            elif col >= num_cols - row:
                color = third_color
                shape_type = "square"
            else:
                color = color_list[1]

            if row%2 == 0 and color != color_list[1]:
                shape_type = "circle"
            elif row%2 == 0 and color == color_list[1]:
                shape_type = 'combined'
            else: 
                shape_type = 'square'

            if shape_type == 'combined':
                draw_circles_with_tangent_point(win, center, window_size, color=color, IncX=30, IncY=26, col=col)
            elif shape_type == 'circle':
                draw_Penultimate_digit(win, center, color, col+1)
            else:
                draw_shape(win, center, shape_size, color, shape_type)

    # Wait for a click and then close the window
    win.getMouse()
    win.close()

