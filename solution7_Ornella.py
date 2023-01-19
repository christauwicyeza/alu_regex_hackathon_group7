#The hex color codes should match the pattern "#XXXXXX" where X is any letter or digit.

import re

def is_hex_color(color):
    pattern = re.compile("^#[0-9A-Fa-f]{6}$")
    return pattern.match(color)

print(is_hex_color("#ff0000")) # True
print(is_hex_color("#abcdef")) # True
print(is_hex_color("#123456")) # True
print(is_hex_color("#GGGHHH")) # False (invalid characters)
print(is_hex_color("#12345"))  # False (too short)
print(is_hex_color("#1234567")) # False (too long)
