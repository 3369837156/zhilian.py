import re
from datetime import datetime

import requests
import time

now = datetime.now()

# Format the date and time as a string
time_string = now.strftime("%Y-%m-%d_%H-%M-%S")  # 使用下划线替换空格，因为文件名中通常不允许有空格

# The name of the file to save
filename = "zhilian_data_" + time_string + ".csv"  # 使用.csv扩展名

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/105',
           'Cookie': 'x-zp-client-id=4a238294-b0ec-44bc-adec-dc44e25554bc; FSSBBIl1UgzbN7NO=50njD1AEzgiZwePDOo8DfZ.56UkY5j5oJYkRizPehaW_c2O3dY1zFSSWuUteNbUfHkIjmAVVPy18vZZtU7l7YAA; Hm_lvt_21a348fada873bdc2f7f75015beeefeb=1719269024; locationInfo_search={%22code%22:%22576%22%2C%22name%22:%22%E5%A4%AA%E5%8E%9F%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; _uab_collina=171926902382882330080597; zp_passport_deepknow_sessionId=8731ffc4sa2e6249628a882a26aee52cbd02; login-type=b; x-zp-device-id=4fb6e89bef260def129af858d1737978; rd-privacy-policy-checked=true; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; rd-staff-id=1203701693; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221203701501%22%2C%22first_id%22%3A%2218b8011e4a0bcf-087c5010db20a88-2d282549-1821369-18b8011e4a112e1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiODAxMWU0YTBiY2YtMDg3YzUwMTBkYjIwYTg4LTJkMjgyNTQ5LTE4MjEzNjktMThiODAxMWU0YTExMmUxIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTIwMzcwMTUwMSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221203701501%22%7D%2C%22%24device_id%22%3A%2218b8011e4a0bcf-087c5010db20a88-2d282549-1821369-18b8011e4a112e1%22%7D; at=7d0bceb067924582b4e8df444b9a5483; rt=e3ec177316024819a67df652ab947bf2; x-zp-authtmp-device-id=30b4a8c2-ff42-4e42-bb46-924f15965493; acw_tc=276077b817193138542263305e0b3816a7ecebb6615ca76277c3eeacbf3629; Hm_lpvt_21a348fada873bdc2f7f75015beeefeb=1719314140; FSSBBIl1UgzbN7NP=5RvjbCbR_NzLqqqDAsSBK0Gj1PxZ.kScZQqOM3nBNN_oFNV95acmykp7K.oiH2AFSNaHIfB6RCrA5uRQEW1PZdrY3OYEy7.Rq8mB_bkbg372mGO0lj_6_jNSPqe9Gi3F3i0Kz_tVF0w8uMqyjMcjF8b1._m00HEAtPOZ3JOXCxRhQCEM5jE3X5tA_3ZbONxi5QU6xxWepMRPn2XSkJAxkolg__1jHoRuWNpT2IvJlgQ6Tg6xpQHieOokRu6a6vntwXKtT2GJ_8qHdk25Y9Dg.7q'}
for page in range(1, 5):
    # 北京上海广州深圳天津武汉西安的url
    url = f"https://sou.zhaopin.com/?jl=530&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&p={page}"
    time.sleep(5)
    # 停顿5秒
    response = requests.get(url, headers=headers).text
    # print(response)
    # exit()
    for i in range(20):
        # 每页有最多30条数据
        name = re.findall(r'"matchInfo":.*?"name":"(.*?)"', response)[i]  # 工作名称
        companyName = re.findall(r'"companyName":"(.*?)"', response)[i]
        cityDistrict = re.findall(r'"cityDistrict":"(.*?)"', response)[i]
        education = re.findall(r'"education":"(.*?)"', response)[i]  # 学历
        salary60 = re.findall(r'"salary60":"(.*?)"', response)[i]  # 薪资
        workingExp = re.findall(r'"workingExp":"(.*?)"', response)[i]  # 经验要求
        property = re.findall(r'"property":"(.*?)"', response)[i]  # 公司性质
        companySize = re.findall(r'"companySize":"(.*?)"', response)[i]  # 公司规模
        workType = re.findall(r'"workType":"(.*?)"', response)[i]  # 工作类型
        positionURL = re.findall(r'"positionURL":"(.*?)"', response)[i]  # 详情页链接
        f = open(filename, 'a', encoding='utf8')
        f.write(
            '{},{},{},{},{},{},{},{},{},{}\n'.format(name, companyName, cityDistrict, education, salary60, workingExp,
                                                     property, companySize, workType, positionURL))

        f.close()


