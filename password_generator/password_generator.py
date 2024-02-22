# This is me trying to follow a tutorial on how to create a password manager
# where I set a password min length and enforces it
# ----------------------------------------------------------------------------

import random
import string  # permits to grab ALL characters to be used in a PWD


# The 2nd and 3rd param are OPTIONAL.
def generate_password(
    param_min_length, param_numbers=True, param_special_characters=True
):
    # list: all alphabet letters (from string module)
    allowed_letters = string.ascii_letters

    # list: all numbers (from string module)
    allowed_numbers = string.digits

    # list: all special chars (from string module)
    allowed_special_chars = string.punctuation

    # Adding ALL the alphabet letters to the generated password
    everything_allowed_for_pwd = allowed_letters
    # now the everything_allowed_for_pwd can include any alphabet letter
    if param_numbers:  # is True
        everything_allowed_for_pwd += allowed_numbers
        # now the everything_allowed_for_pwd is included with ALL number
    if param_special_characters:  # is True
        everything_allowed_for_pwd += allowed_special_chars
        # now the everything_allowed_for_pwd is included with ALL special character

    pwd = ""  # A var storing the password value

    # 3 bool values to structure the following while loop
    meeting_criteria = False
    has_numbers = False
    has_spe_chars = False

    # this while loop functions as:
    # the pwd quality checker
    # and pwd generator
    # as long as meet_criteria is False OR the pwd length doesn't comply keep doing this:
    # which is generating up to X random letters/nums/specials to be inserted into the pwd
    while not meeting_criteria or len(pwd) < param_min_length:
        # generates and stores a random letter/num/special to be inserted into the pwd
        new_char_to_be_inserted = random.choice(everything_allowed_for_pwd)
        # inserts the new_char_to_be_inserted into the pwd
        pwd += new_char_to_be_inserted

        # checks if the new_char_to_be_inserted is in the allowed_numbers list
        if new_char_to_be_inserted in allowed_numbers:
            has_numbers = True
        # if not, checks if the new_char_to_be_inserted is in the allowed_special_chars list
        elif new_char_to_be_inserted in allowed_special_chars:
            has_spe_chars = True

        # because the new char complies as an allowed letter/num/special char
        # meaning the pwd has AT LEAST a letter, a number and a special character
        meeting_criteria = True

        # now we check which param was called and comply with the call
        # !!: the parameters are called True by default (because declared so)
        if param_numbers:  # is True (so, NOT called as False)
            meeting_criteria = has_numbers
            # ongoing compliance
        if param_special_characters:  # is True (so, NOT called as False)
            meeting_criteria = meeting_criteria and has_spe_chars
            # ongoing compliance

    return pwd


# Input prompts:
# an integer for the pwd length
# answering 'n' will set param to false
param_min_length = int(
    input("\nWelcome!\nEnter the minimum length of the password: --> ")
)
has_numbers = input("Do you want to include numbers (y/n)? --> ").lower() == "y"
has_spe_chars = (
    input("Do you want to include special characters (y/n)? --> ").lower() == "y"
)
pwd = generate_password(param_min_length, has_numbers, has_spe_chars)

print("Your generated password is:", pwd)
