# -*- coding: utf-8 -*-
import urllib2
import re

#1 Crawl web page
url = "https://www.ptt.cc/bbs/creditcard/M.1459655925.A.0F9.html"
opener = urllib2.build_opener(urllib2.HTTPSHandler())
opener.addheaders.append(('Cookie', 'over18=1'))
fd = opener.open(url)
data = fd.readlines()

#2 Extract information
'''
1. URL,標題,日期,作者
2. 職業類別,目前工作年資,年齡,年收入,申請卡片,可提供之財力證明,已持有的卡片與額度,近三個月有無申辦,是否貸款,核卡額度,心得
3. 推, 噓, 箭頭次數
'''
infos = []
#2.1 URL,標題,日期,作者
for line in data:
    if "main-content" in line:
        #print line.strip()
        infos.append(line.strip())

#2.2 職業類別,目前工作年資,年齡,年收入,申請卡片,可提供之財力證明,已持有的卡片與額度,近三個月有無申辦,是否貸款,核卡額度,心得
flag = 0
userinfo = ""
for line in data:
    if flag == 1:
        if "ptt.cc" in line:
            break
        userinfo += (line.strip() + "\n")
        continue
    if "main-content" in line:
        flag = 1
        continue

print userinfo
infos.append(userinfo)

#2.3 推, 噓, 箭頭次數
eva = {
    'u' : 0,
    'm' : 0,
    'd' : 0,
}
ptn_tag = "push-tag\">(.+?)<"  # Adding a ? on a quantifier (?, * or +) makes it non-greedy.
for line in data:
    if "push-tag" in line:
        #print line.strip()
        searchobj = re.search(ptn_tag, line.strip())
        tag = searchobj.group(1).strip()
        if tag == "推":
            eva['u'] += 1
        elif tag == "→":
            eva['m'] += 1
        else:
            eva['d'] += 1
print str(eva)
