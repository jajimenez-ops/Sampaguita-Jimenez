# 5. Student score entry

def get_examination_score():
    while True:
        user_input = input("Please enter the examination score (0-100): ")

        try:
            # Convert the input to a float to support decimals.
            # If the user wants integers only, change float() to int().
            score = float(user_input)

            # Check if the numeric value is within the acceptable range
            if 0 <= score <= 100:
                print(f"Success! Valid score entered: {score}")
                return score
            else:
                print("Error: The score must be between 0 and 100. Please try again.")

        except ValueError:
            # Handle cases where the input cannot be converted to a number (e.g., text or symbols)
            print("Error: Invalid input. You must enter a valid numerical value.")