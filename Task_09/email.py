# email simulator using OOP
# create email class
class Email:
    # define class variable has_been_read as false
    has_been_read = False
    # define empty list variable called inbox , to store and access the email objects
    inbox = []
    # create constructor with 3 parameters
    def __init__(self, email_address, subject_line, email_content):
        self.recipient = email_address
        self.subject = subject_line
        self.message = email_content
    # create send method
    def send(self):
        print(f"Sending email to {self.recipient} with subject {self.subject} and message {self.message}")
    # create mark_as_read method
    def mark_as_read(self):
        # change has_been_read to true
        self.has_been_read = True


# create function to create email object and add it to the inbox list
def populate_inbox(email_address, subject_line, email_content):
    # create email object
    email = Email(email_address, subject_line, email_content)
    # add email object to the inbox list
    Email.inbox.append(email)
    # return the email object
    return email

# create 3 sample email objects
email1 = populate_inbox("oreakinodidi@gmail.com", "Hello", "How are you?")
email2 = populate_inbox("oreakinodidi@yahoo.com", "Hi", "How are you doing?")
email3 = populate_inbox("test@gmail.com", "Test", "This is a test email")

# Create a function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    # iterate over the email objects in the inbox list
    for email in Email.inbox:
        # print the email objects with a corresponding number starting from 0
        print(f"\n{Email.inbox.index(email)}: Subject-{email.subject}")

# Create a function which displays a selected email. 
# Once displayed, call the class method to set its 'has_been_read' variable to True.
def read_email():
    # ask user to select an index from the list of emails
    index = int(input("\nEnter the index of the email you want to read:"))
    # call the mark_as_read method to change has_been_read to true
    Email.inbox[index].mark_as_read()
    # print the email object with the selected index
    print(f"\nRecipient: {Email.inbox[index].recipient}\nSubject: {Email.inbox[index].subject}\nMessage: {Email.inbox[index].message}\nRead: {Email.inbox[index].has_been_read}\n")
    #tell the user the email has now been marked as read
    print(f"\nEmail from {Email.inbox[index].recipient} has been marked as read.")
    
# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application
    4. View All Emails

    Enter selection: '''))
       
    if user_choice == 1:
    # add logic to read an email
         read_email()
    elif user_choice == 2:
        # add logic here to view unread emails
        for email in Email.inbox:
            if email.has_been_read == False:
                print(f"\nRecipient: {email.recipient}\nSubject: {email.subject}\nMessage: {email.message}\nRead: {email.has_been_read}\n")
    elif user_choice == 3:
        # add logic here to quit appplication
        print("Goodbye!")
        break
    elif user_choice == 4:
        # add logic here to view all emails
        list_emails()
    else:
        print("Oops - incorrect input.")
