#write a python program that adds all element in a set
# def fruits(friut):
fruit_set = {"orange","berry","apple"}
fruit_list = ["banana","mango","kiwi"]
# fruit_set.update(fruit_list)
fruit_set = set(list(fruit_set) + fruit_list)
print(fruit_set)

#Write a python program to remove an elements in a set at once(C,A,T)
# def sets(set):
set = {"A","B","C","D","E","F"}
set.difference_update({"C","A","F"})
print(set)

#Write a python program that removes the unique item in the sets 
set1 = {"ann","pink","red","blue","white"}
set2 = {"ann","pink","brown","black"}
print(set1.union(set2))
set3 = (set1&set2)
print(set3)

#Romove the set of items that are common in to both set1 and set2
set1 = {"ann","pink","red","blue","white"}
set2 = {"ann","pink","brown","black"}
set1.intersection_update(set2)
print(set1)
#Remove the duplicate items in the list
set1 = {"ann","pink","red","blue","white"}
set2 = {"ann","pink","brown","black"}
print(set1.intersection(set2))

#Given two python set write a python program to update the first set with items
#that exist only in the first set and not in the second set
set1 = {11,22,33,44,66,77}
set2= {88,77,66,65,78,55}
set1.difference_update(set2)
print(set1)


