#The hex color codes should match the pattern "#XXXXXX" where X is any letter or digit.
import re

user_name_pattern= re.compile(r'#(.{})')

user_name = input("Enter a twitter handle: ")

match = re.search(user_name_pattern, user_name)

if match:
    print(user_name)
else:
    print("Invalid twitter handle")
