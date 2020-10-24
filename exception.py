from time import sleep


def get_user_choice(input_prompt, valid_option_list):
    """
    continuously asks user to input one of the valid options, or q to quit
    :str input_prompt:
    :list valid_option_list:
    :return user_input, or None if quitting:
    """
    while True:
        try:
            user_choice = input(input_prompt)
            if user_choice == 'q':
                return None
            if user_choice not in valid_option_list:
                raise ValueError
        except ValueError:
            print('Invalid choice! Please try again.')
            sleep(1)
        else:
            break
    return user_choice


def get_user_qty(input_prompt, max_value, min_value=0):
    """
    continuously asks user to input one of the valid options, or q to quit
    :str input_prompt:
    :float max_value maximum acceptable value:
    :float min_value min acceptable value, default 0:
    :return user_input, or None if quitting:

    """
    while True:
        try:
            user_input = input(input_prompt)

            # shouldn't try to cast to float prior to checking if user is quitting
            if user_input == 'q':
                return None
            user_qty = float(user_input)
            if user_qty > max_value or user_qty < min_value:
                raise ValueError
        except ValueError:
            print(f'Invalid value! Please enter a number between {min_value} and {max_value}.')
            sleep(1)
        else:
            break
    return user_qty



