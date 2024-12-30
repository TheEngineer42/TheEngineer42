"""
Given a string. Determine the total number 
of '+' and '-' symbols in it. 
And also how many such
 symbols are followed by the number zero.
"""

s = 'kjskj+klsj ojkj dkj234-0s45+0+kj-'

print(s.count('+'))
print(s.count('-'))

print(s.count('+0')+s.count('-0'))