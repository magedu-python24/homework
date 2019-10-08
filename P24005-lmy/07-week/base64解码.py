
# base64解码
def base64_decode(src:bytes):
    target = bytearray()
    # 将bytes转为字典，便于检索
    alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    alp_dict = dict(zip(alphabet, range(64)))
    # 判断输入字符串是否是4的整数倍，否则报错
    length = len(src)
    if length % 4:
        print('input error')
        return
    # 从输入字符串中每次取4个
    for offset in range(0, length, 4):
        _src = src[offset:offset+4]
        val = 0
        for i, index in enumerate(_src):
            # 查表
            temp = alp_dict.get(index)
            if temp is not None:
                # 移位
                val += temp << (3-i)*6
        target.extend(val.to_bytes(3, 'big').strip(b'\x00'))
    return bytes(target)

src = b'bWFnZWR1LmNvbQ=='
print(base64_decode(src))