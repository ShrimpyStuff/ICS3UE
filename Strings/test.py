import re
string = "Where now? Who now? When now?"
print(re.split(r"(\?) ", string))