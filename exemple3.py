import re

st = "/usr/home:lumberjack"
regex = r"\/(.*)\/(.*):(.*)'"
match = re.finditer(regex, st)
print(match)

# pop()
# append()
# +=
