#!/usr/bin/env python

import shutil
import psutil

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total *100
	return free > 20

def check_cpu_usage():
	cpu_usage  = psutil.cpu_percent(1)
	return cpu_usage < 75

if not check_disk_usage("/") and not check_cpu_usage():
	print("ERROR!")
else:
	print("Your PC is working fine")
