#!/usr/bin/python3

import unittest
import basecracker as bc

base2_expected = [
    ['qwerty', '011100010111011101100101011100100111010001111001'],
    ['123456 randouum!', '00110001001100100011001100110100001101010011011000100000011100100110000101101110011001000110111101110101011101010110110100100001']
]

base16_expected = [
    ['qwerty', '717765727479'],
    ['123456 randouum!', '3132333435362072616e646f75756d21']
]

base32_expected = [
    ['123456 randouum!', 'GEZDGNBVGYQHEYLOMRXXK5LNEE======'],
    ['a', 'ME======'],
    ['ab', 'MFRA===='],
    ['abc', 'MFRGG==='],
    ['abcd', 'MFRGGZA='],
    ['abcde', 'MFRGGZDF'],
    ['abcdef', 'MFRGGZDFMY======']
]

base64_expected = [
    ['123456 randouum!', 'MTIzNDU2IHJhbmRvdXVtIQ=='],
    ['a', 'YQ=='],
    ['ab', 'YWI='],
    ['abc', 'YWJj'],
    ['abcd', 'YWJjZA==']
]

class TestEncoderDecoder(unittest.TestCase):

    # test base2
    def test_base2_encoder(self):
        global base2_expected
        for expected in base2_expected:
            cipher = bc.base2_encoder(expected[0])
            self.assertEqual(cipher, expected[1])

    def test_base2_decoder(self):
        global base2_expected
        for expected in base2_expected:
            plaintext = bc.base2_decoder(expected[1])
            self.assertEqual(plaintext, expected[0])

    # test base16
    def test_base16_encoder(self):
        global base16_expected
        for expected in base16_expected:
            cipher = bc.base16_encoder(expected[0])
            self.assertEqual(cipher, expected[1])

    def test_base16_decoder(self):
        global base16_expected
        for expected in base16_expected:
            plaintext = bc.base16_decoder(expected[1])
            self.assertEqual(plaintext, expected[0])

    # test base32
    def test_base32_encoder(self):
        global base32_expected
        for expected in base32_expected:
            cipher = bc.base32_encoder(expected[0])
            self.assertEqual(cipher, expected[1])

    def test_base32_decoder(self):
        global base32_expected
        for expected in base32_expected:
            plaintext = bc.base32_decoder(expected[1])
            self.assertEqual(plaintext, expected[0])

    # test base64
    def test_base64_encoder(self):
        global base64_expected
        for expected in base64_expected:
            cipher = bc.base64_encoder(expected[0])
            self.assertEqual(cipher, expected[1])

    def test_base64_decoder(self):
        global base64_expected
        for expected in base64_expected:
            plaintext = bc.base64_decoder(expected[1])
            self.assertEqual(plaintext, expected[0])

if __name__ == '__main__':
    unittest.main()