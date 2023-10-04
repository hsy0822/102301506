#1.输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
x=int(input('请输入第一个整数：'))
y=int(input('请输入第二个整数：'))
z=int(input('请输入第三个整数：'))
nums=[x,y,z]
nums.sort(reverse=True)
print(nums)
print()

# 2.输出九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} × {i} = {i*j}", end="\t")
    print()


''' 输入⼀个字符串，判断字符串中是否含有"ol"这个⼦串， 若
有把所有的"ol"替换为"fzu"，最后把字符串倒序输出'''

string = input("请输入一个字符串：")
if "ol" in string:
    string = string.replace("ol", "fzu")
string = string[::-1]
print(string)


# 3.输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，
# 然后把剩下的整数升序排序，输出列表.

list = input("请输入一个包含字符串和整数的列表，元素之间使用空格分隔：").split()
list = [int(x) for x in list if x.isdigit()]
list.sort()
print(list)


#4.创建一个字典（dict），为字典添加几个键为学号，值为姓名元素，删除学号尾号为偶数的元素，输出字典
students = {"001": "Adm", "002": "Bob", "003": "Chen", "004": "Dang", "005": "Eric"}
keys_to_delete = []    #创建一个空列表，用来储存需要删除的键
for key in students.keys():
    if key[-1] in "02468":
        keys_to_delete.append(key)
for key in keys_to_delete:
    del students[key]       #删除掉字典中存在于列表的元素
print(students)


#5.创建一个函数，这个函数可以统计一个只有数字的列表中所有数字的个数，通过字典方式返回
def count_numbers(list):
    count_dict = {}
    for num in list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict
list = [1,2,3,5,4,3,2,5,1]
result = count_numbers(list)
print(result)

