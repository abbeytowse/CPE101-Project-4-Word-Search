# Project 4
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 05/14/2021

import unittest
from funcs import *


class TestCases(unittest.TestCase):
    def test_divide_string_0(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGET" \
                       "RCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual(divide_string(input_string), ['LLARSHAHLC',
                                                       'AOOLLAMILL',
                                                       'OIDNALHGIH',
                                                       'RBAMCETUHS',
                                                       'SMOSKAGETR',
                                                       'CORCHORROA',
                                                       'IDBSLSAAOM',
                                                       'IGOSMONDFL',
                                                       'HHNGMSDCMA',
                                                       'CMIRRSMLHP'])

    def test_divide_string_1(self):
        input_string = ""
        self.assertEqual(divide_string(input_string), ["", "", "", "", "",
                                                       "", "", "", "", ""])

    def test_divide_string_2(self):
        # testing what happens if string longer than 100 characters
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGET" \
                       "RCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSML" \
                       "HPQRSTUVWXYZ"
        self.assertEqual(divide_string(input_string), ['LLARSHAHLC',
                                                       'AOOLLAMILL',
                                                       'OIDNALHGIH',
                                                       'RBAMCETUHS',
                                                       'SMOSKAGETR',
                                                       'CORCHORROA',
                                                       'IDBSLSAAOM',
                                                       'IGOSMONDFL',
                                                       'HHNGMSDCMA',
                                                       'CMIRRSMLHP'])

    def test_divide_string_3(self):
        # testing what happens if string shorter than 100 characters
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGET"
        self.assertEqual(divide_string(input_string), ['LLARSHAHLC',
                                                       'AOOLLAMILL',
                                                       'OIDNALHGIH',
                                                       'RBAMCETUHS',
                                                       'SMOSKAGET',
                                                       '', '', '', '', ''])

    def test_check_mirror_numbers_0(self):
        self.assertEqual(mirror_numbers(0), 9)

    def test_check_mirror_numbers_1(self):
        self.assertEqual(mirror_numbers(8), 1)

    def test_check_mirror_numbers_2(self):
        self.assertEqual(mirror_numbers(2), 7)

    def test_check_mirror_numbers_3(self):
        self.assertEqual(mirror_numbers(6), 3)

    def test_check_mirror_numbers_4(self):
        self.assertEqual(mirror_numbers(4), 5)

    def test_check_row_forward_0(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "UNIX"
        self.assertEqual(check_row_forward(word_puzzle, word),
                         "UNIX: (FORWARD) row: 9 column: 3")

    def test_check_row_forward_1(self):
        input_string = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBK" \
                       "ABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        word_puzzle = divide_string(input_string)
        word = "RACCOON"
        self.assertEqual(check_row_forward(word_puzzle, word),
                         "RACCOON: (FORWARD) row: 2 column: 2")

    def test_check_row_forward_2(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETR" \
                       "CORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        word_puzzle = divide_string(input_string)
        word = "MILL"
        self.assertEqual(check_row_forward(word_puzzle, word),
                         "MILL: (FORWARD) row: 1 column: 6")

    def test_check_row_forward_3(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "COMPILE"
        self.assertEqual(check_row_forward(word_puzzle, word), None)

    def test_check_row_forward_4(self):
        input_string = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBK" \
                       "ABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        word_puzzle = divide_string(input_string)
        word = "CHICKEN"
        self.assertEqual(check_row_forward(word_puzzle, word), None)

    def test_check_row_forward_5(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETR" \
                       "CORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        word_puzzle = divide_string(input_string)
        word = "MARSH"
        self.assertEqual(check_row_forward(word_puzzle, word), None)

    def test_check_row_backward_0(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "VIM"
        self.assertEqual(check_row_backward(word_puzzle, word),
                         "VIM: (BACKWARD) row: 1 column: 4")

    def test_check_row_backward_1(self):
        input_string = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBK" \
                       "ABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        word_puzzle = divide_string(input_string)
        word = "BEAR"
        self.assertEqual(check_row_backward(word_puzzle, word),
                         "BEAR: (BACKWARD) row: 1 column: 6")

    def test_check_row_backward_2(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETR" \
                       "CORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        word_puzzle = divide_string(input_string)
        word = "HIGHLAND"
        self.assertEqual(check_row_backward(word_puzzle, word),
                         "HIGHLAND: (BACKWARD) row: 2 column: 9")

    def test_check_row_backward_3(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "UNIX"
        self.assertEqual(check_row_backward(word_puzzle, word), None)

    def test_check_row_backward_4(self):
        input_string = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBK" \
                       "ABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        word_puzzle = divide_string(input_string)
        word = "ZEBRA"
        self.assertEqual(check_row_backward(word_puzzle, word), None)

    def test_check_row_backward_5(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETR" \
                       "CORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        word_puzzle = divide_string(input_string)
        word = "CHORRO"
        self.assertEqual(check_row_backward(word_puzzle, word), None)

    def test_check_column_down_0(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "CALPOLY"
        self.assertEqual(check_column_down(word_puzzle, word),
                         "CALPOLY: (DOWN) row: 1 column: 0")

    def test_check_column_down_1(self):
        input_string = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBK" \
                       "ABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        word_puzzle = divide_string(input_string)
        word = "RABBIT"
        self.assertEqual(check_column_down(word_puzzle, word),
                         "RABBIT: (DOWN) row: 1 column: 3")

    def test_check_column_down_2(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETR" \
                       "CORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        word_puzzle = divide_string(input_string)
        word = "HIGUERA"
        self.assertEqual(check_column_down(word_puzzle, word),
                         "HIGUERA: (DOWN) row: 0 column: 7")

    def test_check_column_down_3(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "COMPILE"
        self.assertEqual(check_column_down(word_puzzle, word), None)

    def test_check_column_down_4(self):
        input_string = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBK" \
                       "ABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        word_puzzle = divide_string(input_string)
        word = "ZEBRA"
        self.assertEqual(check_column_down(word_puzzle, word), None)

    def test_check_column_down_5(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETR" \
                       "CORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        word_puzzle = divide_string(input_string)
        word = "MARSH"
        self.assertEqual(check_column_down(word_puzzle, word), None)

    def test_check_column_up_0(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "COMPILE"
        self.assertEqual(check_column_up(word_puzzle, word),
                         "COMPILE: (UP) row: 6 column: 8")

    def test_check_column_up_1(self):
        input_string = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBK" \
                       "ABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        word_puzzle = divide_string(input_string)
        word = "CHICKEN"
        self.assertEqual(check_column_up(word_puzzle, word),
                         "CHICKEN: (UP) row: 8 column: 8")

    def test_check_column_up_2(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETR" \
                       "CORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        word_puzzle = divide_string(input_string)
        word = "FOOTHILL"
        self.assertEqual(check_column_up(word_puzzle, word),
                         "FOOTHILL: (UP) row: 7 column: 8")

    def test_check_column_up_3(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "VIM"
        self.assertEqual(check_column_up(word_puzzle, word), None)

    def test_check_column_up_4(self):
        input_string = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBK" \
                       "ABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        word_puzzle = divide_string(input_string)
        word = "ZEBRA"
        self.assertEqual(check_column_up(word_puzzle, word), None)

    def test_check_column_up_5(self):
        input_string = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETR" \
                       "CORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        word_puzzle = divide_string(input_string)
        word = "GRAND"
        self.assertEqual(check_column_up(word_puzzle, word), None)

    def test_check_diagonal_0(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "CPE"
        self.assertEqual(check_diagonal(word_puzzle, word),
                         "CPE: (DIAGONAL) row: 1 column: 0")

    def test_check_diagonal_1(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = "CALPOLY"
        self.assertEqual(check_diagonal(word_puzzle, word), None)

# testing each check function with an empty inputs
    def test_check_row_forward_empty_strings(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_row_forward(word_puzzle, word), None)

    def test_check_row_backward_empty_strings(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_row_backward(word_puzzle, word), None)

    def test_check_column_down_empty_strings(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_column_down(word_puzzle, word), None)

    def test_check_column_up_empty_strings(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_column_up(word_puzzle, word), None)

    def test_check_diagonal_empty_strings(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_diagonal(word_puzzle, word), None)

# testing each check function with an empty word_puzzle but words given
    def test_check_row_forward_empty_puzzle(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = "CAT"
        self.assertEqual(check_row_forward(word_puzzle, word), None)

    def test_check_row_backward_empty_puzzle(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = "PANCAKES"
        self.assertEqual(check_row_backward(word_puzzle, word), None)

    def test_check_column_down_empty_puzzle(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = "TURKEY"
        self.assertEqual(check_column_down(word_puzzle, word), None)

    def test_check_column_up_empty_puzzle(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = "COUCH"
        self.assertEqual(check_column_up(word_puzzle, word), None)

    def test_check_diagonal_empty_puzzle(self):
        input_string = ""
        word_puzzle = divide_string(input_string)
        word = "TOMATO"
        self.assertEqual(check_diagonal(word_puzzle, word), None)

# testing each check function with a full word_puzzle but no word given
    def test_check_row_forward_no_word(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_row_forward(word_puzzle, word), None)

    def test_check_row_backward_no_word(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_row_backward(word_puzzle, word), None)

    def test_check_column_down_no_word(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_column_down(word_puzzle, word), None)

    def test_check_column_up_no_word(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_column_up(word_puzzle, word), None)

    def test_check_diagonal_no_word(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN" \
                       "OEDSOYQGOBLGQCKGMMCTYCSLOAPUZMXVDMGSXCYZUUIUNIXFNU"
        word_puzzle = divide_string(input_string)
        word = ""
        self.assertEqual(check_diagonal(word_puzzle, word), None)

    # testing if shorter than 100 inputted
    def test_check_row_forward_short_puzzle_0(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN"
        word_puzzle = divide_string(input_string)
        word = "DOG"
        self.assertEqual(check_row_forward(word_puzzle, word), None)

    def test_check_row_forward_short_puzzle_1(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDOGFXPIPVPONDTMVAMN"
        word_puzzle = divide_string(input_string)
        word = "DOG"
        self.assertEqual(check_row_forward(word_puzzle, word),
                         "DOG: (FORWARD) row: 3 column: 1")

    def test_check_row_backward_short_puzzle_0(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNASDFG"
        word_puzzle = divide_string(input_string)
        word = "CAT"
        self.assertEqual(check_row_backward(word_puzzle, word), None)

    def test_check_row_backward_short_puzzle_1(self):
        input_string = "WAQHGTTWEECBMIVQQELTCCXWKWTACLLDELFXPIPVPONDTMVAMNASDFG"
        word_puzzle = divide_string(input_string)
        word = "CAT"
        self.assertEqual(check_row_backward(word_puzzle, word),
                         "CAT: (BACKWARD) row: 2 column: 8")

    def test_check_column_down_short_puzzle_0(self):
        input_string = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVA"
        word_puzzle = divide_string(input_string)
        word = "FISH"
        self.assertEqual(check_column_down(word_puzzle, word), None)

    # this test fails because my functions cannot handle if word is in short
    # puzzle and part of word is in last row

    # def test_check_column_down_short_puzzle_1(self):
        # input_string = "WAFHGTTWEECFOFVQQEFSAISIKWIIILLSGSFXPISVPONHTMVA"
        # word_puzzle = divide_string(input_string)
        # word = "FISH"
        # self.assertEqual(check_column_down(word_puzzle, word),
                         # "FISH: (DOWN) row: 1 column: 3")

    def test_check_column_up_short_puzzle_0(self):
        input_string = "WATTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN"
        word_puzzle = divide_string(input_string)
        word = "HAMSTER"
        self.assertEqual(check_column_up(word_puzzle, word), None)

    # this test fails because my functions cannot handle if word is in short
    # puzzle and part of word is in last row

    # def test_check_column_up_short_puzzle_1(self):
        # input_string = "WATTWEECBMIVQQELSAPXWKHIIILLDELFXAIPVPONDTMVMMN"
        # word_puzzle = divide_string(input_string)
        # word = "HAM"
        # self.assertEqual(check_column_up(word_puzzle, word),
                        # "HAM: (DIAGONAL) row: 2 column: 2")

    def test_check_diagonal_short_puzzle_0(self):
        input_string = "WAQHGTTWEECBMIVQQELILLDELFXPIPVPONDTMVAMN"
        word_puzzle = divide_string(input_string)
        word = "BIRD"
        self.assertEqual(check_diagonal(word_puzzle, word), None)


if __name__ == '__main__':
    unittest.main()
