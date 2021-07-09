# Project 4
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 05/14/2021

from funcs import *


def main():

    input_string = input()    # get user input for puzzle string
    word_puzzle = divide_string(input_string.upper())    # convert puzzle to list

    input_words = input()    # get user input for words
    word_list = input_words.upper().split(" ")    # convert words to list

    print_puzzle(word_puzzle)    # print the word puzzle in rows of 10

    # check puzzle for each word in word_list
    for word in range(len(word_list)):

        solve_puzzle(word_puzzle, word_list[word])


main()
