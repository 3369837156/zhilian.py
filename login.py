import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *

import self as self

registered_users = {'user': '123456'}  # 模拟数据库，存储已注册的用户名和密码

# 第一个窗体
class page1:

    def __init__(self, win):
        self.jizhu = None
        self.cvar = IntVar()
        self.v1 = StringVar()
        self.v2 = StringVar()
        self.win = win
        self.win.title("登录窗口")  # 窗体名称
        self.win.geometry("500x300")  # 窗体的大小
        # self.win.config(bg='yellow')

        # 标签实例化、定位
        self.lab1 = Label(self.win, text="用户名：")
        self.lab1.place(x=100, y=50, width=50, height=30)
        self.lab2 = Label(self.win, text="密  码：")
        self.lab2.place(x=100, y=100, width=50, height=30)
        # 文本框实例化、定位
        self.textname = Entry(textvariable=self.v1)
        self.textpwd = Entry(textvariable=self.v2, show="*")
        self.textname.place(x=180, y=50, width=150, height=30)
        self.textpwd.place(x=180, y=100, width=150, height=30)
        # 登录、重置、退出按钮实例化和定位
        self.butt1 = Button(self.win, text='登录', command=self.login)
        self.butt1.place(x=75, y=180, width=50, height=30)

        self.butt2 = Button(self.win, text='重置', command=self.reset)
        self.butt2.place(x=150, y=180, width=50, height=30)

        self.butt3 = Button(self.win, text='退出', command=self.quit1)
        self.butt3.place(x=300, y=180, width=50, height=30)
        #注册
        self.butt_register = Button(self.win, text='注册', command=self.open_register_window)
        self.butt_register.place(x=225, y=180, width=50, height=30)
        # 记住密码复选框
        self.remb = Checkbutton(self.win, text='记住密码', variable=self.cvar, onvalue=1, command=self.jizhu)
        self.remb.place(x=300, y=150, width=80, height=30)

    # 功能编写：登录窗口、跳转页面
    def login(self):
        user = self.textname.get()
        pwd = self.textpwd.get()
        if user in registered_users and registered_users[user] == pwd:
            self.butt1.destroy()
            self.butt2.destroy()
            self.butt3.destroy()
            self.lab1.destroy()
            self.lab2.destroy()
            self.textname.destroy()
            self.textpwd.destroy()
            self.remb.destroy()
            self.butt_register.destroy()
            page2(root)
        else:
            showwarning('警告', '用户名或密码错误')

    # 功能编写：重置文本框
    def reset(self):
        self.v1.set("")  # self.textname.delete(0,END)
        self.v2.set("")  # self.textpwd.delete(0,END)

    # 功能编写：窗体关闭
    def quit1(self):
        self.win.destroy()

    #注册
    def open_register_window(self):
        # 使用Toplevel创建一个新的窗口作为注册窗口
        register_win = Toplevel(self.win)
        register_win.title("注册窗口")
        page_register(register_win)

    # 第三个
class page_register:
    def __init__(self, win):
        self.win = win
        self.win.title("注册窗口")  # 窗体名称
        self.win.geometry("300x200")  # 窗体的大小

        # 标签和输入框
        self.lab1 = Label(self.win, text="用户名：")
        self.lab1.pack(pady=10)
        self.entry_username = Entry(self.win)
        self.entry_username.pack(pady=10)

        self.lab2 = Label(self.win, text="密  码：")
        self.lab2.pack(pady=10)
        self.entry_password = Entry(self.win, show="*")
        self.entry_password.pack(pady=10)

        # 注册按钮（现在称为“确认”按钮）
        self.butt_confirm = Button(self.win, text='确认', command=self.do_register)
        self.butt_confirm.pack(pady=10)

    def do_register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # 检查用户名是否已经存在
        if username in registered_users:
            messagebox.showerror("注册失败", "用户名已存在！")
            return

            # 将用户信息添加到模拟数据库
        registered_users[username] = password
        print(f"注册用户: {username}, 密码: {password}")

        # 显示注册成功信息
        messagebox.showinfo("注册成功", "用户注册成功！")

        # 关闭注册窗口
        self.win.destroy()

        # 第二个窗体
class page2:
    def __init__(self, win):
        self.win = win
        self.win.title("操作界面")
        self.win.geometry("500x300")
        # self.win.config(bg='blue')

        self.butt4 = Button(self.win, text='爬取', command=lambda: self.run_script_and_show_message('main.py'))
        self.butt4.place(x=100, y=180, width=50, height=30)
        self.butt5 = Button(self.win, text='显示', command=lambda: self.run_script_and_show_message('test1.py'))
        self.butt5.place(x=380, y=180, width=50, height=30)

                # 功能编写：运行指定的Python脚本并在完成后显示消息框

    def run_script_and_show_message(self, script_path):
        try:
            subprocess.run(["python", script_path])  # 确保script_path的路径是正确的
            # 脚本执行完毕后显示消息框
            messagebox.showinfo("爬取完毕", "数据已成功爬取！")
        except Exception as e:
            print(f"Error running script: {e}")

        # 实现窗体


root = Tk()
p1 = page1(root)

root.mainloop()
