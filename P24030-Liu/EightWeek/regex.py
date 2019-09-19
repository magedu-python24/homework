import re

s='not 404 found 张三 99 深圳'
regex=re.compile('[^0-9a-zA-Z\s]+')
print(" ".join(regex.findall(s)))


