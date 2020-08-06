#!/usr/bin/env python
import re
import sys
def arrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    else:
        return "{} {}".format(result[2], result[1])


# name = sys.argv[1]
# print(arrange_name(name))