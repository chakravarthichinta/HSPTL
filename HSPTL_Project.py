'''

print ("Welcome to the Hospital registration form:")
name = input ("Name ::")
Phone_Number = input("Phone number::")
Age = input ("age::")
EMail_ID = input("Email Id::")
Coming_from = input ("Coming_from::")

print (" name:",name,"\n","Ph_no:",Phone_Number,"\n","Age:",Age,"\n","Emaild:",EMail_ID,"\n","Coming from:",Coming_from,"\n")
### need to Save this info in a text file"
'''


# Data to be saved
name = "John Doe"
age = 28
phone_number = "123-456-7890"
email_id = "johndoe@example.com"

# File name
file_name = "user_data.txt"

# Writing data to the file
with open(file_name, "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Phone Number: {phone_number}\n")
    file.write(f"Email ID: {email_id}\n")

print(f"Data saved successfully in '{file_name}'")



from datetime import datetime

# User data
name = "John reddy"
age = 28
phone_number = "123456999"
email_id = "johndoe@example.com"

# Create file name
first4 = name.replace(" ", "")[:4]            # First 4 characters of name (ignoring spaces)
last4 = phone_number[-4:]                     # Last 4 digits of phone number
date_str = datetime.now().strftime("%d%m%y")  # Current date in ddmmyy format

file_name = f"{first4}{last4}{date_str}.txt"

# Write data into the file
with open(file_name, "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Phone Number: {phone_number}\n")
    file.write(f"Email ID: {email_id}\n")

print(f"Data saved successfully in '{file_name}'")
