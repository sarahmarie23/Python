# CS 232 Spring 2022 - Week 10 Lab
# Purpose: To practice using a class and calling its functions.

import math

class Car():
    def __init__(self, x_pos=0, y_pos=0):
        self.x = x_pos
        self.y = y_pos
        self.direction = 0
        self.speed = 0

    # left_or_right is a string "left" or "right"
    # direction is stored as an int as follows:
    #                     0
    #                     |
    #                 3 --+-- 1
    #                     |
    #                     2
    #
    def turn(self, left_or_right):

        if left_or_right == 'left':
            self.direction = 3
        elif left_or_right == 'right':
            self.direction = 1
    
    # time is number of time units to drive forward
    # (speed = distance drive per unit of time)
    def drive(self, time):
       
        if self.direction == 0:
            self.y = self.y + (self.speed * time)
            
        elif self.direction == 1:
            self.x = self.y + (self.speed * time)
            
        elif self.direction == 2:
            self.y = self.y - (self.speed * time)
            
        else:
            self.x = self.x - (self.speed * time)
            

        
            
    # Print all values of data members of object
    # Make it look pretty and readable!
    def print_status(self):
        
        print("*** CAR STATUS ***")
        print("Current position is ({},{})".format(self.x, self.y))
        print("Current speed is {}".format(self.speed))
        print("Current direction is", end=' ')

        if self.direction == 0:
            print('up')
        elif self.direction == 1:
            print('right')
        elif self.direction == 2:
            print('down')
        elif self.direction == 3:
            print('left')

        print("\n")
        
    # amount is change in speed - positive value
    # means speed up, negative means slow down --
    # note that it's possible to go backwards!
    def accelerate(self, amount):

        if amount > 0:
            self.speed += amount
            
            
    # set speed to 0
    def stop(self):
        self.speed = 0
    
    # Calculate and print distance from (0,0)
    def distance_from_origin(self):
        distance = math.sqrt(self.x**2 + self.y**2)
        print("Car's distance from (0,0) is {:.2f} units".format(distance))




