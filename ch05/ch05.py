#-*- coding:utf-8 -*-
import re

fr = open("test.html", "r")
data = fr.readlines()

#-----------------user information --------------------
'''
info_dict = {}
info_dict['quota'] = []
info_dict['think'] = []
flag = 0
quota_flag = 0
think_flag = 0
cnt = 0
while cnt < len(data):
    line = data[cnt].strip()
    if line == "":
        cnt += 1
        continue

    if "main-content" in line:
        flag = 1
        cnt = cnt + 1
        continue
    if flag == 1:
        if "ptt.cc" in line:
            cnt = cnt + 1
            break
        if line != "":
            #print line.strip()
            if "[職業類別]" in line:
                if "：" in line:
                    info_dict['occupy'] = line.split("：")[1]
                if ":" in line:
                    info_dict['occupy'] = line.split(":")[1]

            if "[心得]" in line:
                think_flag = 1
            if think_flag == 1:
                info_dict['think'].append(line)
            if "[已持有的卡片與額度]" in line:
                if "：" in line:
                    info_dict['quota'].append(line.split("：")[1])
                if ":" in line:
                    info_dict['quota'].append(line.split(":")[1])
                quota_flag = 1
                cnt = cnt + 1
                continue
            if quota_flag == 1:
                if "[" in line and  "]" in line:
                    quota_flag = 0
                    cnt = cnt + 1
                    continue
                info_dict['quota'].append(line.strip())
    cnt += 1

print info_dict
for key in info_dict.keys():
    if type(info_dict[key]) == list:
        print key, ",".join(info_dict[key])
    else:
        print key, info_dict[key]

'''
#------------------ push --------------------------------
eva = {
        "u" : 0,
        "m" : 0,
        "d" : 0,
}
ptn_tag = "push-tag\">(.+?)<"
for line in data:
    if "push-tag" in line:
        #print line.strip()
        searchobj = re.search(ptn_tag, line.strip())
        if searchobj:
            tag = searchobj.group(1).strip()
            if tag == "推":
                eva['u'] += 1
            elif tag == "→" : 
                eva['m'] += 1
            else:
                eva['d'] += 1
print eva

fw = open("target.txt", "w")
fw.write("職業類別 " + info_dict['occupy'])
fw.write("推 " + str(eva['u']) + ",")

'''

[目前工作年資]：1年10個月

[年齡]：26

[年收入]：都填500K

[申請卡片]：富邦LINE數位生活卡、元大愛金卡

[可提供之財力證明]：三個月薪資證明&amp;薪資戶頭存摺

[已持有的卡片與額度] : 華南紅J卡 60K
中信酷玩M卡 20K

[近三個月有無申辦] :無

[是否貸款]：無

[核卡額度] :富邦LINE數位生活M卡 30K
元大愛金V卡 50K
[心得]：

3/17 分行申請
3/21 富邦打公司電話照會
3/22 元大簡訊通知審核中
3/23 富邦通知領卡

...skipping 27 lines
結果下來的額度真讓我翻白眼
應該是因為空白的戶頭所以給我最低額度..
但是來膜的雨傘真心好看!
主要拿來在7-11消費使用及繳手機話費
-------------------------------
因為這兩張是去年12月辦的卡片
所以詳細情形已經忘了許多
都是在12月初辦理月中拿到卡片
-------------------------------
富邦LINE數位生活卡
這張卡真是讓我挑戰最多次的卡片
聽聞版上各位大大一致認定好用卡片
我當然也該來辦一張
第一次辦理與華南紅卡同天申請卻兩天速回簡訊打槍
想當然我就隔天帶著扣繳憑單殺去辦理的分行
不料卻變成當天簡訊直接開槍...
如今事隔三月
我又再次申請
與元大愛金同一天申請
終於讓我申請過了
而且核卡速度之快
可見得效率之高
雖然額度只有30K
但有成功申請就非常感動了QQ
目前當作手機話費繳費及網購使用
順便當作STEAM主要消費使用
'''





