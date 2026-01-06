def get_positive_value(prompt_text):
    """
    Docstring for get_positive_value

    Prompt the user for value and reprompt when the value is negative
    """
    # prompt for the value
    value = float(input(prompt_text))

    # check if value is positive and reprompt is needed
    while value < 0:
        print("sorry, the value cannot be negative.")

        value = float(input(prompt_text))

    # return value
    return value


length = get_positive_value("What is the length of the rectangle? ")
width = get_positive_value("What is the width of the rectangle? ")

area = length * width

print(f"The area is {area}")