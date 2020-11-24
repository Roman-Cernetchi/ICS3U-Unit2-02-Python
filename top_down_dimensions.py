#!/usr/bin/env python3
# Created by: Roman Cernetchi
# Created on: November 2020
# This program calculating the area and perimeter of a rectangle
#     while using Top-Down design


def main():
    # This program will calculate Area and Perimeter

    # Input
    length = int(input("Enter the length of the rectangle (mm):"))
    width = int(input("Enter the width of the rectanghle (mm):"))

    # process
    area = length*width
    perimeter = 2*(length+width)

    # Output
    print("")
    print("Area is {}mm^2".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
