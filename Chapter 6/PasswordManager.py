#! python3
# Chapter 6 Project - Simple (Insecure) Password Manager

import sys, pyperclip

PASSWORDS = {
    "email" : "FWK09834JDFpdfkjewr12kdf34",
    "twitter" : "PDF45435kjdsffY534LLdf002",
    "wordpress" : "324KJDFidfs832lkKDF02Dssd",
    "luggage" : "654321"
}

# Check to make sure arg1 is there
if len(sys.argv) < 2:
    print("Usage: python3 " + str(sys.argv[0]) + "[account] - copy account password")
    sys.exit

account = sys.argv[1] # First arg should be the account to retreive the password for

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named: " + account)