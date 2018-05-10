#Area Calculator.py
"""
Created on Wed May  9 18:44:06 2018
@author: kmuss
"""
"""This calculator calculates the area of a shape based on which shape the user selects. """
from math import pi 
from time import sleep 
from datetime import datetime 
now = datetime.now()
print("Welcome to  the Area Calculator!")
print("It is now %s/%s/%s %02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)
hint = "When submitting your answer, don\'t forget to include the correct units! \nExiting... Run again to calculate a new area."
option = input("Enter C for Circle or T for Triangle: ")
option = option.upper()
if option == 'C': 
  radius = float(input("What is the radius?"))
  area = pi * radius **2 
  print("The pie is baking...")
  sleep(1)
  print("Area: %.2f \n %s" % (area, hint))
elif option == 'T': 
  base = float(input("What is the base of the triange?"))
  height = float(input("What is the height of the triange?"))
  area = base * height / 2 
  print("Uni Bi Tri...")
  sleep(1)
  print("Area: %.2f \n %s" % (area, hint))
else: 
  print("This value is garbage. \n The program will now exit")
