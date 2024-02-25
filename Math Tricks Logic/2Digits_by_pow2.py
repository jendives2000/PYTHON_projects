# This is me trying to break down and code a math trick I learnt from a Youtube tutorial.
# The trick applies to any 2 digits number that is > 0 and < 100.
# this is not a trick intended for machines, it's for humans to calculate in a quicker way
# I found the steps very algo-like, so I was curious to see if I can code it out.

# ----------------------------------------------------------------------------
# Here's a breakdown of the steps of the trick, for say, 78²:
# 1. multiply the last digit by itself, so 8² -> gives 64
# 1b. the 4 from 64 is our final number's last digit ([], [], [4]) and we'll add the 6 from 64 to the next step's result
# 2. multiply the first with the 2nd digit and multiply that by 2, so (7 * 8) * 2 -> give (56) * 2 = 112
# 2b. we add to 112 the 6 from step 1b -> gives 118
# 2c. the 8 from 118 is our final number's 2nd digit ([], [8], [4]) and we'll add the 11 from 118 to the next step's result
# 3. multiply the 1st digit by itself, so 7² -> gives 49
# 3b. we add the 11 from step 2c to that, it gives 60
# 3c. 60 is our final result'st 1st digit ([60], [8], [4]) -> 6084
# print(78 * 78)
# ----------------------------------------------------------------------------

import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


# while loop to keep the program running until the user exits it
while True:
    choice = input(
        "\n1. Calculate the ² of a 2 digits number > 9 and < 100.\n2. Exit the program.\nPlease enter your choice (1 or 2) --> "
    )
    if choice == "1":

        # list to store the final result digits:
        list_f_result = []

        user_input = input("\nPlease enter a number > 9 and < 100: --> ")
        x = int(user_input[0])
        y = int(user_input[1])
        # to verify the calculation:
        # print(int(user_input) * int(user_input))

        print(f"\ncalculating: {user_input}²")
        time.sleep(1)

        last_digit = str(y * y)  # 1.

        last_digit_is_1digit = len(last_digit) == 1
        last_digit_is_2digits = len(last_digit) == 2

        if not last_digit_is_2digits:  # Meaning last_digit_is_1digit is True
            list_f_result.append(last_digit)
            calc_second_digit = (x * y) * 2
            second_digit = str(calc_second_digit)
        else:  # Meaning last_digit_is_2digits is True
            list_f_result.append(last_digit[1])
            to_add = int(last_digit[0])
            calc_second_digit = ((x * y) * 2) + to_add
            second_digit = str(calc_second_digit)

        second_digit_is_3digits = len(second_digit) == 3
        second_digit_is_2digits = len(second_digit) == 2
        second_digit_is_1digit = len(second_digit) == 1

        if second_digit_is_3digits:
            list_f_result.insert(0, second_digit[2])  # 2c.
            # turning the remainder to be added in 3b into an integer var 'xy':
            x_of_2c = second_digit[0]
            y_of_2c = second_digit[1]
            xy = x_of_2c + y_of_2c
            to_add_from_2c = int(xy)

            first_digit = str((x * x) + to_add_from_2c)  # 3b.
            list_f_result.insert(0, first_digit)  # 3c.
        elif second_digit_is_2digits:
            list_f_result.insert(0, second_digit[1])  # 2c.
            to_add_from_2c = int(second_digit[0])

            first_digit = str((x * x) + to_add_from_2c)  # 3b.
            list_f_result.insert(0, first_digit)  # 3c.
        else:
            list_f_result.insert(0, second_digit[0])  # 2c.

            first_digit = str(x * x)  # 3.
            list_f_result.insert(0, first_digit)  # 3c.

        f_result = list_f_result[0] + list_f_result[1] + list_f_result[2]

        print(CLEAR, CLEAR_AND_RETURN)
        print(f"\n{user_input}² = {f_result}")

    if choice == "2":
        print("\nProgram ended.\n\n")
        quit()
