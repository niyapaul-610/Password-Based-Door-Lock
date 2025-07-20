# Password-Based Door Lock System

# Set the correct password
correct_password = "ECE123"

# Ask user to enter the password
entered_password = input("Enter the password to unlock the door: ")

# Check if the password matches
if entered_password == correct_password:
    print(" Access Granted! Door Unlocked.")
else:
    print(" Access Denied! Incorrect Password.")
