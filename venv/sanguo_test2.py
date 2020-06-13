import re

#返回查找任务的数量
def find_item(hero):
    with open('sanguo.txt') as f:
        data=f.read().replace('\n','')
        name_num=re.findall(hero,data)#hero在data中出现的次数
        print('主角 %s 出现%s次' %(hero,len(name_num)))

    return name_num




#读取人物信息
#name_dict={}
with open('name.txt') as f_name:
    for line in f_name:
        name=line.split('|')
        for n in name:
            print(n)#遍历输出name.txt中的名字
            name_num=find_item(n)
            #name_dict[n]=name_num
