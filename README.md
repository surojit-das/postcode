--------------------
`postcode` Library
--------------------

### Description
Library `postcode` can be used for validating and formatting a UK postcode.   
User can check whether a particular postcode is valid or not and can also format a particular postcode to a valid postcode.
Package `postcode-0.1-py3-none-any.whl` need to be installed on the system to use `postcode` library.

### How To Install
##### Prerequisite
- Python 3.5 or higher  and `pip` must be installed.
```
python --version
python -m pip --version
```
- `setuptools` and `wheel` also need to be installed. Type below command to install them.
```
sudo python -m pip install --upgrade pip setuptools wheel
```
##### Installation
- Go to the path where package `postcode-0.1-py3-none-any.whl` is placed.
- Type `python -m pip install postcode-0.1-py3-none-any.whl` and enter.
- Package will be installed.

### `postcode` Library Usage:
For Validating a postcode:
```
>>>import postcode
>>>postcode.validate('EC1A 1BB')
'It's a valid postcode.'
>>>postcode.validate('B338TH')
'It's NOT a valid postcode.'
>>>postcode.validate('cr2 6xh')
'It's a valid postcode.'
```
For Formatting a postcode:
```
>>>import postcode
>>>postcode.format_code('ec1a1bb')
'EC1A 1BB'
>>>postcode.format_code('dn55 1pt')
'DN55 1PT'
>>>postcode.format_code('QD6 5XH')
'Entered Code cannot be formatted. Invalid code.'
```

For Help:
```
>>>import postcode
>>>postcode.help()
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
```

### Files
`format.py`, `validate.py` and `help.py` files are for formatting a postcode, validating a postcode and providing the usage of `postcode` respectively.

### Tests
Two testfiles are included for testing purpose.
`test_validate.py` and `test_format.py` for validating testing and formatting testing respectively.
To run these files, enter below commands:
```
python test_validate.py
python test_format.py
```
