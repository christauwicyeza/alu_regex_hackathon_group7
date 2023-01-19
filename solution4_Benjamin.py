import re


isbn = input("enter ISBN number ")

if re.match(r"^(978|979)-\d-\d{3}-\d{5}-\d$", isbn):
  print("Valid ISBN number")
else:
  print("Invalid ISBN number")
