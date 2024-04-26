import re
emails = ['abc@gmail.com','123$tt*@xyz.com', 'good@bad@uk.in','nasa@usa12.space','no-reply@domain.in','ramhanuman@saketa.lok','ruhi.mohan@exter123.123','fake@fake123.fakercom']

validEmails = []
emailPattern =  '[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'
 

for email  in emails:
    result = re.match(emailPattern,email)
    if result:
        validEmails.append(email)
        
print("\n Valid Email List :",validEmails)