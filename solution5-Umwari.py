import re

def is_valid_joke(joke):
    match =re.match(r"why did the.*? \? Because.*" ,joke)
    if match:
        return True
    else:
        return False

print(is_valid_joke("Why did the chicken cross the road? To get to the other side.")) 
print(is_valid_joke("Why did the Tomato turn red? Because it saw the salad dressing."))
print(is_valid_joke("why did the math book look sad? Because it had too many problems."))
print(is_valid_joke("why did the cookie got to the doctor? Because it was feeling crumbly. "))
