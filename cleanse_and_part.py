import csv
f1 = open("jingdongcom2.txt", 'w', encoding='utf-8')
with open("jingdongcom.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        column = row[2]
        f1.write(column)
f.close()
f1.close()
f1 = open('jingdongcom2.txt', 'r', encoding='utf-8')
f2 = open('jingdoncom_c.txt', 'w', encoding='utf-8') #文本清洗后的评论 txt
for line in f1.readlines():
    line = line.replace(' ', '')
    if line == '\n':
        line = line.strip()
    line = ''.join(char for char in line if char.isalnum())
    f2.write(line)
f1.close()
f2.close()
with open('hit_stopwords.txt', 'r', encoding='utf-8') as f_stopwords:
    stopword_list = [word.strip('\n') for word in f_stopwords.readlines()]

import jieba
f2 = open('jingdoncom_c.txt', 'r', encoding='utf-8')
f3 = open('jingdongcom_p.txt', 'w',encoding='utf-8')
content2 = f2.read()
com_p_list = jieba.cut(content2, cut_all = False )
res = []
for com_p in com_p_list:
    if com_p not in stopword_list:
        res.append(com_p)
f3.write('\n'.join(res))
