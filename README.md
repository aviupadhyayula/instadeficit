Instadeficit
===============
A Python script that identifies Instagram accounts you follow that don't follow you back. Uses Instaloader (a Python API for Instagram) to scrape inputted accounts' followers and followees; then finds deltas between the two lists.

Dependencies
------------
- All code is written in Python 3.
- Relies on the 'instaloader' library.
- Relies on the 'getpass' library.

Disclaimer
----------
For private accounts, this script will ask you to input your password. This repository is completely open-source, and this script does not store your password either locally or via caching. All passwords are inputted via the 'getpass' library, and are encrypted and hashed. 

Likewise, the 'instaloader' library that this script uses is [open-source](https://github.com/instaloader/instaloader "https://github.com/instaloader/instaloader"). Feel free to check out its source code to assuage any privacy concerns you may have.

Setup
-----
- Clone this repository to your desired location.
- `python3 -m pip install instaloader`

Usage
-----
### Local ###
Execute the instadeficit.py file. Input your username (and for private accounts, your password) as prompted. (For concerns over inputting your password, check out the section labeled 'Disclaimer' above.)

### Replit ###
Copy-paste the script's source code, and then run it.

Instagram may occasionally block log-ins via Replit. This error is flagged in the terminal as "Login: Checkpoint required. Point your browser to https://instagram.com, follow the instructions, then retry." To fix this problem, log in to Instagram normally via your browser, authorize the log-in activity, and then re-run the script.
