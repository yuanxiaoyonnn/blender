#列表  字符串切片
list1=[1,10,10,8,2,5,4,4,0,5]
#添加
list2=[]
a="元素1"
list2.append(a)
for i in list1:
    new=str(i)
    list2.append(new)

list3=list2+list1
# print(list3)


#删除
print(list2)
list2.pop()  #移除末尾

while True :
    if "4" in list2:
        list2.remove("4")
    else:
        break
print(list2)


#查找
print(list2)
b=list2[3]
print(b)
list2.pop(0)  #移除首位
del list2[0]    #移除首位
print(list2)

#修改
list2[1]="新的元素"
print  (list2)

list4=list2[:-2] #将列表后两位移除成立新数组
list4=list2[-2:]    #将列表后两位单独成立新数组
print(list4)


s="新的元素"
for i in range(len(s)):
    print(s[i],end=" ")

s1=s[:2]  #取从头开始的的两位
print(s1)


list2[1]=list1
print(list2)
