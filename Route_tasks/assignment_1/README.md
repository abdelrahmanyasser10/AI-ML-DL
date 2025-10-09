Machine Learning Journey: Assignment 1
This repository documents my progress and solutions for the assignments in the Route Academy Machine Learning course. This first assignment focuses on foundational programming concepts in Python.

About This Assignment
Assignment Name: Introduction to Programming
Course: Machine Learning with Route Academy
Instructor: Abdelrahman Yasser Mohamed

This assignment covers a range of introductory Python programming problems designed to build a strong foundation in core concepts like control flow, data structures, and basic algorithms.

Problem Solutions
Below is a brief summary of each problem and the approach taken to solve it.

Problem 1: Maximum and Minimum of Three Numbers

Description: Find the maximum and minimum of three numbers, or check if they're equal and determine if the number is positive or negative.
Approach: The solution uses a series of if/elif statements to compare the three numbers and identify the maximum and minimum values. A special case handles when all three numbers are equal.

Problem 2: Check for Vowel Characters

Description: Check for vowel characters in a user-provided word and print the position of any found vowels.
Approach: The program iterates through the input string, checking each character against a predefined list of vowels. If a match is found, it prints the vowel and its index. The input is converted to lowercase to ensure the check is not case-sensitive.

Problem 3: Display Last Digit

Description: Display the last digit of a given number.
Approach: The modulo operator (%) is used with 10 to extract the last digit of the number.

Problem 4: Divisibility Check

Description: Determine if a number is divisible by both 2 and 3.
Approach: The program uses the modulo operator (%) to check for a remainder of 0 when the input number is divided by 2 and 3. It uses the and operator to ensure both conditions are met.

Problem 5: Class Attendance Percentage

Description: Calculate a student's attendance percentage based on total working days and absent days, and determine if they can sit for an exam (requires 75% attendance or more).
Approach: The code calculates the percentage of days attended and then uses an if/else statement to print whether the student is eligible for the exam. It also includes a check to ensure the number of absent days is not greater than the total working days.

Problem 6: String Case Conversion

Description: Convert a string to all uppercase or all lowercase based on which case has fewer characters.
Approach: The program counts the number of uppercase and lowercase characters. An if/elif block then uses these counts to decide whether to convert the string to uppercase or lowercase.

Problem 7: Palindrome and Armstrong Number Check

Description: Check if a number is a palindrome or an Armstrong number.
Approach: To check for a palindrome, the number is reversed and compared to the original. For an Armstrong number, the sum of each digit raised to the power of the number of digits is calculated and compared to the original number.

Problem 8: Number to Words Conversion

Description: Convert a number (from 0-999) to its word representation (e.g., 124 → One hundred and twenty-four).
Approach: A recursive function handles different ranges of numbers (0-19, 20-99, 100-999) by breaking the number down into its constituent parts and mapping them to their word equivalents.

Problem 9: Series Sum Calculation

Description: Calculate the sum of the series 1+4−9+16−25+36...n terms.
Approach: A loop iterates from 2 to n, adding the square of i if i is even and subtracting it if i is odd. The sum starts with 1.

Problem 10: Count Word Occurrences

Description: Count the occurrences of the word "car" and print their positions in a user-provided string.
Approach: The input string is split into words. The code then loops through the list of words to find and count "car", printing its position (index + 1) each time it's found.

Problem 11: Input Type Processing

Description: Process user input differently based on its type: sum digits for a number, remove spaces for text, or split numbers and text if both are present.
Approach: The solution uses string methods like isdigit() and isalpha() to determine the input type. It then applies the appropriate logic: a loop for digit summation, replace() for space removal, or split() to separate numbers and text.

Problem 12: Average of Tuple of Tuples

Description: Calculate the average of numbers within each inner tuple of a tuple of tuples.
Approach: The code iterates through the outer tuple, using sum() and len() for each inner tuple to compute the average. The results are stored in a new list.

Problem 13: Check and Sort List

Description: Check if a list is empty and, if not, sort it in increasing order.
Approach: The solution checks the length of the list. If it's not empty, it uses the built-in sort() method to sort the list in place.

Problem 14: Remove Even Numbers

Description: Remove all even numbers from a given list.
Approach: A loop iterates through the list in reverse order using list.pop(i) to safely remove even numbers without affecting the indices of subsequent elements.

Problem 15: Extract Elements with High Frequency

Description: Extract elements from a list that have a frequency greater than a specified value K.
Approach: The program counts the frequency of each element and adds it to a result_list if its count is greater than K. A check is added to avoid duplicate entries in the final list.

Problem 16: Sort Dictionary Keys and Values

Description: Sort both the values (lists) and the keys of a dictionary.
Approach: The code first sorts the list of values for each key using list.sort(). It then creates a new dictionary by iterating through the sorted keys to produce the final sorted output.

Problem 17: Student Dictionary Management

Description: Create and manage a dictionary of student information (age and grades) with options to view and edit student data.
Approach: The program uses a while loop to create an interactive menu. It provides options to view, edit, or exit. Input validation is included to handle cases where a student isn't found or invalid data is entered.

