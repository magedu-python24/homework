logs = '''
        111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
	111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
	111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
	223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
	111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
	''' 

d={}
for line in logs.split('\n'):
    lines=line.split()
    if lines:
        method=lines[1][1:].upper()
        d[method]=d.get(method,0)+1
for k,v in d.items():
    print('{}:{}'.format(k,v))

