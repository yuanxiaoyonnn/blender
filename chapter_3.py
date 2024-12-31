#if判断
samples = input("请输入你的渲染采样")
#samples=int (samples)
#print(samples,type(samples))

# if type(samples) ==type("字符串"):
#     print("你的数据类型是字符串")
# else:
#     pass

#逻辑运算符
# if samples !="64":
#     print("不等于64")
#     if int(samples) >"64":
#         print ("大于64")
#     elif int(samples)<64:
#         print ("小于64")
# else:
#     print("等于64")

#for循环

for i in range(0,100,3):   #0-100的采样  3为步长
    if i==5:
        break
    print(i)
#while循环
# samples = input("请输入你的渲染采样")
# samples = int(samples)
# while samples <32 :
#     samples = samples + 1
#     if samples == 28 :
#         continue
#     print(samples)