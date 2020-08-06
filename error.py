#!/usr/bin/env python3
import operator
import sys
import re
import csv

error = {}
error_user = {}
per_users = {}
new_dict = {}

filename = sys.argv[1]
error_pattern = r"ticky: ERROR ([\w\s]+)"#.*\(([\w\.\']+)\)$"

with open(filename) as efile:
  lines = efile.readlines()
  for line in lines:
    result = re.search(error_pattern, line)
    print(result)
    if result != None:
      group = result.groups()
      # print(result[1], result[2])
      print(group[0])
      # error_user[group[2]] = error_user.get(group[2], 0) + 1 
      error[group[0]] = error.get(group[0], 0) + 1
new_error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
print(error_user)
with open("error.csv", "w") as file:
  writer = csv.writer(file)
  writer.writerow(["Error","Count"])
  for errors in new_error:
    writer.writerow([errors[0], errors[1]])

pattern = r"ticky: ([A-Z]+) ([\w\s]+) .*\(([\w\.]+)\)$"#" \[(\d+)\] \((\w+)\)$"
with open(filename) as f:
	for line in f:
		result = re.search(pattern, line)
		
		if result != None: #& result[1] == 'INFO':
			if result[1] == "INFO":
				# result = result.groups()
				per_users[result[3]] = per_users.get(result[3],0) +1
				print(result[1], result[2], result[3])
			# errors[result[1]] = errors.get(result[1], 0) + 1
			# result[3] = []
# new_dict = {}
