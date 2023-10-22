#homo list
shop_list=["apples", "bananas", "chips", "cookies", "water", "candy", "chocolates"]
print(shop_list)

#hetero list
name_list=["Joanna", 2005, 17]
print(name_list)

#repetition
list=[5,10,15]
print(list*5)

list2=[-1, -50]
print(list2)

#len function
nos=[5,10,15,20,25,30]
print("numbers in list: ", len(nos))

#lists r mutable
nos[0]=1
nos[1]=9
print(nos)

list3=list+list2
print(list3)

#list slicing
newlist=[2,4,6,8,10,12,14,16,18,20]
result=newlist[1:9]
print(result)

#if and else statement 
thelist=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33]
if 20 not in list:
    print("No")
else:
    print("Yes")

#sort function
g=[2,7,4,9,1,3,6,5,8]
h=g.sort
print(h)