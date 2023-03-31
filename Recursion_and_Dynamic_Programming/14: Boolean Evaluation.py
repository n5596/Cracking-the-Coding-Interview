from os import *
from sys import *
from collections import *
from math import *

def evaluateExp(exp):
	# Write your code here.

	memo = {}

	def recurse(s, boolean):
		mod = (10**9)+7

		if s == "":
			return 0

		if len(s) == 1:
			if s == "T" and boolean:
				return 1
			elif s == "F" and not boolean:
				return 1
			return 0

		if (s, boolean) in memo:
			return memo[(s, boolean)]

		ways = 0
		for i in range(1, len(s), 2):
			op = s[i]
			left_T = recurse(s[:i], True)
			left_F = recurse(s[:i], False)
			right_T = recurse(s[i+1:], True)
			right_F = recurse(s[i+1:], False)

			total_ways = ((left_T+left_F)%mod*(right_T+right_F)%mod)%mod

			if op == "&":
				true_ways = (left_T*right_T)%mod
			elif op == "|":
				true_ways = ((left_T*right_T)%mod+(left_F*right_T)%mod+(left_T*right_F)%mod)%mod
			elif op == "^":
				true_ways = ((left_T*right_F)%mod+(left_F*right_T)%mod)%mod

			if boolean:
				ways += true_ways%mod
			else:
				ways += (total_ways-true_ways)%mod

		memo[(s, boolean)] = ways%mod
		return ways%mod

	return recurse(exp, True)
