#The movie titles should match the pattern "Title (yyyy)", where "Title" is any string of characters, and "yyyy" is a four-digit year.

import re

title_pattern = re.compile(r"(.*) \((\d{4})\)")

title = input("Enter a movie title: ")

match = title_pattern.match(title)

if match:
    print("Title:", match.group(1))
    print("Year:", match.group(2))
else:
    print("Not a valid movie title.")
