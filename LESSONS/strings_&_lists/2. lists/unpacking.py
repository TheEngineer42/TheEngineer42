"""
UNPACKING
- unpacking a list is a way of extracting its elements into inidvidual 
  variables

"""


numbers = [0,1,2,3,4,5,6,7,8,9,10]
print(*numbers) #0 1 2 3 4 5 6 7 8 9 10
print(*numbers, sep = '\n') #1
                            #2
                            #3
                            #...
                            #10

