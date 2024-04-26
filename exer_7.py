import re
emails = ['abc@gmail.com','123$tt*@xyz.com', 'good@bad@uk.in','nasa@usa12.space','no-reply@domain.in','ramhanuman@saketa.lok','ruhi.mohan@exter123.123','fake@fake123.fakercom']

valid_emails = []
email_pattern = '[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,5}$'
 
for email in emails:
    result = re.match(email_pattern,email)
    if result:
        valid_emails.append(email)
        
print("\n Valid Email List :",valid_emails)