#!/usr/bin/python2
# coding=utf-8


# aa = raw_input(u'请输入地址：')
#
# print aa
#
# id = raw_input('id:')
#
# user_name = raw_input('username:')
#
# pass_word = raw_input('password:')
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import turtle
import time

def tree(branchLen, t, p):
    if branchLen > 5:
        t.color("black")
        t.pensize(p)
        p = p-2
        t.forward(branchLen)
        t.right(20)
        painted = tree(branchLen - 10, t, p)
        t.left(40)
        tree(branchLen - 10, t, p)
        t.right(20)
        if not painted:
            t.color("green")
        t.backward(branchLen)
        if not painted:
            t.color("black")
        return 1
    return 0


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    p = 20
    tree(60, t, p)
    myWin.exitonclick()

main()