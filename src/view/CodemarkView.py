#!/usr/bin/env python

# Copyright (c) 2012 Anthony Liu
# All rights reserved.
#
# License: BSD 

import sys
from array import *

class CodemarkManager():

	def __init__(self, parent=None):
		self.haystack = []
		
	def check(self, filename, line):
		if self.haystack.count((filename, line)):
			return 1
		return 0

	def append(self, filename, line):
		if self.check(filename, line) == 0:
			self.haystack.append((filename, line))
		return self.haystack.index((filename, line))
	
	def delete(self, filename, line):
		if self.haystack.count((filename, line)) == 0:
			return -1
		else:
			self.haystack.remove((filename, line))
			return 0
	
	def delete_index(self, index):
		if self.count() <= index:
			return -1
		elif index < 0:
			return -1
		else:
			self.haystack.pop(index)
			return 0
	
	def count(self):
		return len(self.haystack)
	
	def get(self, index):
		if self.count() <= index:
			return (None, None)
		elif index < 0:
			return (None, None)
		else:
			(filename, line) = self.haystack.pop(index)
			self.haystack.insert(index, (filename, line))
			return (filename, line)
		
	def clear(self):
		del self.haystack[:]

	def codemarks(self):
		return self.haystack

	def dump(self):
		for i in range(len(self.haystack)):
			print("cm index ", i, " ", self.haystack[i], file=sys.stderr)

#############################################################################
#
# Basic unit test
#
#############################################################################

if __name__ == '__main__':
	
	cm = CodemarkManager()

	#
	# case 1, basic add, delete
	#
	
	print("Initial empty", file=sys.stderr)
	
	print("cm has ", cm.count(), "items (0)", file=sys.stderr)

	cm.append("file1", 100)
	cm.append("file2", 200)
	cm.append("file3", 300)

	print("cm has " , cm.count(), "items (3) ", file=sys.stderr)
	
	cm.delete("file1", 100)

	print("cm has " , cm.count(), "items (2)", file=sys.stderr)
	
	cm.delete("file2", 100) # not existed

	print("cm has " , cm.count(), "items (2)", file=sys.stderr)

	cm.delete_index(1)

	print("cm has " , cm.count(), "items (1)", file=sys.stderr)

	#
	# case 2, dump
	#

	for i in range(cm.count()):
		(f, l) = cm.get(i)
		print(f, " (#", l, ")", file=sys.stderr)

	#
	# case 3, duplicate
	#

	index = cm.append("file4", 400)
	print("index for file4 #400 is " , index, file=sys.stderr)
	
	index = cm.append("file4", 400)
	print("index for file4 #400 is " , index, " (again)", file=sys.stderr)
	
	print("cm has " , cm.count(), "items (2) ", file=sys.stderr)

	#
	# case 4, dump for eye examine
	#

	print("cm dump for final check", file=sys.stderr)

	cm.dump()
