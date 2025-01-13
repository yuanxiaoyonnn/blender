#函数
#函数传入
#def name_of_print(string,*args):        #* 代表不定量的参数
#    print(string)
#    for arg in args:
#        print(arg)
#name_of_print("字符串",1,2,3,4,5)
#函数传出
# sum_numbers(n1,n2):
#    return n1+n2
#print(sum_numbers(2,2))
#匿名函数
#sum =lambda n1,n2: n1+n2   #函数简化
#print(sum(2,2))
#导入
#import random  #导入函数
#random_nums=[random.randint(0,10) for n in range(10)]  #random.randint  随机0-10的数字 10次
#print(random_nums)


##########################################################################################
#主函数的封装
import random

def main():
    result=sum_numbers(2,2)
    print(result)
    print(sum(1,2))

    random_nums=[random.randint(0,10) for n in range(10)]
    print(random_nums)
def sum_numbers(n1,n2):
    return n1+n2
#匿名函数
sum =lambda n1,n2: n1+n2   #函数简化

if __name__ == '__main__':  #使用该方法被import  直接调用的时候不会直接执行。需要调用方法才能运行  例如chapter_6.main()
    main()


