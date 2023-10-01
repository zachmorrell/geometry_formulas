"""
    Zachary Morrell
    CIT 232 - Intro to Programming Logic
    Module 3 Exercise - Geometry Formulas
    September 12, 2023
"""

import math

# Function used to display the options of the program and navigate those options.
def instructions():
    menu_instructions = [
    "\n*       This program is used to solve specific geometry problems       *",
    "*   Option -   Description                                             *",
    "*     0        Display this message again.                             *",
    "*     1        Calculate the area of a sphere using it's radius.       *",
    "*     2        Calculate the volume of a sphere using it's radius.     *",
    "*     3        Calculate the area of a circle based on it's radius.    *",
    "*     4        Calculate the distance between two planes on a 2d plane.*",
    "*     5        To exit the program entirely.                           *"]
    print(("*"*(len(menu_instructions[0])-1)), "\n".join(menu_instructions),"\n" + ("*"*(len(menu_instructions[0])-1)))

    instructions_active = True
    while(instructions_active):
        option = int(input("Which numeric option do you wish to choose: "))
        match(option):
            case 0:
                print(("*"*(len(menu_instructions[0])-1)), "\n".join(menu_instructions),"\n" + ("*"*(len(menu_instructions[0])-1)))
            case 1:
                sphere_area()
            case 2:
                sphere_volume()
            case 3:
                circle_area()
            case 4:
                distance_between_points()
            case 5:
                exit()
            case _:
                print(f"selected {option}")

# Function displayed after each calculation to request if a user would like to perform more calculations, return to the instructions method, or exit the program.
def continue_calc(current_program):
    programs = [instructions, sphere_area, sphere_volume, circle_area, distance_between_points]
    option = input(f"\nWould you like to continue with the {programs[current_program]} program? (y/n/exit): ").lower()
    if(option == "y" or option == "yes"):
        programs[current_program]()
    elif(option == "exit" or option == "e"):
        exit()
    else:
        programs[0]()

# Function calculates the area of a sphere based on it's radius.
def sphere_area():
    
    print("This program calculates the area of a sphere based on it's radius")
    sphere_radius1 = float(input("Enter the radius of a sphere: "))
    sphere_surface_area = round(4 * math.pi * (sphere_radius1**2), 2)
    print(f"The surface area of the sphere is: {sphere_surface_area}")
    continue_calc(1)

# Function calculates the volume of a sphere based on it's radius.
def sphere_volume():

    print("This program calculates the volume of a sphere based on it's radius")
    sphere_radius2 = float(input("Enter the radius of the sphere: "))
    sphere_volume = round((4/3) * math.pi * (sphere_radius2**3), 2)
    print(f"The volume of the sphere is: {sphere_volume}")
    continue_calc(2)

# Function calculates the area of a circle based on it's radius.
def circle_area():

    print("This program calculates the area of a circle based on it's radius")
    circle_radius = float(input("Enter the radius of the circle: "))
    area_of_circle = round(math.pi * (circle_radius**2), 2)
    print(f"The area of the circle is: {area_of_circle}")
    continue_calc(3)

# Function takes the coordinates x1, y1, x2, and y2 and calculates the distance between the sets.
def distance_between_points():

    print("This program calculates the distance between two points on a 2D plane\nYou will input the point values of (x1, y1) and (x2, y2) separately")
    x1, y1, x2, y2 = float(input("Enter point x1: ")), float(input("Enter point y1: ")), float(input("Enter point x2: ")), float(input("Enter point y2: "))
    distance_between_points = round(math.sqrt((x1 - x2)**2 + (y1-y2)**2), 2)
    print(f"The distance between those points is: {distance_between_points}")
    continue_calc(4)

# Starts the program, could be seen as the main().
instructions()
