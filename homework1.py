# 作业题目：
# # 1、可选择录入科目成绩；录入完成后自动显示当前科目的所有分数和总分数
# # 2、录入科目成绩时，需要附带录入学生名字
# # 3、可显示所有科目成绩
# # 4、可选择退出
# #
# # 自由扩展内容：
# # 上述作业中,每个科目下，名字不能重复

# while True:
#     print('1.录入','2.退出')
#     n = int(input('请选择:'))
#     newd = {'姓名:': '', '语文:': '', '数学:': '', '外语:': '', '总分数:': ''}
#     newd['姓名:'] = str(input('请输入姓名:'))
#     newd['语文:'] = int()
#     newd['数学:'] = int()
#     newd['外语:'] = int()
#     print('姓名:', newd['姓名:'], '语文分数', newd['语文:'], '数学分数', newd['数学:'], '外语分数', newd['外语:'],
#           '总分数', newd['总分数:'])
#
#     if n == 1:
#         while True:
#             print('请选择')
#             print('1.语文', '2.数学', '3.外语', '4.退出')
#             i = int(input('请选择：'))
#
#             if i == 1:
#                 u = {'语文:': newd['语文:']}
#                 newd['语文:'] = int(input('请输入语文分数'))
#                 u = {'语文:': newd['语文:'] }
#                 newd.update(u)
#                 newd['总分数:'] = int(newd['语文:']) + int(newd['数学:']) + int(newd['外语:'])
#                 print('语文:',newd['语文:'])
#                 print('姓名:',newd['姓名:'],  '数学分数', newd['数学:'],  '外语分数', newd['外语:'],  '总分数', newd['总分数:'])
#
#             elif i == 2:
#                 newd['数学:']= int(input('请输入数学分数'))
#                 j = {'数学:': newd['数学:']}
#                 newd.update(j)
#                 newd['总分数:'] = int(newd['语文:']) + int(newd['数学:']) + int(newd['外语:'])
#                 print('数学:', newd['数学:'])
#                 print('姓名:', newd['姓名:'],  '语文分数', newd['语文:'],  '外语分数', newd['外语:'],  '总分数', newd['总分数:'])
#
#             elif i == 3:
#                 newd['外语:'] = int(input('请输入外语分数'))
#                 m = {'外语:': newd['外语:']}
#                 newd.update(m)
#                 newd['总分数:'] = int(newd['语文:']) + int(newd['数学:']) + int(newd['外语:'])
#                 print('外语:', newd['外语:'])
#                 print('姓名:',newd['姓名:'],  '语文分数',newd['语文:'],  '数学分数',newd['数学:'],  '总分数',newd['总分数:'])
#
#             elif i == 4:
#                 print('再见')
#                 break
#     elif n == 2:
#         print('再见')
#         exit()
#
#老师讲的
def showmenu():
    print('1、输入语文成绩')
    print('2、输入数学成绩')
    print('3、输入英语成绩')
    print('4、显示所有成绩')
    print('5、退出')
    print('6、修改语文成绩下某个学生的成绩')
    print('7、修改数学成绩下某个学生的成绩')
    print('8、修改英语成绩下某个学生的成绩')
    print('9、删除语文成绩下某个学生')
    print('10、删除数学成绩下某个学生')
    print('11、删除英语成绩下某个学生')
    n = int(input('请选择:'))
    return n
#1、输入姓名，输入成绩；
#2、将数据存放入scores中；
#3、
def calscore(n,scores):
    keys = tuple(scores.keys())
    key = keys[n-1]
    #print('选择的分组是:',keys[n-1])
    name = input('输入学生的姓名:')
    score = int(input('输入{}成绩:'.format(key)))
    student = {'name':name,'score':score}

    scores[key].append(student)
    students = scores[key]
    print('当前{}分数如下：'.format(key))
    n = 0
    for stu in students:
        print(stu['score'],end='  ')
        n += stu['score']

    print('总分数:',n)

def showallinfo(scores):
    print('*'* 20)
    for key,students in scores.items():
        if len(students) > 0:  #判断当前分组下是否有学生信息；
            print('学科{}分数情况如下'.format(key))
            for stu in students:
                print('姓名：{}，分数{}'.format(stu['name'],stu['score']))
    print('*'* 20)

def change(scores):
    print('*' * 20)
    i = input('请输入需要更改的学生的姓名')
    a = 0
    for key,studengt in scores.items():
        for stu in studengt:
            if stu['name'] == i:
                print('找到了')
                stu['score'] = int(input('请输入新的分数'))
                print('姓名：{}，分数{}'.format(stu['name'], stu['score']))
                a = 1
                break
        if a == 1:
            break
    print('*' * 20)

if __name__ == '__main__':  #表示以下代码只在本文件内运行；
    scores = {'语文':[],'数学':[],'外语':[]}
    print(scores)
    while True:
        n = showmenu()
        if 1 <= n <= 3:
            calscore(n,scores)

        elif n == 4:
            showallinfo(scores)

        elif n == 5:
            print('再见')
            break

        elif 6 <= n <=8:
            change(scores)


# s = [{'zhangsan':100},{'lisi':90},{'liwu':90}]
#
# b = 0
# for stu in s:
#     for key in stu:
#         b +=stu[key]
#     # values = list(stu.values())
#     # score = values[0]
#     # b += score
# print(b)

#
#   # 1、先找到对应的分组
#     # 2、找到这个学生, 判断学生是否存在
#     # 3、输入新的成绩
#     keys = tuple(scores.keys())
#     key = keys[n - 6]
#
#     students = scores[key]
#     name = input('输入要修改分数的学生姓名:')
#     student = searchstudent(students, name)
#     if student is not None:
#         score = int(input('输入新的分数:'))
#         student['score'] = score
#     else:
#         print('该学生不存在')
#
# def delscore():
#     # 1、先找到对应的分组
#     # 2、找到这个学生， 判断学生是否存在
#     # 3、删除这个学生
#     pass