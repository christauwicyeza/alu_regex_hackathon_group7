#The song lyrics should match the pattern "[Verse X] some lyrics", 
# where X is a number, and "some lyrics" can be any string of characters.

import re
song_lyrics = re.compile(r"(\d+)(.+)")
lyrics = input("Enter the song lyrics here :")
match = song_lyrics.match(lyrics)
if match:
    print ("The numbers in the lyrics are  :", match.group(1))
    print (" The other characters are : ", match.group(2))

else:
    print ("Not a valid lyrics.")
