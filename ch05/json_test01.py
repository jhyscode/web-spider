# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 9:28
# @Author  : jhys
# @FileName: json_test01.py

import json
import csv
import pandas as pd

#JSON对象
data = [{
    'name': '小胖',
    'gender': '男',
    'birthday': '1999-10-10',
}]

# test json
with open('data.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(data, indent=2, ensure_ascii=False))

# test csv
with open('list_writer.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'score'])
    writer.writerow(['1001', 'kb', '99'])
    writer.writerow(['1002', 'www', '90'])
    writer.writerow(['1003', 'pp', '56'])

# dict write
# with open('data.csv', 'w', newline='') as csvfile:
#     fieldnames = ['id','name','age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

# read csv
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # for row in reader:
    #     print(row)

# pandas read
df = pd.read_csv('data.csv')
print(df)