"""This module checks the validity of a number, phone numbers and email addresses"""

def valid_number(number):
    """Validates a whole number (optional leading '+').
    Validates both positive and negative numbers
    Parameter -> number: Input to be validated"""
    number = str(number).strip()
    if not number:
        return False
    if number.startswith("+") or number.startswith("-"):
        number = number[1:]
    if not number:
        return False
    for ch in number:
        if not ch.isdigit():
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
    if number.startswith(".") or number.endswith("."):
        return False
    if number.startswith("+") or number.startswith("-"):
        number = number[1:]
        if not number:
            return False
        if number.startswith(".") or number.endswith("."):
            return False
    if "." in number:
        dot_count = number.count(".")
    if dot_count > 1:
        return False
    for ch in number:
            if ch == ".":
                continue
            if not ch.isdigit():
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
    if email.startswith("@") or email.endswith("@"):
        return False
    if email.startswith(".") or email.endswith("."):
        return False
    
    at_count = email.count("@")
    if at_count != 1:
        return False
        
    split_email = email.split("@")
    local = split_email[0]
    domain = split_email[-1]
    
    for ch in local:
        if ch in symbols:
            return False

    if "." not in domain:
        return False
    split_domain = domain.split(".")
    tld = split_domain[-1]  
    
    if len(tld) < 2:
        return False
    
    is_letter = True
    for ch in tld:
        if not ch.isalpha():
            is_letter = False
            break
    
    
    if not is_letter:
        return False
    return True
 
    
if __name__ == "__main__":
    print("Check if the following inputs are valid:")
    print(f"(1)\t56: {valid_number('56')}")
    print(f"(2)\t5.6: {valid_decimal_number('5.6')}")
    print(f"(3)\t6y: {valid_number('6y')}")
    print(f"(4)\ttred: {valid_number('trred')}")
    print(f"(5)\t+234+4536+789: {valid_phone('+234+4356+789')}")
    print(f"(6)\t+-2348108687545: {valid_phone('+-2348108687545')}")
    print(f"(7)\tqwerty@gmail.co.uk.ng: {valid_mail('qwerty@gmail.co.uk.ng')}")
