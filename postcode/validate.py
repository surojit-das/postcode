import sys
import re

def validate(code_received):
    """
    Description:
        Validate the code provided by the User.

        Validity check is done by following below points as mentioned in UK postcode wikipedia page.
        https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting

        1. The postcodes are alphanumeric, and are variable in length: ranging from six to eight characters (including a space) long
        2. The letters QVX are not used in the first position.
        3. The letters IJZ are not used in the second position.
        4. The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A.
        5. The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.
        6. The final two letters do not use the letters CIKMOV.

    Parameters:
        Post code : string

    Retruns:
        string
    """

    # Check if no code was received as an argument
    if not code_received:
        return "No code was received!"
    
    else:
        code_received = code_received.upper()

        # Letters QVX and IJV are not used in first and second positions
        # Letters CIKMOV are not used in the final two letters
        # Postcode 'GIR 0AA' is a special case
        code_regex = '([A-PR-UWY-Z][A-HK-Y]?[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}|[G][I][R] 0[A]{2})'

        outward_code = code_received[:-3].strip()

        # Handle some special cases:
        # The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A
        if len(outward_code) == 3 and re.match('[A-Z][0-9][A-Z]', outward_code):
            code_regex = '([A-PR-UWY-Z]?[0-9][A-HJKPS-UW]? [0-9][ABD-HJLNP-UW-Z]{2}|[G][I][R] 0[A]{2})'
        
        # The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.
        elif len(outward_code) == 4 and re.match('[A-Z]{2}[0-9][A-Z]', outward_code):
            code_regex = '([A-PR-UWY-Z][A-HK-Y]?[0-9][ABEHMNPRVWXY]? [0-9][ABD-HJLNP-UW-Z]{2}|[G][I][R] 0[A]{2})'
            
        valid_code = re.compile('^{}$'.format(code_regex))

        # Validate code
        if valid_code.match(code_received):
            return("It's a valid postcode.")
        else:
            return "It's NOT a valid postcode."


if __name__ == "__main__":
    validate(sys.argv[1])
