"""This module checks the validity of a number, phone numbers and email addresses"""

def valid_number(number):
    """Validates a whole number (optional leading '+').
    Validates both positive and negative numbers
    Parameter -> number: Input to be validated"""
    number = str(number).strip()
    if not number:
        return False
    if number[0] == "+" or number[0] == "-":
        number = number[1:]
    if not number:
        return False
    for ch in number:
        if ch < "0" or ch > "9":
            return False
    return True

def valid_phone(number):
    """Runs a validation on the validity of a phone number
    Parameter 1 -> number: Phone number to be validated"""
    number = str(number)
    starters = "0123456789+"
    starts_with = False
    length_ok = False
    space_hyphen = " -" 
    is_number = False
    
    if number[0] in starters and "+" not in number[1:]:
        starts_with = True
    cleaned = ""
    for n in number:
        if n in space_hyphen:
            continue
        cleaned += n
    if 5 <= len(cleaned) <= 15:
        length_ok = True
    if valid_number(cleaned[1:]):
        is_number = True
    
    if starts_with and length_ok and is_number:
        return True
    return False

def valid_mail(email):
    """Validates a provided email address.
    Parameter 1 -> email: Email address to be validated"""
    email = str(email)
    index = len(email) - 1
    symbols = "!\"#$%&'()*+,/:;<=>?@[\\]^`{|}~"
    if ".." in email:
        return False
        
    if "@" not in email:
        return False
    
    if " " in email:
        return False
    
    if email[-1] == "." or email[0] == ".":
        return False
    
    at_count = 0
    at_pos = -1
    
    for i in range(len(email)):
        if email[i] == "@" and i != 0 and i != index:
            at_count += 1
            at_pos = i
 
    if at_pos == -1:
        return False
    
    local = email[:at_pos]
    domain = email[at_pos + 1:]
    
    for ch in local:
        if ch in symbols:
            return False

    idx = -1
    for i in range(len(domain) - 1, -1, -1):
        if domain[i] == '.':
            if i == 0 or i == len(domain) - 1:
                return False
            idx = i
            break
    if idx == -1:
        return False
    
    tld = domain[idx + 1:]
    
        
    if len(tld) < 2:
        return False
    
    is_letter = True
    for ch in tld:
        if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
            is_letter = False
            break
    
    if at_count != 1:
        return False
    
    
    if not is_letter:
        return False
    return True
 
    
if __name__ == "__main__":
    print("Check if the following inputs are valid:")
    print(f"(1)\t56: {valid_number(56)}")
    print(f"(2)\t6y: {valid_number('6y')}")
    print(f"(3)\ttred: {valid_number('trred')}")
    print(f"(4)\t+234+4536+789: {valid_phone('+234+4356+789')}")
    print(f"(5)\t+2348108687545: {valid_phone('+2348108687545')}")
    print(f"(6)\tqwerty@gmail.co.uk.ng: {valid_mail('qwerty@gmail.co.uk.ng')}")
