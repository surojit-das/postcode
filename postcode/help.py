
def help():

    print('''\n
    Description:
    ------------
    To validate and format a particular code for UK postcode.

    Usage:
    ------ 
    To Validate
    >>> postcode.validate('AA9A 9AA')
    'It's a valid postcode.'

    >>> postcode.validate('AA9A9AA')
    'It's NOT a valid postcode.'
    

    To Format
    >>> postcode.format('aa9a9aa')
    'AA9A 9AA'

    >>> postcode.format('df9a9ca')
    'Entered Code cannot be formatted. Invalid code'
    
    ''')

if __name__ == "__main__":
    help()

