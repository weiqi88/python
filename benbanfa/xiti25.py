#coding=utf-8
def break_words(stuff):
	"""This function will break up words for us ."""
	words = stuff.split(' ')#通过指定分隔符对字符串进行切片,分割空格
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)#sorted 迭代排序

def print_first_word(words):
	"""print the first word ofter popping it off."""
	word = words.pop(0)#pop从列表中移除并返回第一个对象或者obj
	print word

def print_last_word(words):
	"""Prints the last word after popping it off"""
	word=words.pop(-1)#pop从列表中移除并返回最后一个对象或者obj
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words=break_words(sentence)#调用break_words 对空格切片
	return sort_words(words)#对分片后的 字符进行排序
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words =break_words(sentence)#调用break_words 对空格切片
	print_first_word(words)#pop从列表中移除并返回第一个对象或者obj
	print_last_word(words)#pop从列表中移除并返回最后一个对象或者obj
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)#对字符切片后的字符串进行排序
	print_first_word(words)#pop从列表中移除并返回第一个对象或者obj
	print_last_word(words)#pop从列表中移除并返回最后一个对象或者obj
	





















	
	
	
	
	
	
	