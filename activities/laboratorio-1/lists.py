import math

#Topics: Lists
#1. Given a Python list. Turn every item of a list into its square root
#2. Concatenate two lists with string items index-wise
#
#3. Given a two Python list. Iterate both lists simultaneously such that list1 should display item in
#original order and list2 in reverse order
#4. Remove empty strings from the list of strings
#5. Add item 7000 after 6000 in the following Python List
#list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#Expected output:
#
#6. Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like
#the following list
#list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
#Expected output:
#
#7. Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update
#the first occurrence of a value
#8. Given a Python list, remove all occurrence of 20 from the list


#ITEM 1
list = [1,9,81,142,180,256]

for ind in range(len(list)):
    #print(math.sqrt(each))
    list[ind]= math.sqrt(list[ind])

print(list);

list = []

#ITEM 2
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

for ind in range(len(list1)):
    #list[ind]=list1[ind]+list2[ind]
    list.append(list1[ind] + list2[ind])

print(list)

#ITEM 3
list1=[0,1,2,3,4,5,6,7,8,9]
list2=['a','b','c','d','e','f','g','h','j','k']

for i in range(len(list1)):
    print(list1[i])
    print(list2[len(list2)-i-1])

# OR

print("item4.b")

for i,j in zip(list1, reversed(list2)):
    print(i)
    print(j)

###I have been reading about more python stylistic solutions, which involve mainly the use of 'zip'

#ITEM 4



