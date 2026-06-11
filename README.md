# 📇 Contact Manager – A Python CLI App

# 👨‍⚕️ About the Author
> *“Medical student who codes. Building health tech, one line at a time.”*
> 
I’m **NaijaCodeClinician** – a Nigerian, a future physician, and a self‑taught Python programmer.  
I’m currently working through **OpenStax Introduction to Python Programming**. This is one of my first complete projects.  
I believe the best doctors will also understand technology. Every line of code brings me closer to building tools that improve healthcare in Nigeria.

## 🧩 Project Description

**Contact Manager** is a command‑line application that lets you store, search, update, and delete contacts with phone and email validation.  
It uses **parallel lists** (no dictionaries yet – I haven’t reached that chapter) and my own `validation.py` module for phone and email checks.

## ✨ Features

- ✅ Add a contact (name, phone number, optional email)  
- ✅ View all contacts in a clean list  
- ✅ Search contacts by partial name match  
- ✅ Update phone number or email address  
- ✅ Delete a contact with confirmation  
- ✅ Phone validation – supports spaces, hyphens, leading `+`, length 5‑15  
- ✅ Email validation – checks `@`, dot after `@`, and TLD letters  
- ✅ Duplicate prevention (no duplicate names, phone numbers, or emails)  
- ✅ Graceful exit with countdown

## 🚀 How to Run

1. **Install Python 3** (I use Termux on Android, but it works on any system).  
2. Clone this repository or download the two files:  
   - `contact_manager.py`  
   - `validation.py`  
3. Open a terminal in the project folder and run:  
   ```bash
   python contact_manager.py


🛠️ Dependencies

· Python 3 (standard library only – no external packages)

📁 Files

· contact_manager.py – main program
· validation.py – phone and email validation logic (no regex, just loops and conditionals)

🔮 What I’ve Learned & Next Steps

This project taught me:

· How to structure a multi‑function program
· Input validation without external libraries
· The importance of flags (is_found, has_lower, etc.)
· How to keep parallel lists in sync

Next improvements (when I learn more):

· Save contacts to a CSV file (Chapter 14 – Files)
· Add a graphical interface with Flask (Chapter 15)
· Replace parallel lists with dictionaries (Chapter 10)

💬 Feedback Welcome

I’m still learning, so any suggestions, code reviews, or ideas are highly appreciated.
Feel free to open an issue or contact me via GitHub.



Author: `NaijaCodeClinician`


License: MIT

