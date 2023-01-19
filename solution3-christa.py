#The twitter handles should match the pattern "@username", where "username" can be any string of letters and digits.

import re

user_name_pattern= re.compile(r'@([a-zA-Z0-9]+)')

user_name = input("Enter a twitter handle: ")

match = re.search(user_name_pattern, user_name)

if match:
    print(user_name)
else:
    print("Invalid twitter handle")
            