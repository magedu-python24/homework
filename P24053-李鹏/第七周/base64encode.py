
alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64encode(src:str):
    """
    base64编码：基于64个可打印字符来标识二进制数据（字节码）的编码方式。实现方式：每三个8bit的字节转换成四个6bit的
                字节，然后把6bit字节两高位添0，组成四个8bit的字节

    规则：
            1.把3字节变成4字节；
            2.每76个字符增加一个换行符；
            3.处理结束符

    待优化的问题：
            1.每76个字符需增加一个换行符；
            2.未处理结束符;
    :param src:
    :return:
    """
    ret = bytearray()
    if isinstance(src, str):
        _src = src.encode('ascii')
    else:
        return

    # step 1:对字节码每3个进行分组，并处理补零问题
    count = 0
    for offset in range(0, len(_src), 3):
        triple = _src[offset: offset+3]

        if offset + 3 > len(_src):
            count = 3 - len(triple)
            triple = triple + b'\x00' * count

        # 将字节码转换成二进制，为编码做准备
        b = int.from_bytes(triple, byteorder='big')

        # step 2:3个字节码一组，二进制共24位，按照每6位（从高位/低位均可）一组进行重新分组：通过向右移位后取低6位实现
        for i in  range(18, -1, -6):
            index = b >> i & 0x3f
            ret.append(alphabet[index])

    # step 3: 根据补零个数，编码后增加'='
    for i in range(1, count+1):
        ret[-i] = 61

    return bytes(ret)


print(base64encode('abc'))