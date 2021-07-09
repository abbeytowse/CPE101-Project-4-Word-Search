# Project 4
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 05/14/2021


# helper functions for check word helper functions
def mirror_numbers(num):

    """
    Input type: integer
    Output type: integer
    Function: takes integer and returns its mirrored value in range 0-9
    """

    if num == 0:    # swap 0 and 9
        num = 9
    elif num == 9:
        num = 0
    elif num == 1:    # swap 1 and 8
        num = 8
    elif num == 8:
        num = 1
    elif num == 2:    # swap 2 and 7
        num = 7
    elif num == 7:
        num = 2
    elif num == 3:    # swap 3 and 6
        num = 6
    elif num == 6:
        num = 3
    elif num == 4:    # swap 4 and 5
        num = 5
    elif num == 5:
        num = 4

    return num    # return swapped value


def is_row_length_valid_and_word_not_empty(word_puzzle, row, word):

    """
    Input type: list, integer, string, respectively
    Output type: boolean
    Function: returns true if row in word_puzzle is length 10 and word
    not empty
    """

    # check each element of list is len 10 and word contains chars
    if len(word_puzzle[row]) == 10 and word != "":

        return True

    else:

        return False


def reverse_row(word_puzzle, row_of_interest):

    """
    Input type: list and string, respectively
    Output type: string
    Function: reverses order of each element in row
    """

    reversed_row = ""    # create empty str to store reversed row in

    # reverse order of characters in row
    for character in range(len(row_of_interest)):

        reversed_row = reversed_row + \
                       row_of_interest[abs(character - len(word_puzzle)) - 1]

    return reversed_row


def reverse_puzzle(word_puzzle):

    """
    Input type: list
    Output type: list
    Function: reverses order of elements in a list
    """

    # create empty list to store reversed puzzle in
    reversed_puzzle = []

    # reverse the order of elements in the list word_puzzle
    for element in range(len(word_puzzle)):

        reversed_puzzle.insert(0, word_puzzle[element])

    return reversed_puzzle


def is_word_found_column(word_puzzle, word, row, column, matching_char):

    """
    Input types:  list, string, integer, integer, and string respectively
    Output type: boolean
    Function: goes up/down column and checks for word
    """

    for letter in range(len(word)):    # look at each letter in a word

        # prevents an out of bounds error and allows short puzzle solution
        if row + letter <= 9 and len(word_puzzle[row + letter]) == 10:

            # if matching letter is found
            if word[letter] == word_puzzle[row + letter][column]:

                # add matching letter to matching_char
                matching_char = matching_char + word[letter]

            else:  # exit for loop if letter doesn't match

                break

        else:    # if an out of bounds error would occur

            return False

    if matching_char == word:    # if entire word is found

        return True

    else:    # if entire word is not found

        return False


def is_word_found_diagonal(word_puzzle, word, row, column, matching_char):

    """
    Input types: list, string, integer, integer, and string, respectively
    Output type: boolean
    Function: goes through down right diagonal and checks for words
    """

    for letter in range(len(word)):    # look at each letter in a word

        # prevents an out of bounds error
        if row + letter <= 9 and column + letter <= 9 and \
                len(word_puzzle[row + letter]) == 10:

            # if matching letter is found
            if word[letter] == word_puzzle[row + letter][column + letter]:

                # add matching letter to matching_char
                matching_char = matching_char + word[letter]

            else:  # exit for loop if letter doesn't match

                break

        else:     # if an out of bounds error would occur

            return False

    if matching_char == word:    # if entire word is found

        return True

    else:    # if entire word is not found

        return False


def give_location(word, direction, row, column,):

    """
    Input type: string, string, integer, & integer, respectively
    Output type: string
    Function: state the location of the word when found
    """

    return word + ": " + "(" + direction + ")" + " row: " + str(row) + \
        " column: " + str(column)


# check for words helper functions
def check_row_forward(word_puzzle, word):

    """
    Input types: list of string and string, respectively
    Output type: string
    Function: checks if word is found forward in row and gives location
    """

    for row in range(len(word_puzzle)):    # look at each row in puzzle

        if is_row_length_valid_and_word_not_empty(word_puzzle, row, word):

            row_of_interest = word_puzzle[row]    # get each row
            column = row_of_interest.find(word)   # search each row for word

            if column != -1:  # if the word found

                return give_location(word, "FORWARD", row, column)

        else:    # if row length invalid or no word given, can't solve

            return None


def check_row_backward(word_puzzle, word):

    """
    Input types: list and string, respectively
    Output type: string
    Function: checks if word is found backward in row and gives location
    """

    for row in range(len(word_puzzle)):    # look at each row in puzzle

        if is_row_length_valid_and_word_not_empty(word_puzzle, row, word):

            # reverse each row and check for word
            row_of_interest = word_puzzle[row]
            reversed_row = reverse_row(word_puzzle, row_of_interest)
            column = reversed_row.find(word)

            if column != -1:    # if word found

                # change location of found word to correct for backward rows
                column = mirror_numbers(column)

                return give_location(word, "BACKWARD", row, column)

        else:    # if row length invalid or no word given, can't solve

            return None


def check_column_down(word_puzzle, word):

    """
    Input type: list and string, respectively
    Output type: string
    Function: checks if word is found down a column and gives location
    """

    for row in range(len(word_puzzle)):    # look at each row in puzzle

        if is_row_length_valid_and_word_not_empty(word_puzzle, row, word):

            # look at each col in puzzle
            for column in range(len(word_puzzle[row])):

                # if first letter of word found
                if word[0] == word_puzzle[row][column]:

                    # create empty string to store matching letters in
                    matching_char = ""

                    if is_word_found_column(word_puzzle, word, row,
                                            column, matching_char):

                        return give_location(word, "DOWN", row, column)

        else:    # if row length invalid or no word given, can't solve

            return None


def check_column_up(word_puzzle, word):

    """
    Input type: list and string, respectively
    Output type: string
    Function: checks if word is found up a column and gives location
    """

    reversed_puzzle = reverse_puzzle(word_puzzle)

    for row in range(len(reversed_puzzle)):    # look at each row in puzzle

        if is_row_length_valid_and_word_not_empty(word_puzzle, row, word):

            # look at each col in puzzle
            for column in range(len(reversed_puzzle[row])):

                # if first letter of word found
                if word[0] == reversed_puzzle[row][column]:

                    # create empty string to store matching letters in
                    matching_char = ""

                    if is_word_found_column(reversed_puzzle, word, row,
                                            column, matching_char):

                        # mirror location found to adjust for backwards list
                        row = mirror_numbers(row)

                        return give_location(word, "UP", row, column)

        else:    # if row length invalid or no word given, can't solve

            return None


def check_diagonal(word_puzzle, word):

    """
    Input type: list and string, respectively
    Output type: string
    Function: checks if word is found in down right diagonal
    and gives location
    """

    for row in range(len(word_puzzle)):    # look at each row in puzzle

        if is_row_length_valid_and_word_not_empty(word_puzzle, row, word):

            # look at each col in puzzle
            for column in range(len(word_puzzle)):

                # if first letter of word found
                if word[0] == word_puzzle[row][column]:

                    # create empty string to store matching letters in
                    matching_char = ""

                    if is_word_found_diagonal(word_puzzle, word, row,
                                              column, matching_char):

                        return give_location(word, "DIAGONAL", row, column)

        else:    # if row length invalid or no word given, can't solve

            return None


# function to solve puzzle
# this function will only find the FIRST occurrence of a word
def solve_puzzle(word_puzzle, word):

    """
    Input types: list and string, respectively
    Output type: strings
    Function: prints solution to word_puzzle by using check functions
    """

    # check if a check function can find word
    if check_row_forward(word_puzzle, word) is not None:

        print(check_row_forward(word_puzzle, word))

    elif check_row_backward(word_puzzle, word) is not None:

        print(check_row_backward(word_puzzle, word))

    elif check_column_down(word_puzzle, word) is not None:

        print(check_column_down(word_puzzle, word))

    elif check_column_up(word_puzzle, word) is not None:

        print(check_column_up(word_puzzle, word))

    elif check_diagonal(word_puzzle, word) is not None:

        print(check_diagonal(word_puzzle, word))

    # give message if empty puzzle is given
    elif word_puzzle == ["", "", "", "", "", "", "", "", "", ""]:

        print("Can't solve a blank puzzle!")

    elif word == "":    # give message is no word is given

        print("Can't solve puzzle with no word list!")

    else:    # if word is not found by any check function

        print(word + ": word not found")


# function to divide input string into a list of length 10
def divide_string(input_string):

    """
    Input type: string
    Output type: list
    Function: turns input_string into a list of 10 lists of length 10
    """

    word_puzzle = []    # create empty list to store str in

    # store every 10 char as an element in str word_puzzle
    for i in range(10):

        divided_string = input_string[i*10: i*10 + 10]    # grab 10 char
        word_puzzle.append(divided_string)    # append 10 char to list

    return word_puzzle


# function to print puzzle for final output
def print_puzzle(word_puzzle):

    """
    Input Type: list
    Output type: strings
    Function: prints word_puzzle as rows of strings
    """

    # don't print puzzle if blank string is given
    if not word_puzzle == ["", "", "", "", "", "", "", "", "", ""]:

        print("Puzzle:\n")    # print header

        # print each item in the word_puzzle list
        for i in range(len(word_puzzle)):

            print(word_puzzle[i])

        print()    # print blank line for formatting
