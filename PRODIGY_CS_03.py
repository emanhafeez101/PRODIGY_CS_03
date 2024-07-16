import re

def password_complexity_checker(password):
    """
    Checks the complexity of a given password based on specific criteria:
    - Length of at least 8 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one special character
    - Contains at least one number

    Prints the strength of the password as 'Strong password', 'Good password', or 'Weak password' based on the total score.

    :param password: The password string to be evaluated.
    """
    
    # Check if password length is at least 8 characters
    len_score = len(password) >= 8
    
    # Check if password contains at least one uppercase letter
    uppercase_score = bool(re.search(r'[A-Z]', password))
    
    # Check if password contains at least one lowercase letter
    lowercase_score = bool(re.search(r'[a-z]', password))
    
    # Check if password contains at least one special character
    special_char_score = bool(re.search(r'[!@#$%^&*()_+|":><?]', password))
    
    # Check if password contains at least one number
    number_score = bool(re.search(r'[0-9]', password))
    
    # Calculate total score based on the presence of the criteria
    total_score = len_score + uppercase_score + lowercase_score + special_char_score + number_score
    
    # Provide feedback based on the total score
    if total_score == 5:
        print("Strong password")
    elif total_score >= 3:
        print("Good password")
    else:
        print("Weak password")

# Prompt user to enter a password
password = input("Enter a password: ")

# Check the complexity of the entered password
password_complexity_checker(password)
