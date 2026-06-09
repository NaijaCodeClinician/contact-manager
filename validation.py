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

def valid_decimal_number(number):
    """Validates both a whole number and a decimal (optional leading '+').
    Number can either be negative or positive
    Parameter -> number: Input to be validated"""
    number = str(number).strip()
    dot_count = 0
    if not number:
        return False
    if number[0] == "." or number[-1] == ".":
        return False
    if number[0] == "+" or number[0] == "-":
        number = number[1:]
    for ch in number:
            if ch == ".":
                dot_count += 1
                if dot_count > 1:
                    return False
            elif '0' > ch or ch > '9':
                return False
    return True
        
def valid_phone(number):
    """Runs a validation on the validity of a phone number
    Parameter 1 -> number: Phone number to be validated"""
    number = str(number)
    starters = "0123456789+"
    space_hyphen = " -"
    
    if len(number) < 5:
        return False
    if number[0] not in starters or "+" in number[1:]:
        return False
    if number[1] in space_hyphen or number[1] == "+":
        return False
    cleaned = ""
    for n in number:
        if n in space_hyphen:
            continue
        cleaned += n
    if 5 > len(cleaned) or len(cleaned) > 15:
        return False
    if not valid_number(cleaned[1:]):
        return False
    return True

def valid_mail(email):
    """Validates a provided email address.
    Parameter 1 -> email: Email address to be validated"""
    email = str(email)
    index = len(email) - 1
    symbols = "!\"#$%&'()*,/:;<=>?@[\\]^`{|}~"
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
    print(f"(1)\t56: {valid_number("56")}")
    print(f"(2)\t5.6: {valid_decimal_number("5.6")}")
    print(f"(3)\t6y: {valid_number('6y')}")
    print(f"(4)\ttred: {valid_number('trred')}")
    print(f"(5)\t+234+4536+789: {valid_phone('+234+4356+789')}")
    print(f"(6)\t+-2348108687545: {valid_phone('+-2348108687545')}")
    print(f"(7)\tqwerty@gmail.co.uk.ng: {valid_mail('qwerty@gmail.co.uk.ng')}")
