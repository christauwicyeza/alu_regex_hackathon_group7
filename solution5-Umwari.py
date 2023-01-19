import re

def is_valid_joke(joke):
    match = re.match(r"Why did the (.*?) \? Because(.*)")
    if match:
        return True
    else:
        return False

print(is_valid_joke("Why did the chicken cross the road? To get to the other side.")) #True
print(is_valid_joke("Why did the tomato turn red? Because it saw the salad dressing.")) #True
print(is_valid_joke("Why did the math book look sad? Because it had too many problems.")) #True
print(is_valid_joke("Why did the cookie go to the doctor? Because it was feeling crumbly.")) #True

