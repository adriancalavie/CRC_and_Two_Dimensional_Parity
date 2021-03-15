from crc_and_two_dimensional_parity import *


def main_menu():
    yes_answer = ('Y', 'y', 'Yes', 'yes', 'True', '1', 'Affirmative', 'affirmative')

    message = input("please enter a message: ").lstrip()

    answer = input("Do you want to use two-dimensional parity on the message? ").lstrip()
    if answer in yes_answer:
        two_dimensional_parity_msg = get_two_dimensional_parity_for(message)
        if two_dimensional_parity_msg is not False:
            print(f'This is the message after the two-dimensional parity algorithm: {two_dimensional_parity_msg:s}')
            # if check_two_dimensional_parity(100100111011010011011):
            if check_two_dimensional_parity(two_dimensional_parity_msg):
                print('The message transmitted correctly')
            else:
                print('The message got error-ed on the way!')
        else:
            print("This message isn't a multiple of 7! the two-dimensional parity algorithm can't be applied!")

    polynomial = input(f"For the inserted message({message:s}), please enter a polynom: ")

    # message = '11010011100110110110101'
    # polynomial = '1011'

    reminder = get_reminder(message, polynomial)
    print(f'The reminder is {reminder:s}')

    answer = input(f'Do you want to modify the message({message:s})? ').lstrip()
    if answer in yes_answer:
        index = int(input(f'which bit do you want to edit? select a  value from 0 to {len(message) - 1:d}. this '
                          f'will be inverted(0 becomes 1 and 1 becomes 0)').lstrip())
        message_as_list = list(message)
        message_as_list[index] = '1' if message_as_list[index] is '0' else '0'
        message = ''.join(message_as_list)

    if is_correct(message, polynomial, reminder):
        print('The message transmitted correctly')
    else:
        print("The message DIDN'T transmit correctly!")


if __name__ == '__main__':
    main_menu()
