#!/usr/bin/env python
import re
import sys

# filename = sys.argv[1]
def get_errors(filename):
	per_users = {}
	pattern = r"ticky: ([A-Z]+) ([\w\s]+) .*\(([\w\.]+)\)$"#" \[(\d+)\] \((\w+)\)$"
	with open(filename) as f:
		for line in f:
			result = re.search(pattern, line)
			
			if result != None: #& result[1] == 'INFO':
				if result[1] == "INFO":
					# result = result.groups()
					per_users[result[3]] = per_users.get(result[3],0) +1
					# print(result[1], result[2], result[3])
				# errors[result[1]] = errors.get(result[1], 0) + 1

	return per_users

# print(get_errors(filename))

