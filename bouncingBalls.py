#Importing needed modules
import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKYBLUE = (135, 206, 250)
TURQ = (64, 224, 208)

#Screen dimensions
SCREEN_H = 500
SCREEN_W = 700

pygame.init()

# Set the width and height of the screen [width, height]
size = (SCREEN_W, SCREEN_H)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Manage how fast the screen updates
clock = pygame.time.Clock()

#Creating the Ball Class
class Ball:
    """
    Used to create the Ball object

    It takes:
    screen - Where to draw/display the object
    x - Starting x position of the ball
    y - Starting y position of the ball
    xSpeed - Speed of the x position of the ball
    ySpeed - Speed of the y position of the ball
    width - Width of the ball
    colorList - List of colors to make the ball "flash"

    """
    def __init__(self, screen, x, y, xSpeed, ySpeed, width, colorList):
        #Initializing ball instance variables
        self.screen = screen
        self.x = x
        self.y = y
        self.x_speed = xSpeed
        self.y_speed = ySpeed
        self.ball_width = width
        self.color_list = colorList
        self.ball_color = self.color_list[random.randint(0,len(self.color_list)-1)]
    #Function nextPos: Moves (Calculates) the ball to the next position
    def nextPos(self):
        #If the ball hits the right or left walls of the screen, it will move the opposite direction
        if self.x <= (self.ball_width) or self.x >= (700 - (self.ball_width)):
            self.x_speed = -1 * self.x_speed
        #If the ball hits the top or bottom walls of the screen, it will move the opposite direction
        if self.y <= (self.ball_width) or self.y >= (500 - (self.ball_width)):
            self.y_speed = -1 * self.y_speed
        #Move the ball to the next location.
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        #Set a new ball color
        self.ball_color = self.color_list[random.randint(0, len(self.color_list) - 1)]
    #Function draw: Draws the ball on the canvas to show movement
    def draw(self):
        pygame.draw.circle(self.screen, self.ball_color, (self.x,self.y), self.ball_width, 0)


#Creating Random Balls
def createRandBall():
    #Get random values
    x = random.randint(0, 700)
    y = random.randint(0, 500)

    x_speed = random.randint(-10,10)
    y_speed = random.randint(-10,10)

    ball_width = random.randint(20,30)

    #Create color list : colors are globally defined
    colors= [BLACK, WHITE, GREEN, RED, BLUE, SKYBLUE,TURQ]

    #Creating a Ball Object with random values
    return Ball(screen, x, y, x_speed,y_speed, ball_width, colors)

#Creating my Ball Objects
ball1 = createRandBall()
ball2 = createRandBall()
ball3 = createRandBall()

#Ball List
balls = [ball1, ball2, ball3]

# -------- Main Program Loop -----------
while done == False:
    # --- Main event loop: Checks for events with each loop/frame
    for event in pygame.event.get():
        #If the "x" button was hit, quit (done with game)
        if event.type == pygame.QUIT:
            done = True
        #If the mouse pressed down on the canvas
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Get the mouses position
            mouse_pos = pygame.mouse.get_pos()
            #Move a random ball to that mouse position
            moveBall = balls[random.randint(0, len(balls) - 1)]
            moveBall.x = mouse_pos[0]
            moveBall.y = mouse_pos[1]

    # --- Game logic: Where the balls need to calculate their next position
    ball1.nextPos()
    ball2.nextPos()
    ball3.nextPos()
     

    # --- Screen-clearing code: We need to clear the screen and redraw the next position to make the allusion it is moving
    screen.fill(TURQ)

    # --- Drawing code should go here
    
    # Because we need to re-draw the circle each time (since we cleared the screen), we need to re-draw the balls
    ball1.draw()
    ball2.draw()
    ball3.draw()

    # --- Go ahead and update the screen with what was drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
