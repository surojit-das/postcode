import unittest
import postcode

class TestFormat(unittest.TestCase):

    # Test for formatting valid postcodes
    def test_format_codes(self):

        some_codes = {"ec1a1bb": "EC1A 1BB", # AA9A 9AA
                      "w1a 0ax": "W1A 0AX",  # A9A 9AA
                      "S1 1ae": "S1 1AE",    # A9 9AA
                      "b33 8Th": "B33 8TH",  # A99 9AA
                      "cR2 6xH": "CR2 6XH",  # AA9 9AA
                      "dn55 1PT": "DN55 1PT" # AA99 9AA
                     }

        for key, value in some_codes.items():

            #value = "'" + value + "'"
            result = postcode.format_code(key)
            self.assertEqual(result, value)

    # Test for invalid postcodes
    def test_invalid_format_codes(self):
        
        some_invalid_codes = ["FD1ABBB", # No digits in Inward code
                             "q1a 0ax",  # First letter starts with Q
                             "V1 1AE",   # First letter starts with V
                             "x33 8th",  # First letter starts with X
                             "RI2 6XH",  # Second letter start with I
                             "CJ2 6XH",  # Second letter start with J
                             "CZ2 6XH",  # Second letter start with Z
                             "A6L 1AE",  # Only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A
                             "a6r 1ae",  # Only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A
                             "A6O 1AE",  # Only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A
                             "EC1C 4BB", # Only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A
                             "EC1D 4BB", # Only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A
                             "EC1S 4BB", # Only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A
                             "dn55 1ct", # Final two letters do not use the letters CIKMOV
                             "dn55 1pi", # Final two letters do not use the letters CIKMOV
                             "DN55 1KT", # Final two letters do not use the letters CIKMOV
                             "DN55 1PM", # Final two letters do not use the letters CIKMOV
                             "dn55 1ot", # Final two letters do not use the letters CIKMOV
                             "DN55 1PV", # Final two letters do not use the letters CIKMOV
                             "DNN 1PV",  # No digits in Outward code
                             "DN 1PV",   # No digits in Outward code
                             "345 1PV",  # No letters in Outward code
                             "34 1PV",   # No letters in Outward code
                             "DN55 BPV", # No digits in Inward code
                             "DN55 44V", # Last two characters must be letters in Inward code
                             "DN55 444"  # No letters in Inward code
                            ]

        for code in some_invalid_codes:

            result = postcode.format_code(code)
            self.assertEqual(result, "Entered Code cannot be formatted. Invalid code")
		

if __name__ == "__main__":
    unittest.main()
