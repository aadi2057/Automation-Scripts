#!/usr/bin/env python

from rearrange_name import arrange_name
import unittest

class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Lovelace, Ada"
		expected = "Ada Lovelace"
		self.assertEqual(arrange_name(testcase), expected)

	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(arrange_name(testcase),expected)

	def test_double_name(self):
		"""This method tests if there is a middle name in the string given."""
		testcase = "Jha, Aaditya K."
		expected = "Aaditya K. Jha"
		self.assertEqual(arrange_name(testcase),expected)

	def test_single_name(self):
		"""This method checks if the script runs correctly when single name is given"""
		testcase = "Aaditya"
		expected = "Aaditya"
		self.assertEqual(arrange_name(testcase), expected)



unittest.main()