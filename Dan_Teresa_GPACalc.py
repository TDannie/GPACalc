
# declaring variables
sum = 0
x = 0
length = 0

# write a loop to provide a promt and receive user's input
# check for input errors and numbers
while True:
    try:
        y = int(input("How many grades would you like to input: "))
        if y <= 0:
            raise ValueError("Please enter a valid number greater than 0.")
        break
    except ValueError:
        print("Please enter a valid number.")

# while :  
# check while length is less than the # of grades input, then add corresponding points to sum.
while length < y:
    grade = input("Enter a letter grade for a course: ").upper()
    if grade == 'A':
        sum = sum + 4.0
        length += 1
    elif grade == 'B':
        sum = sum + 3.0
        length += 1
    elif grade == 'C':
        sum = sum + 2.0
        length += 1
    elif grade == 'D':
        sum = sum + 1.0
        length += 1
    elif grade == 'F':
        sum = sum + 0.0
        length += 1
    else:
        print("Please try again. Enter a letter grade (A, B, C, D, F): ")

    #    pass
    pass
    
# calculate final gpa
if length >= 1:
    final_gpa = sum / float(length)
# print the final result
    print("Your GPA is: " + str(round(final_gpa, 2)))
else:
    ("You did not enter a valid number, please try again.")