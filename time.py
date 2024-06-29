from datetime import datetime
import requests
import re

# 假设headers已经定义好了
headers = {
    # ...
}

# Get the current date and time
now = datetime.now()

# Format the date and time as a string
time_string = now.strftime("%Y-%m-%d_%H-%M-%S")  # 使用下划线替换空格，因为文件名中通常不允许有空格

# The name of the file to save
filename = "zhilian_data_" + time_string + ".csv"  # 使用.csv扩展名

for page in range(1, 5):
    # 北京上海广州深圳天津武汉西安的url
    url = f"https://sou.zhaopin.com/?jl=530&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&p={page}"
    time.sleep(5)  # 停顿5秒
    response = requests.get(url, headers=headers).text

    # 在这里添加数据提取和写入CSV的逻辑
    # ...（省略了之前的正则表达式匹配部分）

    # 使用with语句来自动关闭文件
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        # 写入CSV头部（只在第一个文件写入，或者您可能想检查文件是否为空）
        if page == 1:
            f.write(
                'name,companyName,cityDistrict,education,salary60,workingExp,property,companySize,workType,positionURL\n')

            # 假设您已经提取了数据（name, companyName, ...）
        # 写入数据
        f.write(
            '{},{},{},{},{},{},{},{},{},{}\n'.format(name, companyName, cityDistrict, education, salary60, workingExp,
                                                     property, companySize, workType, positionURL))
