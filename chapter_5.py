#列表 其他功能
#列表去重
list1=[1,10,10,8,2,5,4,4,0,5]
list2=list(set(list1))   #set 是集合  list 是列表
print(list2)



#字典
dict1 = {"sex":"male","age":24,"name":"田所浩二"}
#增删查改

print(dict1["sex"])  #查询字典

dict1["height"]=1.80  #新增字典
dict1["height"]=1.56  #修改字典
del dict1["height"]  #删除字典
print(dict1)
#遍历字典
for k in dict1.keys():
    print(k)
for v in dict1.values():
    print(v)
 for k,v in dict1.items():
    print(k,v)
# 列表到字典
list3=[1,10,10,8,2,5,4,4,0,5]
list4=[str(i)for i in list3]
#等价于下方
lis4=[]
for i in list3:
    lis4.append(str(i))

dict2=dict(zip(list3,list4))
print(dict2)

for k,v in dict2.items():
    print(k,v)