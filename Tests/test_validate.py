import unittest
import postcode

class TestValidate(unittest.TestCase):

    # Test for valid postcodes
    def test_valid_codes(self):

        valid_codes = ["EC1A 1BB", # AA9A 9AA
                       "w1a 0ax",  # A9A 9AA
                       "M1 1AE",   # A9 9AA
                       "b33 8th",  # A99 9AA
                       "CR2 6XH",  # AA9 9AA
                       "dn55 1PT"  # AA99 9AA
                      ]

        for code in valid_codes:

            result = postcode.validate(code)
            self.assertEqual(result, "It's a valid postcode.")

    # Test for invalid postcodes
    def test_invalid_codes(self):
        
        invalid_codes = ["FD1A1BB",  # No Space
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
                         "D 1PV",    # No digits in Outward code
                         "1PV",      # No Outward code
                         "345 1PV",  # No letters in Outward code
                         "34 1PV",   # No letters in Outward code
                         "3 1PV",    # No letters in Outward code
                         "DN55 BPV", # No digits in Inward code
                         "DN55 44V", # Last two characters must be letters in Inward code
                         "DN55 444"  # No letters in Inward code
                        ]

        for code in invalid_codes:

            result = postcode.validate(code)
            self.assertEqual(result, "It's NOT a valid postcode.")
		

if __name__ == "__main__":
    unittest.main()
