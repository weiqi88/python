#coding=utf-8
from collections import Iterable

L = ['Hello', 'World', 18, 'Apple', None] 

l = [s.lower() if isinstance(s,str) else s for s in ex if s != 18]



print l