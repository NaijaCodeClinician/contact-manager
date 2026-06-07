import time
from validation import valid_phone, valid_mail

def max_width(name, phone, email):
    name_width = 0
    phone_width = 0
    email_width = 0
    for details in range(len(name)):
        len_contact_name = len(name[details])
        if len_contact_name > name_width:
            name_width = len_contact_name + 2
        len_phone_num = len(phone[details])
        if len_phone_num > phone_width:
            phone_width = len_phone_num + 2
        len_email_address = len(email[details])
        if len_email_address > email_width:
            email_width = len_email_address + 2
    total_width = name_width + phone_width + email_width
        
    return name_width, phone_width, email_width, total_width
        
def add_contact(name, phone, email):
    """This function takes the user's input (Contact name, Phone number and Email address), and appends it to parallel lists (name, phone, email)"""
    while True:
        contact_name = input("Input contact name: ").lower().strip()
        if not contact_name:
            print("Contact field can't be empty")
            continue
        if contact_name in name:
            print("Contact already exists")
            continue
        name.append(contact_name)
        break
    while True:
        phone_number = input("Input phone number: ").strip()
        if not phone_number:
            print("Phone number field is empty")
            continue
        if not valid_phone(phone_number):
            print("Input a valid phone number")
            continue
        if phone_number in phone:
          print("A contact with this number already exists")
          continue
        phone.append(phone_number)
        break
    while True:
        choice = input("Would you like to input the email address of the saved contact (y/n)? ").strip().lower()
        if choice == "n":
            email.append("N/A")
            break
        elif choice == "y":
            while True:
                address = input("Input Email Address: ").strip()
                if not address:
                    print("Address field is empty")
                    continue
                if not valid_mail(address):
                    print("Enter a valid email address")
                    continue
                if address in email:
                  print("Email already in use")
                  continue
                email.append(address)
                break
        else:
            print("Invalid choice")
            continue
        break

def view_contacts(name, phone, email):
    """Views the available contacts in the user's contact list (name, phone, email)"""
    if not name:
        print("No contact has been saved")
    else:
        name_width, phone_width, email_width, total_width = max_width(name, phone, email)
        print(f"{'YOUR CONTACTS':^{total_width}}")
        print("_" * total_width)
        print(f"{'NAME':<{name_width}}{'PHONE NUMBER':^{phone_width}}{'EMAIL ADDRESS':>{email_width}}")
        print("_" * total_width)
        for i in range(len(name)):
            print(f"{name[i].title():<{name_width}}{phone[i]:^{phone_width}}{email[i]:>{email_width}}")
            print("_" * total_width)

def search_contact(name, phone, email):
    """Searches for a contact, using the contact's name or search item"""
    if not name:
        print("Your contact list is empty, cannot proceed with search. Do well to update your contact list")
    else:
        while True:
            search_term = input("Enter Contact's name or a search term: ").strip().lower()
            if not search_term:
                print("Enter a search term")
                continue
            print("====== SEARCH RESULTS ======")
            is_found = False
            for i in range(len(name)):
                if search_term in name[i]:
                    print(f"\tName: {name[i].title()}\n\tPhone Number: {phone[i]}\n\tEmail Address: {email[i]}")
                    is_found = True
                    print()
            if not is_found:
                print("No contact with inputted search term found")
            while True:
              choice = input("Would you like to continue search (y/n): ")
              if not choice:
                print("Enter a choice")
                continue
              elif choice == "n":
                print("SEARCH CANCELLED")
                return
              elif choice == "y":
                break
              else:
                print("Invalid choice")
                continue

def update_contact(name, phone, email):
    if not name:
        print("Contact list is empty")
    else:
        while True:
            contact = input("Enter contact's name to be updated, to quit, input 'done': ").strip().lower()
            if not contact:
              print("Contact field can't be empty")
              continue
            if contact == 'done':
              print("You can use the Option '3' feature, to search for contact's name")
              return
            if contact not in name:
              print("Contact does not exist\n")
              continue
            break
        for i in range(len(name)):
          if contact == name[i]:
            idx = i
            while True:
              choice = input("Pick 'phone' to update Phone number , or 'email' to update Email Address: ").strip().lower()
              if not choice:
                print("Enter a choice")
                continue
              elif choice == "phone":
                while True:
                  number = input("Enter the new phone number: ").strip()
                  if not number:
                    print("Enter a number")
                    continue
                  if not valid_phone(number):
                    print("Enter a valid phone number")
                    continue
                  if number in phone:
                    print("A contact with this number already exists")
                    continue
                  phone[idx] = number
                  while True:
                    choice = input("Would you like to update contact's email address (y/n)? ").strip().lower()
                    if not choice:
                      print("Enter a choice")
                      continue
                    elif choice == "n":
                      print("CONTACT DETAILS HAS BEEN UPDATED SUCCESSFULLY")
                      return
                    elif choice == "y":
                      while True:
                        address = input("Enter the new contact email address: ").strip()
                        if not address:
                          print("Address field can't be empty: ")
                          continue
                        if not valid_mail(address):
                          print("Enter a valid Email Address")
                          continue
                        if address in email:
                          print("Email Address already in use")
                          continue
                        email[idx] = address
                        print("CONTACT DETAILS HAS BEEN UPDATED SUCCESSFULLY")
                        return
                    else:
                      print("Invalid choice")
                      continue
                    break
              elif choice == "email":
                while True:
                  address = input("Enter the new email address: ").strip()
                  if not address:
                    print("Enter an email address")
                    continue
                  if not valid_mail(address):
                    print("Enter a valid email address")
                    continue
                  if address in email:
                    print("Email Address already in use")
                    continue
                  email[idx] = address 
                  while True:
                    choice = input("Would you like to update contact's phone number (y/n)? ").strip().lower()
                    if not choice:
                      print("Enter a choice")
                      continue
                    elif choice == "n":
                      print("CONTACT DETAILS HAS BEEN UPDATED SUCCESSFULLY")
                      return
                    elif choice == "y":
                      while True:
                        number = input("Enter the new contact phone number: ").strip()
                        if not number:
                          print("Phone number field can't be empty: ")
                          continue
                        if not valid_phone(number):
                          print("Enter a valid Phone number")
                          continue
                        if number in phone:
                          print("A contact with this phone number already exists")
                          continue
                        phone[idx] = number
                        print("CONTACT DETAILS HAS BEEN UPDATED SUCCESSFULLY")
                        return
                    else:
                      print("Invalid choice")
                      continue
                    break
              break
            break

def delete_contact(name, phone, email):
  if not name:
    print("No contact has been saved")
  else:
    while True:
      print("========== YOUR CONTACTS ==========")
      for nam in name:
        print(f"{nam.title()}")
        print()
      print()
      print("To quit this process input 'done'")
      contact = input("Enter the name of the contact you want to delete: ").strip().lower()
      if not contact:
        print("Input a name")
        continue
      if contact == "done":
        print("DELETION CANCELLED")
        break
      if contact not in name:
        print("No contact exists with this name")
        continue
      break
    for i in range(len(name)):
      if contact == name[i]:
        idx = i
        while True:
          choice = input("You are about to delete the inputted contact, pick 'y' to proceed, and 'n' to cancel: ").strip().lower()
          if not choice:
            print("Pick a choice")
          elif choice == 'n':
            print("CONTACT DELETION CANCELLED")
            break
          elif choice == 'y':
            del name[idx]
            del phone[idx]
            del email[idx]
            break
          else:
            print("Invalid Choice")
            continue
        break

def leave(name, phone, email):
  for i in range(3, -1, -1):
    print(f"\rExiting the app in {i}", end = "")
    time.sleep(1)
  print("\n")
  print("YOU HAVE EXITED THE APP")
  exit()

print("\n" + "="*50)
print("\t\tCONTACT MANAGER")
print("="*50)
print("\n1.\tAdd contact")
print("2.\tView all contacts")
print("3.\tSearch contact by name")
print("4.\tUpdate contact (phone/email)")
print("5.\tDelete contact")
print("6.\tExit\n")
name = []
phone = []
email = []
functions = [add_contact, view_contacts, search_contact, update_contact, delete_contact, leave]
choices = ["1", "2", "3", "4", "5", "6"]
while True:
  choice = input("Pick a choice from 1 - 6: ").strip()
  if choice not in choices:
    print("Invalid Choice")
    continue
  index = int(choice) - 1
  action = functions[index](name, phone, email)
  print()
