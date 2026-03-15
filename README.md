Last updated 15 March 2026.
# Simple-Expense-Tracker
A simple expense tracker in python (Using a Command-Line Interface)

This expense tracker takes 3 inputs:
1. What did the user spend on 
2. How much the user spent
3. What category the user would like to input

The program will also save those 3 inputs to a text file with a date using python's with and open functions.
The program also checks if the values entered are valid or not (For the specific input, and uses error handling in order for the program to continue running.)

The program has 2 main functions:
1. Adding a new expense which will append to the text file for easy reading
2. Directly reading expenses from the text file in the CLI


What I learned through this project:
1. File I/O, how to read and write text files directly in python
2. How to properly use error handling in the real world
3. Input Validation
4. How to use the datetime module
5. Membership checking with a list through the in operator


## How to Run
1. Make sure you have Python installed
2. Run the following command in your terminal:
```
python expenses.py
```