#! python3
# Chapter 16 Project - Send emails with a random chore to recipients

import os, sys, logging, smtplib, random, TestGmailCredentials

# Setup
choreList = ['dishes', 'sweeping', 'mopping', 'car wash', 'cooking', 'making drinks']
recipientList = {'alice' : 'alice@example.com',
                 'bob' : 'bob@example.com',
                 'charlie' : 'charlie@example.com',
                 'dave' : 'dave@example.com',
                 'ellie' : 'ellie@example.com'}
fromEmail = TestGmailCredentials.email.get('un') + "@gmail.com"
fromPassword = TestGmailCredentials.email.get('pw')

# Establish SMTP connection
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(fromEmail, fromPassword)

# Assign chore and email each person their chore
for name, email in recipientList.items():
    # Find a random chore and delete it from the list to avoid duplicate chores assigned
    randomChore = random.choice(choreList)
    choreList.remove(randomChore)

    # Send the email message
    emailBody = 'Subject: Your chore for the week\nHello %s,\n\nYour chore for\
        the week is: %s\n\nRegards,\nChore Taskmaster' % (name, randomChore)
    print("Sending email to: %s (%s)..." % (name, email))
    sendMailStatus = smtpObj.sendmail(fromEmail, email, emailBody)

    # Check for errors
    if sendMailStatus == {}:
        print("There was an error sending mail to: %s (%s)" % (email, sendMailStatus))

smtpObj.quit()
print("Done.")