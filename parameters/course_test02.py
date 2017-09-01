#!/usr/bin/python2
#coding=utf-8


import csv

file_1 = open(r'C:\Users\Administrator\PycharmProjects\data\course_test02.csv', 'r')
list_1 = csv.reader(file_1)
for row, pars in enumerate(list_1):
    if row >= 1:
        # 课件名称
        courseware_name = pars[0].decode('gb2312')
        # 课件图片地址
        courseware_file = pars[1].decode('gb2312')
        # 课程分类
        course_classify = pars[2].decode('gb2312')
        # 管理部门
        manage_departmen = pars[3].decode('gb2312')
        # 课程标签
        tag = pars[4].decode('gb2312')
        # 学习期
        date = pars[5].decode('gb2312')
        # 讲师
        lecturer = pars[6].decode('gb2312')
        # 有效期
        start_time = pars[7].decode('gb2312')
        end_time = pars[8].decode('gb2312')
        # 课程简介
        intro = pars[9].decode('gb2312')
        # 选修学分
        start_credit = pars[10].decode('gb2312')
        end_credit = pars[11].decode('gb2312')
        # 结业条件
        # 课程学习  study
        # 课后考试  exam
        # 课程评价  comment
        # Completion_condition = {'study': '//label[@for="ui_0_pass_by_study"]', 'exam': '//label[@for="ui_0_pass_by_exam"]',
        #                         'comment': '//label[@for="ui_0_pass_by_comment"]'}
        # 学分
        credit = pars[12].decode('gb2312')
        # 积分
        integral = pars[13].decode('gb2312')
        # 部门
        department = pars[14].decode('gb2312')
        # 部门标签
        tag_department = pars[15].decode('gb2312')
        # 岗位
        post = pars[16].decode('gb2312')
        # 职位
        position = pars[17].decode('gb2312')
        # 标签
        label = pars[18].decode('gb2312')
        # 用户名称
        usersname = pars[19].decode('gb2312')
file_1.close()


