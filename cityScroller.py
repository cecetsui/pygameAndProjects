#Import needed modules
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

#Helper function : Provides random color
def random_color():
    return random.choice(colors)

# Initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    """
    Used to create the building object

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left().
            A negative integer draws the building left to right ().
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x_point, y_point, width, height, color):
        #Initializing 
        self.x_p = x_point
        self.y_p = y_point
        self.w = width
        self.h = height
        self.c = color

    def draw(self):
        #uses pygame and the global screen variable to draw the building on the screen
        pygame.draw.rect(screen, self.c, [self.x_p, self.y_p, self.w, self.h])

    def move(self, speed):
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right 
            A negative integer moves the building to the left  
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """
        self.x_p -= speed



class Scroller(object):
    """
    Used to create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.w = width
        self.h = height
        self.b = base
        self.c = color
        self.s = speed
        self.buildings = []
        self.add_buildings()



    def add_buildings(self):
        #Will call add_building until there the buildings fill up the width of the scroller.
        cwidth = 0 
        while (cwidth <= self.w):
            self.add_building(cwidth)
            cwidth += self.buildings[-1].w




    def add_building(self, x_location):
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """
        building_width = random.randint((self.w // 20), (self.w // 4))

        max_height = self.b - self.h # this sets the maximum height each building can be

        # The building height will be a random integer between 1/4th and just under the max_height
        building_height = random.randint((max_height // 4), (max_height - 1))

        y_location = self.b - building_height # This tells the building where along the y-axis to draw itself

        self.buildings.append(Building(x_location, y_location, building_width, building_height, self.c))

    def draw_buildings(self):
        #This calls the draw method on each building.
        for build in self.buildings:
            build.draw()

    def move_buildings(self):
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """
        for build in self.buildings:
            build.move(self.s)
        new_building_location = self.buildings[-1].x_p  + self.buildings[-1].w
        self.add_building(new_building_location)

#Define colors of the scrollers
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)


#Creating Scroller objects
front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic: Move the scrollers to new position (move buildings)
    back_scroller.move_buildings()
    middle_scroller.move_buildings()
    front_scroller.move_buildings()

    # --- Screen-clearing: Clear screen and redraw to make the allusion it is moving
    screen.fill(BACKGROUND_COLOR)

    # --- Redraw the buildings after moving and clearing screen 
    back_scroller.draw_buildings()
    middle_scroller.draw_buildings()
    front_scroller.draw_buildings()


    # --- Go ahead and update the screen with what was drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
