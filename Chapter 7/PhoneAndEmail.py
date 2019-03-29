#! python3
# Chapter 7 - Project to use regex to match phone #'s and emails from clipboard

import pyperclip, re

phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?              # area code xxx or (xxx)
    (\s|-|.)?                       # separater - or " " or .
    (\d{3})                         # first 3 digits xxx
    (\s|-|.)                        # separater - or " " or .
    (\d{4})                         # last 4 digits xxxx
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension ext or x or ext. xxxxx
)""", re.VERBOSE)

emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something (TLD)
)""", re.VERBOSE)

# get clipboard text
text = str(pyperclip.paste())

matches = []

# find all the phone numbers first
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += " x" + groups[8]
    matches.append(phoneNum)

# find all emails next
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy the results to the clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("There were no phone numbers or email addresses found.")