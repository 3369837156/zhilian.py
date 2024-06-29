import tkinter as tk
from tkinter import ttk
import pandas as pd

from main import filename


def show_csv_in_table(csv_file):
    # 读取CSV文件
    df = pd.read_csv(csv_file)

    # 创建主窗口
    root = tk.Tk()
    root.title("CSV Data Viewer")

    # 创建一个Frame来容纳Treeview
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)

    # 创建一个Treeview
    tree = ttk.Treeview(frame, columns=df.columns.tolist(), show='headings')

    # 设置列标题
    for col in df.columns:
        tree.heading(col, text=col)

        # 调整列宽以适应内容
        # 这里只是一个示例，你可能需要动态计算合适的列宽
        tree.column(col, width=100, anchor='center')

        # 将DataFrame的数据添加到Treeview中
    for index, row in df.iterrows():
        tree.insert('', 'end', values=row.tolist())

        # 将Treeview添加到Frame中
    tree.pack(fill='both', expand=True)

    # 运行主循环
    root.mainloop()


# 调用函数并传入CSV文件名
show_csv_in_table(filename)  # 替换为你的CSV文件名