alphabet=b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
betalpha=[-1]*128
length=len(alphabet)
for i in range(length):
    betalpha[alphabet[i]]=i

def base64encode(src:str):
    if isinstance(src,str):
        _src=src.encode()
    else:
        return
    target = bytearray()
    length=len(_src)
    o=length%3
    for offset in range(0,length-o,3):
        tripe=int.from_bytes(_src[offset:offset+3],'big')
        target.append(alphabet[tripe>>18])
        target.append(alphabet[tripe>>12&0x3F])
        target.append(alphabet[tripe>>6&0x3F])
        target.append(alphabet[tripe&0x3F])
    if o==1:
        tripe=int.from_bytes(_src[length-o:],'big')
        target.append(alphabet[tripe>>2])
        target.append(alphabet[tripe<<4&0x3F])
        target.append(61)
        target.append(61)
    elif o==2:
        tripe=int.from_bytes(_src[length-o:],'big')
        target.append(alphabet[tripe>>10])
        target.append(alphabet[tripe>>4&0x3F])
        target.append(alphabet[tripe<<2&0x3F])
        target.append(61)
    return bytes(target)

def base64decode(src:str):
    if isinstance(src,str):
        _src=src.encode()
    else:
        return
    target = bytearray()
    length=len(_src)
    if length%4==2:
        _src+="=="
    elif length%4==3:
        _src+="="

    for offset in range(length):
        o=offset%4
        if o==0:
            b1=betalpha[_src[offset]]
        elif o==1:
            b2=betalpha[_src[offset]]
        elif o==2:
            b3=betalpha[_src[offset]]
        else: 
            b4=betalpha[_src[offset]]
            target.append(b1<<2|(b2>>4&0x3))
            if b3==-1:
                break
            target.append((b2<<4&0xF0)|(b3>>2&0xF))
            if b4==-1:
                break
            target.append(b3<<6&0xFC|b4)
    return str(bytes(target),encoding="utf8")
code='bWFnZWR1LmNvbQ=='
decode=base64decode(code)
print('{} decode:  {}'.format(code,decode))

decode='magedu.com'
code=base64encode(decode)
print('{} encode:  {}'.format(decode,code))

