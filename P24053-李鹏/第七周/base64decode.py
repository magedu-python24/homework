alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64decode(src:str):
    """
    base64解码：

    思路：按照编码的逆操作，每4个字符进行一次截断，再进行移位运算

    待优化的问题：
            1.输入的字符串不是一个正确的base64编码，解码会出现错乱
    :param src:
    :return:
    """
    ret = bytearray()
    if isinstance(src, str):
        _src = src.encode('ascii')
    else:
        return

    for offset in range(0, len(_src), 4):
        temp = 0x00
        block = _src[offset: offset+4]
        for i, letter in enumerate(reversed(block)):
            index = alphabet.find(letter)
            if index == -1:
                continue
            temp += index << 6*i
        ret.extend(temp.to_bytes(3, 'big'))

    return bytes(ret.strip(b'\x00'))

print(base64decode('YWJj'))