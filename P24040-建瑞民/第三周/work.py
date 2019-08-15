logs = '''



111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 



111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 



111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 



223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 



111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 



'''

l = logs.split('\n')
newlist = []
result = []
for i in l:
    if i == '' or i=='\u3000':
        continue
    else:
        x = i.split(' ')
        y = x[1].lower().lstrip('"')
        newlist.append(y)
        
        for j,v in enumerate(result):
            if y == v[0]:
                result[j][1] += 1
                break
        else:
            result.append([y,1])

for i in result:
    print('{0:<5}{1:<2}'.format(i[0],i[1]))
