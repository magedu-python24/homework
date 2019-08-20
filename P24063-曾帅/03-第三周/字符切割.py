logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
''' 
a=0
b=0
for i in logs.splitlines():
     s=i.split() 
     for j in s: 
         if j.strip('"').upper() == 'POST': 
              a += 1 
         elif j.strip('"').upper() == 'GET': 
              b += 1 
print('POST:', a) 
print('GET:', b) 