# 尝试摄取知识
# 厌学的人必遭毒打
# 中文编码声明注释，在文件开头加上中文声明注释，用以指定源码文件的编码格式  例：coding:gdk放在开头就是指定源码为gdk格式
print(12424)
print('hello World')
print('hello\nWorld')
print('hello\tchenyi')
print('helloo\b\tworld')

# chr是charcode，意思是字符码，使用的是unicode汉字编码表
print('----------------字符码，编码-----------------------')
print(chr(0b100111001011000))
print(ord('乘'))

# 保留字、标识符，命名时避免重复
print('------------------保留字、标识符---------------------')
import keyword
print(keyword.kwlist)

# 变量的标识：对象存储内存地址，id（obj)
# 变量类型：type（obj）
print('-----------------变量类型----------------------')
name='小丑'
print('标识',id(name))
print('类型',type(name))
print('值',name)

# 0b二进制  0o八进制  0x十六进制
# 浮点数存储不精确（例如1.1+2.2不得3.3），所以引入模块decimal解决问题
print('-----------------浮点数不准确----------------------')
n1=1.1
n2=2.2
print(n1+n2)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

# 字符串可以用单双三引号都可以使用，三引号可以写成多行(单双则不行)
print('------------------引号---------------------')
str1='尝试摄取知识'
str2="厌学的人必遭毒打"
str3="""强者！
不会停止学习！"""
print(str1)
print(str2)
print(str3)

# 类型转换 int(),str(),float()。将str转换int型时，字符串必须为数字串（整数），非数字串不允许转换；
# 浮点数转换时，整数转换成浮点数末尾+.0，文字不允许转换

# input函数 输入时作为的是string类型进行储存的，所以要将输入的值的类型进行转换
'''
print('----------------input函数-----------------------')
a1=float(input('请输入被除数：'))
b1=float(input('请输入除数：'))
# print(a1/b1)
'''

# 运算符： + - * / 整除（//） % 幂运算符（**）
print('--------------------运算符-------------------')
print(11//5)
print(2**3)
# 一正一负的整除公式，向下取整
print(9//-4)  #-3
# 一正一负取余遵循公式
print(9%-4)   #-3 公式 余数=被除数-除数*商  9-（-4）*（-3）=-3   这里的商用的是尚书整除的商
print(-9%4)   #3    -9-4*(-3)=3
# 赋值运算符  支持链式赋值  支持参数赋值 += -= /= //= %=  支持系列解包赋值
a2=b2=c2=20
print(a2,b2,c2)
a3,b3,c3=20,30,40
print(a3,b3,c3)
# 交换值
a3,b3=b3,a3
print(a3,b3)

# 比较运算符 ,比较结果为bool类型 > >= < <= == !=
print('------------------比较运算符---------------------')
a4,b4=30,40
print("a4>b4吗?",a4>b4)
# 比较对象的标识使用  is  ; is not
print('------------------is  ; is not---------------------')
a5=10
b5=10
print(a5==b5)  #true   此时a5和b5值和id都相等(计算机看到10之前有储存地址就直接给b5)
print(a5 is b5)  #true  is not同理
lst1=[11,22,33,44]  #大概类似数组的东西,储存地址不同
lst2=[11,22,33,44]
print(lst1==lst2) #true
print(lst1 is lst2) #false

# bool运算符  :  and , or , not , in , not in
print('----------------bool运算符 -----------------------')
s1='i hate the world'
print('w' in s1) # True    w在里面,所以为true
print('w' not in s1)  #False w在里面,所以为false

# 位运算符  :按位与&，按位或|(先将数转换为二进制，然后依次比较，按位与是同位相同为1，按位或是同位相同为0)
#          左移位运算符<<(高位舍弃，低位补0)，右移位运算符>>(低位溢出舍弃，高位补0)
print('---------------位运算符-----------------------')
print(4&8)  # 100  1000   结果为0000  0
print(4|8)  # 100  1000   结果为1100  12
print(4<<1)  # 向左移动1个位置 相当于乘2
print(4<<2)  #            相当于乘2乘2
# 运算符优先级  算术运算>位运算>比较运算>bool运算

# 程序的组织结构 顺序结构、选择结构、循环结构
# 对象的bool值，0，空（），false的bool值为false，其他的为true
# 选择结构
'''
print('--------------选择结构-------------------------')
money=1200
s2=int(input('假如我有1200块，并且我想取出'))
money=money-s2
if money>=0:
    print('取款成功，余额为:',money)
else:
    print('你的余额不够，少取点')
'''

#多分支结构  if嵌套结构
'''
print('----------------多分支结构  if嵌套结构-----------------------')
score=int(input('请输入你的成绩：'))
if score>=90 and score<=100:
    print('太牛辣！')
    if score==100:      #if嵌套
        print('是试卷最多只有100分限制了你吗？')
    else:
        print('请保持')
elif 80<=score<90:     #python 独特写法
    print('有点东西，但不多')
else:
    print('请不要乱来')
'''
#条件判断 表达式 true执行前面的句子
'''
print('-----------------条件判断 ----------------------')
Q=input('你是高手吗？ y/n')
print('真的吗？' if Q=='y' else "小丑")
'''

#pass语句，，什么都不做，只是一个占位符，用到需要写句子的地方，为了让程序不报错

#range()函数 用于生成一个整数序列
# range(stop)  range (start,stop)  range(start,stop,step)   起点，终点，间隔
print('-------------------range()函数--------------------')
r1=range(10)
r2=range(1,10)
r3=range(1,10,2)
print(list(r1))
print(list(r2))
print(list(r3))

#  while循环
print('-----------------while循环----------------------')
s2=1
sum1=0
while s2<=100:
    if not bool(s2%2):  #  可以替换为if s2%2==0:
        sum1+=s2
    s2+=1
print('while实现1到100之间的偶数和为：',sum1)
#  for-in循环
print('------------------for-in循环---------------------')
for i1 in 'python':
    print(i1)
for _ in range(6):
    print('我是帅哥，我是帅哥')
for i2 in range(6):
    print(i2)
sum2=0
for i3 in range(101):
    if i3%2==0:
        sum2+=i3
print('if语句实现求100内偶数和',sum2)
#for循环实现100-999之间水仙花数（个十百分别三次方相加和原数相等）
print('-------------------100-999之间水仙花数--------------------')
print('100-999之间的水仙花数')
for a6 in range(100,999):
    ge=a6%10
    shi=a6//10%10
    bai=a6//100
    if a6==ge**3+shi**3+bai**3:
        print(a6)

# 流程控制语break  终止语句，可以和if、while  参考c++
# 流程控制语continue  结束循环进行下一次循环  参考c++
# else 参考c++
# 嵌套循环  参考c++
for i in range(1,7):
    for j in range(1,6):
        print('*',end='\t')   # 不换行输出
    print()  #换行   如果不手动设置end，则end=‘n’，所以print()默认为换行输出
# 99乘法表
print('-----------------99乘法表----------------------')
for i in range(1,10):
    if i<=9:
        for j in range(1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
        print()


# 列表（参考c++数组）
# 代表列表的创建的创建方式  []   list()
# 列表元素顺序排列
# 索引反映唯一数据  第一个为0 或 最后一个为-1（负数索引），每个元素间隔为1
# 可以存储不同的数据类型，相同的元素
# 根据需要动态分配和回收内存（c++输麻了...）
print('--------------列表-------------------------')
lst3=['hello','chenyi','handsome boy',666]
print(lst3[0],lst3[-4])
# 获取列表元素的索引  如果存的是相同元素则只返回第一个的索引
print(lst3.index('handsome boy'))
# 指定范围内查找元素
'''
print(lst3.index('chenyi',2,3))  # ValueError: 'chenyi' is not in list
'''

# 获取列表中的多个元素    列表名[start:stop:step]  切片查找范围[start,stop)  step默认为1，可省略不写
print(lst3[::-1])  # 从后往前列出
print(lst3[2::-1])  # 从指定位置往前
# 使用in not in 判断列表中是否有指定元素

# 列表元素的增加操作
# append()  在列表末尾添加一个元素
print('------------------列表元素的增加操作---------------------')
lst3.append('shuai guo')
print(lst3)
# extend()  在列表末尾至少添加一个元素
lst4=[1,2,3,4,5]
lst3.append(lst4)  #  将lst4作为一个元素添加进lst3
print(lst3)
lst3.extend(lst4)  #  将lst4作为5个元素添加进lst3
print(lst3)
# insert()  在列表的任意位置添加一个元素
lst3.insert(2,20)
print(lst3)
# 切片  在列表的任意位置添加至少一个元素
lst3[2:2]=lst4
print(lst3)
 #如果让lst4中的元素代替lst3的元素 lst3[:]=lst4

# 删除操作
# remove() 一次删除一个元素；重复元素只删除一个；元素不存在会报错ValueError
print('----------------删除操作-----------------------')
lst3.remove(20)
print(lst3)
# pop()删除一个索引位置上的元素；不指定就删除最后一个元素
lst3.pop(10)
print(lst3)
# 切片  一次至少删除一个元素  切片的范围[,)
new_lst=lst3[0:10]
print('原列表：',lst3)
print('切片删除后的列表：',new_lst)
lst3[0:10]=[]
print('在原列表上进行删除：',lst3)
# clear()清空列表  del删除整个列表
lst4.clear()
print(lst4)
# del lst4
# print(lst4)  会报错

# 修改列表元素
print('-----------------修改列表元素----------------------')
lst3[4]=100
print(lst3)
lst3[2:4]=[99,66,88]  #  可以多换，可以少换
print(lst3)

# 列表元素的排序操作  排序在原列表上进行的
print('----------------列表元素的排序操作-----------------------')
lst3.sort()  #  一般情况下是升序
print(lst3)
# 降序
lst3.sort(reverse=True)
print(lst3)
# 使用内置函数sorted()排序，会产生新列表
new_lst2=sorted(lst3)
print(lst3)
print('new_lst2',new_lst2)
new_lst3=sorted(new_lst2,reverse=True)  #降序
print('new_lst3',new_lst3)

# 列表生成式   要有一定的规则
print('----------------列表生成式-----------------------')
lst5=[i for i in range(1,10)]
print(lst5)
lst5=[i*i for i in range(1,10)]
print(lst5)
lst5=[i*3 for i in range(1,5)]
print(lst5)


# 字典  以键值对的方式存储数据，字典是一个无序序列，不可变序列（不能执行增删改操作）
# 花括号进行创建    ；   内置函数dict（）进行创建
print('-----------------字典----------------------')
scores1={'chenyi':666,'python':777}
print(scores1)
print(type(scores1))
print()
student1=dict(name='chenyi',age=20)
print(student1)
print(type(student1))
# 空字典
print()
d1={}
print(d1)

# 获取字典中的元素  []    ；get()
print('----------------获取字典中的元素-----------------------')
print(scores1['chenyi'])  #  如果元素不存在，会报错
print(scores1.get('python'))  #  元素不存在不会报错，而是输出None
print(scores1.get('陈六',404))  #  404是在查找’陈六‘不存在时的，提供的一个默认值

print('------------------字典中的操作---------------------')
# key的判断  用 in ；  not in
# 删除操作  del scores1['python']  清空字典   scores.clear()
# 字典元素新增
scores1['陈六']=99
print(scores1)
# 字典元素修改
scores1['陈六']=100
print(scores1)
# 获取键 key()
# 获取值 values()
# 获取对 items()
# 字典元素遍历
for item in scores1:
    print(item,scores1[item])

# 特点  1.key不允许重复，value可以重复  2.key是不可变对象  3.字典也是根据需要动态伸缩  4.字典比较浪费内存，属于空间换时间

# 字典生成式  内置函数zip()
items1=['apple','peach','grape']
prices=[10,20,30,40,50]
d2={i.upper():j     for i,j in zip(items1,prices)}  #.upper是将关键字大写   将items1作为键，proces作为值生成字典
print(d2)


print('----------------元组-----------------------')
# 元组 python内置结构之一，是不可变序列
# 可变序列（增删改操作地址，不发生改变）  列表  字典
# 不可变序列（增删改操作，地址改变）  字符串  元组
t1=('python','陈',33)         # 直接小括号创建
t2=tuple(('hello','世界',22))   # 内置函数tuple()函数创建
t3='chenyi','shuaige',66     # 括号可以省
t4=(10,)                     # 只有一个元素不能省，不然就是str类型了
print(type(t1),type(t2),type(t3),type(t4))
# 元组的对象本身是不可变对象，则不能引用其他对象
# 元组的对象如果是可变对象，则可变对象的引用不允许改变，但数据可以改变
t5=(1,2,3,4,[10,20,30])
print(t5)
# t5[4]=100会报错
t5[4].append(100)
print(t5)

# 集合  内置数据结构 可变类型（列表、字典）  集合是没有value的字典
# {}   ;   内置函数set()
print('-----------------集合----------------------')
s3={1,2,3,4,5,5,5,6,7}
print(s3)  #  集合中的元素不允许重复，否则自动删除
s4=set(range(6))
print(s4)
print(set([12,45,465,48,79]))   #  列表转换为集合
print(set((42,45,689,78)))  #  元组
print(set('python'))  #  字符串  因为经过哈希计算，是无序的
s5=set()  #  定义空集合
print(s5,type(s5))

print('-----------------集合的相关操作----------------------')
# 集合中的判断操作 in ； not in
print(100 in s4)
print(3 in s4)
# 集合中的增加   无序
print('-----------------集合增加操作----------------------')
s4.add(122)   # 加一个
print(s4)
s4.update({120,119,110})  #  加好多个
print(s4)
s4.update((134,353,6464))  #  添加元组
print(s4)
s4.update([100,200,300])  # 加列表
print(s4)
# 删除
print('------------------集合删除操作---------------------')
s4.remove(122)  #  一次删一个，指定元素不存在则报错
print(s4)
s4.discard(500)  #  一次删一个，指定元素不存在不报错
print(s4)
s4.pop()# 随机删除  不能够指定元素
print(s4)
s4.clear()  #  清空操作
print(s4)

# 集合间的关系
print('------------------集合间的关系---------------------')
s5={10,20,30,40}
s6={40,30,20,10}
print(s5==s6)  #  判断是否相等
print(s5!=s6)
s7={10,20,30,40,50,60}
print(s5.issubset(s7))  #  s5是s7得子集
print(s7.issuperset(s5))   #  s7是s5的超集
s8={10,33,22,20,40}
print(s8.isdisjoint(s7))  #  判断是否有交集，有交集则为False  ；没有交集则为True

# 集合的数学操作
print('-----------------集合的数学操作----------------------')
print(s8.intersection(s7))  #  打印交集
print(s8 & s7)              #  同上
print(s7.union(s8))         #  打印并集
print(s7 | s8)              #  同上
print(s7,'   ',s8)          #  集合没发生改变
print(s7.difference(s8))    #  打印差集   s7减去交集部分剩下的
print(s7-s8)                #  同上
print(s7.symmetric_difference(s8))  #  对称差集  s7和s8除去交集剩下的
print(s7^s8)                        #  同上
print(s7.symmetric_difference_update(s8))  #

# 集合生成式
print('-----------------集合生成式----------------------')
lst6=[i*i for i in range(10)]
print(lst6)
s9={i*i for i in range(10)}    #  类似列表，但是无序
print(s9)



# 字符串的驻留机制   即对相同字符串不会开辟新地址进行保存
print('---------------字符串的驻留机制------------------------')
# 字符串长度为0或1时
# 符合标识符（数字、字母、下划线）的字符串
# 字符串只在编译时进行驻留，而非运行时
# [-5，256]之间的整数数字

# sys中的inter方法强制2个字符串指向同一个对象
# pycharm对字符串进行了优化

# 优点：需要值相同的字符串是直接从字符串池里拿来使用，避免频繁的创建和销毁
# 在需要进行字符串的拼接时，建议使用str类型的join方法，而非+，因为join()方法是先计算出所有字符串的长度，然后再进行拷贝，只new一次对象，效率比 + 要高
print('------------------字符串的查找操作---------------------')
z1='hello,hello'
print(z1.index('lo'))     #  查找字符串第一次出现的位置，找不到会报错
print(z1.rindex('lo'))    #  查找最后一次出现位置，找不到会报错
print(z1.find('lo'))      #  查找第一次位置，找不到输出-1
print(z1.rfind('lo'))     #  查找最后一次位置，找不到输出-1
print('------------------字符串的大小写转换(都会产生新字符串)---------------------')
z2='hello,python'
print(z2.upper())  #  所有字符串转换成大写，产生新字符串
print(z2.lower())  #  所有字符串转换成小写
print(z2)
z3='hello,CHENYIyi'
print(z3.swapcase())    #  大变小，小变大
print(z3.capitalize())  #  第一个字符转换成大写，其余变小写
print(z3.title())       #  把每个单词第一个大写，其余小写
print(z3)
print('-------------------字符串内容对齐操作--------------------')
print(z3.center(19,'*'))  #  居中对齐
print(z3.ljust(20,'-'))   #  左对齐
print(z3.rjust(20,'+'))   #  右对齐，宽度小于原值则输出原值
print(z3.rjust(6,'*'))
print(z3.zfill(20))       #  右对齐，左边只能用0填充
print('-489'.zfill(8))    #  在负号前面+0
print('-------------------字符串的劈分操作--------------------')
z4='hello world 666'
z5='hello|world|666'
print(z4.split())                      #  默认空格为分界线，返回值是一个列表
print(z5.split(sep='|'))               #  可以指定分界符
print(z5.split(sep='|',maxsplit=1))    #  可以指定分界次数
# rsplit从右边开始劈分

# 字符串的判断
print('-----------------字符串的判断----------------------')
print('1.','hello'.isidentifier())  # 判断指定字符串是否是合法标识符
print('2.','hello_张三_123'.isidentifier())
print('3.','\t'.isspace())  # 判断指定字符串是否全部由空白字符组成（回车，换行，水平制表）
print('4.','abc'.isalpha())  # 判断指定字符串是否全部由字母组成
print('5.','绽放三'.isalpha())
print('6.','张三1'.isalpha())
print('7.','123四'.isdecimal())  # 判断指定字符串是否全部由十进制数字组成
print('8.','123'.isdecimal())
print('9.','123四'.isdecimal())
print('10.','Ⅰ Ⅱ Ⅲ'.isdecimal())
print('11','123四'.isnumeric())   # 判断指定字符串是否全部由数字组成
print('12','abc1'.isalnum())  # 判断指定字符串是否由数字和字母组成

print('-----------------字符串的替换，合并----------------------')
print(z2.replace('python','java'))
z6='hello,python,python,python'
print(z6.replace('python','java',2))  #  指定替换内容 ，指定次数

# 字符串的合并
lst7=['hello','java','python']
print('|'.join(lst7))
print(''.join(lst7))

t6=('hello','java','python')
print(''.join(t6))

print('*'.join('python'))

print('-----------------字符串的比较操作----------------------')
# 字符串的比较操作
# 运算符：>,>=,<,<=,==,!=
# 比较规则:首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，
# 依次比较下去，直到两个字符串中的字符不相等时，
# 其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较
print('apple'>'app')
print('apple'>'banana')   # 相当于97>98为false

print('------------------字符串的切片操作---------------------')
# [start:end:step]
print(z6[1:10:2])
print(z6[::-1])

print('-------------------格式化字符串--------------------')
# 几种方式
# 一、%作为占位符  %s 字符串；%i 整数；%f 浮点数
# 二、{}作占位符
# 三、f-string
age=20
print('巴拉巴拉%s,balabala%d' % (name,age))
print('巴拉巴拉{0},balabala{1}'.format (name,age))
print(f'巴拉巴拉{name},balabala{age}')
print('%10d'%99)  #10表示宽度
print('%.3f'%3.14159265354)  #表示小数点后三位
print('%10.3f'%3.14159265354)#同时表示宽度和精度
print('hellohello')
print('{:.3}'.format(3.14159265354))#.3表示一共三位数
print('{:.3f}'.format(3.14159265354))#表示三位小数
print('{:10.3}'.format(3.14159265354))#同时表示

print('-------------字符串的编码转换--------------------------')
s8='好好学习天天向上'
# 编码
print(s8.encode(encoding='GBK'))#GBK中编码格式中，一个字符占两个字节
print(s8.encode(encoding='UTF-8'))#UTF-8中编码格式中，一个字符占三个字节
# 解码
#type代表就是一个二进制数据（字节类型的数据）
byte=s8.encode(encoding='GBK')#编码
print(byte.decode(encoding='GBK'))#解码

byte=s8.encode(encoding='UTF-8')#编码
print(byte.decode(encoding='UTF-8'))#解码


print('------------------函数的创建和调用---------------------')
# 函数的创建
def calc(a,b):
    c=a+b
    return c
result1=calc(10,20)
print(result1)

result2=calc(b=10,a=20)#关键字传递
print(result2)

print('------------------函数的返回值--------------------')
# 函数返回多个值时，结果为元组   只有一个时就是返回他自己的类型
def fun(num):
    odd=[]#存奇数
    even=[]#存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even

lst8=[10,29,34,23,44,53,55]
print(fun(lst8))

print('-----------------函数参数定义----------------------')
def fun(*args):   #  定义个数可变的参数 ，就是不知道有几个参数的时候加符号 *
    print(args)
fun(10)
fun(10,20,30)

def fun1(**args):    #  定义个数可变的关键字形参加符号 **    ； 结果为字典
    print(args)
fun1(a=10)
fun1(a=10,b=20,c=30)

print('-------------------函数的调用--------------------')
lst9=[111,222,333]
def fun2(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun2(10,20,30)
print('--------------')
fun2(*lst9)  # 在函数调用时，将列表的每个元素都转换作为位置实参传入
print('--------------')
dic1={'a':11,'b':22,'c':33}
fun2(**dic1)   # 在函数调用时，将字典的每个元素都转换作为位置实参传入

def fun3(a,b,*,c,d):   # 从*之后的参数必须使用关键字传参
    pass
# 函数参数位置
def fun4(a,b,*,c,d,**arg1):
    pass
def fun5(*arg1,**arg2):
    pass

print('-------------------变量的作用域--------------------')
# 局部变量、全局变量参考c++
def fun6():
    global name1   # global是在函数内定义的全局变量
    name1='joker'
    print(name1)

fun6()
print(name1)

print('-----------------递归函数----------------------')
# 参考c++

print('-----------------遇到bug自己查----------------------')


print('------------------异常处理机制---------------------')
# try  except，可以多加几个except ，为了避免纰漏，最后可加一个except BaseException
'''
try:
    a6=int(input('请输入第一个整数'))
    b6=int(input('请输入第二个整数'))
    result3=a6/b6
    print('结果是：',result3)
except ZeroDivisionError:
    print('除数不允许为0')
except ValueError:
    print('只能输入数字')
print('结束')
'''
# try...except...else结构
'''
    a6=int(input('请输入第一个整数'))
    b6=int(input('请输入第二个整数'))
    result3=a6/b6
except BaseException as e:     #   这里的会报e里所报错的东西
    print('出错了')
else:
    print('结果是：',result3)
'''
# try...except...else...finally 无论如何finally都会执行
# Python 常见异常类型
# ZeroDivisionError   除（取模）为0
# IndexError          序列中没有此索引（index）
# KeyError            映射中没有这个键
# NameError           未申明/初始化对象（没有属性）
# SyntaxError         Python 语法错误
# ValueError          传入无效的参数

# Traceback打印异常信息

print('----------------类与对象-----------------------')
'''
class Student:  #  定义类class,类名每个单词首字母大写
    native_place='重庆'  #  直接写在类里的变量，成为类属性
def __init__(self,name,age):
    self.name=name  #  self.name称为实体属性，进行一个赋值操作，将局部变量name的值赋值给实体属性
    self.age=age

    # 实例方法   在类之内定义的称为方法，类之外定义的称为函数
    def eat(self):
        print('cy吃饭')
# 静态方法
@staticmethod
def method():
    print('使用了staticmethod进行修饰，所以我是静态方法')

# 类方法
@classmethod
def cm(cls):
    print('使用了classmethod进行修饰，所以我是类方法')
'''
print('-----------------对象的创建----------------------')
# 实例名=类名（）

# 创建Student类的对象
# stu1=Student('张三',20)
# Student.eat(stu1)      stu1.eat()    也可以像c++一样调用

# 类属性的使用方式
# print(Student.native_place)  访问类属性
# Student.cm()  调用类方法    属于对象，可以通过cls访问
# Student.sm()  调用静态方法   定义在类里的函数


print('-----------------动态绑定属性和方法----------------------')
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在睡觉')

stu1=Student('张三',20)
stu2=Student('李四',30)
stu1.gender='女'   # 只为stu1绑定性别  stu2则没有gender这个属性，实现动态绑定属性
def show():
    print('定义在类之外的，称为函数')
stu1.show=show()     # 只为stu1绑定方法  stu2则没有这个方法，实现动态绑定方法

# 在Python中没有单独的私有属性标识符，所以一般用两个下划线(__)表示
class A:
    pass
class B:
    pass
class C(A,B):  #  继承
    pass
#方法重写，参考c++，子类重写后可以用super().xxx()屌用父类中被重写的方法
# object类是所由类的父类，内置函数dir()可以查看指定对象所有属性
# 简单地说，多态就是“具有多种形态"，它指的是:即便不知道一个变量所引用的对象到底是什么类型,
# 仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型,动态决定调用哪个对象中的方法。
# __dict__获得类对象或实例对象所绑定的所有属性和方法的字典
# __len__()通过重写__len__()方法，让内置函数1en()的参数可以是自定义类型
#__add__()通过重写_add_(方法，可使用自定义对象具有“+”功能
# __new__()用于创建对象
# __init__()对创建的对象进行初始化

# print('-----------------拷贝----------------------')
# Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此,源对象与拷贝对象会引用同一个子对象
# 使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同(copy.deepcopy)

print('-----------------模块----------------------')
# 模块的导入
import math
from math import pi  # 从模块中导入某个函数
print(pi)
# 如果想导入自己写的模块
import calc  # 引用自己写的模块，将目标标记为源代码根目录

print(calc.add(10,110))

print('-----------------包----------------------')
import package
import calc  #使用import方式进行导入时，只能跟包名或模块名

from package import module1
from package.module1 import a  #  使用from ...import可以导入包,模块,函数，变量
'''
sys      与Python解释器及其环境操作相关的标准库
time     提供与时间相关的各种函数的标准库
os       提供了访问操作系统服务功能的标准库
calendar 提供与日期相关的各种函数的标准库
urllib   用于读取来自网上（服务器）的数据标准库
json     用于使用JSON序列化和反序列化对象
re       用于在字符串中执行正则表达式匹配和替换
math     提供标准算术运算函数的标准库
decimal  用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging  提供了灵活的记录事件、错误、警告和调试信息等目志信息的功能
'''
import urllib.request
print(urllib.request.urlopen('https://www.bilibili.com/').read())  # 用于爬虫等


# 第三方模块安装  cmd中下载
# pip install 模块名
# 第三方模块名的使用
# import 模块名

print('----------------文件的读写操作-----------------------')
# 内置函数open()语法规则
# file=open(filename [,mode,encoding])
# file:被创建的文件对象   open:创建文件对象的函数  filename:要创建或者打开的文件名
# mode:模式默认为只读  encoding:默认文本文件中字符的编写格式为gbk
'''
file=open('a.txt','r')
print(file.read())
file.close()
'''

# r   以只读模式打开文件，文件的指针将会放在文件的开头
# w   以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
# a   以追加模式打开文件，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾
# b   以二进制方式打开文件，不能单独使用，需要与共它模式一起使用，rb，或者wb
# +    以读写方式打开文件，不能单独使用，需要与其它模式一起使用，a+

# read([size])         从文件中读取size个字节或字符的内容返回。若省略[size]，则读取到文件末尾，即一次读取文件所有内容
# readline()           从文本文件中读取一行内容
#readlines()           把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
# write(str)           将字符串str内容写入文件
# writelines(s_list)   将字符串列表s_list写入文本文件，不添加换行符
#  seek(offset[, whence])       把文件指针移动到新的位置，offset表示相对于whence的位置:offset:为正往结束方向移动，为负往开始方向移动
#                               whence不同的值代表不同含义:
#                               0:从文件头开始计算（默认值)
#                               1:从当前位置开始计算
#                               2:从文件尾开始计算
# tell()               返回文件指针的当前位置
# f1ush()              把缓冲区的内容写入文件，但不关闭文件
# close()              把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源

print('---------------with语句------------------------')
# with语句可以自动管理上下文资源，不论什么原因跳出with块,都能确保文件正确的关闭，以此来达到释放资源的目的
'''
with open('a.txt','r') as file1:
    print(file1.read())
'''

print('-----------------os模块----------------------')
# os模块操作目录
'''
import os
os.system('calc.exe')  #  可以打开系统的一些操作
os.startfile('C:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe')   #  直接调用可执行文件
'''
# getcwd()                             返回当前的工作目录
# listdir(path)                        返回指定路径下的文件和目录信息
# mkdir(path[, mode])                  创建目录
# makedirs(path1/path2.. . [, mode])   创建多级目录
# rmdir(path)                          删除目录
# removedirs(path1/path2.. . . . .)    删除多级目录
# chdir(path)                          将path设置为当前工作目录

# os.path模块操作目录
import os.path
print(os.path.abspath('text.py'))
# abspath(path)           用于获取文件或目录的绝对路径
# exists(path)            用于判断文件或目录是否存在，如果存在返回True,否则返回False
# join(path, name)        将目录与目录或者文件名拼接起来
# split()                 分离文件名和目录名
# splitext()              分离文件名和扩展名
# basename(path)          从一个目录中提取文件名
# dirname(path)           从一个路径中提取文件路径，不包括文件名
# isdir(path)             用于判断是否为路径





# 生成。exe执行文件
# win+R cmd  : pip Install PyInstaller
# pyinstaller -F + 需要生成的py文件地址
print('---------------------------------------')