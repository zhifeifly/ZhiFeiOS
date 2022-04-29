from operator import truediv
from re import S
import tkinter.messagebox
import os#导入模块
from turtle import *
import getpass
import time
import winreg
import webbrowser
import sched
import subprocess
def add(x, y):
   """相加"""
 
   return x + y
 
def subtract(x, y):
   """相减"""
 
   return x - y
 
def multiply(x, y):
   """相乘"""
 
   return x * y
 
def divide(x, y):
   """相除"""
 
   return x / y
 
def clear():os.system('cls')
print("    |                      ")
print("    |       |--|               ")
print("    |       |  |  ADING          ")
print("    |       |--|        ......    ")
print("    |--------                      ")
time.sleep(5)#等待5秒Wait 5 min
clear()#清空cls
username=input("Your Name:")
userpassword=getpass.getpass("Your password:")#登录Login
clear()
print("----------------------------------------")
print("|    ------                            |")
print("|        /     |----   ------   -----  |")
print("|       /      |       |    |   |      |")#图标
print("|      /       |----   |    |   |----  |")
print("|    --------  |       ------       |  |")
print("|              |                -----  |")
print("----------------------------------------")
print("Welcome to the zhifeiOS "+username+"! You can enter 'help' to see os command.")
n="1"
os = input(username+"@"+"ZFIOS ")#欢迎+提示符Welcome+Info message
while n!="2":
     if os == "help":
      print("powerd = powerd")
      print("messagebox = enter message")
      print("www = internet")#疑问info
      print("password = password oper0ate")
      print("about")
      print("turtle")
      print("game=turtle game")
      print("              ")
      print("URL:www.zhifeifly.com/os")
      time.sleep(10)
      n="1"
#------------------------------电源操作PowerSwitch----------------------------------#
     if os == "powerd":
        
        print("You can exit or sleep or cls. ")
        pw=input()
        if pw =="exit":#电源，if来判断关闭或睡眠Power,if to switch off or sleep.
            exit()
        if pw =="sleep":
            clear()
        if pw =="cls":
            n="2"
#-----------------------------信息框Messagebox----------------------------------#

     else:
            if os == "messagebox":
                print("Welcome to the ---------msseagebox-----------!You can enter lost of msseage.")
                title=input("Messagebox(Title)>")
                msseage=input("Messagebox(Message)>")#信息框Messagebox
                show=input("Messagebox(Show:info error)>")
                if show == "info":
                   tkinter.messagebox.showinfo(title,msseage)
                else:
                    if show == "error":
                       tkinter.messagebox.showerror(title,msseage)
                    else:#判断图标输入Judge icons input.
                        print("Error!code:001ee1331.Please try again.")
                if show == "exit":
                    n="2"        
#--------------------------浏览器Internet--------------------------------#
            if os == "www":
                
                print("Welcome to the internet!You can see many picture/Video in it.")
                www=input("Internet(URL)>")
                webbrowser.open( www )#浏览器
                n="2"
#------------------------密码管理器Password operate---------------------------------------#
            if os == "password":
                
                print("Welcome to the zfos password operate!Enter 'help'to see command.")
                pw=input("Password operate>")
                if pw =="help":
                    print("restaruent")
                    print("see password")#密码显示和重置Password see or restaurand
                if pw =="restaurent":
                    userpassword=getpass.getpass("Your password:")
                if pw =="see password":
                    print(userpassword)
                if pw =="exit":
                    n="2"
                    #M    A    D    E    W    I    T    H    Z    F    I
                    #zhifeifly Co., ltd.,
#----------------------------------关于About----------------------------#
            if os == "about":
                
                print("Made with zhifeifly liuhaozhe,Beta1.0.0仅供学习或者快捷使用。Copyright©2019~2022 by zhifeifly.")
                time.sleep(10)
                n="2"   
#---------------------------小海龟Turtle-----------------------------------#
            if os == "turtle":
                print("Welcome to the turtle game!you can play the turtle.")
                turtle=input("Turtle(operate=circle/wjx)>")
                if turtle == "circle":
                    circle(120)
                if turtle == "exit":
                    n="2"
                if turtle == "wjx":
                    print("Start python pentagram...")
                    time.sleep(5)
                    color("white")
                    penup
                    goto(-130.85,0)
                    color("red")
                    pendown
                    goto(-130.85,0)
                    goto(-30.85,0)
                    goto(0,95.27)
                    goto(30.85,0)               #画五角星Draw Star
                    goto(130.85,0)
                    goto(50.83,-58.72)
                    goto(81.8,-153.72)
                    goto(0,-95.22)
                    goto(-81.8,-153.72)
                    goto(-50.83,-58.72)
                    goto(-130.85,0)
                    tkinter.messagebox.showinfo("Info","Turtle is on the terminal!")
            if os == "game":
                color("orange")
                goto(300,0)
                circle(100,180)#操场外围
                goto(0,200)
                circle(100,180)
                hideturtle()
                penup()
                goto(20,10)
                pendown()
                width(5)
                color("red")#跑道
                forward(250)
                circle(80,180)
                forward(250)
                circle(80,180)
                t1=Turtle()
                t1.shape("turtle")
                t1.penup()
                t1.goto(20,10)#判断输入值
                t1.speed(1)
                circle=int(input("Please enter number of laps>"))
                while(circle):
                 t1.forward(250)#While循环
                 t1.circle(80,180)
                 t1.forward(250)
                 t1.circle(80,180)
                 tkinter.messagebox.showinfo("Info","OK!")
                 exit()
#This Python OS 1.0.0 Made with zhifeifly.In Github.
