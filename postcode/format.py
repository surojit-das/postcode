import sys
import re

def format_code(code_received):
    """
    Description:
        Formats the code provided by the User to a legitimate code.

        Formatting is done by following below points as mentioned in UK postcode wikipedia page.
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

    if len(code_received) < 5 or len(code_received) > 8:
        return "Code length is invalid."
    
    else:
        
        outward_code_regex = '([A-PR-UWY-Z][A-HK-Y]?[0-9][A-Z0-9]?|[G][I][R])' # QVX and IJZ letters can't be used in first and second position.
        inward_code_regex = '([0-9][ABD-HJLNP-UW-Z]{2}|0[A]{2})' # Because final two letters don't use the letters CIKMOV.

        code_received = code_received.upper() # Convert the code to Upper Case

        inward_code = code_received[-3:].strip()  # Last three characters represent inward code
        outward_code = code_received[:-3].strip() # Rest characters respresnt outward code
    
        # Handle some special cases
        # The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A
        if len(outward_code) == 3 and re.match('[A-Z][0-9][A-Z]', outward_code):
            outward_code_regex = '([A-PR-UWY-Z]?[0-9][A-HJKPS-UW]?|[G][I][R])'
        
        # The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.
        elif len(outward_code) == 4 and re.match('[A-Z]{2}[0-9][A-Z]', outward_code):
            outward_code_regex = '([A-PR-UWY-Z][A-HK-Y]?[0-9][ABEHMNPRVWXY]?|[G][I][R])'
        
        valid_outward_code = re.compile('^{}$'.format(outward_code_regex))
        valid_inward_code = re.compile('^{}$'.format(inward_code_regex))
    
        if valid_outward_code.match(outward_code) and valid_inward_code.match(inward_code):
            formatted_code = outward_code + ' ' + inward_code
            return formatted_code

        else:
            return 'Entered Code cannot be formatted. Invalid code'
    

if __name__ == "__main__":
    format_code(sys.argv[1])
