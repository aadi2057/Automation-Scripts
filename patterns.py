#!/usr/bin/env python
import re
import sys
from ticky_check import get_errors
import operator
import csv

filename = sys.argv[1]
error_per_user = {}
error = {}
hybrid = {}
per_user = get_errors(filename)
error_pattern = r"ticky: ERROR ([\w \']*) \(([\w\.]+)\)"
username = r"\(([\w\.]+)\)$"
with open(filename) as file:
	reader = file.readlines()
	# print(reader)
	for line in reader:
		line = line.strip()
		# users = re.search(username,  line)
		
		result = re.search(error_pattern, line)
		if result != None:
			# print(result[1])
			# print(result[2])
			error[result[1]] = error.get(result[1], 0) + 1
			error_per_user[result[2]] = error_per_user.get(result[2], 0) + 1
	for line in reader:
		line = line.strip()
		users = re.search(username, line)
		# print(users[1])	
		hybrid[users[1]] = [error_per_user.get(users[1], 0), per_user.get(users[1], 0)]
new_error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
new_hybrid = dict(sorted(hybrid.items(), key=operator.itemgetter(0)))
print(new_hybrid)
with open("__error_message.csv", "w+") as efile:
	writer = csv.writer(efile)
	writer.writerow(["Error","Count"])
	for items in new_error:
		writer.writerow([items[0], items[1]])

print(new_hybrid)
with open("user_statistics.csv", "w+") as perUser:
	writer = csv.writer(perUser)
	writer.writerow(["User","Info","Error"])
	for key, items in new_hybrid.items():
		print(items)
		writer.writerow([key,items[1], items[0] ])
# print(per_user)
# print(error_per_user)
print(error)
