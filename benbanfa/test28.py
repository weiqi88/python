#coding=utf-8
import xiti25
sentence = "All good things come to those who wait"
words = xiti25.break_words(sentence)

print (words)

sorted_words =xiti25.sort_words(words)
print(sorted_words)

xiti25.print_first_word(words)


xiti25.print_last_word(words)


xiti25.print_first_word(sorted_words)

xiti25.print_last_word(sorted_words)

print(sorted_words)

xiti25.print_first_and_last(sentence)

xiti25.print_first_and_last_sorted(sentence)

help(xiti25)
help(xiti25.break_words)
