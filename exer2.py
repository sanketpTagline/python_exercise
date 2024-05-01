from collections import Counter

names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
name_length = []
for i in names:
    name_length.append(len(i))

print("\nNames:",names)   
print("\nName Lengths :",name_length)

lengths_count = Counter(name_length)

print('\nThe three most frequent name lengths are :')    
for length, count in lengths_count.most_common(3):
    name_list = [name for name in names if len(name) == length]
    print(count,"names of Length",length,":" ,name_list)
    
print('\nThe three least frequent name lengths are :')
for length, count in lengths_count.most_common()[:-4:-1]:
    name_list = [name for name in names if len(name) == length]
    print(count,"names of Length",length,":" ,name_list)