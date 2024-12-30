import random


classmates_list = []

def height_of_classmates(): #making random list of heights for 5 people
    random.seed(42)
    for i in range(5):
        classmates = random.randint(120,200)
        classmates_list.append(classmates)

def sorting_classmates(): #sorting those fellas
    junk_num = []
    for i in range(len(classmates_list)): #in our case we need to make sure that each number gets to the end, so even if biggest number is in the end, it gets to the beginning
        for j in range (len(classmates_list) - 1): #number of changes in our list, to rechange all elements
            if classmates_list[j] > classmates_list[j+1]:
                junk_num = classmates_list[j]
                classmates_list[j]  = classmates_list[j+1]
                classmates_list[j+1] = junk_num

def sorting_Petya(): #putting Petya in place + 
    junk = []
    for i in range(len(classmates_list)):
        for j in range(len(classmates_list)-1):
            if classmates_list[j] > classmates_list[j+1]:
                junk = classmates_list[j]
                classmates_list[j] = classmates_list[j+1]
                classmates_list[j+1] = junk
               

            elif classmates_list[j] == classmates_list[j+1]:
                print("Petya's place is: ", j+2)
                return 0
            
    print("Petya's place is: ", classmates_list.index(x) +1) # shows his place if there is no similiar numbers
            


                

            

height_of_classmates()   
print(f"unsorted list {classmates_list}")

sorting_classmates()
print(f'sorted list of clasmates{classmates_list}')

x = int(input('height of Petya: '))
classmates_list.append(x)

print(f"sorted list with Petya unsorted {classmates_list}")


sorting_Petya()
print(f"sorted list with Petya sorted  {classmates_list}")



 #FINISHED, but is done terribly
