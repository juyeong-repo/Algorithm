# source: https://school.programmers.co.kr/learn/courses/30/lessons/120896
# solution1: Counter 사용, solution2: list comprehension 사용
from collections import Counter

def solution1(s):
	string = []
	for i,j in Counter(s).items():
		if j == 1:
			string.append(i)
			return ''.join(sorted(string))
		

def solution2(s):
    return ''.join(sorted([c for c in s if s.count(c) == 1]))