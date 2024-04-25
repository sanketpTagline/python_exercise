import re 

string = 'PQRQRQRQ'
substring = 'QRQ'
 
x = len(re.findall("(?=(QRQ))", string))
print(x)
