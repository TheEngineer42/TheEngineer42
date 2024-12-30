s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo',0,8))


print(s.startswith('foo'))
print(s.startswith('goo'))


s = 'foo bar foo baz foo qux'
print(s.rfind('foo'))
print(s.rfind('bar'))
print(s.rfind('qu'))
print(s.rfind('python'))
