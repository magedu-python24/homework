
# base64编码
def base64_encode(src:str):
    target = bytearray()
    alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    # 将输入的字符串转成bytes，防止不同编码的字符所占用的字节长度不相同，而造成编码错误
    _src = bytes(src, encoding='utf-8')
    # 从输入字符串中，依次取3个，不足3个补ascii空
    length = len(_src)
    r = 0
    for offset in range(0, length, 3):
        val = _src[offset:offset+3]
        r = 3-len(val)
        if len(val) < 3:
            val += b'\x00' * r
        # 将bytes转成int
        temp = int.from_bytes(val, 'big')
        # 移位操作，将3*8-->4*6
        for i in range(18, -1, -6):
            index = temp >> i & 0x3f
            target.append(alphabet[index])
    # 替换尾部AA为=
    if r:
        target[-r:] = b'=' * r
    return bytes(target)

src = 'magedu.com'
print(base64_encode(src))


