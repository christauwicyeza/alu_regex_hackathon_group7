#The jokes should match the pattern "Why did the ... ? Because...", where the first part of the pattern can be any string of characters, and the second part can be any string of characters

import re 

pattern = re.compile(r"(Why did the (.*?) \? Because(.*))")

joke = "Why did the tomato turn red? Because it saw the salad dressing."

match = pattern.match(joke)
if match:
    print("First part:", match.group(1))
    print("Second part:", match.group(2))
else:
    print ("It is not a joke")

