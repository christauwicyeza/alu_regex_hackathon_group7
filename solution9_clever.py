#!/usr/bin/python3
#The IP addresses should match the pattern "xxx.xxx.xxx.xxx" where x is a digit between 0 and 255.
import re


ip = input(" enter Ip address ")

if re.match(r"(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9])\.(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9])\.(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9])", ip):
  print("Valid Ip address")
else:
  print("Invalid Ip address")