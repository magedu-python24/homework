logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
logs=logs.strip("\n")
ls=logs.splitlines()
G_count=0
P_count=0
for i in range(len(ls)):
    ls_in=ls[i].split(" ")
    lx=ls_in[1].strip("\" ")
    if lx.upper()=="GET":
        G_count+=1
    elif lx.upper()=="POST":
        P_count+=1
print("Get"+" "+str(G_count))
print("Post"+" "+str(P_count))
