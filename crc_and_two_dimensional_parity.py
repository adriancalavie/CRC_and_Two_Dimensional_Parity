def get_reminder(message, polynomial):
    """Returns the remainder for a given message and polynomial.
    Both should be in binary base.



    :type polynomial: str
    :type message: str
    """
    polynomial = polynomial.lstrip('0')
    message_length = len(message)

    padding = (len(polynomial) - 1) * '0'
    message_padded = list(message + padding)

    while '1' in message_padded[:message_length]:

        current_shift = message_padded.index('1')

        for i in range(len(polynomial)):
            message_padded[current_shift + i] = str(int(polynomial[i] != message_padded[current_shift + i]))

    return ''.join(message_padded)[message_length:].lstrip('0')


def is_correct(message, polynomial, remainder):
    """Returns True if the message transmitted correctly.


    :type remainder: str
    :type polynomial: str
    :type message: str
    """
    polynomial = polynomial.lstrip('0')
    message_length = len(message)

    padding = remainder.rjust(len(polynomial) - 1, '0')
    message_padded = list(message + padding)

    while '1' in message_padded[:message_length]:

        current_shift = message_padded.index('1')

        for i in range(len(polynomial)):
            message_padded[current_shift + i] = str(int(polynomial[i] != message_padded[current_shift + i]))

    return '1' not in ''.join(message_padded)[message_length:]


def get_two_dimensional_parity_for(message):
    """
    Returns the message with a two-dimensional parity check on



    :type message: str
    """
    if len(message) % 7 is not 0:
        return False

    matrix = list(list())

    for i in range(int(len(message) / 7)):
        matrix.append([char for char in message[i * 7:(i + 1) * 7]])

    for line in matrix:
        line.append(str(len(''.join(line).replace('0', '')) % 2))

    line = list()
    for i in range(len(matrix[0]) - 1):
        column = [row[i] for row in matrix if row[i] is '1']
        line.append(str(len(column) % 2))

    matrix.append(line)

    message = ''
    for row in matrix:
        message += ''.join(row)
    return message


def check_two_dimensional_parity(message):
    """
    Returns True or False based on the unwrapping of the message

    :param message: a binary string
    :return: bool
    :type message: str
    """

    if (len(message) - 7) % 8 != 0:
        return False

    last_line = message[-7:]

    matrix = list(list())

    for i in range(int((len(message) - 7) / 8)):
        matrix.append([char for char in message[i * 8: (i + 1) * 8]])

    for line in matrix:
        if str(len([char for char in line[:(len(line) - 1)] if char is '1']) % 2) != line[-1]:
            return False

    for j in range(len(matrix[0]) - 1):
        column = [row[j] for row in matrix if row[j] is '1']
        if last_line[j] != str(len(column) % 2):
            return False

    return True
