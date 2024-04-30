#!/usr/bin/env python
# coding: utf-8

# ## “How Old is Your Dog in Human Years?” Calculator
# 
# In this assignment, you will write a program that calculates a dog’s age in human years.
# The program will prompt the user for an age in dog years and calculate that age in human years.
# Allow for int or float values, but check the user’s input to make sure it's valid -- it should be numeric and positive.
# Otherwise, let the user know their input is not valid.
# 
# You can use the following rules to approximately convert a medium-sized dog’s age to human years:
# - For the first year, one dog year is equal to 15 human years
# - For the first 2 years, each dog year is equal to 12 human years
# - For the first 3 years, each dog year is equal to 9.3 human years
# - For the first 4 years, each dog year is equal to 8 human years
# - For the first 5 years, each dog year is equal to 7.2 human years
# - After that, each dog year is equal to 7 human years.  (Note: This means the first 5 dog years are
# equal to 36 human years (5 * 7.2) and the remaining dog years are equal to 7 human years each.)
# 
# Print the result in the following format, substituting for **dog_age** and **human_age**: "The given dog age **dog_age**
# is **human_age** in human years."  Round the result to 2 decimal places.  Note: If there is a 0 in the hundredths place,
# you can drop it, e.g. 24.00 can be displayed as 24.0.

# Considering invalid inputs:
# * Your program must ask the user for an age in dog years - hint: use the input() function
# * We are going to test invalid inputs - make sure that your code can handle negative value inputs and non-numerical inputs!
# * For invalid inputs, make sure that your printed response adheres to the following:
#  - If a text-based input is provided, make sure your response contains the word 'invalid'.  
#  - If a negative input is provided, make sure your response contains the word 'negative'.  


# In[61]:


import traceback

def calculator():
    # Get dog age
    
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)
        
        if d_age < 0:
            print("input is negative, input postive number")
            
        else:
            if d_age <= 1.0:
                h_age = d_age * 15.0
                h_age = round (h_age, 2)
                print("The given dog age", d_age, "is", h_age, "in human years.")
            elif d_age <= 2.0:
                h_age = d_age * 12.0
                h_age = round (h_age, 2)
                print("The given dog age", d_age, "is", h_age, "in human years.")
            elif d_age <= 3.0:
                h_age = d_age * 9.3
                h_age = round (h_age, 2)
                print("The given dog age", d_age, "is", h_age, "in human years.")
            elif d_age <= 4.0:
                h_age = d_age * 8.0
                h_age = round (h_age, 2)
                print("The given dog age", d_age, "is", h_age, "in human years.")
            elif d_age <= 5.0:
                h_age = d_age * 7.2
                h_age = round (h_age, 2)
                print("The given dog age", d_age, "is", h_age, "in human years.")
            else:
                h_age = ((d_age - 5) * 7) + 36
                h_age = round (h_age, 2)
                print("The given dog age", d_age, "is", h_age, "in human years.")
        

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
    
        
    except ValueError as e:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function




