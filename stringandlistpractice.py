str = "It's Thanksgiving day. It's my birthday, too!"
print str.index("day")

str = str.replace("day", "month", 1)
print str

x = [1, 22, 33, 44, 55, 66 ]
print min(x)
print max(x)

y = ["Banana", "Pineapple", "Papaya", "Coconut", "Mango"]
z = [y[0], y[len(y)-1]]
print z

list = ["cat","dog","worm","rat"]
list = sorted(list)
print list
list1 = list[0:(len(list)/2)]
print list1
list2 = list[(len(list)/2):len(list)]
print list2
list2.insert(0, list1)
print list2
